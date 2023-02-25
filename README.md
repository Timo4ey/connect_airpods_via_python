# Connection airpods to lamptop bind (Linux)

If want to automate connecting and disconnect your Airpods to your laptop clicking a couple of buttons then you are in the right place.

There are you'll find the easy way to do it.

Just follow the steps.

## Step 1. Create a clone 
## Step 2. Change the content of the varaible `airpods_address`
1. Change the content of the varaible `airpods_address` in file `config.py` to your device's address.

How to check addres of your device?
Just connect you device rutine way and run this command `bluetoothctl info` in the console. The first string will be the address of your devise.

Write out this code in the ` config.py`
```python
airpods_address = 'ID of your device'
```
## Step 3. Change the path to your `main.py` file 
0. Open the directory where is the repo 
1. Use the command to know the path `readlink -f scr/main.py`
2. Open file `airpodsPro.sh` and change the path to yours
Here
```bash
python3 /home/connect_airpods_python/scr/main.py
```
## Step 4. Change the rules
Execute this command to make the script runnable for you : `chmod u+x airpodsPro.sh`

## 5. Add Shortcut
You can do use UI Settings -> Keyboard -> Keyboard Shortcuts -> scroll down -> Custom Shortcuts
![alt]('img/Screenshot from 2023-02-25 16-24-02.png')