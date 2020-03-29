# Inspiration from https://www.includehelp.com/python/copy-and-replace-files-in-python.aspx 
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
print(src_dir) 

class MyFileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        event.
        self.copy_file()
    
    def on_created(self, event):
        self.copy_file()
        
    def copy_file(self):
        for source_file in os.listdir(folder_to_track):
            src = f"{folder_to_track}{os.path.sep}{source_file}"
            timestamp = datetime.datetime.now().strftime("%d-%m-%y-%H-%M")
            target = f"{destination}{os.path.sep}{timestamp}-{source_file}"
            shutil.copy(src, target)

folder_to_track = f"{os.getcwd()}{os.path.sep}testsubject{os.path.sep}source" 
destination = f"{os.getcwd()}{os.path.sep}testsubject{os.path.sep}destination"
event_handler = MyFileHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
