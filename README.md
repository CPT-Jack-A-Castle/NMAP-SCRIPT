# NMAP-SCRIPT
Scan multiple IP addresses using Windows NMAP - create list of vulnerable IPs


This is written in Python for Windows CMD/PS.

It will implement batch files and python script to scan IP addresses provided by an excel spreadsheet.


NOTE!

CHANGE RELEVANT LOCATION AND NAMING DATA (see *NAMING DATA*)

Please check to see how to call your python in CMD.

Mine is written as "python3" but newer versions may require "py" instead.


You can download Python here:

https://www.python.org/downloads/release/python-3102/

Use the recommended installer


Once installed we will need to install pandas.

Open CMD and type -

pip install pandas


You will be required to have NMAP installed for Windows:

https://nmap.org/download.html

See under "Microsoft Windows binaries"

"Latest stable release self-installer"


We will be using the vulners.nse script to search for exploits.

Download latest version of vulners.nse here:

https://github.com/vulnersCom


Once your NMAP has been installed, replace vulners.nse here:

C:\Program Files (x86)\Nmap\scripts (typical location for 64bit Windows)


For uninterrupted scans I found that disabling the "Quick Edit Mode" on CMD fixed my issue.

Once the NMAP scan had started, it would get stuck and require a random key input to resume.

To do this open CMD, right click on the top left of the window and select "Defaults".

Untick the "Quick Edit Mode", click "OK" and close the CMD to save the setting.

Right click nmap_full_scan.bat file and run as administrator


*NAMING DATA*


The IP addresses are pulled from an Excel spreadsheet and column name, ensure to input them into the ip_add_bat.py file.

Change 'FILE-LOCATION' (eg:) 'C:\IPSCAN\ipaddresses.xlsx'

Change 'SHEET-NAME' (eg:) 'Sheet1'

Change 'COLUMN-NAME' (eg:) 'IP ADDRESS'


nmap_full_scan needs to edited to point to your 'FILE-LOCATION'

Using the above (eg:) C:\IPSCAN


crit_list.py needs to search a folder containing the .txt outputs from the NMAP scan.

Set "FOLDER-LOCATION" (eg:) C:\IPSCAN

#Remember to escape "\" within the code loop


I have added "pause" between certain steps to maintain control over the process, but they can be removed.


This is a work in progress and has been my first project involving Python and Windows batch files.

Feedback is welcome, specially to simplify the code as well as steps involved.

Currently I am working on using the "critical" output to link back to the original Excel sheet and highlight the critical IP Addresses.

-RAGECPT
