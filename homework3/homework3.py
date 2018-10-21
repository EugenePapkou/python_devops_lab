import configparser
import datetime
import json
import psutil
import time


configParser = configparser.RawConfigParser()
configParser.read("settings.conf")
output = configParser.get('common', 'output')
interval = float(configParser.get('common', 'interval')) * 60

i = 1
while True:
    cpu = psutil.cpu_percent(interval=1)
    disk = psutil.disk_usage('/')
    vm = psutil.virtual_memory()
    disk_io = psutil.disk_io_counters(perdisk=False)
    net_stat = psutil.net_if_stats()

    sys_state = [cpu, disk, vm, disk_io, net_stat]
    string = "\n\nCPU: " + str(cpu) + "\n\nDisk usage: " + str(disk) + \
             "\n\nVirtual memory: " + str(vm) + "\n\nIO information: " \
             + str(disk_io) + "\n\nNetwork statistics: " + str(net_stat)

    # creating timestamp
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S: ')

    if output == "plain":
        final_str = "\n\n SNAPSHOT %d:" % i + st + string
        with open("plain.txt", "a") as txt_file:
            txt_file.write(final_str)
        print("TIMESTAMP %d was written to plain.txt" % i)

    elif output == "json":
        dict_json = {"SNAPSHOT:": i, "TIMESTAMP": st, "CPU": cpu,
                     "DiskUsage": disk, "VirtualMemory": vm,
                     "IOInformation": disk_io, "NetworkStatistics": net_stat}
        with open('sys_info.json', 'a') as json_file:
            json.dump(dict_json, json_file)
        print("TIMESTAMP %d was written to sys_info.json" % i)
    else:
        print("Bad config (settings.conf). Please, check it.")
        break
    i += 1
    time.sleep(interval)
