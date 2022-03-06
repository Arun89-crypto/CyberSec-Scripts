# How to use this script.

### Download the zip and unzip it

```shell
mkdir LoginTester
cd LoginTester
unzip ../LoginTester.zip
```

### Install requirements.txt

```shell
pip install -r requirements.txt
```

### Options

**REDIRECT OPTIONS** (insert at end)

-roff : To turn off redirects (in some cases website can redirect to login and may return 200 as status code at end Saying found so in order to bypass that and analyzing the redirect params we can get the true user)

-ron : To turn on redirects

### Formats

- **Format for one user**

  ```shell
  python3 LoginTester.py -one [username] [password_file_path] [Request Link] [redirect options]
  ```

- **Format for multiple users**
  ```shell
  python3 LoginTester.py -mul [username_file_path] [password_file_path] [Request Link] [redirect option]
  ```

**IMPORTANT!! (info regarding the host URL)**

Double check the url to which you are sending the requests like if your target is using PHP then check the form action (using using page source or browser extension).
In case of REST API request check the API path using inspect or with appropriate browser extension.
