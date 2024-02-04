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

# Week 2 Update

## 1. Features Implemeted

##### (1) A home page to select from join / login / register.

##### (2) A login page to fill in user id and password to login.

##### (3) A register page to create accounts. After registering, redirect to the login page and automatically fill in the user id and password.

##### (4) After login, user can see thier list of events and a button to create a new event.

##### (5) One can select one of the events in the list to retrieve the information (and get started, not implemented yet) and go back to the event list.

##### (6) A create-event page to fill in the information and create an event. A invitation code will generated for future use.

##### (7) After creating the event, redirect to the event-info page (like (5)).

##### (8) Others features include a page of Terms and Policies, a button to sign out, etc.

#### To conclude, the user (organizer) can sign up (register), sign in (login), create events and see the information of created events.

## 2. Major Difficulties and Challenges

* ##### Miss the invitation code at first. Everything related to the attributes of an event and the table of events needed to start over.
* ##### Unfarmiliar with the styling of components.
* ##### Complicated design and implementation of page-routing, especially routing with parameters in vue3.

## 3. Learning Resourses

* ##### [Vue.js documentation](https://vuejs.org/guide/introduction.html)
* ##### [ Bootstrap v5.3 documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* ##### [Django documentation](https://docs.djangoproject.com/en/5.0/)
* ##### [Stack Overflow](https://stackoverflow.com/)
* ##### [CSDN](https://www.csdn.net/)

