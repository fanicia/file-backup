import re
import os



base_path = f"C:{os.path.sep}Users{os.path.sep}Morten{os.path.sep}Projects{os.path.sep}file-backup{os.path.sep}testsubject{os.path.sep}source"
destination_path = f"C:{os.path.sep}Users{os.path.sep}Morten{os.path.sep}Projects{os.path.sep}file-backup{os.path.sep}testsubject{os.path.sep}destination"
changed_path = f"C:{os.path.sep}Users{os.path.sep}Morten{os.path.sep}Projects{os.path.sep}file-backup{os.path.sep}testsubject{os.path.sep}source{os.path.sep}folder1{os.path.sep}folder2{os.path.sep}sub-file1.txt"

# This turns the annoying "\" into "/", in case we are on windows
base_path = base_path.replace(os.path.sep, "/")
changed_path = changed_path.replace(os.path.sep, "/")

# print(base_path)
# print(changed_path)

regex = re.compile(f"({base_path})(.*)")

if re.match(regex, changed_path):
    match = re.search(regex, changed_path)
    print(match.group())
    print(match.group(0))
    print(match.group((1)))
else:
    print(False)


base_path = base_path.replace("/", os.path.sep)
changed_path = changed_path.replace("/", os.path.sep)
# print(base_path, "\n", changed_path)
