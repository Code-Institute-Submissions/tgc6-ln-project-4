# **PROJECT 4 : THEMASKSHOP E-COMMERCE WEBSITE**

## Objective    
**theMASKshop** is a e-commerce platform that allows sellers and buyers to transact on the platform. As mask have become an essential item, the platform allows different mask-makers and resellers to market their product. 
    
### SCOPE
The website allows User to :
* Allow User to register for new account and login 
* CREATE / READ / UPATE / DELETE a product for sale
    
### Demo
A live demo can be found here. https://lionel-proj4.herokuapp.com/

### UX
User Story
There are mainly 3 types of users for this website 
* Owner
    - set  up a platform for buyer and resellers to interact and engage in a sales transaction
    - generate revenue from hosting fee and potential advertising fees on advertising banners in the future.
* Registered User
    - surf for product to buy and make a purchase through a secured platform
* Register Resellers
    - create and list their product suites
    - leverage on the potential customer base from the platform to market their product
    - generate sales through the platform 

### Technologies Used
1. HTML, CSS & Javascript 
2. Bootstrap 
3. Python 
4. SQLite (during development)
5. Postgres (when deployed onto Heroku)
6. Heroku (deployment)
8. Django Crispy Forms for styling Forms
9. Cloudinary for storing images 
10. Stripe for handling payment 
11. Whitenoise to manage static file 
12. Gunicorn 
13. Gitpod online IDE
14. CrispyForms (Together with Boostrap 4) https://django-crispy-forms.readthedocs.io/en/latest/install.html#
16. Fontawesome


### Features
		
**My Design of the site :**
* Easy for resellers to navigate and post / update and remove their products
* Simple and easy for user to browse and make purchase for the products
    
_Current Limitations:_
* no search function at the moment due to time limitation
* Social media links not link not set up

### Testing
(i) Mobile Responsiveness

This site was tested across multiple devices multiple mobile devices (iPhone 4, 5, 7: Chrome and Safari, iPad, Samsung Galaxy) to ensure compatibility and responsiveness.)

(ii) Browser Compatibility

This site was tested across multiple devices multiple mobile devices (iPhone 4, 5, 7: Chrome and Safari, iPad, Samsung Galaxy) to ensure compatibility and responsiveness.)

(iii) User authentication restricts access and allows superusers to create, edit and delete product.

(iv) Test Cases
Manual Testing is done to ensure that the all functions are functional.
Test Results as follows :

*No* | *Steps* | *Expected Results* | *Observations*
--- | --- | --- | ---
**SUPERUSER LOGIN**|
1  | Upon login | `option __Admin Console__ appears on navbar` | **Pass*
2  | Click on **Admin console** | `route to admin console and display all products` | **Pass*
3  | Click on **Add Product** | `route to add product page for user to enter and submit in new product` | **Pass*
4  | Click on **Edit (Pen logo)** | `route to edit a product and submit in the changes` | **Pass*
5  | Click on **Remove Product** | `route to remove product page for user to confirm the removal of product` | **Pass*


*No* | *Steps* | *Expected Results* | *Observations*
--- | --- | --- | ---
**Normal Browsers**|
1 | On index page, click on **desired product 'image' or 'name'** | `Route to display selected product information`| **Pass** 
2 | In product detail page, click **Add to cart** |`add quantity of 1 to cart`|**Pass**
3 | In cart page, click **+ sign** |`add 1 to the quantity`|**Pass**
4 | In cart page, click **- sign** |`reduce 1 from the quantity`|**Pass**
5 | In cart page, click **checkout** |`route to summary of items and payment option`|**Pass**
6 | In payment page, click **Pay with card** |`Stripe default payment form pops up for user to key and submit`|**Pass**
7 | In payment form, click **Pay** |`aPayment made and routed to index page with message for payment made`|**Pass**

_To test checkout please key in the following credit card details:_

    Email: -any email address of your choosing-
    Card information: 4242 4242 4242 4242
    MM/YY: 12 / 22
    CVC: -any number of your choosing 3 or 4 digit-


### Deployment
This site is hosted using Heroku App Link : 
https://lionel-proj4.herokuapp.com/

All codes are uploaded to GitHub and links are made to Heroku by installing in bash terminal in projects.
Regular commits are push to the Github subsequently push to heroku to deploy.
.gitignore file is added to remove files that are not required or files that we do not wish to be uploaded to Github

To deploy on Heroku:
* To list all the requirements in requirements.txt, run the following command in terminal:
* pip3 freeze --local > requirements.txt
* Procfile need to be created to run gunicorn upon deployment
* Git push to Heroku Master after all the documents are properly set up
* All public keys and private keys for the following need to be added to in Heroku Config Vars settings:
- CLOUDINARY_API_KEY
- CLOUDINARY_API_SECRET
- CLOUDINARY_CLOUD_NAME
- DATABASE_URL
- STRIPE_PUBLISHABLE_KEY
- STRIPE_SECRET_KEY

### Media
Pictures are extracted from www.pexel.com

### Credits
Uses W3School for many reference (https://www.w3schools.com/)
Uses Fontawesome for the various icons (https://fontawesome.com/)
Uses Bootstrap for templates (https://getbootstrap.com/)

 
