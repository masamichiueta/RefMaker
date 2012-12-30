#RefMaker

"RefMaker" is a simple reference manager for you. You can create and save your references. 

The creators of RefMaker are @maasaamiichii and @kyonpeeeei.

We want to improve RefMaker more and more.

**Please folk RefMaker and send pull request.**


###Amazing Features of RefMaker
***

**1  Manage your references**

You can create your reference lists very easily. You are no longer having to worry about the management of your references.

**2  Share your references**

Searching references from huge resources is very troublesome. You can share your references with friends.

**3  Follow your friends**

You can follow your friends, acquaintances, respected researchers. If your followers are in similar fields, it's easy to discover good references.

[RefMaker Web Site](http://www.ref-maker.com)

# Requirements

* Python 2.7 and higher version
* Python libraries
    * Please check "requirements.txt"
* MySQL 5.0 and higher version
* Git

# Install

This install guide is written assuming that git, mysql, apache mod_wsgi and python are already installed and set up.

## 1. Download RefMaker

Clone RefMaker repository.

```
$ git clone https://github.com/maasaamiichii/RefMaker.git /path/to/your_local_repository
```


## 2. Install Python libraries
```
$ cd /path/to/your_local_repository/refmaker
$ sudo pip install -r requirements.txt
```

## 3. Setup MySQL

Create MySQL database.

```
$ cd /path/to/your_local_repository/refmaker
$ mysql -u root -p < db/create_tables.sql
$ mysql -u root -p < db/insert_bibtype_info.sql
```

## 4. Setup configuration

Copy a configuration example.

```
$ cp config/refmaker.ini.example config/refmaker.ini
```
    
Then, edit refmaker.ini.
Change **SQLALCHEMY_DATABASE_URI**, **MAIL_USERNAME**, **MAIL_PASSWORD** according to your environment.

```
DEBUG=False
TESTING=False

SECRET_KEY = 'secret key here'

SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/refmaker?charset=utf8'

DEFAULT_MAIL_SENDER = 'info@ref-maker.com'
SECURITY_REGISTERABLE = True
SECURITY_CONFIRMABLE = True
SECURITY_RECOVERABLE = True

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'user_name@gmail.com'
MAIL_PASSWORD = 'password'

SECURITY_PASSWORD_HASH = 'sha512_crypt'
SECURITY_PASSWORD_SALT = 'secret-shared-key-goes-here'

SECURITY_POST_LOGIN_VIEW = '/'

NUM_BY_PAGE = 50
```

If you want to use virtualenv, you have to edit **config/virtualenv.ini**.
Specify activate python file for your virtualenv.
Notice that you must not add quotation characters (', ") to the file path.

```
$ cp config/virtualenv.ini.example config/virtualenv.ini
    
[virtualenv]
VIRTUALENV_ACTIVATE=/path/to/env/bin/activate_this.py       
```

If you do not use virtualenv, delete this file (virtualenv.ini).

## 5. Setup Apache2

Setup WSGI in apache2 configuration like the following:

```
apache
<virtualhost *:80>
    DocumentRoot "/path/to/your_local_repository/refmaker/app"
    ServerName refmaker.example.com
    WSGIScriptAlias / /path/to/your_local_repository/refmaker/app/refmaker.wsgi
</virtualhost>
```

Restart apache.

Access to **http://refmaker.example.com** from Web browser.


# License

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.

You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.