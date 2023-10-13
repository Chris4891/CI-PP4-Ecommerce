# Django Shop

Django Shop is a sophisticated online e-commerce platform characterized by its minimalist and engaging user interface. Our primary objective at Django Shop is to offer our users an uncluttered and intuitive interface, ensuring a seamless experience while shopping for the most up-to-date and superior products. We take pride in providing our customers with an opportunity to procure high-quality products at exceptionally competitive prices, maintaining the utmost standards of excellence.
(Developer: Kristijan Kolar)


![PP4](/WorkingSnaps/responsivetest.png)


[Live Demo](https://chris4891.pythonanywhere.com/)


## Table of Contents
- [**User Experience**](#user-experience)
- [**Features**](#features)
   - [Existing Features](#existing-features)
   - [Future Features](#future-features)
- [**Technical Design**](#technical-design)
   - [Agile Design](#agile-design)
   - [Data Model](#data-model)
   - [Wireframes](#wireframes)
- [**Technologies Used**](#technologies-used)
   - [Frameworks & Tools](#frameworks--tools)
- [**Validation**](#validation)
   - [Testing](#testing)
   - [Device Testing](#device-testing)
   - [Automated Testing](#automated-testing)
- [**Bugs**](#bugs)
   - [Solved Bugs](#solved-bugs)
   - [Remaining Bugs](#remaining-bugs)
- [**Deployment**](#deployment)
- [**Credits**](#credits)




# User Experience

### **User Stories**

#### **Site User**
- As a user I can view a home page of items so that I can view one to buy
- As a user I can view a catagories of products so that i can navigate to the desired one
- As a user I can click on an item to view ut's details
- As a user I can view the price on an individual product and its images
- As a user I can register for an account so that I can interact with content
- As a user I can add the desired item to cart
- As a user I can view all my cart items and their grand total
- As a user I can view add a product/item to favourites by marking it as favourite
- As a user I can click and view the social media links for the store

#### **Registered User**
- As a registered user I can add my email address
- As a registered user I can view my profile id
- As a registered user I can view my social account
- As a registered user I can logout so that other users cannot access my account
- As a registered user I can access my profile so that I can edit my details
- As a registered user I can delete my email address

#### **Site Admin**
- As a site admin I can add items
- As a site admin I can create, read, update, and delete items so that I can display the items that I want
- As a site admin I can delete or update user's profile so that I can manage my website
- As a site admin I can delete or update user's information
- As a site admin I can create coupons for my customers
- As a site admin I can create, update and delete categories so that I can manage my website


#### **Testing User Stories**



### Agile Methodology


[Back to Table Of Contents](#table-of-contents)


# Installation

`pip install django`

`virtualenv env`

# For Mac/ Linux

`source env/bin/activate`

# For Window

`./env/Scripts/activate`

`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python -m manage runserver`

# For Admin Login

```python
python manage.py createsuperuser
Username : admin
Password : 12345678
```


# Postgresql Configuration

Migrating from SQLite to PostgreSQL:
Prerequisites
Ensure you have PostgreSQL installed and running on your server.
Have your PostgreSQL credentials (database name, username, and password) ready.
Make sure you have a backup of your SQLite database in case anything goes wrong.
Step 1: Install Required Packages
Install the psycopg2 package, which is a PostgreSQL adapter for Django.
pip install psycopg2


'Creating a Postgresql Db'
createdb your_database_name
python manage.py migrate

'Creating user'
sudo -u postgres psql
createuser --interactive --pwprompt your_username
to exit => \q

OR 
for creating user other method:
CREATE USER your_username WITH PASSWORD 'your_password';
ALTER ROLE your_username SUPERUSER;
\q


