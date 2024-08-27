**Overview**
Platform: The website is a Facebook clone, a type of social networking site where users can create posts, interact with other users by liking and commenting, and manage their profiles.

**Key Features**

1. User Registration and Authentication:
Every user must create a unique account. This process involves providing personal details and setting up login credentials (username and password).
Authentication ensures that only registered users can access certain features of the website, like creating posts or interacting with others.

2. User Posts:
Users can create their own posts. These posts can contain text, images, or other media, depending on how you've implemented it.
Posts are stored in the SQL database, along with metadata like timestamps and user information.

3. Interactions:
Users can like and comment on other users' posts. These interactions enhance engagement on the platform and foster a sense of community.

5. Admin Panel:
There is an admin login that allows site administrators to manage users and content. This could include deleting inappropriate posts, managing user accounts, and maintaining the overall health of the site.

Technologies Used
Backend: Django Framework
Frontend: HTML, CSS, and JavaScript
Database: SQL


Requirements:
asgiref==3.3.0
dj-database-url==0.5.0
Django==3.1.3
django-ckeditor==6.0.0
django-heroku==0.3.1
django-js-asset==1.2.2
Pillow==8.0.1
psycopg2==2.8.6
pytz==2020.4
sqlparse==0.4.1
whitenoise==5.2.0


How to run the project:
pip install -r Requirements.txt
python manage.py runserver

Go to http://127.0.0.1:8000/
