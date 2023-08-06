#!/usr/bin/env python
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

import argparse
import sys
import os

from termipod.itemlist import ItemList
from termipod.ui import UI
from termipod.config import Config


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Manage your podcasts in your terminal. '
                    'It handle RSS feeds and also Youtube channels.\n'
                    'When no argument is provided UI is shown.')
    parser.add_argument('-f', type=str, metavar='config_file',
                        help='Alternate configuration file')
    parser.add_argument('--add', type=str, metavar='url',
                        help='Add Youtube channel or RSS feed')
    parser.add_argument('--add-yt-count', type=int, metavar='count',
                        help='Limit number of youtube elements retrieved')
    parser.add_argument(
        '--auto', type=str, nargs=2, metavar=('url', 'pattern'),
        help="Pattern for media to be downloaded automatically "
             "('.*' for all)")
    parser.add_argument(
        '--up', type=str, nargs='?', const=True,  metavar='url',
        help='Update channels and download new videos for channels '
             'maked as auto')
    parser.add_argument('--disable-channel', type=str, metavar='url',
                        help='Disable channel by url')
    parser.add_argument('--remove-channel', type=str, metavar='url',
                        help='Remove channel and media by url')
    parser.add_argument(
        '--export-channels', type=str, nargs='?',
        const=True, metavar='filename',
        help='Export channel list (url and name, one channel by line). '
             'Argument can be followed by filename')
    args = parser.parse_args()

    # Init configuration
    config_params = {}
    if args.f:
        config_params['config_path'] = args.f
    config = Config(**config_params)
    os.chdir(config.media_path)

    if len(sys.argv) == 1 or (len(sys.argv) == 3 and args.f):
        UI(config)

    else:
        item_list = ItemList(config, wait=True)

        if args.add:
            if args.add_yt_count:
                item_list.new_channel(args.add, args.add_yt_count)
            else:
                item_list.new_channel(args.add)

        if args.auto:
            url, auto = args.auto
            item_list.channel_set_auto([url], auto)

        if args.up:
            if isinstance(args.up, bool):
                item_list.update_channels()
            else:
                item_list.update_channels([args.up])

        if args.disable_channel:
            item_list.disable_channels([args.disable_channel])

        if args.remove_channel:
            item_list.remove_channels([args.remove_channel])

        if args.export_channels:
            channels = item_list.export_channels()
            if isinstance(args.export_channels, bool):
                output = sys.stdout
            else:
                output = args.export_channels
            print(channels, file=open(output, 'w'))


if __name__ == "__main__":
    main()
