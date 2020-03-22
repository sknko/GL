#!/usr/bin/python3

import platform
import argparse
import psutil

parser = argparse.ArgumentParser(description='Basic system info and Metrics')
parser.add_argument('switch', type=str, default="basicinfo", nargs='?', help='Optional switch cpu | mem')
args = parser.parse_args()

def basicinfo():
    print("System: {0}".format(platform.uname().system))
    print("Node Name: {0}".format(platform.uname().node))
    print("Release: {0}".format(platform.uname().release))
    print("Version: {0}".format(platform.uname().version))
    print("Physical cores: {0}".format(psutil.cpu_count(logical=False)))
    print("Total cores: {0}".format(psutil.cpu_count(logical=True)))

def cpu():
    print("system.cpu.idle {0}".format(psutil.cpu_times().idle))
    print("system.cpu.user {0}".format(psutil.cpu_times().user))
    print("system.cpu.guest {0}".format(psutil.cpu_times().guest))
    print("system.cpu.iowait {0}".format(psutil.cpu_times().iowait))
    print("system.cpu.stolen {0}".format(psutil.cpu_times().steal))
    print("system.cpu.system {0}".format(psutil.cpu_times().system))

def mem():
    print("virtual total {0}".format(psutil.virtual_memory().total))
    print("virtual used {0}".format(psutil.virtual_memory().used))
    print("virtual free {0}".format(psutil.virtual_memory().free))
    print("virtual shared {0}".format(psutil.virtual_memory().shared))
    print("swap total {0}".format(psutil.swap_memory().total))
    print("swap used {0}".format(psutil.swap_memory().used))
    print("swap free {0}".format(psutil.swap_memory().free))
    
# Implement a script which prints basic information about your OS to console
if args.switch == 'basicinfo':
    basicinfo()
# The script should accept a single parameter to specify which metrics set to print
# prints CPU metrics
elif args.switch == 'cpu':
    cpu()
# prints RAM metrics
elif args.switch == 'mem':
    mem()
else:
    parser.error("illegal switch")