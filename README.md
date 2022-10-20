The script was run on Windows 10 WSL2 Ubuntu 20.04 LTS.

### Step 1. Install Python 3.11

How to install the python version we need you can check [here](https://linuxways.net/ubuntu/how-to-install-python-3-11-on-ubuntu-20-04/) or follow the steps:

* Update Ubuntu package lists
```
sudo apt update
```
* Then install the software-properties-common package
```
sudo apt install software-properties-common
```
* Let's add deadsnakes PPA, which provides the latest versions of Python
```
sudo add-apt-repository ppa:deadsnakes/ppa
```
* Installing Python 3.11
```
sudo apt install python3.11
```
* Install additional packages
```
sudo apt install python3.11-dev python3.11-venv -y
```

### Step 2. Create an environment to download packages
```
python3.11 -m venv [environment name]
````
Switching environments:
```
source [environment name]/bin/activate
```
*Success!* 😊

### Step 3. Load all the required libraries.
Let's use the **requirements.txt** file

```
pip install -r requirements.txt
```
The libraries necessary for work will be loaded.

### Step 4. New error.
When you try to execute the script a new error will appear: **"ValueError: index cannot be a set "**.

Pay attention to which file and line the error refers to  
**File "<...>/lib/python3.11/site-packages/pandas/core/frame.py", line 637, in __init__**

Error correction:
* go to the directory with this file 
```
cd <...>/lib/python3.11/site-packages/pandas/core
```
* open the file (personally, I use **nano**)
```
nano frame.py
```
* find the line containing our error **"index cannot be a set "**, expectedly it is line 636, although in actuality it is 640. These lines should be commented or deleted. 
```
#if index is not None and isinstance(index, set):
#    raise ValueError("index cannot be a set")
```
* Save the changes

After that, the script should work correctly.
