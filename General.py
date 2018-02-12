import os
import csv
from datetime import timedelta
from datetime import datetime
import time

def write_file(filename):
	with open(filename, 'w') as fp:
		Header = [['Complaint Number', 'Date of Complaint','Date of Complition', 'Category','Sub-Category', 'Ward', 'Landmark', 'Problem Description','Responsible Person','Status','Location of Complaint', 'Address of Applicant ']]
		a = csv.writer(fp,delimiter=',')
		a.writerows(Header)
	fp.close()

def append_data(print_list, filename):
	with open(filename,'a') as fp:
		a = csv.writer(fp,delimiter=',')
		a.writerows(print_list)
	fp.close()

def save(com_no, war_no, curr_date, sdate, edate):
	with open('backup.txt','w') as fp:
		fp.write(str(com_no) + '\n')
		fp.write(str(war_no) + '\n')
		fp.write(curr_date + '\n')
		fp.write(sdate + '\n')
		fp.write(edate + '\n')
		fp.write(str(1) + '\n')


def string_to( idate ):
	l = list(map(int, idate.split('.')))
	o_date = datetime(l[2],l[1],l[0])
	return o_date

def Date_to(date1):
	dd = date1.strftime('%d') + '.' + date1.strftime('%m') + '.' + str(date1.year)
	#print dd + ' general'
	return dd

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

# def mapping_file(list1):
# 	with open('mapping.csv','a') as fp:
# 		a = csv.writer(fp, delimiter=',')
# 		a.writerows(list1)		
# 	fp.close()


# everything u comment can be used in future

#write_file()
#append_data()
# sdate = '1.01.2017'
# edate = '2.01.2017'
# start_date = string_to(sdate)
# end_date = string_to(edate)

# for single_date in daterange(start_date, end_date):
#     print single_date.strftime("%Y-%m-%d")