import psutil
import platform
import subprocess as sp
import os
import random
from colorama import init
#init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

def credits():
    print('Created by Tedley Meralus | @zukukashi')
    #print('Report issues at https://github.com/tedleyem/python-dojo/issues')

def print_fetch_logo():
    logo = cprint(figlet_format('PyFETCH', font='nancyj-underlined'),
        'black', 'on_green', attrs=['bold'],) 

# Get user@hostname 
def get_current_user():
    uname_output = sp.getoutput('whoami')
    hostname_output = sp.getoutput('hostname')
    results = print(uname_output + '@' + hostname_output)
    
# define system  
def get_os_info():
    os_output = sp.getoutput('uname -srm')
    #print('OS: ' + os_output)
    print(os_output)

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
    #
    #print('Host: ' + dev_product_name + ' ' + dev_product_version) 
    print(dev_product_name + ' ' + dev_product_version) 

# get kernel version
def get_kernel_version():
    host_output = sp.getoutput('uname -r')
    #print('Kernel: ' + host_output)
    print(host_output)

# get uptime
def get_system_uptime():
    uptime = sp.getoutput("echo $(awk '{print $1}' /proc/uptime) / 60 | bc")
    #print('Uptime: ' + uptime + ' minutes')
    print(uptime)

# get Packages 
def get_packages():
    #print('Packages: TEST')
    print('TEST')

# shell 
def get_shell_info():
    #print('Shell: TEST')
    print('TEST')

# get resolution 
def get_resolution():
    resolution_output = sp.getoutput("xdpyinfo | awk '/dimensions:/ {printf $2}'")
    #print('Resolution: ' + resolution_output)
    print(resolution_output)

# Desktop Environment
def get_desktop_environment():
    #print('DE: TEST')
    print('TEST')


# Windows Manager 
def get_window_manager():
    #print('WM: TEST')
    print('TEST')

# get terminal info 
def get_terminal_manager():
    #print('Terminal: TEST')
    print('TEST')

# get cpu info 
def get_cpu_info():
    #print('CPU: TEST')
    print('TEST')
    
# get gpu info 
def get_gpu_info():
    #print('GPU: TEST')
    print('TEST')

def get_mem_info(): 
    mem_used = sp.getoutput("free --mega | awk '{print NR==1?$2:$1$4}'")
    mem_total = sp.getoutput("free --mega | awk '{print NR==1?$3:$1$4}'")
    #mem_total = sp.getoutput("awk '/^Mem/ {print $1}' < free -m")
    print('Memory: ' + mem_used + ' / ' + mem_total )

def color_theme_block():
    #print('Test: Color theme block')
    print('TEST')

# Fetch the info collected
def fetch_sys_info():
    div_string = print('------------------------') 
    fetch_logo = print_fetch_logo()
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
    div_string = print('------------------------') 


def fetch_sys_info_color():
    system_info = { 
        '': print('------------------------'),
        '': print_fetch_logo(),
        '': get_current_user(),
        '': print('------------------------'),  
        cprint('OS: ',"green"): get_os_info(), 
        cprint('Host: ',"green"): get_host_info(), 
        cprint('Kernel: ',"green"): get_kernel_version(), 
        cprint('Uptime: ',"green"): get_system_uptime(), 
        cprint('Packages: ',"green"): get_packages(),
        cprint('Shell: ',"green"): get_shell_info(), 
        cprint('Resolution: ',"green"): get_resolution(),
        cprint('DE: ',"green"): get_desktop_environment(),
        cprint('WM: ',"green"): get_window_manager(), 
        cprint('Terminal: ',"green"): get_terminal_manager(),
        cprint('CPU: ',"green"): get_cpu_info(),
        cprint('GPU: ',"green"): get_gpu_info(),
        cprint('Memory: ',"green"): get_mem_info(),
        '': print('------------------------'),  
        cprint('Credits: ',"white"): credits(),
        '': print('------------------------'),  
    },

    return system_info

if __name__ == "__main__":
    fetch_sys_info_color()
    
 