#/bin/python
sudo apt install python3.11 
sudo apt install python3.11-venv
python3 -m venv env && sleep 2
source env/bin/activate
python3 -m pip install -r requirements.txt 