import time
import re
from DjangoLogAnalysis.livegraph import live_plotter
import numpy as np
def main(path):
	f = open(path, 'r')
	count = 0
	asctimne_pre=''
	line1=[]
	x_vec = ["-10s","-9s","-8s","-7s","-6s","-5s","-4s","-3s","-2s","-1s","0"]
	y_vec = [0,0,0,0,0,0,0,0,0,0,0]
	while True:
		line = f.readline()
		if line =='':
			y_vec[-1] = 0
			line1 = live_plotter(x_vec,y_vec,line1)
			y_vec = np.append(y_vec[1:],0.0)
		else:
			try:
				line = line.split(' - ')
				level= line[0]
				acstime = line[1]
				acstime= re.findall(r"\d\d\d\d-\d\d-\d\d\ \d\d:\d\d:\d\d",acstime)
				message = line[2]
				if acstime == asctimne_pre:
					count +=1
				else:
					asctimne_pre = acstime
					y_vec[-1] = count
					line1 = live_plotter(x_vec,y_vec,line1)
					y_vec = np.append(y_vec[1:],0.0)
					count = 0
			except:
				pass