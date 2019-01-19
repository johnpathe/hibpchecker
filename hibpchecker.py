#!/usr/bin/env python
# 
#allow input from file at command line
#incorporate other dump checkers sites - ghostproject.fr, OTHER?
#incorporate cred stuffer program
#allow user to supply a single email address at the command line
	#verify email addr supplied at command line is valid
#allow user to supply a filename
	#specify file format (one email addr per line)

#make this work with just regular python requests instead of using this HIBP library imported below
import json

# MUST INSTALL THIS FIRST!!!
#using this library https://github.com/kernelmachine/haveibeenpwned

from hibp import HIBP


'''
hibp execute() returns a list. each item in list is each breach this account appears in
'''

'''
Inside each list item is a dict() with the following keys:
[u'PwnCount', u'Domain', u'IsSensitive', u'Name', u'Title', u'DataClasses', u'IsRetired', u'IsSpamList', u'BreachDate', u'IsFabricated', u'ModifiedDate', u'LogoPath', u'AddedDate', u'IsVerified', u'Description']

'''

def pwnedChecker(account):
	req1 = HIBP.get_account_breaches(account)
	req1.execute()
	result = req1.response
	print 'Checking Account: %s ...' % account

	if isinstance(result,str):
		print 'It appears %s was not involved in any breaches.' % account
		print 'Response from HIBP API: %s' % result
	if isinstance(result,list):
		print 'Number of breaches this account appears in %d' % len(result)
		for breach in result:
			print 'Breach Name: %s' % breach['Name']
			print 'Breach Date: %s' % breach['BreachDate']
	print '\n'

#form a list of accounts to check on HIBP
#format is: accounts = ['email1@foo.com' 'email2@bar.com']


accounts = []
with open('emaillist.txt') as fh:
	for line in fh:
		accounts.append(line.rstrip('\n'))

for account in accounts:
	pwnedChecker(account)





# checking another dump checker site stuff would go here


# using a cred stuffer would go here





