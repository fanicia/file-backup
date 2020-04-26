from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# importing the modules
import os.path
import shutil
import datetime
import time
import re

# getting the current working directory
src_dir = os.getcwd()

# printing current directory
print("########## File-backup started ###########")

class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            self.copy_file(event.src_path)
    
    def on_created(self, event):
        if not event.is_directory:
            self.copy_file(event.src_path)
        
    def copy_file(self, src):
        src_file_name = src.split(os.path.sep).pop()
        destination_sub_path = self.extract_changed_sub_path(folder_to_track, src)
        sub_path_list = destination_sub_path.split(os.path.sep)
        changed_file_name = sub_path_list.pop()
        path_to_file = f"{os.path.sep.join(sub_path_list)}{os.path.sep}"

        timestamp = datetime.datetime.now().strftime("%d-%m-%y-%H-%M") # not the prettiest datetime-format, but it's filename-friendly
        target = f"{destination}{path_to_file}{timestamp}-{changed_file_name}"
        print(os.linesep)
        print(src)
        print("       |")
        print("       |")
        print("       V")
        print(target)
        print(os.linesep)
        print("----------------------------------------")

        
        os.makedirs(f"{destination}{path_to_file}", exist_ok = True)    
        shutil.copy(src, target)

        

    def extract_changed_sub_path(self, base_path, changed_path):
        # This turns the annoying "\" into "/", in case we are on windows
        base_path = base_path.replace(os.path.sep, "/")
        changed_path = changed_path.replace(os.path.sep, "/")

        # use positive lookbehind assertion to find the part of the path after the base_path of the source
        regex = re.compile(f"(?<={base_path})(.*)")
        match = re.search(regex, changed_path)
        sub_path = match.group().replace("/", os.path.sep)
        return sub_path




folder_to_track = f"{os.getcwd()}{os.path.sep}testsubject{os.path.sep}source" 
destination = f"{os.getcwd()}{os.path.sep}testsubject{os.path.sep}destination"
print(f"{folder_to_track} --> {destination}")

event_handler = FileHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

print("########## File-backup ended ###########")