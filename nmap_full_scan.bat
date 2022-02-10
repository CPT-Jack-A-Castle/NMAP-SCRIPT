cd "FILE-LOCATION"
mkdir output
python3 cmd_prompt.py > tool.bat

pause

cd output
"FILE-LOCATION"\tool.bat
cd ..
python3 crit_list.py > criticals.txt

pause