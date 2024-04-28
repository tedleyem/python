import psutil
import platform
import subprocess
import os
#import torch # for gpu check
#from uptime import uptime

# TO DO 
# import Logos from Logos
# get gpu info 
# get uptime of system 

# more info on platform module 
# https://docs.python.org/3/library/platform.html

# Get user@hostname 
def get_current_user():
    print('Test: user@test')
    
# define system  
def get_os_info():
    #try:
    #    distribution = subprocess.check_output(['lsb_release', '-ds']).decode().strip()
    #    return distribution if distribution else platform.platform()
    #except FileNotFoundError:
    #return platform.platform()
    print('Test: OS: OS INFO')

# define host info 
def get_host_info():
    # https://docs.python.org/3/library/os.html
    #try:
    #    distribution = subprocess.check_output(['lsb_release', '-ds']).decode().strip()
    #    return distribution if distribution else platform.platform()
    #except FileNotFoundError:
    #    return platform.platform()
    print('Test: Host: HOST INFO')
    socket.gethostbyaddr(socket.gethostname())

# get kernel version
def get_kernel_version():
    print('Test: Kernel: kernel version')
    return platform.uname().release

# get uptime
def get_system_uptime():
    print('Test: Uptime: its on so its up (uptime)')

# get Packages 
def get_packages():
    print('Test: Packages: packages list')

# shell 
def get_shell_info():
    if platform.system() == 'Windows':
        return "CMD / PS"
    else:
        shell = os.environ.get('SHELL')
        if shell:
            return shell.split('/')[-1]
        return "Shell not detected"

# get resolution 
def get_resolution():
    print('Test: Resolution: resolution info')

# Desktop Environment
def get_desktop_environment():
    if platform.system() == 'Windows':
        return "Windows Explorer"
    else:
        de = os.environ.get('XDG_CURRENT_DESKTOP')
        if de:
            return de 
        return "DE not detected"
        print('DE: desktop env')

# Windows Manager 
def get_window_manager():
    wm = subprocess.getoutput('echo $XDG_SESSION_DESKTOP')
    if wm:
        return wm
    else:
        return "WM not detected"

# get terminal info 
def get_terminal_manager():
    print('Test: terminal info')

# get cpu info 
def get_cpu_name():
    if platform.system() == 'Windows':
        try:
            process = subprocess.Popen(
                "wmic cpu get name", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE
            )
            output, _ = process.communicate()
            output = output.decode("utf-8").strip().split("\n")
            return output[1] if len(output) > 1 else "CPU Name Not Found"
        except Exception as e:
            print(f"Error while fetching CPU name: {e}")
            return "CPU Name Not Found"
    elif platform.system() == 'Darwin':
        return platform.uname().processor
    elif platform.system() == 'Linux':
        with open('/proc/cpuinfo') as f:
            for line in f:
                if line.strip() and line.rstrip('\n').startswith('model name'):
                    return line.rstrip('\n').split(':')[1].strip()
    return 'CPU Name Not Found'

def get_cpu_util():
    cpu_utilization = f"{psutil.cpu_percent()}% utilized"
    return cpu_utilization

def get_cpu_info():
    full_cpu_info = print('{cpu_name} - {cpu_utilization}')
    #return full_cpu_info
    print('Test: cpu info')
    
# get gpu info 
def get_gpu_info():
    print('Test: gpu info')
    #gpu_data = torch.cuda.get_device_name()
    #print('test')
    #gpus = GPU.getGPUs()
    #gpu_data = [f"{gpu.name}" for gpu in gpus]
    ##gpu_info = print('GPU': ', '.join(gpu_data) )
    #return gpu_data

def get_mem_info():
    print('Test: memory info')
    #mem = psutil.virtual_memory()
    #mem_used = f"{int(mem.used / (1024 * 1024))}MB / {int(mem.total / (1024 * 1024))}MB"
    #return mem_used 

def color_theme_block():
    print('Test: Color theme block')

# Fetch the info collected
def fetch_sys_info():
    current_user = get_current_user()
    div_string = print('------------------------') 
    os_string = get_os_info()
    host_string = get_host_info()
    kernel_version = get_kernel_version()
    system_uptime = get_system_uptime() # kind of redundant but its cool 
    package_info = get_packages()
    shell_info = get_shell_info()
    res_info = get_resolution() 
    desktop_env = get_desktop_environment()
    window_manager = get_window_manager()
    terminal_info = get_terminal_manager()
    cpu_info = get_cpu_info()
    gpu_info = get_gpu_info()
    mem_info = get_mem_info()
    colors_info = color_theme_block()

    system_info = {
        '': current_user,
        '': div_string,
        'OS': os_string,
        'Host': host_string,
        'Kernel': kernel_version,
        'Uptime': system_uptime,
        'Packages': package_info,
        'Shell': shell_info,
        'Resolution': res_info,
        'DE': desktop_env,
        'WM': window_manager,
        'Terminal': terminal_info,
        'CPU': cpu_info,
        'GPU': gpu_info,
        'Memory': mem_info,
    },
    return system_info

# Print out all gathered info in for loop
def display_sys_info(system_info):

    total_lines = max(len(system_info))

    for line_num in range(total_lines): 
        sys_info_line = list(system_info.items())[line_num] if line_num < len(system_info) else None

        if sys_info_line:
            key, value = sys_info_line
#            if key == 'GPU':
#                print(f"{logo_line}{' ' * (max_logo_length - len(logo_line))}    {key}: {value}")
#            else:
#                print(f"{logo_line}{' ' * (max_logo_length - len(logo_line))}    {key}: {value}")
#        else:
#            print(f"{logo_line}{' ' * (max_logo_length - len(logo_line))}")

if __name__ == "__main__":
    sys_info = fetch_sys_info()
    
    display_sys_info(sys_info)

 