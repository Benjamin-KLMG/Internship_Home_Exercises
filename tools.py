# -*- coding: utf-8 -*-
"""
deezer
Data Engineer (Internship) Home Exercises

"""

import sys
from operator import itemgetter
from pathlib import Path


def read_and_precess_file(file_name):
  """
  this function takes as input a sound file with format like "song_data.csv" 
  and returns a song dictionary plus file header.
  """
  song_dict={}
  #path = Path(file_name)
  try:
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

  except FileNotFoundError:
    msg = " \n Sorry, the file "+ file_name + " does not exist. \n \n"
    print(msg)


def sorted_data_by_Number_of_times(dict_song:dict,limit:int):
  """
    this function takes as input the sound dictionary and performs the sorting, 
    then it returns the first k according to the value of variable limit .

  """
  sorted_dict_song = {}
  for key in sorted(dict_song):

    sorted_dict_song[key] = sorted(dict_song[key], key=itemgetter(2), reverse=True)[:limit]
  return sorted_dict_song


def write_file(sorted_dict_song:dict, head):
  """
    this fonction saves the results in a text file
    
  """
  with open("data/output/result.txt", 'w') as f:
    f.write('%s' % head)
    for key in sorted_dict_song:
      for song in sorted_dict_song[key]:
        f.write(",".join(str(e) for e in song) + "\n")



# def main():
#   file_name = "data/input/song_data.csv"
#   limit = 10
#   file_name = sys.argv[1]
#   limit = int(sys.argv[2])

#   dict_song,head = read_and_precess_file(file_name)
#   sorted_dict_song = sorted_data_by_Number_of_times(dict_song,limit)
#   write_file(sorted_dict_song, head)


# if __name__ == "__main__":
#     main()
