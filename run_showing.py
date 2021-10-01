#!/usr/bin/env python3

import sys
import subprocess


class Episode:
    def __init__(self, filename, options=[]):
        self.filename = filename
        self.options = options


playlist_index = 0
if len(sys.argv) > 1:
    playlist_index = int(sys.argv[1])


playlists = [[]]
with open("playlist.txt") as f:
    line = f.readline()
    while line:
        options = []
        if line.startswith("#"):
            directive = line[1:].strip()
            line = f.readline()
            if directive.startswith("break"):
                playlists.append([])
                continue
            else:
                options = directive.split()
        playlists[-1].append(Episode(line.rstrip(), options))
        line = f.readline()

playlist = playlists[playlist_index]

command = ['mpv', '--pause', '--alang=jpn', '--slang=eng', '--no-osc']
for episode in playlist:
    command.append('--{')
    command.extend(episode.options)
    command.append(episode.filename)
    command.append('--}')

print(command)

subprocess.run(command)
