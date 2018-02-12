# MCGM_WEB_CRAWLER
Date:6/01/2018, Author = Meet shah(aka slim_shah)

MCGM_WEB_CRAWLER, is a platform independent web crawler bot made for scrapping data from complaint management portal of Mumbai city(https://goo.gl/J9vZ7L). The script is made in python 2.7.12 and has following explicit dependencies:<br>
	1) selenium webdriver<br>
	2) mozilla geckodriver (Available at: https://github.com/mozilla/geckodriver/releases)

# Using Geckodriver in linux:
	From the above provided link, download the appropriate geckodriver according to your system. After 
    downloading and extracting(unzipping) the driver, move it to location where selenium library 
	will look for it. To do this type in the following command into terminal.

	~$ cp geckodriver /usr/bin/geckodriver

	Unluckly Right now i haven't wrote the code for installing libraries automatically. Hopefully if time
    permits then i will write it, otherwise you have to install all the libraies and drivers manually :(
# Using Geckodriver in Windows:
	After you download Geckodriver, You will need to make some changes in 'Scrapper.py' file. 
	Intialize driver variable with following way: 
      driver = webdriver.Firefox(executable_path=r'your\path\geckodriver.exe')
	if you want to use driver in headless mode,then add options arguments as well.

# Warnings !!!
	1) As MCGM caledar is having some issues while calculating number of days in February, while inputting
    date range please divide your range in two parts {[Jan-Fed] | [March-December]}, otherwise 
	program will stop executing. 

	for example, if you want scrap data of 1 year, then you need to run this script two times giving in 
    following inputs respectively.
		1st time: 
			sdate='01.01.YYYY'
			edate= 'XX.02.YYYY' [last day of february varies according to leap year so figure it out
                                        corretly]
		2nd time:
			sdate='01.03.YYYY'
			edate='31.12.YYYY'

	2) If you encounter following error "ivframe not found", then please check your internet connection.

# Message_for_Developer:
     -> If you could write logic for downloading all dependencies automatically, then your help is much
        appreciated.
 	 -> Tweaking_Warning:
		  If you are a developer and want to modify this code and reuse if for yourself, then please
      watchout for the following exceptions while tweaking this code.
         1) Timeout Exception            <-- selenium.common.exceptions.TimeoutException -->
	     2) Move Target Out of Bounds    <-- selenium.common.exceptions.MoveTargetOutOfBoundsException -->
        *3) Stale Element Reference      <-- selenium.common.exceptions.StaleElementReferenceException -->
	     4) No Such Element              <-- selenium.common.exceptions.NoSuchElementException -->
			
      * = Most Annoying and difficult to get rid of.

	 -> links referred:
		 stale element : https://stackoverflow.com/questions/43036566/iterate-over-webelements-in-selenium-python
		 innner html   : https://stackoverflow.com/questions/35905517/how-to-get-innerhtml-of-whole-page-in-selenium-driver
