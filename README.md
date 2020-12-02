## About script
this tool test open redirect vulnerability to each http subdomain via signs EX.. [/, //,\\/, etc..] <br> 
use any tool to know what is subdomains which run http/https EX.. httprobe or any Tec. <br>
cat subdomains | httprobe > https.txt | use tool on this file [https.txt] <br>
the tool will put the sign and request all urls , when found redirect will alert you. <br>
the tool have argument -m, --multiple , this arg make many testing ex.. bruteforce parameters and try many signs

## Installation
i am make code to auto install modules only must have modules [importlib, pip] then tool will install all modules automatically but if found any error you can install all modules manually
```console
svn checkout https://github.com/Abdulrahman-Kamel/mini-hacks/trunk/redir-trick
pip3 install importlib pip
```
 if append modules install error use: sudo pip3 install -r requirements.txt

or install manually
```bash
pip3 install requests
pip3 install argparse
pip3 install urllib3
pip3 install futures
pip3 install sys
```
## Usage
short arg     | long arg      | Description
------------- | ------------- |-------------
-u            | --urls        | File contain urls
-s            | --sign        | Determine one or multiple signs which put every url [Default = /]
-m            | --multiple    | will try many testing [open-redirect] on url 
-t            | --threads     | Threads number to multiProccess [Default = 100]
-T            | --timeout     | Time out waiting if delay request , [Default 3]
-o            | --output      | Save the results to text file
-h            | --help        | show the help message and exit

if you want use multiple signs usage -s, --sign /,\/,//,\/\/  ==> seperator via [,]

## Examples
- Default usage
```python
python3 redir_trick.py --urls https.txt
```
- Put multiple signs  
```python
python3 redir_trick.py --urls https.txt --sign @,/
```
- Determine redirect domain/ip
```python
python3 redir_trick.py --urls https.txt --redirect google.com
```
- Determine threads and timeout
```python
python3 redir_trick.py --urls https.txt --threads 200 --timeout 10
```
- try many testing
```python
python3 redir_trick.py --urls https.txt --threads 200 --timeout 10 -m
```