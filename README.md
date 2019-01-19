# hibpchecker

README.md

This is a very basic python script to check email addresses on haveibeenpwned.com
add a list of email addresses to a text file and run this script to find out which breaches the email appears in and when the breach occurred.


You must install this python library first for this to work:
https://github.com/kernelmachine/haveibeenpwned

$ cd /path/to/store/this/
$ sudo git clone https://github.com/kernelmachine/haveibeenpwned
$ sudo pip install hibp


Thus far the tool requires a file in the current path called emaillist.txt which contains an email address on each line to be checked by the HIBP API.

Once you populate emaillist.txt simply run:
$ python hibpchecker.py

Enjoy.
