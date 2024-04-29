import psutil
import platform
import subprocess as sp
import os

# TO DO 
# import Logos from Logos
# get gpu info  
# https://docs.python.org/3/library/platform.html
# subprocess 
# https://docs.python.org/3/library/subprocess.html#module-subprocess

# Get user@hostname 
def get_current_user():
    uname_output = sp.getoutput('whoami')
    hostname_output = sp.getoutput('hostname')
    print(uname_output + '@' + hostname_output)
    
# define system  
def get_os_info():
    os_output = sp.getoutput('uname -srm')
    print('OS: ' + os_output)

# define host info 
def get_host_info():
    #device_dir = sp.getoutput('cat /sys/devices/virtual/dmi/id/')
    dev_product_name = sp.getoutput('cat /sys/devices/virtual/dmi/id/product_name')
    dev_product_version = sp.getoutput('cat /sys/devices/virtual/dmi/id/product_version')
    # create if statement to check device files
    #dev_board_vendor = board_vendor     
    #dev_board_name = board_name       
    # host_output = sp.getoutput('command')
    # Host: 82SG IdeaPad 5 15ABA7 
    # product name #product version
    print('Host: ' + dev_product_name + ' ' + dev_product_version) 

# get kernel version
def get_kernel_version():
    host_output = sp.getoutput('uname -r')
    print('Kernel: ' + host_output)

# get uptime
def get_system_uptime():
    uptime = sp.getoutput("echo $(awk '{print $1}' /proc/uptime) / 60 | bc")
    print('Uptime: ' + uptime + ' minutes')

# get Packages 
def get_packages():
    print('Packages: TEST')

# shell 
def get_shell_info():
    print('Shell: TEST')

# get resolution 
def get_resolution():
    resolution_output = sp.getoutput("xdpyinfo | awk '/dimensions:/ {printf $2}'")
    print('Resolution: ' + resolution_output)

# Desktop Environment
def get_desktop_environment():
    print('DE: TEST')

# Windows Manager 
def get_window_manager():
    print('WM: TEST')

# get terminal info 
def get_terminal_manager():
    print('Terminal: TEST')

# get cpu info 
def get_cpu_info():
    print('CPU: TEST')
    
# get gpu info 
def get_gpu_info():
    print('GPU: TEST')

def get_mem_info(): 
    mem_used = sp.getoutput("xdpyinfo | awk '/dimensions:/ {printf $2}'")
    mem_total = sp.getoutput("xdpyinfo | awk '/dimensions:/ {printf $2}'")
    print('Memory: ' + mem_used + ' / ' + mem_total )

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

if __name__ == "__main__":
    fetch_sys_info()
    
 