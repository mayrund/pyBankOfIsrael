import urllib2
import datetime
from BeautifulSoup import BeautifulSoup as Soup

class rates:

	@staticmethod
	def rates(date):
		if type(date) is not datetime.date:
			raise TypeError('Please provide a date in YYYYMMDD format')
		print 'Calling bank...'
		rates.call_bank(date)

	def latest_rates(self):
			call_bank()

	def params(date):
		return {'rate': date}

	@staticmethod
	def call_bank(date):
		print 'calling bank'
		url = 'http://www.bankisrael.gov.il/currency.xml'
		request = urllib2.Request(url, "r")
		response = urllib2.urlopen(url)
		xml = response.read()
		print xml
		soup = Soup(xml)
		rates.parse(soup)

	@staticmethod
	def parse(xml):
		if xml.currencies.error1 is not None:
			if xml.currencies.error1.string == 'Requested date is invalid or':
				raise TypeError('rates not available on the given date')
		print xml.currencies.last_update.string
