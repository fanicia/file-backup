import re
import os

base_path = f"C:{os.path.sep}Users{os.path.sep}Morten{os.path.sep}Projects{os.path.sep}file-backup{os.path.sep}testsubject{os.path.sep}source"
destination_path = f"C:{os.path.sep}Users{os.path.sep}Morten{os.path.sep}Projects{os.path.sep}file-backup{os.path.sep}testsubject{os.path.sep}destination"
changed_path = f"C:{os.path.sep}Users{os.path.sep}Morten{os.path.sep}Projects{os.path.sep}file-backup{os.path.sep}testsubject{os.path.sep}source{os.path.sep}folder1{os.path.sep}folder2{os.path.sep}sub-file1.txt"

# This turns the annoying "\" into "/", in case we are on windows
base_path = base_path.replace(os.path.sep, "/")
changed_path = changed_path.replace(os.path.sep, "/")

regex = re.compile(f"(?<={base_path})(.*)")

match = re.search(regex, changed_path)
print(match.group())

base_path = base_path.replace("/", os.path.sep)
changed_path = changed_path.replace("/", os.path.sep)
