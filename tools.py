# -*- coding: utf-8 -*-
"""
deezer
Data Engineer (Internship) Home Exercises

"""

from operator import itemgetter



class Data():

  def __init__(self):
      self.song_dict = {}
      self.head = ""
      
  
  def read_and_precess_file(self,file_name):
    """
    this function takes as input a sound file with format like "song_data.csv" 
    and returns a song dictionary plus file header.
    """
 
    try:
      with open(file_name, "r") as file:
        self.head= file.readline()

        for line in file:

          line = line.strip("\n").split(",")
          line[1] = line[1].upper()
          line[2] = int(line[2])
          if line[1] in self.song_dict:
            self.song_dict[line[1]].append(line)
          else:
            self.song_dict[line[1]]= [line]
        #return song_dict,head

    except FileNotFoundError:
      msg = " \n Sorry, the file "+ file_name + " does not exist. \n \n"
      print(msg)


  def sorted_data_by_Number_of_times(self,limit:int):
    """
      this function takes as input the sound dictionary and performs the sorting, 
      then it returns the first k according to the value of variable limit .

    """
    sorted_dict_song = {}
    for key in sorted(self.song_dict):
      sorted_dict_song[key] = sorted(self.song_dict[key], key=itemgetter(2), reverse=True)[:limit]
    self.song_dict = sorted_dict_song


  def write_file(self,output="data/output/result.txt"):
    """
      this fonction saves the results in a text file
      
    """
    
    with open(output, 'w') as f:
      f.write('%s' % self.head)
      for key in self.song_dict:
        for song in self.song_dict[key]:
          f.write(",".join(str(e) for e in song) + "\n")
    
    print("You can found output at : "+output)
