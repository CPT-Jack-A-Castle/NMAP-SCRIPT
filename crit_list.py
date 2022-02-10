import os
import re

path = "FOLDER-LOCATION"
all_files = os.listdir(path)

#REMEMBER TO ESCAPE "\" (EG:) C:\\IPSCAN
new_list = []
for root, dirs, files in os.walk("FOLDER-LOCATION"):
    for file in files:
        if file.endswith('.txt'):
            with open(os.path.join(root, file), 'r') as f:
                if 'EXPLOIT' in f.read():
                    with open(os.path.join(root, file), 'r') as f:
                        new_list.append(str(f.read()))

var = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

crit_list =  []
for s in new_list:    
    crit_list.append(var.findall(s)[0])

i = 0
while i < len(crit_list):
    print(crit_list[i])
    i = i + 1
