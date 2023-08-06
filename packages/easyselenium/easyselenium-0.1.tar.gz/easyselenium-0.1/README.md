easySelenium [![Travis Status](https://travis-ci.com/SeleniumHQ/selenium.svg?branch=master)](//travis-ci.com/SeleniumHQ/selenium/builds) [![AppVeyor Status](https://ci.appveyor.com/api/projects/status/pg1f99p1aetp9mk9/branch/master?svg=true)](https://ci.appveyor.com/project/SeleniumHQ/selenium/branch/master)
========
<a href="https://selenium.dev"><img src="https://selenium.dev/images/selenium_logo_square_green.png" width="180" alt="Selenium"/></a>

easyselenium is write on the top of selenium to make selenium easier for begineers for ready built in funtions only they need to call the functions and pass the arguments.All extra thing time delay and webdriver wait select findping xpath will do in backend.
Get rid of using time delays

The project is made possible by volunteer contributors who've
generously donated thousands of hours in code development and upkeep.

Selenium's source code is made available under the [Apache 2.0 license](https://github.com/SeleniumHQ/selenium/blob/master/LICENSE).

## Documentation


## from easy selenium import *
## open_browser()
```sh
with optional arguments

headless = True/False (to work without browser)
path = 'your drirectory by default is default directory'
browser = 'chrome'/'firefox'/ie
debug = True/False (to print what is happening inside the code)

Example
This is by default arguments

## open_browser(headless=False,path="chromedriver.exe",browser='chrome',debug=False)
```

## open_url(url='www.google.in')
```sh
with optional arguments

url = 'your web url'
new_tab = True/False (open in new tab or same)
Example
This is by default arguments

## open_url(url='www.step2success.in',new_tab=True)
```


## window_handle(no=1)
```sh
To switch to your popup or another tab window ()
by default time to wait is 50 sec

```

## switch_frame (no=1 or name='mainframe')
```sh
To switch to iframe or frame with no or name
by default time to wait is 50 sec
```


## click_on (text='submit'or image='imagepath' or id='submit' or css='send' or xpath='this')
To Click on buton based on iamge/Text or xpath
by default time to wait is 50 sec
```sh
with optional arguments

repeat=True/False (True-To double click on item)
```


## send_text (text='your text' with  id='submit' or css='send' or xpath='this')
```shTo send text to block
by default time to wait is 50 sec
```sh
with optional arguments

with_enter=True/False (True-To enter after type text)
```

## select_dropdown (option ='option to select' with  id='submit' or css='send' or xpath='this')
```sh
To select option in dropdown with partial text
by default time to wait is 50 sec
```


## read_text (id='submit' or css='send' or xpath='this')
```sh
To read text from element/multiple elements
It is samrt enough to automatically detect if single or multiple element is present
Value/Text is present

Then return you a list of elemnts with tuple insde it containing text,value and session_id
by default time to wait is 50 sec
```

## close_window (no=1)
```sh
To switch and close the provided window
optional switch_to=0
to switch to this window after closing
```

## alerts (text='yes'/'no'/'custom'/blank to read it text)
```sh
To accept/decline/send text/read text from alert box
```


Example :

```sh
import time

from easyselenium import *
import time
open_browser(path="chromedriver.exe",browser='chrome',debug=True)
#open_broswer(executable_path=r"chromedriver.exe",browser='firefox')
#open_broswer(executable_path=r"chromedriver.exe",browser='ie')
#open_broswer(browser='chrome',headless=True)

open_url(url="https://step2success.in/registration-page-demo/")
open_url(url="https://step2success.in/iframe-demo/",new_tab=True)
window_handle(no=0)
send_text(text='Ankit',id='first_name')
send_text(text='Kothari',id='last_name',with_enter=True)
select_dropdown(option='What is your Birthdate?',id='dropdown')
#click_on(text='REGISTER')
#click_on(id='register')


time.sleep(3)

window_handle(no=1)
switch_frame(no=0)
read_text(href ='#')
click_on(text='Follow On Twitter')

window_handle(no=2)

#close_window(no=2)

```


