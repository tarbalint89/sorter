import os
import shutil
from datetime import datetime

# create batch file with this code in it: "C:\Program Files\Python39\python.exe" "D:\sorter.py"
# then place it here:
# C:\Users\Bálint\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
# and the script starts on every statup


d = {"Images": [".jpg",".jpeg",".png",".gif"],
        "Videos": [".avi",".mkv",".mp4"],
        "Music":[".mp3",".wav"],
        "Executables": [".exe", ".msi"],
        "Documents": [".pdf",".doc",".md",".txt"],
        "Compressed": [".zip",".iso",".rar",".7zip"],
        "Scripts": [".py",".js",".c",".sh"],
        "Python Wheels": [".whl"],
        "Torrents": [".torrent"],
        "Linux Packages": [".deb"]}

paths = {"Images": "D:\\Files\\Images\\",
        "Videos": "D:\\Files\\Videos\\",
        "Music": "D:\\Files\\Music\\",
        "Executables": "D:\\Files\\Executables\\",
        "Documents": "D:\\Files\\Documents\\",
        "Compressed": "D:\\Files\\Compressed\\",
        "Scripts": "D:\\Files\\Scripts\\",
        "Python Wheels": "D:\\Files\\Python Wheels\\",
        "Torrents": "D:\\Files\\Torrents\\",
        "Linux Packages": "D:\\Files\\Linux Packages\\"
        }

try:
	if __name__ == "__main__":
	    downloads = os.listdir("C:\\Users\\Bálint\\Downloads")
	    for file in downloads:
	        for i in d:
	            for e in d[i]:
	                if e in file:
	                    shutil.move("C:\\Users\\Bálint\\Downloads\\"+file, paths[i]+file)
except Exception as e:
	print(e)
	with open("D:\\Files\\logs.txt", "a") as f:
		time = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
		data = str(time)+" --- "+e
		f.write(data)
