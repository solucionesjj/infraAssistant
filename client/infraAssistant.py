import shutil
import psutil
import math
import platform
import json
import win32security
import datetime
import wmi


c = wmi.WMI()

# print(c.Win32_UserAccount())

# Get user accounts and last login times
for user in c.Win32_UserAccount():
    # print(user.Name)
    user_info = c.Win32_NetworkLoginProfile(user.Name)
    # if user_info:
    #     last_login = user_info[0].LastLogon.strftime("%Y-%m-%d %H:%M:%S") if user_info[0].LastLogon else "Never logged in"
    # else:
    #     last_login = "Error retrieving data"
    # print(f"User: {user.Name} - Last Login: {last_login}")

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

# get_all_storage_devices_space()




# print(get_os_info())

# print(json.dumps(psutil.net_if_addrs(), indent=1))

# Linux
# import subprocess

# # Get user accounts from /etc/passwd
# with open('/etc/passwd', 'r') as passwd_file:
#     users = [line.split(':')[0] for line in passwd_file.readlines()]

# # Get last login times
# last_logins = {}
# for user in users:
#     try:
#         last_login = subprocess.check_output(['lastlog', '-u', user]).decode('utf-8').split('\n')[-2].split()
#         last_logins[user] = last_login[4] if len(last_login) > 1 else "Never logged in"
#     except subprocess.CalledProcessError:
#         last_logins[user] = "Error retrieving data"

# # Print user accounts and last login times
# for user, last_login in last_logins.items():
#     print(f"User: {user} - Last Login: {last_login}")

# MAC
# import subprocess

# # Get user accounts
# users = subprocess.check_output(['dscl', '.', 'list', '/Users']).decode('utf-8').split('\n')

# # Get last login times
# last_logins = {}
# for user in users:
#     if user:
#         last_login = subprocess.check_output(['last', '-1', user]).decode('utf-8').split('\n')[0].split()
#         last_logins[user] = last_login[4] if len(last_login) > 1 else "Never logged in"

# # Print user accounts and last login times
# for user, last_login in last_logins.items():
#     print(f"User: {user} - Last Login: {last_login}")






