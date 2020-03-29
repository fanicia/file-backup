from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# importing the modules
import os
import shutil
import datetime
import time

# getting the current working directory
src_dir = os.getcwd()

# printing current directory
print("########## File-backup started ###########")

class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if (not event.is_directory):
            self.copy_file(event.src_path)
        
    def copy_file(self, src):
            # split the src into list and get the last element to get the src_file
            src_file_name = src.split(os.path.sep).pop() 
            timestamp = datetime.datetime.now().strftime("%d-%m-%y-%H-%M") # not the prettiest datetime-format, but it's filename-friendly
            target = f"{destination}{os.path.sep}{timestamp}-{src_file_name}"
            print(os.linesep)
            print(src)
            print("       |")
            print("       |")
            print("       V")
            print(target)
            print(os.linesep)
            shutil.copy(src, target)

folder_to_track = f"{os.getcwd()}{os.path.sep}testsubject{os.path.sep}source" 
destination = f"{os.getcwd()}{os.path.sep}testsubject{os.path.sep}destination"
print(f"{folder_to_track} --> {destination}")

event_handler = FileHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=False)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
