import re
import pandas as pd
import subprocess

#NOTE THAT THE DATA NEEDS TO BE IMPORTED FROM AN EXCEL SHEET GIVEN IN THE BELOW LINE
data = pd.read_excel (r'FILE-LOCATION', sheet_name='SHEET-NAME')
df = pd.DataFrame(data, columns= ['COLUMN-NAME'])

ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
ipl = df.values.tolist()
ip_add = []
ip_rem = []

#BELOW SCRIPT WILL FILTER FOR IP ADDRESSES, ANYTHING ELSE IS PUT INTO ip_rem LIST
for s in ipl:
    var = (str(s).translate({ord(i): None for i in "[']"}))
    if ip_add_pattern.search(str(var)):
        ip_add.append(var)
    else: ip_rem.append(var)

#BELOW SCRIPT CREATES BATCH FILE, YOU CAN CHANGE THE NMAP FLAGS AND NAMING CONVENTION TO SUIT YOUR NEEDS
i = 0
while i < len(ip_add):
    name = (str(ip_add[i].replace(".","_"))+".txt ")
    print(("nmap --script vulners.nse -v -sV -T4 --max-retries 1 -oN ")+(name)+(ip_add[i]))
    i = i + 1