import time
from Scrapper import scrap

#Initializing start date and end date. To reduce skewness in data it is advised to fetch data by one month at a time
sdate = '01.01.2017'
edate = '31.01.2017'

#Initializing control variables, there are 31 category and 27 wards in website
com_init=0; war_init=0; curr_date=''
on=1

while on:
	try:
		tp = scrap(sdate, edate, 'data.csv')
		com_init,war_init,curr_date =  tp.new_data()
	except:
		time.sleep(60)

	if com_init==31 and war_init == 27 and curr_date==edate:
		on=0

print('scrapping Finished')
