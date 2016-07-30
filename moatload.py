###Step 1###
#Initial Concept#
#Click the button#
'''

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.touch_actions import TouchActions

driver = webdriver.Firefox()
driver.get("https://moat.com/advertiser/state-farm")
#assert "State Farm Creatives | Moat" in driver.title

elem = driver.find_element_by_id("paginate-button")
#drive.find_element_by_xpath('//*[@id="paginate-button"]')
print elem
elem.click()

#elem.send_keys(Keys.TAB)
#elem.send_keys(Keys.END)
#assert "No results found." not in driver.page_source
#driver.close()

"""
<div id="paginate-button" class="button" data-bind="click: $parent.paginate, visible: moreCreatives">Load more</div>
"""
'''

###Step 2###
#Wait for the button to be clickable, then click#
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://moat.com/advertiser/state-farm")
assert "State Farm Creatives | Moat" in driver.title

#Refreshes page before fully loading.
#Helps script run sooner if slow Internet
webpage = driver.find_element_by_tag_name("body")
webpage.send_keys(Keys.F5)

#content = driver.find_element_by_id("all-ads")
#Either all-ads or popup-template
#print content
#content.send_keys(Keys.END)

try:
    element = WebDriverWait(driver, 45).until(
        EC.element_to_be_clickable((By.ID, "paginate-button"))
    )
	#wait = WebDriverWait(driver, 10)
	#element = wait.until(EC.element_to_be_clickable((By.ID,'someid')))

finally:
	elem = driver.find_element_by_id("paginate-button")
	#driver.find_element_by_id("paginate-button").click()
	elem.click()
	#print elem
	#driver.quit()
	#print elem

#'''

###Step 3###
#Loop clicking clickable buttons#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, TimeoutException


driver = webdriver.Firefox()
driver.get("https://moat.com/advertiser/state-farm")
assert "State Farm Creatives | Moat" in driver.title

webpage = driver.find_element_by_tag_name("body")
webpage.send_keys(Keys.F5)

#content = driver.find_element_by_id("all-ads")
#all-ads or popup-template
#print content
#content.send_keys(Keys.END)

#HTML for Ad count. Static number.
#<div class="creative-count"><span>18,263 creatives</span></div>

#count = driver.find_element_by_xpath('//*[@id="comp-header"]/div[1]/div[2]/span')
#print count

#pagesize = driver.findvarinscript
##for (int i = 0; i < 10; i++)
#while pagesize > 0:
#try:
#finally:
#p	agesize--


#while count.exists()

#pass : #put some loop here
"""
try:
    driver.find_element_by_id("paginate-button").click()
	#wait = WebDriverWait(driver, 10)
	#element = wait.until(EC.element_to_be_clickable((By.ID,'someid')))

except ElementNotVisibleException:
	    element = WebDriverWait(driver, 45).until(
        EC.element_to_be_clickable((By.ID, "paginate-button"))
    	)
    	    driver.find_element_by_id("paginate-button").click()


finally:
	#elem = driver.find_element_by_id("paginate-button")
	#driver.find_element_by_id("paginate-button").click()
	#elem.click()
	#print elem
	#driver.quit()
	#print elem
	pass
"""
a = True

while a == True:
	try:
		#60s too long 30s too short
	    element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "paginate-button"))
    	)
    	    driver.find_element_by_id("paginate-button").click()
		#wait = WebDriverWait(driver, 10)
		#element = wait.until(EC.element_to_be_clickable((By.ID,'someid')))

	except ElementNotVisibleException:
		    pass
		    #a = False

	except TimeoutException:
			webpage.send_keys(Keys.F5)

#	finally:
		#elem = driver.find_element_by_id("paginate-button")
		#driver.find_element_by_id("paginate-button").click()
		#elem.click()
		#print elem
#		driver.quit()
		#print elem