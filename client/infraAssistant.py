import shutil
import psutil
import math
import platform

def get_os_info():
    system = platform.system()
    release = platform.release()
    version = platform.version()
    machine = platform.machine()
    processor = platform.processor()
    uname = platform.uname()

    return f"Operating System: {system}, Release: {release}, Version: {version}, Machine: {machine}, Processor: {processor}, Uname info: {uname}"


def get_space(directory):
    total, used, free, percent = psutil.disk_usage(directory)
    return math.ceil(total/ (1024 * 1024 * 1024)), math.ceil(used/ (1024 * 1024 * 1024)), math.ceil(free / (1024 * 1024 * 1024)), percent

def get_all_storage_devices_space():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        if (partition.fstype):
            device = partition.device
            print(device)
            total, used, free, percent = get_space(partition.mountpoint)
            print(f"Device: {device}, {partition.mountpoint}, Total Space: {total} GigaBytes,Used Space: {used}, Free Space: {free} GigaBytes. ({percent}%)")

get_all_storage_devices_space()




print(get_os_info())