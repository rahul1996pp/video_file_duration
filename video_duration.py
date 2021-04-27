import datetime
from datetime import timedelta
from moviepy.editor import VideoFileClip
from texttable import Texttable
from pathlib import Path


def file_duration(file_name):
    clip = VideoFileClip(file_name)
    duration = clip.duration
    filename_list.append(file_name)
    duration_sec.append(duration)
    vide_duration_seconds = str(timedelta(seconds=duration))
    duration_list.append(duration_split(vide_duration_seconds))


def duration_split(data):
    data = data.split(":")
    return f'{data[0]}H:{data[1]}M:{data[2].split(".")[0]}S'


def draw_table():
    t = Texttable()
    data = zip(filename_list, duration_list)
    data_list = [list(i) for i in data]
    t.header(headers)
    t.add_rows(data_list, header=False)
    t.set_cols_align(['c', 'c'])
    print(t.draw())
    total_time = duration_split(str(datetime.timedelta(seconds=sum(duration_sec))))
    print("[*] Total time is :- ", total_time)
    with open("output.txt", 'a') as fi:
        code = """
           VIDEO FILES DURATION CALCULATOR
           
 ██▀███   ▄▄▄       ██░ ██  █    ██  ██▓    
▓██ ▒ ██▒▒████▄    ▓██░ ██▒ ██  ▓██▒▓██▒    
▓██ ░▄█ ▒▒██  ▀█▄  ▒██▀▀██░▓██  ▒██░▒██░    
▒██▀▀█▄  ░██▄▄▄▄██ ░▓█ ░██ ▓▓█  ░██░▒██░    
░██▓ ▒██▒ ▓█   ▓██▒░▓█▒░██▓▒▒█████▓ ░██████▒
░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░ ▒░▓  ░
  ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░▒░ ░░░▒░ ░ ░ ░ ░ ▒  ░
  ░░   ░   ░   ▒    ░  ░░ ░ ░░░ ░ ░   ░ ░   
   ░           ░  ░ ░  ░  ░   ░         ░  ░ code generated by Rahul.p
"""
        fi.write(code)
        fi.write(t.draw())
        fi.write(f"\n[*] Total time is :- {total_time}")


def main():
    global duration_sec, filename_list, duration_list, headers
    duration_sec = []
    filename_list = []
    duration_list = []
    headers = ['File name', 'Duration']
    count = 1
    folder = input("[+] Enter folder name or drag and drop :- ").replace('"', '')
    for ext in ["**/*.mp4", "**/*.mkv"]:
        file_data = Path(folder).glob(ext)
        for file in file_data:
            print("[+] Processing file :- ", count, end='\r')
            file_duration(str(file))
            count += 1
    draw_table()


def credit():
    print("""
           VIDEO FILES DURATION CALCULATOR
           """)
    print("""
 ██▀███   ▄▄▄       ██░ ██  █    ██  ██▓    
▓██ ▒ ██▒▒████▄    ▓██░ ██▒ ██  ▓██▒▓██▒    
▓██ ░▄█ ▒▒██  ▀█▄  ▒██▀▀██░▓██  ▒██░▒██░    
▒██▀▀█▄  ░██▄▄▄▄██ ░▓█ ░██ ▓▓█  ░██░▒██░    
░██▓ ▒██▒ ▓█   ▓██▒░▓█▒░██▓▒▒█████▓ ░██████▒
░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░ ▒░▓  ░
  ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░▒░ ░░░▒░ ░ ░ ░ ░ ▒  ░
  ░░   ░   ░   ▒    ░  ░░ ░ ░░░ ░ ░   ░ ░   
   ░           ░  ░ ░  ░  ░   ░         ░  ░ code generated by Rahul.p
""")


try:
    credit()
    main()
except KeyboardInterrupt:
    print("[-] Exiting ....")
except OSError:
    print("[-] Can't read the file skipping ")
except Exception as ex:
    print("[-] Error occurred :- ", ex)
