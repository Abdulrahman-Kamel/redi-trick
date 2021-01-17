## About script
this tool test open redirect vulnerability via signs EX.. [/, //,\\/, etc..] <br> 
cat subdomains | httprobe > https.txt | use tool on this file [https.txt] <br>
the tool will put the sign and send request , when found redirect will alert you. <br>
the tool have argument -m, --multiple , this arg make many testing , some testing is bruteforce parameters and try many signs

## Installation
i am make code to auto install modules only must have modules ``` importlib , pip ``` <br> 
```bash 
pip3 install importlib,pip 
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
python3 redir_trick.py --urls https.txt --sign \\/,/,//
```
- Determine threads and timeout
```python
python3 redir_trick.py --urls https.txt --threads 200 --timeout 10
```
- try many testing
```python
python3 redir_trick.py --urls https.txt --threads 200 --timeout 10 -m
```
