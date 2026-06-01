import os
import subprocess

files = os.listdir("videos")
for file in files:
    tn = file.split("[")[0].split("Hindi")[1]
    file_name = file.split(" ｜ ")[0]
    print(tn ,file_name)
    subprocess.run(["ffmpeg" ,"-i", f"videos/{file}" , f"audios/{tn}_{file_name}.mp3"])

