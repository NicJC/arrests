import pandas as pd
import requests
from io import StringIO
import os
import numpy as np
from bs4 import BeautifulSoup


# Get data



url = 'https://mpdc.dc.gov/sites/default/files/dc/sites/mpdc/publication/attachments/Arrests%20by%20Year%202020.csv'
req = requests.get(url)
data = StringIO(req.text)
arrests = pd.read_csv(data, parse_dates=['Arrest Date'])

url = 'https://mpdc.dc.gov/sites/default/files/dc/sites/mpdc/publication/attachments/Arrests%20by%20Year%2C%202019.csv'
req = requests.get(url)
data = StringIO(req.text)
arrests1=pd.read_csv(data, parse_dates=['Arrest Date'])

url1 = 'https://mpdc.dc.gov/sites/default/files/dc/sites/mpdc/publication/attachments/Arrests%20by%20Year%2C%202018.csv'
req1 = requests.get(url1)
data1 = StringIO(req1.text)
arrests2=pd.read_csv(data1, parse_dates=['Arrest Date'])

url2 = 'https://mpdc.dc.gov/sites/default/files/dc/sites/mpdc/publication/attachments/Arrests%202017%20Public.csv'
req2 = requests.get(url2)
data2 = StringIO(req2.text)
arrests3=pd.read_csv(data2, parse_dates=['Arrest Date'])

url3 = 'https://mpdc.dc.gov/sites/default/files/dc/sites/mpdc/publication/attachments/Arrests%202016%20Public.csv'
req3 = requests.get(url3)
data3 = StringIO(req3.text)
arrests4=pd.read_csv(data3, parse_dates=['Arrest Date'])

url4 = 'https://mpdc.dc.gov/sites/default/files/dc/sites/mpdc/publication/attachments/Arrests%202015%20Public.csv'
req4 = requests.get(url4)
data4 = StringIO(req4.text)
arrests5=pd.read_csv(data4, parse_dates=['Arrest Date'])

url5 = 'https://mpdc.dc.gov/sites/default/files/dc/sites/mpdc/publication/attachments/Arrests%202014%20Public.csv'
req5 = requests.get(url5)
data5 = StringIO(req5.text)
arrests6=pd.read_csv(data5, parse_dates=['Arrest Date'])

url6 = 'https://mpdc.dc.gov/sites/default/files/dc/sites/mpdc/publication/attachments/Arrests%202013%20Public.csv'
req6 = requests.get(url6)
data6 = StringIO(req6.text)
arrests7=pd.read_csv(data6, parse_dates=['Arrest Date'])


a = arrests.append(arrests1,ignore_index = True)
a = a.append(arrests2,ignore_index = True)
a = a.append(arrests3,ignore_index = True)
a = a.append(arrests4,ignore_index = True)
a = a.append(arrests5,ignore_index = True)
a = a.append(arrests6,ignore_index = True)
a = a.append(arrests7,ignore_index = True)


pd.options.display.float_format = '{:,.0f}'.format

Arrests = a[['Arrest Year', 'Arrest Date','Age','Defendant Race','Defendant Ethnicity','Defendant Sex'
          ,'Arrest Category', 'Arrest Latitude','Arrest Longitude','Defendant District']]

Arrests.columns = ['Year', 'Date', 'Age','Race','Ethnicity','Sex','Category','Latitude','Longitude','District']

pd.options.display.float_format = '{:,.0f}'.format
Arrests.to_csv("Arrests.csv")
