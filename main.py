
import sys
import tools as tls

def main():
  file_name = "data/input/song_data.csv"
  limit = 10
  file_name = sys.argv[1]
  limit = int(sys.argv[2])

  dict_song,head = tls.read_and_precess_file(file_name)
  sorted_dict_song = tls.sorted_data_by_Number_of_times(dict_song,limit)
  tls.write_file(sorted_dict_song, head)


if __name__ == "__main__":
    main()
