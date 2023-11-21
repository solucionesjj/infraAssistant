import shutil
import psutil
import math

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