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
- [**Admin Login**](#admin-login)
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

### Products

- The items/Products are displayed in form of a "Product Card"

- The image covers most of the are along with a product status tag.

- The product could be new collection or on sale ine either case a tag is displayed on the image of the product.

- The title of the item/product is displayed along with the price tag

- The option to add the item to cart is displayed at the bottom

![Products](/WorkingSnaps/features/products.png)

### Add to cart

- The item can be added to cart by selecting the respective option.

- A pop-up is displayed notifying the product that has been added to the cart.

![addedtocart](/WorkingSnaps/features/addedtocart.png)

### Favourites

- An item/product can be added to favourites by pressing the heart icon on the top right corner of the product image.

![Favourites](/WorkingSnaps/features/favourite.png)

### Price Filter

- The user can apply a price filter.

- Items would be displayed within the budget constraint given by the user.

![pricefilter](/WorkingSnaps/features/pricefilter.png)

### Color Filter

- The user can apply a color filter.

- Only the products that are themed on that particular color will be displayed.

![colorfilter](/WorkingSnaps/features/colorfilter.png)

### Item Search

- The user can search for his/her specific product.

- The matching or closest to matching results are shown to the user.

![searchproduct](/WorkingSnaps/features/searchproducts.png)

### Social Media

- The user can click on any of the social media icon.

- Upon clicking the user would be redirected to the website's social link.

- Please Note that at this point in time these icons only redirect to the main social media pages.

![socialmedia](/WorkingSnaps/features/socialmedia.png)

### Sorting

- The user can apply various sorting techniques to view the appropriate list of items.

- The user can choose Default sorting.

- The user can choose popularity as a sorting method.

- The user can choose price: low to high as a sorting method.

- The user can choose price: high to low as a sorting method.

- The user can choose from predefined pricing options as a methos viewing items.

![sorting](/WorkingSnaps/features/sorting.png)

### View Cart

- The user can view his/her items that he/she added to the cart at any time by clicking the shopping bag icon on the top right corner of website.

![shoppingbag](/WorkingSnaps/features/shoppingbag.png)

### Login

- An autheticated user or admin can login into the website.

- username and password are required for login.

- Upon login users with different permissions can add delete or change different things and sections of the website.

![LogIn](/WorkingSnaps/features/login.png)

### Recent Actions

- Upon login the user/admin can view the recent actions that have been take.

- This acts as a sort of a log file for any new user or mapping the changes.

![recentactions](/WorkingSnaps/features/recentactions.png)

### Accounts

- Upon login all the registered accounts can be viewed.

- This includes the email addresses of all the users.

- The ability to add more.

- The ability to delete previous users account.

![Accounts](/WorkingSnaps/features/accounts.png)

### Authentication and Authorization

- Upon login the user/admin can add groups or users.

- The ability to limit each individual's permissions on website.

- This feature allows to distinguish between different actors.

![Authorization](/WorkingSnaps/features/authorization.png)

### Core

- Upon login the core features of the website can be viewed.

- The ability to add any more core features to the website.

- The ability to delete any existing core feature/s of the website.

- The ability to modify/change the existing core features.

![Core](/WorkingSnaps/features/core.png)

### Social Accounts

- Upon login the users would have the ability to set the Social accounts for the website.

- The ability to add more social accounts such as facebook, X, Instagram to the website to increase it's reach to the potential customers.

- The ability to delete any previously linked social account of the website.

![SocialAccounts](/WorkingSnaps/features/SocialAccounts.png)

### Add Users

- Upon login the users would have the ability to add more users.

- This would require a unique username.

- A password for that unique username.

- A confirm password for that user.

- Upon adding the user his/her permissions can be set and his access can be limited.

![AddUsers](/WorkingSnaps/features/adduser.png)

### Add Items

- Upon login the users/admin would have the ability to add items/products.

- This includes adding product Title, Product's price, any discounted price, Product's category, Product's label, slug, stock no. short description and long description.

![Add items](/WorkingSnaps/features/additem.png)

### Add coupon

- Upon login the users/admin would have the ability to add coupons.

- This includes setting the coupon's unique code and amount.

![Add coupons](/WorkingSnaps/features/addcoupon.png)

### Add Category

- Upon login the user/admin would have the ability to add product category.

- This includes naming the category title, it's slug, a description for that particular category, Category image, and a flag that can bet set to active.

![Add category](/WorkingSnaps/features/addcategory.png)

### Add Billing Address

- Upon login the users can add or delete their billing address.

- This includes selecting the user(that is authenticated), his Street address, apartment address, country, zip, and address type.

![Add billing](/WorkingSnaps/features/addbilling.png)

### Add Order Item

- Upon Login the user can add his/her order items/s.

- This includes selscting the user.

- Flag that tells if the item has been ordered.

- Selecting the item that has been ordered.

- Selecting the quantity of the item.

![Add Order](/WorkingSnaps/features/addorderitem.png)

### Add order

- Upon login the users can add their complete order.

- This can include multiple items from different categories as opposed to the previous "Add Order Item".

- Multiple order parameters need to be set in order to add a complete order.

![Add Order](/WorkingSnaps/features/addorder.png)

### Add payment

- Upon login the user can add his/her payment method.

- Since the website uses stripe as payment gateway, the user must add his/her stripe charge id along with selecting his/her username and the amount.

![Add Payment](/WorkingSnaps/features/addpayment.png)

### Add Refund

- Upon Login the users/admins can add or delete a refund.

- This included selecting the approriate order.

- The reason for refund.

- A flag that tells if the refund is accepted or not.

- And the email id of the user.

![Add Refund](/WorkingSnaps/features/addrefund.png)

### Add Slide

- Upon Login the users can add or delete slides displayed on the home page.

- This includes including the main caption and the sub-caption.

- Providing the link for the slide.

- Browsing for the photo on system for the slide.

- A flag that tells if that slide has gone active into production or not.

![Add Slide](/WorkingSnaps/features/addslide.png)

### Password change

- Upon login the user/admin can request to change his/her password.

- This includes typing in the old password.

- typing in the new password and typing it again for confirmation.

![Password Change](/WorkingSnaps/features/passwordchange.png)

### Theme

- Upon login the user can choose the theme he/she wants.

- By default it is set to dark.

- It can be switched to light/dark/default

![Theme](/WorkingSnaps/features/theme.png)

## Technical Design

[Coolors.co](https://coolors.co/) was used to create following colour pallette. 

![Colour pallette](/WorkingSnaps/features/colorpallette.png)

- Tomato, white, Jordy Blue and black colour were used for Django shop.

[Fonts Awesome](https://fontawesome.com/) was used for fonts in this project. 

### Agile Design

- Using Github projects I created issues for User Stories, fixes and to-do list which helped me manage my task. 

- As it was my first time using Agile approach, I found myself very often adding new user stories and adjusting existing user stories in different ways.

#### View Board

- As a visual representation of the project's status, I was using View Board. Here is the [link](https://github.com/users/Chris4891/projects/1)

## Testing

### Device Testing

- project was tested during and post development on following devices:

   - Mac
   - Iphone 8 plus
   - Ipad Air

### Browser Testing

- Project was tested during and post development on following browsers:

   - Chrome
   - Firefox
   - Safari

### Automated Testing

- Automated testing was conducted utilizing the "unittest" module from the Python standard library, which is integrated with Django's unit tests. 


[Back to Table Of Contents](#table-of-contents)

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


