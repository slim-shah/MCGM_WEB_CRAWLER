"""
Date: 08/01/2018, Author = Meet Shah(a.k.a = slim_shah)

"""
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from General import *
from random import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import traceback
import os.path
import time

class scrap:
	com_init=1
	war_init =1
	filename=''
	curr_date = ''
	com_no =''
	war_no =''
	print_list = list()
	sdate = ''
	edate = ''
	restart=0

	#constructor for scrap class
	def __init__(self, sdate, edate, filename):
		print 'scraping started'
		self.filename = filename		
		temp = list()
		os.environ['Moz_HEADLESS']='1'

		#Looking for anybackup file present in directory
		if os.path.isfile('backup.txt'):
			with open('backup.txt', 'rt') as fp:
				for line in fp:
					line.replace('\n', '')
					temp.append(line[:len(line)-1])
		
			self.com_init = int(temp[0])
			self.war_init = int(temp[1])
			self.curr_date = temp[2]
			self.sdate = string_to(temp[3])
			self.edate = string_to(temp[4])
			self.restart = int(temp[5])

			if string_to(self.curr_date) == self.edate and self.com_intit == 31:
				exit(0)

		else:
			self.com_init = 1
			self.sdate = string_to(sdate)
			self.edate = string_to(edate)
			self.war_init = 1
			self.restart = 0 
			self.curr_date=''
			write_file(self.filename)

	#Closing Browser Safely
	@staticmethod
	def close_browser(driver):
		try:
			driver.close()
		except:
			pass

	#Loads MCGM url and activates search by deatil button
	@staticmethod
	def activate_complaint_ward(driver):
		driver.get("http://www.mcgm.gov.in/irj/portal/anonymous?NavigationTarget=navurl://18185c4b0c784a63fda50f9863ea44fd")
		driver.implicitly_wait(3)
		driver.switch_to.frame('ivuFrm_page0ivu0')
		try:
			radio_button = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "//*[@name='OBJECT_ID1'][@value='2']")))
		except Exception as e:
			self.close_browser(driver)

		#activates complaint and ward option
		ActionChains(driver).click(radio_button).perform()
	
	@staticmethod
	def add_data_to_list(driver):
		temp =  []
		sub_cat=''
		Category=''
		#complaint_number
		X = driver.find_element_by_xpath("//div[@id='content']//form/table[1]/tbody/tr[1]/td[2]/b").text
		complaint_number = X.encode('utf-8').strip()
		
		#Date of Application
		X = driver.find_element_by_xpath("//div[@id='content']//form/table[1]/tbody/tr[1]/td[4]").text
		Date_of_Application = X.encode('utf-8').strip()
		#hindi prbdescription: /html/body/div/form/table[1]/tbody/tr[2]/td[2]
		#hindi complainaint_name: /html/body/div/form/table[1]/tbody/tr[2]/td[1]

		#English prbdescription: /html/body/div/form/table[1]/tbody/tr[3]/td[2]
		#English complainaint_name: /html/body/div/form/table[1]/tbody/tr[2]/td[2]

		try:
			#Complaint_description
			X = driver.find_element_by_xpath("//div[@id='content']//form/table[1]/tbody/tr[3]/td[2]").text
			Complaint_description = X.encode('utf-8').strip()


		except NoSuchElementException:
			#Complaint_description
			X = driver.find_element_by_xpath("//div[@id='content']//form/table[1]/tbody/tr[2]/td[2]").text
			Complaint_description = X.encode('utf-8').strip()			

		#Department_name	
		X = driver.find_element_by_xpath("//div[@id='content']//form/table[2]/tbody/tr[2]/td[2]").text
		Department_name = X.encode('utf-8').strip()

		#Status
		X = driver.find_element_by_xpath("//div[@id='content']//form/table[2]/tbody/tr[3]/td[2]").text
		Status = X.encode('utf-8').strip()

		temp.append(complaint_number)
		temp.append(Date_of_Application)
		temp.append(Complaint_description)
		temp.append(Department_name)
		temp.append(Status)

		#Marathi complaint
		try:
			Print = driver.find_element_by_id('PRINT')
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			hover = ActionChains(driver).move_to_element(Print)
			hover.click(Print).perform()
			driver.implicitly_wait(5)
			
			#complaint number
			c_n = driver.find_element_by_xpath("/html/body/form/div/table[1]/tbody/tr[3]/td[2]/b").text
			
			#Category
			X = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "//div[@id='content']//table[1]/tbody/tr[4]/td[2]"))).text
			Category = X.encode('utf-8').strip()

			#sub Category
			X = driver.find_element_by_xpath("//div[@id='content']//table[1]/tbody/tr[5]/td[2]").text
			sub_cat = X.encode('utf-8').strip()

			#location of complaint
			X = driver.find_element_by_xpath("//div[@id='content']//table[5]/tbody/tr[2]/td[2]").text
			house_name = X.encode('utf-8').strip()  #1

			Y = driver.find_element_by_xpath("//div[@id='content']//table[5]/tbody/tr[2]/td[4]").text
			house_no = Y.encode('utf-8').strip()    #2
			
			Y = driver.find_element_by_xpath("//div[@id='content']//table[5]/tbody/tr[3]/td[2]").text
			Street1 = Y.encode('utf-8').strip()     #3
			
			Y = driver.find_element_by_xpath("//div[@id='content']//table[5]/tbody/tr[3]/td[4]").text
			Street2 = Y.encode('utf-8').strip()     #4
			
			Y = driver.find_element_by_xpath("//div[@id='content']//table[5]/tbody/tr[4]/td[2]").text
			Area1 = Y.encode('utf-8').strip()       #5  
			
			Y = driver.find_element_by_xpath("//div[@id='content']//table[5]/tbody/tr[4]/td[4]").text
			Area2 = Y.encode('utf-8').strip()	    #6

			Y = driver.find_element_by_xpath("//div[@id='content']//table[5]/tbody/tr[5]/td[2]").text
			city = Y.encode('utf-8').strip()        #7

			Y = driver.find_element_by_xpath("//div[@id='content']//table[5]/tbody/tr[5]/td[4]").text
			Pincode = Y.encode('utf-8').strip()     #8

			#Address of  complaint
			Y = driver.find_element_by_xpath("/html/body/form/div/table[5]/tbody/tr[10]/td[2]").text
			X_House_no = Y.encode('utf-8').strip()

			Y = driver.find_element_by_xpath("/html/body/form/div/table[5]/tbody/tr[10]/td[4]").text
			X_House_name = Y.encode('utf-8').strip()

			Y = driver.find_element_by_xpath("/html/body/form/div/table[5]/tbody/tr[11]/td[2]").text
			X_street1 = Y.encode('utf-8').strip()
			
			Y = driver.find_element_by_xpath("/html/body/form/div/table[5]/tbody/tr[11]/td[4]").text
			X_street2 = Y.encode('utf-8').strip()

			Y = driver.find_element_by_xpath("/html/body/form/div/table[5]/tbody/tr[12]/td[2]").text
			X_area1 = Y.encode('utf-8').strip()

			Y = driver.find_element_by_xpath("/html/body/form/div/table[5]/tbody/tr[12]/td[4]").text
			X_area2 = Y.encode('utf-8').strip()

			Y = driver.find_element_by_xpath("/html/body/form/div/table[5]/tbody/tr[13]/td[2]").text
			X_city = Y.encode('utf-8').strip()

			X_pincode = ' '

			Y = driver.find_element_by_xpath("/html/body/form/div/table[5]/tbody/tr[14]/td[2]").text
			X_state = Y.encode('utf-8').strip()

			Y = driver.find_element_by_xpath("/html/body/form/div/table[5]/tbody/tr[14]/td[4]").text
			X_country = Y.encode('utf-8').strip()
			temp.insert(2,'######')
			temp.insert(3,Category)
			temp.insert(4,sub_cat)
			#no landmark in Marathi complain
			temp.insert(5,' ')

			loc = house_name+','+house_no+','+Street1 +','+Street2+','+Area1+','+Area2+','+city+','+Pincode
			add_ = X_House_no+','+X_House_name+','+X_street1+','+X_street2+','+X_area1+','+X_area2+','+X_city+','+X_pincode+','+X_state+','+ X_country 
			
			temp.append(loc)
			temp.append(add_)

			driver.switch_to.default_content()
			return temp,1,Date_of_Application
		
		#English Complaints
		except:
			#switching to appropriate frame
			x1 = driver.find_element_by_xpath("//div[@id='content']//iframe[2]")
			driver.switch_to.frame(x1)
			
			#sub-category
			x = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "//div[@id='viewer']/div/div[2]/div[11]")))
			content = x.get_attribute('innerHTML')
			Val= content.strip(':')
			#Val = Val.encode('utf-8').strip(':')
			sub_cat = Val[2:]

			x = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "//div[@id='viewer']/div/div[2]/div[12]"))) 
			content = x.get_attribute('innerHTML')
			Y = content.encode('utf-8').strip()
			
			if Y != 'Description':
				sub_cat = sub_cat + ' ' + Y 

			#22-85, fetching arbitary location to perform linear search on it
			location = list()
			for i in range(22,85):
				try:				
					x = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "//div[@id='viewer']/div/div[2]/div[" + str(i) +  "]")))
					content = x.get_attribute('innerHTML')
					location.append(content.encode('utf-8').strip(' '))
				except:
					break

			#location of complaint
			i = location.index('House  Name')
			n = location.index('Pincode')
			label1 = ['House  Name', 'House  No.', 'Street1', 'Street2', 'Area1', 'Area2','City', 'Pincode']

			List1 = location[i:n+2]
			for i in label1:
				try:
					List1.remove(i)
				except:
					continue

			Landmark=' '
			try:
				i = location.index('Landmark')
				loc = location[i+1].strip(':')
				Landmark = loc[2:]
			except:
				Landmark =' '
			

			#Address of Applicant
			i = location.index('Address  of  Applicant  :')
			n = location.index('Telephone(O)')
			label2=['House  No', 'House  Name', 'Street1','Street2', 'Area1', 'Area  2', 'City', 'Pin  Code', 'State', 'Country']

			List2 = location[i+1:n]

			for i in label2:
				try:
					List2.remove(i)
				except:
					continue
			
			date='######'
			try:
				date_end_index = location.index('Responsible  :')
				if date_end_index!=-1:
					date_ = location[date_end_index+1]
					date_i = date_.index('Date')
					date = date_[date_i+7:]
							
				else:
					date ='######'
			except:
				date ='######'


			temp.insert(2,date)
			temp.insert(3,Category)
			temp.insert(4,sub_cat)
			temp.insert(5,Landmark)
			
			loc = ','.join(List1)
			add_ = ','.join(List2)
			
			temp.append(loc)
			temp.append(add_)

			return temp,0,Date_of_Application



	def new_data(self):
		try:
			# Open up a Firefox browser and navigate to web page
			options = Options()
			options.add_argument("--headless")
			driver = webdriver.Firefox(firefox_options=options)
			driver.maximize_window()
			self.activate_complaint_ward(driver)
						
			current_category = ''
			current_ward = ''
			
			select_complain = driver.find_element_by_id('CMPTYPE')
			complaint_all_options = select_complain.find_elements_by_tag_name("option")

			#Iterating over all complaint category
			for com in range(self.com_init,32):
				current_category = complaint_all_options[com].text
				current_category = current_category.encode('utf-8').strip()	
				self.com_no = com
				complaint_all_options[com].click()

				select_ward = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID, 'WARD')))
				ward_all_options = select_ward.find_elements_by_tag_name("option")

				if self.restart == 0:
					self.war_init=1
					self.restart = 0

				#Iterating over all the wards persent in that complaint
				for war in range(self.war_init, len(ward_all_options)):
					current_ward = ward_all_options[war].text
					current_ward = current_ward.encode('utf-8').strip()
					self.war_no = war
					ward_all_options[war].click()
					print 'currently crawling Category: ' + current_category + ', Ward: ' + current_ward
					
					self.print_list = list()
					on =1
					if self.restart == 1 and self.curr_date != '':
						i_start_date = string_to(self.curr_date)
					else:
						i_start_date = self.sdate
					while on:
						sdate_string = Date_to(i_start_date)
						self.curr_date = sdate_string
						s_20 = i_start_date + timedelta(18)
						
						if s_20 <= self.edate :
							s_20_p = Date_to(s_20)

						else:
							s_20_p = Date_to(self.edate)
							on = 0

						select_start_date = driver.find_element_by_id('compdate')
						select_end_date = driver.find_element_by_id('compdate_t')
						
						driver.execute_script("arguments[0].value = arguments[1]", select_start_date, sdate_string)
						driver.execute_script("arguments[0].value = arguments[1]", select_end_date, s_20_p)
						search = driver.find_element_by_xpath("//input[@id='Search']")
						try:
							ActionChains(driver).click(search).perform()

						except UnexpectedAlertPresentException:
							alert = driver.switch_to_alert()
							alert.accept()
							select_ward_ = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID, 'WARD')))
							ward_all_options_ = select_ward.find_elements_by_tag_name("option")
							ward_all_options_[war].click()
							driver.execute_script("arguments[0].value = arguments[1]", select_start_date, sdate_string)
							driver.execute_script("arguments[0].value = arguments[1]", select_end_date, s_20_p)
							search = driver.find_element_by_xpath("//input[@id='Search']")
							ActionChains(driver).click(search).perform()

						except MoveTargetOutOfBoundsException:
							search = driver.find_element_by_xpath("//input[@id='Search']")
							driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
							ActionChains(driver).click(search).perform()
							#.move_to_element(search)
							
						except:
							traceback.print_exc()
							driver.save_screenshot("Unknown_exception_search.png")

						try:
							driver.implicitly_wait(5)
							select_radio = driver.find_element_by_xpath("//form[@name='forma1']/table/tbody")
							radio_all_options = select_radio.find_elements_by_tag_name("input")

							for radio_option in range(len(radio_all_options)):
								#To avoid stale element error
								radio_all_options[radio_option].click()
								driver.find_element_by_id('Continue').click()
								driver.implicitly_wait(5)
								
								temp=list() 
								temp,Control,Date_of_Application = self.add_data_to_list(driver)
								self.curr_date = Date_of_Application
								if temp[3]=='':
									temp[3] = current_category

								temp.insert(5,current_ward)
								self.print_list.append(temp)				
								
								if Control ==1:
									driver.execute_script("window.history.go(-2)")
								else:
									driver.switch_to.default_content()
									driver.execute_script("window.history.go(-1)")

								driver.switch_to.frame('ivuFrm_page0ivu0')
								select_radio = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "//form[@name='forma1']/table/tbody")))
								radio_all_options = select_radio.find_elements_by_tag_name("input")

						except NoSuchElementException:	 
								print 'no complaints in sepecified date in Category: \'' + current_category + '\'  Ward: \'' + current_ward + '\' Date start: \'' + sdate_string + '\' Date end: \'' + s_20_p +'\''

						except TimeoutException:
							print 'Timeout inside radio'
							self.close_browser(driver)
							driver.save_screenshot("timeout.png")
							time.sleep(20)

						except Exception as e:
							print 'Unknown error occurred'
							traceback.print_exc()
							driver.save_screenshot("Unknown_.png")
							print 'Dont close the window'
							self.close_browser(driver)  

						append_data(self.print_list, self.filename)
						del self.print_list[:]
						
						#Save Data to file: backup.txt
						if self.com_no!='' and self.war_no!='':
							save(self.com_no, self.war_no, self.curr_date, Date_to(self.sdate), Date_to(self.edate))
						
						#Reload the page						
						try:
							self.close_browser(driver)
							driver = webdriver.Firefox(firefox_options=options)
							#driver = webdriver.Firefox()
							driver.maximize_window()
							self.activate_complaint_ward(driver)
							select_complain = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID, 'CMPTYPE')))
							complaint_all_options = select_complain.find_elements_by_tag_name("option")
							complaint_all_options[com].click()		
							select_ward = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID, 'WARD')))
						
						except:
							driver.implicitly_wait(10)
							self.close_browser(driver)
							driver = webdriver.Firefox(firefox_options=options)
							#driver = webdriver.Firefox()
							driver.maximize_window()
							self.activate_complaint_ward(driver)
							select_complain = driver.find_element_by_id('CMPTYPE')
							complaint_all_options = select_complain.find_elements_by_tag_name("option")
							complaint_all_options[com].click()
							select_ward = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID, 'WARD')))

						ward_all_options = select_ward.find_elements_by_tag_name("option")
						ward_all_options[war].click()
						
						#incrementing date
						i_start_date = s_20 + timedelta(1)
	

					#Reload the page						
					try:
						self.close_browser(driver)
						driver = webdriver.Firefox(firefox_options=options)
						#driver = webdriver.Firefox()
						driver.maximize_window()
						self.activate_complaint_ward(driver)
						select_complain = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID, 'CMPTYPE')))
						complaint_all_options = select_complain.find_elements_by_tag_name("option")
						complaint_all_options[com].click()		
						select_ward = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID, 'WARD')))

					except:
						self.close_browser(driver)
						driver = webdriver.Firefox(firefox_options=options)
						driver.maximize_window()
						self.activate_complaint_ward(driver)
						select_complain = driver.find_element_by_id('CMPTYPE')
						complaint_all_options = select_complain.find_elements_by_tag_name("option")
						complaint_all_options[com].click()
						select_ward = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID, 'WARD')))
						
					ward_all_options = select_ward.find_elements_by_tag_name("option")
				#End of Ward Options Loop
				
					
				
			#End of Complaint options Loop

		except Exception as e:
			try:
				driver.save_screenshot("Main_Exception.png")
			except:
				print 'screenshot1 passed'
			traceback.print_exc()
			print 'Error occured in main try block!\n'

		finally:
			self.close_browser(driver)
			print 'pls wait while saving your work'
			if self.com_no!='' and self.war_no!='':
				save(self.com_no, self.war_no, self.curr_date, Date_to(self.sdate), Date_to(self.edate))
			return self.com_no,self.war_no,self.curr_date

	#End of new_data