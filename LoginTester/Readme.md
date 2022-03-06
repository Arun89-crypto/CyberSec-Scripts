# How to use this script.

### Download the zip and unzip it

```shell
mkdir LoginTester
unzip LoginTester.zip > LoginTester
```

### Install requirements.txt

```shell
pip install -r requirements.txt
```

- **Format for one user**

  ```shell
  python3 LoginTester.py -one [username] [password_file_path] [Request Link]
  ```

- **Format for multiple users**
  ```shell
  python3 LoginTester.py -mul [username_file_path] [password_file_path] [Request Link]
  ```

**IMPORTANT!! (info regarding the host URL)**

Double check the url to which you are sending the requests like if your target is using PHP then check the form action (using using page source or browser extension).
In case of REST API request check the API path using inspect or with appropriate browser extension.
