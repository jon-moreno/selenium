#Example 0 pypi.python.org/pypi/selenium
#
'''
#import the webdriver module from selenium library
from selenium import webdriver

#using webdriver module with .Firefox() method. 
#Appears to open a temporary selenium profile
#on computer and returns Webdriver? Object variable
browser = webdriver.Firefox()
#invoking .get method on browser object. "Gets" the website given as parameter
browser.get('http://seleniumhq.org/')
#'''

#Example 1 '''

from selenium import webdriver
#import the Keys class from the given file
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://www.yahoo.com')

#My code
"""
if browser.title == 'Yahoo':
	#Find the search box
	#<input id="uh-search-box" type="text" name="p">
	elem = browser.find_element_by_name('p')
	#Simulates a user typing string & hitting return key
	elem.send_keys('seleniumhq' + Keys.RETURN)

else: browser.quit()#"""

#Ex code
"""
#Checks that title matches string. If not, code stops
#assert 'Yahoo' in browser.title

#Find the search box <input id="uh-search-box" type="text" name="p">
elem = browser.find_element_by_name('p')
#Simulates a user typing string & hitting return key
elem.send_keys('seleniumhq' + Keys.RETURN)

#Closes the browser
browser.quit() 
#"""
#'''

#Example 2
'''
import unittest

class GoogleTestCase(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.addCleanup(self.browser.quit)

	def testPageTitle(self):
		self.browser.get('http://www.google.com')
		self.assertIn('Google', self.browser.title)

if ___name___ == '___main___':
	unittest.main(verbosity=2)
#'''