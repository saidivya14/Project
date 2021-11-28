# Project

It is a simple, User-friendly, secured website that helps to clone the best features of classroom

## Features Included

>  ### Users
>  - User can register/login/logout/reset-password in this website
>  - When user registered he/she will get confirmation message in mail
>  - User can reset password through mail
>  - User can edit their profile

>  ### Classroom
>  - User can create/join a classroom
>  - User who created classroom can post announcement/create assignment/review assignment and grade assignment of students
>  - User can post assignment only in the classroom they created
>  - User can see due assignments in to do
>  - User can review students submissions in to review
>  - User can comment publicly in classroom or privately under his/her submission
>  - User can see the teachers/students in particular classroom 

>  ### Courses
> - One can ADD/UPDATE/DELETE course
> - Every course contains title, description, reference link, tumbnail image

>  ### IDE
>  - User can write any number of lines of code in their preferred language
>  - Used sphere-engine API to create IDE

> ### CALENDAR
> - User can create/edit events in calendar
> - User can see calendar in the calendar page

## Setup the project 

**1. Clone Repository & Install Packages**
```sh
git clone https://github.com/saidivya14/Project.git
pip install -r requirements.txt
```

**2. Setup Environment**
```sh
python -m  venv venv
source venv/bin/activate
``````
OR on Windows
```sh
python -m  venv venv
activate.bat
``````

**3. Migrate & Start Server**
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
