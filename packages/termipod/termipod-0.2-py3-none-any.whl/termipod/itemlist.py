# -*- coding: utf-8 -*-
#
# termipod
# Copyright (c) 2018 Cyril Bordage
#
# termipod is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# termipod is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import re
import operator
import os
from threading import Thread

import os.path

import termipod.backends as backends
import termipod.player as player
from termipod.database import DataBase


class ItemList():
    def __init__(self, config, print_infos=print, wait=False):
        self.db_name = config.db_path
        self.wait = wait
        self.db = DataBase(self.db_name, print_infos)
        self.print_infos = print_infos
        self.medium_areas = []
        self.channel_areas = []
        self.media = []
        self.channels = []

        self.add_channels()
        self.add_media()

        self.player = player.Player(self, self.print_infos)
        self.download_manager = \
            backends.DownloadManager(self, self.wait, self.print_infos)

        # Mark removed files as read
        for medium in self.media:
            if 'local' == medium['location'] and \
                    not os.path.isfile(medium['filename']):
                self.remove(medium=medium, unlink=False)

    def media_update_index(self):
        for i, medium in enumerate(self.media):
            medium['index'] = i

    def channel_update_index(self):
        for i, channel in enumerate(self.channels):
            channel['index'] = i

    def add_channels(self, channels=None):
        if channels is None:
            channels = self.db.select_channels()

        self.channels[0:0] = channels
        self.channel_update_index()
        self.update_channel_areas()  # TODO smart

    def disable_channels(self, channel_ids):
        channels = self.channel_ids_to_objects(channel_ids)
        for channel in channels:
            channel['disabled'] = True
            self.item_list.db.update_channel(channel)

    def remove_channels(self, channel_ids):
        channels = self.channel_ids_to_objects(channel_ids)
        urls = [c['url'] for c in channels]
        self.db.channel_remove(urls)

        # Count how many objects will be removed
        num_channel = len(urls)
        num_media = 0

        # Update channels and media
        for channel in channels:
            channel_idx = self.channels.index(channel)
            del self.channels[channel_idx]
            mi_to_remove = [i for i, m in enumerate(self.media)
                            if m['channel'] == channel]
            mi_to_remove.sort(reverse=True)
            num_media += len(mi_to_remove)
            for mi in mi_to_remove:
                del self.media[mi]

        self.media_update_index()
        self.channel_update_index()
        self.print_infos('%d channel(s) and %d media removed' %
                         (num_channel, num_media))

    def add_medium_area(self, area):
        self.medium_areas.append(area)

    def add_channel_area(self, area):
        self.channel_areas.append(area)

    def add_media(self, media=None):
        if media is None:
            self.media = []
            media = self.db.select_media()

        self.media[0:0] = media
        self.media_update_index()

        self.update_medium_areas(new_media=media)

    def update_medium_areas(self, new_media=None, modified_media=None):
        for area in self.medium_areas:
            if new_media is None and modified_media is None:
                area.reset_contents()
            else:
                if new_media is not None:
                    area.add_contents(new_media)
                if modified_media is not None:
                    area.update_contents(modified_media)

    def update_channel_areas(self):
        for area in self.channel_areas:
                area.reset_contents()

    def add(self, medium):
        self.media.append(medium)
        self.update_strings()

    def download(self, indices):
        if isinstance(indices, int):
            indices = [indices]

        media = []
        for idx in indices:
            medium = self.media[idx]

            channel = self.db.get_channel(medium['url'])
            self.download_manager.add(medium, channel)
            media.append(medium)

    def play(self, indices):
        # Play first item
        idx = indices[0]
        medium = self.media[idx]
        self.player.play(medium)
        # Enqueue next items
        self.playadd(indices[1:])

    def playadd(self, indices):
        for idx in indices:
            medium = self.media[idx]
            self.player.add(medium)

    def stop(self):
        self.player.stop()

    def switch_read(self, indices, skip=False):
        if isinstance(indices, int):
            indices = [indices]

        media = []
        for idx in indices:
            medium = self.media[idx]
            if medium['state'] in ('read', 'skipped'):
                medium['state'] = 'unread'
            else:
                if skip:
                    medium['state'] = 'skipped'
                else:
                    medium['state'] = 'read'
            self.db.update_medium(medium)
            media.append(medium)

        self.update_medium_areas(modified_media=media)

    def remove(self, idx=None, medium=None, unlink=True):
        if idx:
            medium = self.media[idx]

        if not medium:
            return

        if unlink:
            if '' == medium['filename']:
                self.print_infos('Filename is empty')

            elif os.path.isfile(medium['filename']):
                try:
                    os.unlink(medium['filename'])
                except FileNotFoundError:
                    self.print_infos('Cannot remove "%s"' % medium['filename'])
                else:
                    self.print_infos('File "%s" removed' % medium['filename'])
            else:
                self.print_infos('File "%s" is absent' % medium['filename'])

        self.print_infos('Mark "%s" as local and read' % medium['title'])
        medium['state'] = 'read'
        medium['location'] = 'remote'
        self.db.update_medium(medium)

        self.update_medium_areas(modified_media=[medium])

    def new_channel(self, url, count=-1, auto='', genre=''):
        if isinstance(count, str):
            if count == '':
                count = -1
            else:
                count = int(count)

        self.print_infos(f'Add {url} ({count} elements requested)')
        # Check not already present in db
        channel = self.db.get_channel(url)
        if channel is not None:
            self.print_infos('"%s" already present (%s)' %
                             (channel['url'], channel['title']))
            return False

        thread = Thread(target=self.new_channel_task,
                        args=(url, count, auto, genre))
        thread.daemon = True
        thread.start()
        if self.wait:
            thread.join()

    def new_channel_task(self, url, count, auto, genre):
        # Retrieve url feed
        data = backends.get_data(url, self.print_infos, True, count)

        if data is None:
            return False

        # Add channel to db
        data['genre'] = genre
        data['auto'] = auto
        data['disabled'] = 0
        self.db.add_channel(data)

        # Update medium list
        media = self.db.add_media(data, update=True)

        self.add_channels([data])
        self.add_media(media)

        self.print_infos(data['title']+' added')

    def channel_id_to_object(self, channel_id):
        if isinstance(channel_id, int):  # idx in channels
            channel = self.channels[channel_id]
        elif isinstance(channel_id, str):  # url
            channel = self.db.get_channel(channel_id)
            if channel is None:
                self.print_infos('Channel "%s" not found' % channel_id)
        elif isinstance(channel_id, dict):  # channel object
            channel = channel_id
        else:  # error
            channel = None
        return channel

    def channel_ids_to_objects(self, channel_ids):
        channels = [self.channel_id_to_object(c) for c in channel_ids]
        return [c for c in channels if c is not None]

    def channel_set_auto(self, channel_ids, auto=None):
        """ Switch auto value or set it to a value if argument auto is
        provided """
        for channel_id in channel_ids:
            channel = self.channel_id_to_object(channel_id)
            title = channel['title']

            if auto is None:
                if '' == channel['auto']:
                    new_value = '.*'
                else:
                    new_value = ''
            else:
                new_value = auto
            channel['auto'] = new_value
            self.print_infos('Auto for channel %s is set to: "%s"' %
                             (title, new_value))

            self.db.update_channel(channel)

        self.update_channel_areas()

    def channel_set_genre(self, channel_ids, genre):
        for channel_id in channel_ids:
            channel = self.channel_id_to_object(channel_id)
            title = channel['title']

            old_genres = channel['genre'].split(',')
            if genre not in old_genres:
                genres = set(old_genres+[genre])
                channel['genre'] = ','.join(genres)
                self.print_infos('Add %s for channel %s' % (genre, title))
            self.db.update_channel(channel)

        self.update_channel_areas()

    def update_channels(self, channel_ids=None):
        self.print_infos('Update...')
        if channel_ids is None:
            channels = self.db.select_channels()
            channels = [c for c in channels if not c['disabled']]
        else:
            channels = self.channel_ids_to_objects(channel_ids)

        thread = Thread(target=self.update_task, args=(channels, ))
        thread.daemon = True
        thread.start()
        if self.wait:
            thread.join()

    def update_task(self, channels):
        all_new_media = []

        need_to_wait = False
        for i, channel in enumerate(channels):
            self.print_infos('Update channel %s (%d/%d)...' %
                             (channel['title'], i+1, len(channels)))

            data = backends.get_data(channel['url'], self.print_infos)

            if data is None:
                continue

            new_media = self.db.add_media(data)
            if not new_media:
                continue

            all_new_media = new_media+all_new_media

            # Automatic download
            if not '' == channel['auto']:
                regex = re.compile(channel['auto'])
                sub_media = [medium for medium in new_media
                             if regex.match(medium['title'])]
                for s in sub_media:
                    self.download_manager.add(s, channel)
                    need_to_wait = True
        self.print_infos('Update channels done!')

        all_new_media.sort(key=operator.itemgetter('date'), reverse=True)
        self.add_media(all_new_media)

        if self.wait and need_to_wait:
            self.print_infos('Wait for downloads to complete...')
            self.download_manager.wait_done()

    def export_channels(self):
        exports = []
        for c in self.channels:
            export = '%s - %s' % (c['url'], c['title'])
            if c['disabled']:
                export = '# '+export
            exports .append(export)
        return '\n'.join(exports)
