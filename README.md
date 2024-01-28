# QYay App! - A web application

## 1. Environment

**OS: Windows 10**

**IDE: VSCode**

**Browser: Edge**

## 2. Tech Stack

### (1) Frontend:

**Framework: vue3 (v 3.4.15)**

**JavaScript node.js v 20.11.0**

### (2) Backend:

**Framework: Django (v 5.0)**

**Python: v 3.12.1**

### (3) Database:

**Engine: MySQL**

### 3. Run Locally

#### (1) Start the Mysql service

The database must follow these properties:

Database name: **qyay**

Local user name: **root**

Local user password: **123456**

Local port: **3306**

Note that the "Hello world!" message and other information are all from the database so you need to copy my database before testing.

#### (2) Go to the backend directory (/QYay_Backend) in a console

#### (3) Run the following command to start the backend server

```cmd
python3.12 manage.py runserver
```

Now the backend server is running on port: http://localhost:3306

#### (4) Go to the frontend directory (/QYayApp) in a console

#### (5) Run the following command to start the frontend server

```cmd
npm run dev
```

Now the backend server is running on port: http://localhost:5173

#### (6) Open  the following link in a browser to start the web app

[QYay App!](http://localhost:5173 )
