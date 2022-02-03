# -*- coding: utf-8 -*-
"""
deezer
Data Engineer (Internship) Home Exercises

"""

from operator import itemgetter
from pathlib import Path


def read_and_precess_file(file_name):
  song_dict={}
  #countries = []
  # on crée un objet de la classe Path, associé au nom de fichier
  path = Path(file_name)
  with open(file_name, "r") as file:
    head= file.readline()


    for line in file:

      line = line.strip("\n").split(",")
      line[1] = line[1].upper()
      line[2] = int(line[2])
      if line[1] in song_dict:
        song_dict[line[1]].append(line)
      else:
        song_dict[line[1]]= [line]
    return song_dict,head


def sorted_data_by_Number_of_times(dict_song:dict,limit):
  sorted_dict_song = {}
  for key in sorted(dict_song):
    #print(key)
    sorted_dict_song[key] = sorted(dict_song[key], key=itemgetter(2), reverse=True)[:limit]
  return sorted_dict_song


def write_file(sorted_dict_song, head):
  with open("result.txt", 'w') as f:
    f.write('%s' % head)
    for key in sorted_dict_song:
      for song in sorted_dict_song[key]:
        f.write(",".join(str(e) for e in song) + "\n")



def main():
  file_name="data/song_data.csv"
  dict_song,head_= read_and_precess_file(file_name)

  sorted_dict_song = sorted_data_by_Number_of_times(dict_song,limit=100)

  write_file(sorted_dict_song, head_)


if __name__ == "__main__":
    main()
