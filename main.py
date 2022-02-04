
import sys
from tools import Data

def main():


  if len(sys.argv) == 3:
    file_name = sys.argv[1]
    limit = int(sys.argv[2])
  else:
    print("The default data will be use to perform")
    file_name = "data/input/song_data.csv"
    limit = 100

  # dict_song,head = tls.read_and_precess_file(file_name)
  # sorted_dict_song = tls.sorted_data_by_Number_of_times(dict_song,limit)
  # tls.write_file(sorted_dict_song, head)

  song_data = Data()
  song_data.read_and_precess_file(file_name)
  song_data.sorted_data_by_Number_of_times(limit)
  song_data.write_file()
  #print(song_data.song_dict)


if __name__ == "__main__":
    main()
