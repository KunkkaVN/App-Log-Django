import re,time
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
x=[]
array_count=[]
array_info =[]
array_debug =[]
array_warning =[]
array_error =[]
array_critical =[]
def read_log_count(path):
    count = 0
    info = 0
    debug = 0
    warning =0
    error = 0
    critical =0 
    asctimne_pre=''
    f = open(path, 'r')
    line = 'begin'
    while line !='':
        line = f.readline()
        levelname = re.findall(r"(INFO|DEBUG|WARNING|ERROR|CRITICAL)",line)
        asctime_now = re.findall(r"\d\d\d\d-\d\d-\d\d\ \d\d:\d\d:\d\d",line)
        if levelname:
            if asctime_now[0]== asctimne_pre:
                count +=1
                if levelname[0] == "INFO":
                    info +=1
                elif levelname[0] == "DEBUG":
                    debug +=1
                elif levelname[0] == "WARNING":
                    warning +=1
                elif levelname[0] == "ERROR":
                    error +=1
                elif levelname[0] == "CRITICAL":
                    critical +=1
            else:
                asctimne_pre = asctime_now[0] 
                now = datetime.strptime(asctimne_pre, "%Y-%m-%d %H:%M:%S")
                x.append(now)
                array_count.append(count)
                array_info.append(info)
                array_debug.append(debug)
                array_warning.append(warning)
                array_error.append(error)
                array_critical.append(critical)
                count=0
                info= 0
                debug = 0
                warning =0
                error = 0
                critical = 0
def graph_log():
    plt.plot(x,array_info)
    plt.plot(x,array_debug)
    plt.plot(x,array_warning)
    plt.plot(x,array_error)
    plt.plot(x,array_critical)
    plt.gcf().autofmt_xdate()
    plt.legend(['info', 'debug', 'warning', 'error','critical'], loc='upper right')
    plt.show()
def main(path):
    read_log_count(path)
    graph_log()