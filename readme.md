# DevOps ProCamp Entry Task

Script collects basic information about OS and prints to console

## Prerequisites

+ Supported Python versions are 2.7 and 3.4+.
+ psutil (python system and process utilities) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python.

## Installing

```
$ sudo apt-get install gcc python3-dev
$ sudo apt-get install python3-pip
$ sudo pip3 install psutil
```

## Usage

Assign the execution permissions

```
$ chmod +x ./dopc.py
```

Show help

```
$ ./dopc.py --help
```

Sample output

```
$ ./dopc.py
System: Linux
Node Name: ubuntu
Release: 5.3.0-28-generic
Version: #30~18.04.1-Ubuntu SMP Fri Jan 17 06:14:09 UTC 2020
Physical cores: 1
Total cores: 1
```
```
$ ./dopc.py cpu
system.cpu.idle 138508.03
system.cpu.user 3705.78
system.cpu.guest 0.0
system.cpu.iowait 164.2
system.cpu.stolen 0.0
system.cpu.system 1486.77
```
```
$ ./dopc.py mem
virtual total 2017083392
virtual used 942198784
virtual free 538390528
virtual shared 109682688
swap total 1023406080
swap used 810381312
swap free 213024768
```

## Built With

* [Visual Studio Code](https://code.visualstudio.com/) - Visual Studio Code editor

