import os
import xml.etree.ElementTree as ET
from os import listdir
from os.path import isfile, join


# Get the History directory
historyDirectory="I:\Fancyclopedia History"

userCounts={}

# Walk the site directory finding the XML file for each page
# pages are located at a/a/<name>
alphabet="abcdefghijklmnopqurstuvwxyz0123456789"
for i in range(0, len(alphabet)-1):     # First letter
    for j in range(0, len(alphabet)-1):     # Second letter
        dirname=os.path.join(historyDirectory, alphabet[i], alphabet[j])
        if os.path.isdir(dirname):
            dirs=[join(dirname, f) for f in listdir(dirname) if os.path.isdir(join(dirname, f))]
            for dir in dirs:        # pages
                subdirs=[join(dir, f2) for f2 in listdir(dir) if os.path.isdir(join(dir, f2))]
                for subdir in subdirs:      # Versions
                    e=ET.parse(os.path.join(subdir, "metadata.xml")).getroot()
                    id=e.find("name").text.strip()
                    if id in userCounts.keys():
                        userCounts[id]=userCounts[id]+1
                    else:
                        userCounts[id]=1


# Print a listing sorted by user ID
keys=userCounts.keys()
keys=sorted(keys)
print("\n\n\nListing by user\n")
for key in keys:
    print(key+": "+str(userCounts[key]))

# Print a listing sorted by count
print("\n\n\nListing by count\n")
for w in sorted(userCounts, key=userCounts.get, reverse=True):
  print(w+":  "+str(userCounts[w]))