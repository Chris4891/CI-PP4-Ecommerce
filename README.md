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
- [**Installation**](#installation)
   - [Mac/Linux](#for-mac-linux)
   - [Windows](#for-windows)
- [**PostgresSQL Configuration**](#postgresql-configuration)
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
- I used GitHub Projects to create a view, I used issues to make a to-do list for all the tasks that needed to be done.

- By using this method I divided this large project into smaller chunks which made it alot easier to manage.

- I mantained a checklist of wht needed to be done and what has already been done which helped me track my progress.

- Agile Methodology and GitHub Projects helped me map my progress against time.  

Click [here](https://github.com/users/Chris4891/projects/1) to view the github project


[Back to Table Of Contents](#table-of-contents)



# Features

## Existing Features


### Nav-bar and Logo

- The Navbar features all the categories that the user can browse through.
  
- The c1, c2, c3 and c4 are dummy sategories that can be modifies for adding further categories of products.

- The Django Shop logo was designed using canva and when clicked takes the user back to the home page of the website.

- The cart option has a small counte indicating the number items in the cart (please note that for the demo setup clicking the cart returns #, main usage implemented in core)

- A user can login into the website by clicking the login button on the navbar.

`Nav bar`
![Nav-bar](/WorkingSnaps/features/navbar.png)


### Home Page

- The home page has a animated slider to keep the UI aesthetic and clean, it also has a shop now button which leads users to listed products.

- All the categories of products are listed which enlarge upon clicking

- Featured products are also listed

- Season's Essential attire and it's image is also listed

- Training essentials and more products are also listed at the bottom

`Product Slide`
![Slider](/WorkingSnaps/features/slider.png)

`Categories`
![Categories](/WorkingSnaps/features/categories.png)

`Featured Products`
![Featured](/WorkingSnaps/features/featured.png)

`Season's Essential`
![Essential](/WorkingSnaps/features/essential.png)

`Training Essential`
![Training](/WorkingSnaps/features/training.png)

`More Products`
![More](/WorkingSnaps/features/more.png)

### Footer 

- The footer contains all the dummy buttons that you would find on a real ecommerce shop

- The contact Us button would display a pop-up with my contact details

- All the buttons can be made functional for future

- My copyrights have also been added at the bottom of the footer

`Footer`
![Footer](/WorkingSnaps/features/footer.png)
`Contact`
![Contact](/WorkingSnaps/features/contact.png)

# Installation
- First we need to install django library by the following command:
`pip install django`

- Then we need to create a virtual enviorment by following command:
`virtualenv env`

## For Mac/ Linux

`source env/bin/activate`

## For Windows

`./env/Scripts/activate`

`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python -m manage runserver`

# Admin Login

We can create a superuser for performing CRUD operations by following method:

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


