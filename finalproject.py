#import modules for the weather api and for charting 
import requests
import pandas as pd
import csv

#create the url
endpoint = 'https://api.darksky.net/forecast/'
key = '6455810f4cca4cadc79a7d750ef322a7'
lat = '34.0522'
lon = '118.2437'
year = int(input("Choose a year to show temperature "))
time = str(year) + '-01-12T15:00:00'


#assemble full url
url = endpoint + key + '/' + lat + ',' + lon + ',' + time

# get data from website 
r = requests.get(url)

weather = r.json()

#make csv file
csvfile = open('scatterplot.csv', 'w')
csvwriter = csv.writer(csvfile, delimiter = ',')
csvwriter.writerow(['Date', 'Temperature'])

#create data
for x in range(year,2016):
    #assemble full url
    time = str(x) + '-01-12T15:00:00'
    url = endpoint + key + '/' + lat + ',' + lon + ',' + time
    r = requests.get(url)
    weather = r.json()
    Temperature = weather['currently']['temperature']
    csvwriter.writerow([x, Temperature])
#complete the csv file
csvfile.close()    

#set up bokeh for the graph
import bokeh 
from bokeh.charts import Scatter, output_file, save
df = pd.read_csv('scatterplot.csv')
p = Scatter(df, x = 'Date', y = 'Temperature', color = 'red', title = "Temperature History On My Birthday", legend = 'top_right', xlabel = "Year", ylabel = "Temperature")

#save the file
output_file('scatterplot12.html')
save(p)
