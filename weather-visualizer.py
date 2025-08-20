import random

from datetime import datetime , timedelta
import matplotlib.pyplot as plt

class weatherdata :
    def __init__ (self , date , temprature ):
        self.date = date
        self.temprature =  temprature 

start_date = datetime.now()
weather_data = []

for i in range (30):
    day = start_date + timedelta(days = i)
    temp = round (random.uniform(5 , 35) ,  1)
    weather_data.append(weatherdata(day , temp))

cold_days = []
mild_days = []
hot_days = []


for data in weather_data :
    if data.temprature < 15 :
        cold_days . append (data)
    elif data.temprature <= 25 :
        mild_days . append (data)
    else:
        hot_days . append (data)


labels = ["cold (<15 c)" , "mild(15-25 c)" , "hot (>25 c )"]
sizes = [len(cold_days) , len(mild_days) , len(hot_days)]
colors = ["skyblue" , "gold" , "tomato"]


plt.figure(figsize= (6 , 6) )
plt.pie(sizes , labels=labels ,colors=colors , autopct = "%1.1f%%" , startangle=140)
plt.axis("equal")
plt.show()