#!/usr/bin/env python
# By Abdulrahman Kamel
# Version 1.2

import importlib # to check modules
import pip 	 # to install modules

# func to check and install modules
def install(package):
	spam_spec   = importlib.util.find_spec(package)
	check_found = spam_spec is not None

	if check_found == False:
		pip.main(['install', package])

install('requests')		# instead of pip3 install requests
install('argparse')		# instead of pip3 install argparse
install('urllib3')		# instead of pip3 install urllib3
install('concurrent.futures')	# instead of pip3 install concurrent.futures
install('os')		# instead of pip3 install os
#install('sys')			# instead of pip3 install sys

import requests
import argparse
import urllib3 
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
from sys import exit
import os

# set arguments
parser_arg_menu = argparse.ArgumentParser(epilog='Example: python3 redir_tricks.py --urls https.txt ',prog='tool', formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=15))
parser_arg_menu.add_argument(
"-u" , "--urls" , help="File contain urls",
metavar=""
)
parser_arg_menu.add_argument(
"-s" , "--sign" , help="Determine one or multiple signs which put every url [Default = /]",
metavar=""
)
parser_arg_menu.add_argument(
"-m" , "--multiple" , help="will try many testing [open-redirect] on url", action='store_true'
)
parser_arg_menu.add_argument(
"-t", "--threads" , help="Threads number to multiProccess [Default = 200]",
metavar=""
)
parser_arg_menu.add_argument(
"-T", "--timeout" , help="Time out waiting if delay request , [Default 3]",
metavar=""
)
parser_arg_menu.add_argument(
"-o", "--output" ,help="Save the results to text file", 
metavar=""
)

# refrences variables
arg_menu     = parser_arg_menu.parse_args()
max_threads  = int(arg_menu.threads) if arg_menu.threads  else int(200)
max_timeout  = int(arg_menu.timeout) if arg_menu.timeout  else int(3)
redirect_to  = "bing.com" 
urls_lines   = sum(1 for line in open(arg_menu.urls)) if arg_menu.urls else 0

# can use [re] modules replace this list
redi_list    = [
'http://'    + redirect_to,
'https://'   + redirect_to,
'http://' 	 + redirect_to + '/',
'https://'   + redirect_to + '/',
'http://www.' + redirect_to,
'https://www.'+ redirect_to,
'http://www.' + redirect_to + '/',
'https://www.'+ redirect_to + '/'
]

# colors
h = '\035[90m'	 # Header
b = '\033[96m'   # Blue
g = '\033[92m'	 # Green
y = '\033[93m'	 # Yellow
r = '\033[91m'	 # Red
e = '\033[0m'	 # End
B = '\033[1m' 	 # Bold
u = '\033[4m' 	 # underLine
n = '\033[5;91m' # notic

HEADER = g+' redir_trick testing open redirect vulnerability to each http url \n Test: ['+str(urls_lines)+'] url Please wait some time.\n'+r+' Developer By: '+n+ '@Abdulrahman-Kamel\n\n'+e
FOOTER = r+'\t'*5+'Terminated\n'+e
print(HEADER)

# create logs dir
if os.path.exists('logs') != True:
	os.makedirs('logs')

# check if logs/errors.txt > 5k line .. remove
f_error = 'logs/errors.txt'
if os.path.exists(f_error):
	f_lines = sum(1 for line in open(f_error))
	if f_lines > 5000:
		os.remove(f_error)

# skeap ssl error 
urllib3.disable_warnings()

# check on missing argument
if not arg_menu.urls:
	print('missing argument: -u, --urls'); exit(1)

# filter sign argument
if arg_menu.sign:
	signs = arg_menu.sign.split(',') if ',' in arg_menu.sign else arg_menu.sign

else:
	signs = "/"


# func to write in output file
def write(file, value):
	global output
	output = open(file,'a+')
	output.writelines(value)

# func to return message
def msg(msg_type,URL,STATUS,HEADER):
	color   = r + URL + e + ' [' + str(STATUS) + ']\nRedirect to: ' + b + HEADER + e + '\n\n'
	uncolor = URL + ' [' + str(STATUS) + ']\nRedirect to: ' + HEADER + '\n\n'

	if msg_type == 'color':
		return color
	elif msg_type == 'uncolor':
		return uncolor


class default():

	def one_sign(self, url):

		sign = signs
		
		try:
			response = requests.get(url + sign + redirect_to , verify=False, allow_redirects=False, timeout=max_timeout)
			if response.headers['Location']:
				if response.headers['Location'][0:20] in redi_list:
					print(msg('color',response.url,str(response.status_code) +'] ['+ sign ,response.headers['Location']))

					if arg_menu.output:
						write(arg_menu.output , msg('uncolor',response.url,str(response.status_code) +'] ['+ sign ,response.headers['Location']))

		except Exception as er:
			write('logs/errors.txt',str(er)+'\n')


	def multi_sign(self, url):

		if type(signs) is list:
			
			try:
				for single_sign in signs:
					response = requests.get(url + single_sign + redirect_to , verify=False, allow_redirects=False, timeout=max_timeout)
					if response.headers['Location']:
						if response.headers['Location'][0:20] in redi_list:
							print(msg('color',response.url,str(response.status_code) +'] ['+ single_sign ,response.headers['Location']))

							if arg_menu.output:
								write(arg_menu.output , msg('uncolor',response.url,str(response.status_code) +'] ['+ single_sign ,response.headers['Location']))

			except Exception as er:
				write('logs/errors.txt',str(er)+'\n')

class multiple():

	# http schema
	global schema
	schema = ["http://" , "https://"]

	# params name
	global params
	params = ["url" , "redirect" , "redir" , "uri" , "next" , "rurl" , "to" , "out" , "continue" , "domain"]

	# signs
	global _signs
	_signs = ["/" , "//" , "///" , "////" , "\\/" , "\\/\\/" ,"\\//"  , "//\\;@" , "/." , "\\/." , "\\" , "\\\\"]


	def try_signs(self, url):

		# try all signs
		for _sign in _signs:
			try:
				response = requests.get(url + _sign + redirect_to , verify=False, allow_redirects=False, timeout=max_timeout)
				if response.headers['Location']:
					if response.headers['Location'][0:20] in redi_list:
						print(msg('color',response.url,str(response.status_code) +'] ['+ _sign ,response.headers['Location']))

						if arg_menu.output:
								write(arg_menu.output , msg('uncolor',response.url,str(response.status_code) +'] ['+ _sign ,response.headers['Location']))

				
			except Exception as er:
				write('logs/errors.txt',str(er)+'\n')


	def try_params(self, url):

		R = schema[1] + redirect_to
		full_params = "?url="+R+"&redirect="+R+"&redir="+R+"&uri="+R+"&next="+R+"&rurl="+R+"&to="+R+"&out="+R+"&continue="+R+"&domain="+R

		try:
			response = requests.get(url + full_params , verify=False, allow_redirects=False, timeout=max_timeout)

			if response.headers['Location']:
				if response.headers['Location'][0:20] in redi_list:
					for p in params:
						response = requests.get(url + '?'+p+'='+schema[1]+redirect_to , verify=False, allow_redirects=False, timeout=max_timeout)
						if response.headers['Location'][0:20] in redi_list:
							print(msg('color',response.url,str(response.status_code) + '] param[' +p ,response.headers['Location']))

							if arg_menu.output:
								write(arg_menu.output , msg('uncolor',response.url,str(response.status_code) + '] param[' +p ,response.headers['Location']))

		except Exception as er:
			write('logs/errors.txt',str(er)+'\n')


def tool(url):

	defu  = default()
	multi = multiple()

	# no arg
	if not (arg_menu.sign and arg_menu.multiple):
		defu.one_sign(url)

	# -s 1 
	if type(signs) is not list and not arg_menu.multiple:
		defu.one_sign(url)

	# -s 1,2 
	if type(signs) is list and not arg_menu.multiple:
		defu.multi_sign(url)

	# -m
	if arg_menu.multiple and not arg_menu.sign:
		multi.try_signs(url)
		multi.try_params(url)

	# -m , -s 1 
	if type(signs) is not list and arg_menu.sign and arg_menu.multiple:
		defu.one_sign(url)
		multi.try_signs(url)
		multi.try_params(url)

	# -m , -s 1,2
	if type(signs) is list and arg_menu.multiple:
		defu.multi_sign(url)
		multi.try_signs(url)
		multi.try_params(url)


if __name__ == '__main__':


	# make single url from file
	with open(arg_menu.urls, 'r') as f:
	    single_url = [line.rstrip() for line in f]

	# run tool via multipleProccess
	with PoolExecutor(max_threads) as executor:
	    for _ in executor.map(tool, single_url):
	    	pass

	# close files
	if arg_menu.urls:
		open(arg_menu.urls , 'r').close()

	if arg_menu.output:
		open(arg_menu.output, 'a+').close()

	try:
		open('logs/errors.txt','a+').close()
	except:
		pass

print(FOOTER)
