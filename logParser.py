#!/usr/bin/env python
# python v2.7.x
# written AWP, 3.12.2014

import re
from collections import Counter

class Log():

	def __init__(self, logFilePath):
		self.logFilePath = logFilePath
		self.foundIpList = []
		self.flattenFoundIpList = []
		self.foundIpCounter = Counter()

	def report(self, topCount=10, filterInternal=False):
		self.filterInternal = filterInternal
		self.topCount = topCount

		with open(self.logFilePath, "r") as log:
			for logLine in log:
				self.foundIpList.append(re.findall( r'[0-9]+(?:\.[0-9]+){3}', logLine))

		# convience - flatten list
		self.flattenFoundIpList = [item for sublist in self.foundIpList for item in sublist]

		if self.filterInternal is True:
			# Note: IPv4 Only
			internalIpFilter = re.compile(r'(^127\.0\.0\.1)|(^10\.)|(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)|(^192\.168\.)')
			self.internalFilteredIpFoundList = [ip for ip in self.flattenFoundIpList if not internalIpFilter.match(ip)]

			for ipAddress in self.internalFilteredIpFoundList:
				self.foundIpCounter[ipAddress] +=1
			return self.foundIpCounter.most_common(self.topCount)

		else:
			for ipAddress in self.flattenFoundIpList:
				self.foundIpCounter[ipAddress] +=1
			return self.foundIpCounter.most_common(self.topCount)


def main():
	print Log('apache.log').report(filterInternal=True)

if __name__ == '__main__':
	main()