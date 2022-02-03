
import sys
from tools import Data

def main():
  file_name = "data/input/song_data.csv"
  limit = 10
  file_name = sys.argv[1]
  limit = int(sys.argv[2])

  # dict_song,head = tls.read_and_precess_file(file_name)
  # sorted_dict_song = tls.sorted_data_by_Number_of_times(dict_song,limit)
  # tls.write_file(sorted_dict_song, head)

  song_data = Data()
  song_data.read_and_precess_file(file_name)
  print(song_data.song_dict)

if __name__ == "__main__":
    main()
