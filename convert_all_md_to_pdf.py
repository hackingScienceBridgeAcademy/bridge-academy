import fnmatch
import os
from shutil import copyfile
from os.path import basename

matches = []
ims = []

for root, dirnames, filenames in os.walk('.'):
    for filename in fnmatch.filter(filenames, '*.md'):
        os.system("markdown-pdf " + os.path.join(root, filename) + " -o ./PDFs/" + os.path.splitext(filename)[0] + ".pdf")
