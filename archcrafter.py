import subprocess
import argparse
import os


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
        self.parser.add_argument("-mv", "--move", help="move the files instead of copying".title())

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

    def move(self):
        subprocess.call("")
Archcrafter()
