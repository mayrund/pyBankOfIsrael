import urllib2
import datetime
import BeautifulSoup

class rates:

	@staticmethod
	def rates(date):
		if type(date) is not datetime.date:
			raise TypeError('Please provide a date in YYYYMMDD format')
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
		response = urllib2.urlopen(request)
		xml = response.read()
		print xml

