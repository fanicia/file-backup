import re
import os

{os.path.sep}

base_path = f"C:{os.path.sep}Users{os.path.sep}Morten{os.path.sep}Projects{os.path.sep}file-backup{os.path.sep}testsubject{os.path.sep}source"

destination_path = f"C:{os.path.sep}Users{os.path.sep}Morten{os.path.sep}Projects{os.path.sep}file-backup{os.path.sep}testsubject{os.path.sep}destination"

changed_path = f"C:{os.path.sep}Users{os.path.sep}Morten{os.path.sep}Projects{os.path.sep}file-backup{os.path.sep}testsubject{os.path.sep}source{os.path.sep}folder1{os.path.sep}folder2{os.path.sep}sub-file1.txt"

escaped_base = re.escape(base_path)
escaped_changed_path = re.escape(changed_path)
print(escaped_base)
print(escaped_changed_path)


# if (re.match(f"^{re.escape(base_path)}", re.escape(changed_path))):
#     print(True)
# else:
#     print(False)


if re.match('^hello', 'helloworld'):
    print(True)
else:
    print(False)