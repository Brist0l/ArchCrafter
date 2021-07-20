import subprocess
import argparse
import os
import shutil


class Archcrafter:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="add songs to archcraft's MP3 player".title())
        self.add_args()
        self.args = self.parser.parse_args()

        self.ending = (".mp3", ".wma")

        self.from_music_path = ""
        self.to_music_path = "~/Music"
        self.contents = ""
        self.songs = []

    def add_args(self):
        self.parser.add_argument("MusicPath", help="specify the folder of the music files".title(), type=str)
        self.parser.add_argument("-mv", "--move",action="store_true", help="move the files instead of copying".title())

    def _verify_location(self):
        return True if os.path.isdir(self.args.MusicPath) else False

    def get_songs(self):
        if self._verify_location():
            self.from_music_path = self.args.MusicPath
            self.contents = os.listdir(self.from_music_path)
            for file in list(self.contents):
                if file.endswith(self.ending):
                    self.songs.append(file)
        else:
            raise NotADirectoryError

    def add_songs(self):
        self.get_songs()
        subprocess.call("pkill mpd")
        subprocess.run("cd ~/.mpd")
        subprocess.run("rm mpd.db")
        subprocess.run("mpd &")

    def move_songs(self):
        for a_song in self.songs:
            if self.args.move:
                shutil.move(a_song, self.to_music_path)
            else:
                shutil.copy(a_song, self.to_music_path)


Archcrafter()
