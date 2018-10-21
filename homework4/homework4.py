import configparser
import datetime
import json
import psutil
import time


class SnapshotState(object):
    def __init__(self):
        self.cpu = psutil.cpu_percent(interval=1)
        self.disk = psutil.disk_usage('/')
        self.vm = psutil.virtual_memory()
        self.disk_io = psutil.disk_io_counters(perdisk=False)
        self.net_stat = psutil.net_if_stats()

    @staticmethod
    def time_stamp():
        time_stamp = time.time()
        time_stamp_h = (datetime.datetime.fromtimestamp(time_stamp).
                        strftime('%Y-%m-%d %H:%M:%S: '))
        return time_stamp_h

    def get_state_in_plain(self, i):
        time_st = self.time_stamp()
        sys_stat = ("\n\n SNAPSHOT %d:" % i + time_st +
                    "\n\nCPU: " + str(self.cpu) +
                    "\n\nDisk usage: " + str(self.disk) +
                    "\n\nVirtual memory: " + str(self.vm) +
                    "\n\nIO information: " + str(self.disk_io) +
                    "\n\nNetwork statistics: " + str(self.net_stat))
        return sys_stat

    def get_state_in_json(self, i):
        time_st = self.time_stamp()
        dict_json = {"SNAPSHOT": i, "TIMESTAMP": time_st,
                     "CPU": self.cpu, "DiskUsage": self.disk,
                     "VirtualMemory": self.vm,
                     "IOInformation": self.disk_io,
                     "NetworkStatistics": self.net_stat}
        return dict_json


class ParserWriter(object):
    output = None
    interval = None

    def parser_config(self, conf_file_path):
        config_parser = configparser.RawConfigParser()
        config_parser.read(conf_file_path)
        self.output = str(config_parser.get('common', 'output'))
        self.interval = float(config_parser.get('common', 'interval')) * 60

    def writer_file(self, conf_file_path):
        i = 1
        self.parser_config(conf_file_path)
        while True:

            if self.output == "plain":
                state_now = SnapshotState()
                snapshot_data = state_now.get_state_in_plain(i)
                with open("plain.txt",
                          "a") as txt_file:
                    txt_file.write(snapshot_data)
                print("TIMESTAMP %d was written to plain.txt" % i)

            elif self.output == "json":
                state_now = SnapshotState()
                snapshot_data = state_now.get_state_in_json(i)
                with open("sys_info.json", 'a') as json_file:
                    json.dump(snapshot_data, json_file)
                print("TIMESTAMP %d was written to sys_info.json" % i)
            else:
                print("Bad config (settings.conf). Please, check it.")
                break
            i += 1
            time.sleep(self.interval)


obj_run_monitoring = ParserWriter()
obj_run_monitoring.writer_file("settings.conf")
