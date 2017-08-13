import fnmatch
import os
from shutil import copyfile

matches = []
ims = []

for root, dirnames, filenames in os.walk('../Go4Code/summer_school'):
    for filename in fnmatch.filter(filenames, '*.md'):
        matches.append(os.path.join(root, filename))

for root, dirnames, filenames in os.walk('../Go4Code/summer_school'):
    for filename in fnmatch.filter(filenames, '*.png'):
        ims.append(os.path.join(root, filename))

for root, dirnames, filenames in os.walk('../Go4Code/summer_school'):
    for filename in fnmatch.filter(filenames, '*.jpg'):
        ims.append(os.path.join(root, filename))

for root, dirnames, filenames in os.walk('../Go4Code/summer_school'):
    for filename in fnmatch.filter(filenames, '*.jpeg'):
        ims.append(os.path.join(root, filename))

teacher_files = [
"trinket_links.md"
]

for m in matches:
    fname = os.path.basename(m)

    if fname in teacher_files:
        copyfile(m, "./teachers/"+fname)
    else:
        copyfile(m, "./docs/"+fname)

for m in ims:
    fname = os.path.basename(m)
    copyfile(m, "./docs/media/"+fname)
