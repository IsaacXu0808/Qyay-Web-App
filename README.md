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

**Engine: MySQL8.0**

### 3. Run Locally

#### (0) Make sure you have a up-to-date version of [Node.js](https://nodejs.org/en), [MySQL8.0](https://dev.mysql.com/downloads/) and [Python3.12](https://www.python.org/downloads/) installed before setting up.

#### (1) Setup the database.

##### (1.1) Make sure the mysql service is on (for Windows computers, I go to task manager --> service --> mysql80 --> right click and start, or you may [Start MySQL from the Windows Command Line](https://dev.mysql.com/doc/refman/8.0/en/windows-install-archive.html).

Please be aware of your local user name, local user password and local port number.


##### (1.2) Create a new database called "qyay". I suggest you use a [MySQL Workbench](https://www.mysql.com/products/workbench/). You can either run the command or use the GUI to manipulate the database.

```sql
create DATABASE qyay
```

##### (1.3) Configure the connection between Django and MySQL. You can change any of these settings in /QYay_Backend//QYay_Backend/settings.py line 89 to 98 into your settings. My settings are as following:

Database name: **qyay**

Local user name: **root**

Local user password: **123456**

Local port: **3306**

##### (1.4) Go to the backend directory (/QYay_Backend/QYay_Backend/) in a console. Run the following commands to migrate the database:

```cmd
python3.12 manage.py makemigrations
```

```cmd
python3.12 manage.py migrate
```

An alternative is to copy my database "/qyay/" to your local MySQL data folder. Then you can use my test data which have many items. The following account is recommanded:

(user id: week2test, password: I2FTI2FT).

#### (2) You need a few Python packages before launching teh backend server. Run the following commands to ensure that they are installed for Python3.12.

```cmd
python3.12 -m pip install django
```

```cmd
python3.12 -m pip install pymysql
```

```cmd
python3.12 -m pip install mysqlclient
```

#### (3) Go to the backend directory (/QYay_Backend/QYay_Backend/) in a console and run the following command to start the backend server.


```cmd
python3.12 manage.py runserver
```

Now the frontend server is running on port: http://localhost:8000.

#### (4) Go to the frontend directory (/QYayApp) in a console. I inculde the modules in the folder so you do not need to install any dependencies. However, to make sure everything needed exists, run the command:

```cmd
npm install
```

#### (5) Run the following command to start the frontend server.

```cmd
npm run dev
```

Now the backend server is running on port: http://localhost:5173

#### (6) Open  the following link in a browser to start the web app.

[QYay App!](http://localhost:5173 )

##### (7) The pages are temporarily designed for only (2520 * 1440) display so it is strongly recommanded to zoom in or zoom out the pages to a proper size if you use a display with other sizes (e.g. 80% for a 1920 * 1080 screen).

# Week 2 Update

## 1. Features Implemented

#### (1) A home page to select from join / login / register.

#### (2) A login page to fill in user id and password to login.

#### (3) A register page to create accounts. After registering, redirect to the login page and automatically fill in the user id and password.

#### (4) After login, the user can see their list of events and a button to create a new event.

#### (5) One can select one of the events in the list to retrieve the information (and get started, not implemented yet) and go back to the event list.

#### (6) A create-event page to fill in the information and create an event. An invitation code will generated for future use.

#### (7) After creating the event, redirect to the event-info page (like (5)).

#### (8) Other features include a Terms and Policies page, a button to sign out, etc.

#### To conclude, the user (organizer) can sign up (register), sign in (login), create events and see the information of created events.

## 2. Major Difficulties and Challenges

* #### Miss the invitation code at first. Everything related to the attributes of an event and the table of events needed to start over.
* #### Unfamiliar with the styling of components.
* #### Complicated design and implementation of page-routing, especially routing with parameters in vue3.

## 3. Learning Resources

* #### [Vue.js documentation](https://vuejs.org/guide/introduction.html)
* #### [ Bootstrap v5.3 documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* #### [Django documentation](https://docs.djangoproject.com/en/5.0/)
* #### [Stack Overflow](https://stackoverflow.com/)
* #### [CSDN](https://www.csdn.net/)

# Week 3 Update

## 1. Features Implemented

#### (1) Organizers can activate (start) and enter an event on the entry page. They go back to the event list page after termination.

#### (2) By entering an event, the organizer can see the question list, go back to    their event list page or terminate the current event. Note that the organizer cannot submit questions.

#### (3) An viewer (audience) can input the six-digit invitation code to search for an event on the join page. If the event is currently ongoing, they can enter the event and see the question list.

#### (4) The viewer can see the question list and edit and submit new questions on the question list page. New questions are shown on the bottom of the list. No user info will be associated with questions so that questioning is completely anonymous.

#### To conclude, the following two user stories are implemented. In addition, organizers can edit the status of their events (unactive / ongoing / terminated).

* As an attendee, I want to join the event using a unique link or code, so that I can submit my questions.
* As an attendee, I want to submit questions anonymously, so that I can freely ask questions without any privacy concerns.

## 2. Major Difficulties and Challenges

* #### Miss the invitation code at first. Everything related to the attributes of an event and the table of events needed to start over.
* #### Unfamiliar with the styling of components.
* #### Complicated design and implementation of page-routing, especially routing with parameters in vue3.
* #### Fitting the size of the page to different devices is difficult and still under 

## 3. Learning Resources

* #### [Vue.js documentation](https://vuejs.org/guide/introduction.html)
* #### [ Bootstrap v5.3 documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* #### [Django documentation](https://docs.djangoproject.com/en/5.0/)
* #### [Stack Overflow](https://stackoverflow.com/)
* #### [CSDN](https://www.csdn.net/)
