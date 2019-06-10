import re,time
from datetime import datetime
import os, sys
from DjangoLogAnalysis import user_behavior
def log_analyst(line,list_usersname):
    result=''
    if 'INSERT INTO "request_request"' in line and 'login' in line:
        query = re.findall(r"args=\[(.+)\]",line)
        if re.match(r"(datetime.+\)), F",query[0]):
            time = re.findall(r"(datetime.+\)), F",query[0])[0]
            times = re.findall(r"\((.+)\)",time)[0]
            times = times.replace(' ',',').split(',,')
            times = datetime(int(times[0]),int(times[1]),int(times[2]),int(times[3]),int(times[4]),int(times[5]))
            query=query[0].replace(time,'time').split(',')
        else:
            times = re.findall(r"(\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d)", query[0])[0]
            query=query[0].replace(times,'time').split(',')
        status = query[0]
        method = re.findall(r"(POST|GET|PUT|DELETE)",query[1])[0]
        ip = re.findall(r"(\d+.\d+.\d+.\d+)",query[6])[0]
        path = query[2]
        user = query[9]
        result = "|%20s|%10s|%20s|%100s|%50s|%20s|\n"%(times,status,str(ip),str(user),str(path),list_usersname)
        list_usersname=''
    return result, list_usersname

def main(path):
    f = open(path, 'r')
    line = 'begin'
    lines =''
    list_usersname = ''
    login_detail="|%20s|%10s|%20s|%100s|%50s|%20s| \n"%('Time','status', 'IP','user agent','path','attach to user')
    while line !='':
        line = f.readline()
        if not re.match(r"(INFO|DEBUG|WARNING|ERROR|CRITICAL)",line):
            lines += line
        else:
            if lines !='':
                if "username" in lines and "auth_user" in lines:
                    username = re.findall(r"('\w+')",lines)
                    if username:
                        username = username[0].split("'")
                        username = username[1]
                        list_usersname = username
                result,list_usersname = log_analyst(lines,list_usersname)
                if result !='':
                    login_detail +=result
            lines = line
    f.close()
    link = os.path.abspath(os.path.dirname(sys.argv[0]))
    f = open(link+'\ResultAnalysis\\analys_login.txt','w')
    f.write(login_detail) 
    f.close()
    user_behavior.main(path)