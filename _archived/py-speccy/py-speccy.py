import platform
import argparse

parser = argparse.ArgumentParser()
#parser.add

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    size_factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < size_factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= size_factor

def ram_stats():
    # Memory Information
    print("="*10, "Memory Information", "="*10)

def cpu_stats():
    # print CPU information
    print("="*10, "CPU Info", "="*10)

def disk_stats():
    # Disk Information
    print("="*10, "Disk Information", "="*10)
    print("Partitions and Usage:")

def more_stats():
    cpu_stats()
    disk_stats()
    ram_stats()

def System_information():
    print("="*10, "System Information", "="*10)
    print(f"user@hostname")
    uname = platform.uname()
    print(f"OS: {uname.system} {uname.release} {uname.machine}")
    print(f"Host: {uname.node}")
    print(f"Kernel: test")
    print(f"Uptime: test")
    print(f"Memory: test")
    print(f"Packages: test")
    print(f"Shell: test")
    #more_stats()
    print(f"CPU: test")
    print(f"RAM: test")
    print(f"Motherboard: test")
    print(f"Graphics: test")
    print(f"Storage: test")
    print(f"Optical Drives: test")
    print(f"Audio: test")
    print(f"")
    #print(f"Tip: --full for full system specs")
    #print(f"Tip: --h for help")

if __name__ == "__main__":
    System_information()
