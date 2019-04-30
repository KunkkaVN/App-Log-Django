from pymongo import MongoClient
import pymongo
import datetime
from config import config_mongodb as mg
def connect_db():	
	connection = MongoClient(mg["MONGODB_HOST"], mg["MONGODB_PORT"])
	collection = connection[mg["DB_NAME"]][mg["COLLECTION_NAME"]]
	return collection

collection = connect_db()

def distane_time(time):
	time = time + datetime.timedelta(0,900)
	return time
def GMT7(time):
	time = time + datetime.timedelta(0,25200)
	return time
def get_data(collection):
	x=[]
	y=[]
	number= 0
	logs = collection.find()
	begin= logs[0]["time"]
	for log in logs:
		time = log["time"]
		print (time)
		if begin<= time and time < distane_time(begin):
			number +=1		
		else:
			x.append(GMT7(begin).strftime('%H:%M:%S'))
			y.append(number)
			begin = distane_time(begin)		
			number =0
	x.append(GMT7(begin).strftime('%H:%M:%S'))
	y.append(number)
	return x,y
x,y = get_data(collection)

from livegraph import static_plotter
static_plotter(x,y)

