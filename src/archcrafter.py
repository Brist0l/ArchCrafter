#!/usr/bin/env python3

import argparse
import os
import shutil
import subprocess
import getpass
import time


class Arch:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Add Songs To The Inbuilt Music Player in ArchCraft .")
        self.add_args()
        self.args = self.parser.parse_args()

        self.user = getpass.getuser()

        self.extensions = ('.mp3', '.wma')
        self.music_loc = f'/home/{self.user}/Music'

        self.location = self.args.location

        self.songs = []

        self.get_songs()

    def add_args(self):
        self.parser.add_argument('location', help="The Directory Of Your Music Files")
        self.parser.add_argument('-s', '--subdirectories', help="To Specify Whether to Add Songs from SubDirectories",
                                 action="store_true")
        self.parser.add_argument('-mv', '--move', help="Move The Files instead of Copying Them .", action="store_true")

    def _check(self):
        return True if os.path.isdir(self.location) else False

    def get_songs(self):
        if self._check():
            if self.args.subdirectories:
                for dir_path, dir_name, files in os.walk(self.location):
                    for file in files:
                        if file.endswith(self.extensions):
                            self.songs.append(file)
            else:
                for file in list(os.listdir(self.location)):
                    if file.endswith(self.extensions):
                        self.songs.append(file)
            self.moc_songs()
        else:
            self.parser.print_help()

    def moc_songs(self):
        os.chdir(self.location)
        if self.args.move:
            for songs in self.songs:
                shutil.move(songs, self.music_loc)
        else:
            for songs in self.songs:
                shutil.copy(songs, self.music_loc)
        self.mpd()

    @staticmethod
    def mpd():
        subprocess.call("pkill mpd", shell=True)
        subprocess.call("mpd &", shell=True)
        # time.sleep(0.2)
        subprocess.call("mpc update", shell=True)
        subprocess.call("mpc ls | mpc add", shell=True)


Arch()
