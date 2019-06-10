import re,time
from datetime import datetime
import os, sys
def main(path):
    link = os.path.abspath(os.path.dirname(sys.argv[0]))
    f = open(path, 'r')
    line = 'begin'
    g = open(link+'\ResultAnalysis\\user_behavior.txt','w')
    write= "|%20s|%100s|\n"%('Time','Behaviour')
    g.write(write)
    while line !='':
        line = f.readline()
        if re.match(r"(INFO)",line):
            time = re.findall(r"(\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d)", line)[0]
            line=line.replace(time,'time').split(' - ')
            write= "|%20s|%100s"%(time,line[2])
            g.write(write)
    g.close()
    f.close()