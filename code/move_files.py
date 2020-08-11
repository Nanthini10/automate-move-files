import zipfile
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# pip install watchdog
import json
import time

class MoveHandler(FileSystemEventHandler):
	# When the destination folder is modified we will perform the following checks and move
	def on_modified(self, event):
		for file in os.listdir(source_folder):

			src = os.path.join(source_folder, file)
			name, extension = os.path.splitext(src)

			if os.path.isdir(src):
				destination = os.path.join(destination_folder, "Folders")
			else:
				destination = None
				# Alter these extensions as you please appropriately
				img_exts = [".jpg", ".jpeg", ".png"]
				docs_exts = [".pdf", ".docx", ".doc", ".mobi"]
				code_exts = [".py", ".ipynb", ".sh", ".run"]
				html_exts = [".html", ".htm", ".json"]
				data_exts = [".csv", ".orc", ".parquet"]
				disk_exts = [".dmg", ".app", ".pkg"]
				cal_exts = [".ics"]
				video_exts = [".mov", ".mp4"]
				audio_exts = [".mp3"]
				compressed_exts = [".zip", ".bz2"]
				# Under destination folder create the follow folders and as many as you please
				if extension in img_exts:
					destination = os.path.join(destination_folder, "Images")
				elif extension in docs_exts:
					destination = os.path.join(destination_folder, "Docs")
				elif extension in code_exts:
					destination = os.path.join(destination_folder, "Code")
				elif extension in html_exts:
					destination = os.path.join(destination_folder, "Webpages")
				elif extension in data_exts:
					destination = os.path.join(destination_folder, "Data")
				elif extension in disk_exts:
					destination = os.path.join(destination_folder, "Apps")
				elif extension in cal_exts:
					destination = os.path.join(destination_folder, "Calendar")
				elif extension in video_exts:
					destination = os.path.join(destination_folder, "Video")
				elif extension in audio_exts:
					destination = os.path.join(destination_folder, "Audio")
				elif extension in compressed_exts:
					destination = os.path.join(destination_folder, "Zip")
				else:
					# Did not match any of the interested extensions!
					destination = os.path.join(destination_folder, "Misc")

			if destination:
				shutil.move(src, destination)

# Change source and destination as needed.
source_folder = "/users/Nanthini/Downloads/"

destination_folder = "/users/Nanthini/Desktop/Downloaded/"

move_handler = MoveHandler()
obeserver = Observer()
obeserver.schedule(move_handler, source_folder, recursive=True)
obeserver.start()

try:
	while True:
		time.sleep(10)
except KeyboardInterrupt:
	obeserver.stop()
obeserver.join()