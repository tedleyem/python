import os
import platform
import subprocess
import sys
import argparse

# Function to fetch system information
def get_system_info():
    system_info = {}

    # Get OS details
    system_info['OS'] = platform.system()
    system_info['OS Version'] = platform.version()
    system_info['Architecture'] = platform.architecture()[0]
    system_info['Machine'] = platform.machine()
    system_info['Processor'] = platform.processor()

    # Get Memory info (Linux-specific)
    if system_info['OS'] == 'Linux':
        memory = subprocess.check_output("free -h", shell=True).decode()
        system_info['Memory'] = memory.splitlines()[1]

    # Get CPU info (Linux and macOS-specific)
    if system_info['OS'] == 'Linux':
        cpu = subprocess.check_output("lscpu", shell=True).decode()
        system_info['CPU'] = cpu.splitlines()[0]
    elif system_info['OS'] == 'Darwin':  # macOS
        cpu = subprocess.check_output("sysctl -n machdep.cpu.brand_string", shell=True).decode()
        system_info['CPU'] = cpu.strip()

    # Get Disk space info
    disk = subprocess.check_output("df -h --total | grep total", shell=True).decode()
    system_info['Disk'] = disk.splitlines()[0]

    # Get Uptime
    uptime = subprocess.check_output("uptime -p", shell=True).decode()
    system_info['Uptime'] = uptime.strip()

    return system_info

# Function to print system information
def print_system_info(system_info):
    print(f"OS: {system_info['OS']} {system_info['OS Version']}")
    print(f"Architecture: {system_info['Architecture']}")
    print(f"Machine: {system_info['Machine']}")
    print(f"Processor: {system_info['Processor']}")
    if 'Memory' in system_info:
        print(f"Memory: {system_info['Memory']}")
    if 'CPU' in system_info:
        print(f"CPU: {system_info['CPU']}")
    print(f"Disk: {system_info['Disk']}")
    print(f"Uptime: {system_info['Uptime']}")

# Function to copy system info to clipboard
def copy_to_clipboard(system_info):
    # Prepare the text to copy
    info_text = "\n".join([f"{key}: {value}" for key, value in system_info.items()])
    
    # For Linux (requires xclip)
    if sys.platform == 'linux':
        try:
            subprocess.run(['xclip', '-selection', 'clipboard'], input=info_text, text=True, check=True)
            print("System info copied to clipboard!")
        except FileNotFoundError:
            print("xclip is not installed. Please install it to use clipboard functionality.")
    
    # For macOS (requires pbcopy)
    elif sys.platform == 'darwin':
        subprocess.run('pbcopy', input=info_text, text=True, check=True)
        print("System info copied to clipboard!")

# Main function to parse arguments and execute functionality
def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="System Info Fetcher like Neofetch")
    parser.add_argument('--copy', action='store_true', help="Copy system info to clipboard")

    # Parse arguments
    args = parser.parse_args()

    # Get system information
    system_info = get_system_info()

    # Print system information
    print_system_info(system_info)

    # If --copy is passed, copy the info to clipboard
    if args.copy:
        copy_to_clipboard(system_info)

if __name__ == "__main__":
    main()
