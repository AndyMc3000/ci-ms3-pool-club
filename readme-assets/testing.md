<a name="top-of-page">![Cill na Martra Pool Club (CPC) Logo created using Canva.com and Clipart.com](/readme-assets/cpcp-logo-readme-header.png)</a>


# Cill na Martra Pool Club - Testing Document :microscope: #  

<br>

## Table of Contents ##
1. [Development Testing](#development-testing)
1. [User & Client Stories Testing](#user-client-stories-testing)
1. [Code Validation](#code-validation)
1. [Manual Testing](#manual-testing)
1. [Browser Testing](#browser-testing)

<br>

## 1. <a name="development-testing">Development Testing</a> ##

During the development process I manually tested elements, components, and functions after I added them to the website. If I encountered an issue or bug, in most cases I worked to resolve it straight away. 

I have listed the tests I did including those where I encountered bugs here (mostly these are in date order, but some tests would have been done at several different times during development;

#### Tests ####

* Tested deployed app. The first thing I did was to setup my development environment and deploy an app on Heroku. To do this I created a GitHub repository using the Code Institute template. I then used GitPod as my IDE for the project. I created the following files; index.html, app.py, env.py, requirements.txt and a Procfile on GitPod. I then installed Flask, PyMongo, and dnspython. I then created a new database in MongoDB Atlas, created a collection in that, and connected that database to my main application file (app.py). I then created a new app on Heroku adding my environment variables, while also setting up automatic deployment when updates were pushed to my GitHub repository. I then used Flask to create a base.html file, along with a new template/view (index.html). I also added a python function to that view to call data from my test collection on MongoDB. When I commited and pushed my changes, and refreshed my Heroku app url, the required data was listed on the page as expected. 
* README links and images test. I also began writing up my README.md file around this time, and over time would update my README with content and files etc. I created a folder called readme-assets and added any images or files I wanted to include in my README to it. These files included a header logo, an image showing a screenshot of the site on multiple devices, and images showing the site colours, site fonts, and logo's for the technologies used. The README also contains links to a Sitemap image, and six different wireframe images. It also contains a link to this testing document. Once I added any files or links to my README I tested them to ensure that they presented or worked as expected. All worked as expected.
* Added a Bootstrap Navigation bar to base.html, complete with Club logo linking to index.html, along with navigation links to Home (index.html), Log In (login.html), and Register (register.html). I tested all links and they worked as expected.
* Created a footer on base.html to include a club logo linking to index.html. I tested it and it worked as expected.
* Added Bootstrap (CSS and JavaScript), FontAwesome, and jQuery CDN links, as well as static files for my JavaScript and CSS files. I tested that the stylesheets are being target corrected by adding content etc. They worked as expected.
* Added a carousel at the bottom of base.html for sponsor banners. Each banner links to an external website. I tested that functionality and it worked as expected.
* Added a login.html page, and added login functionality in app.py. Once logged in a user should be taken to their Player Homepage. I tested this and it worked as expected.
* Added additional Nav bar links to navbar on base.html. These new links link to 'MyHome' (player-home.html), 'Log Out' (I added a logout function in app.py), and 'Admin' (admin-home.html. Using Jinja2 I restricted the visibility of these links to registered users. I tested the Log Out link and it functioned as expected (I was redirected to the login.html with a flash message to say I had successfully been logged out).
* Added a carousel to the top of index.html for 'hero images' and promotional messaging. The carousel slides include a button which link to the registration page using the Jinja2 tempalting language(register.html). I tested the carousel functionality and the button links and all worked as expected.
* Added a button to the introduction section on index.html which links a user to the registration page. I tested it and it worked as expected.
* Added 'Current League' button to the 'Our Leagues' section on index.html which links a user to the active league Table. I tested it and it worked as expected
* Added 'Contact Us' form to index.html. Using the EmailJS email service, this form can be used to send a message to Club organisers. A user would also receive an email by way of confirmation that their message had been received by the club. I setup an EmailJS template and added the required JavaScript to my script.js file. I also added Bottstrap form validation JavaScript for all forms to script.js. Once everything was in place I tested the system and it worked as expected.
* Created templates for 'Player Home' and 'Admin Home' and added cards for each view linked from those pages. Each card has a button which links to the relevant template view. I tested these and all worked as expected.
* Created templates for all required pages. Added 'Back' buttons to the top and bottom of these pages. Tested all and all worked as expected.
* Exception Handling


#### [Back To Top ^ ](#top-of-page) ####

<br>

## 2. <a name="user-client-stories-testing">User & Client Stories Testing</a> ##

I tested each of the Client and User stories which were used to determine the features, functions and styling of the CPC website. See the results of these tests here; 

#### Client Stories ####
> - [x] “One of the main goals of the website is to grow the membership of Cill na Martra Pool Club, and to provide value to visitors in the information is provides about the CPC.” - Result: The site describes what the club is, what the benefits are of being a member, and how leagues operate.
> - [x] “The website must give Club organisers a place to add new members and create and edit Leagues.
> - [x] “The website must allow users on the site to view the current League Table.” 
> - [x] “The website must allow new members to register and join the Club.” 
> - [x] “The website must provide an area where club members can view their current League statistics.”
> - [x] “The website must provide an area where club members can add a Match result when they have acted as a Match Referee. Adding a match must update the League Table and a members League statistics appropriately.”
> - [x] “The website must provide an area where club members can edit and update their Account information.”
> - [x] “The website must provide an area where site Admininstrators can add a new League."
> - [x] “The website must provide an area where site Admininstrators can add a new Player/Member."
> - [x] “The website must provide an area where site Admininstrators can edit or delete a League."
> - [x] “The website must allow users to find contact details for Club organisers and include a Contact Us form.”
> - [x] “The website must have a section showing banner adverts for CPC sponsors.”
> - [x] “The website must be mobile-friendly.”
> - [x] “The website colours must be dark. The website will be used by Players at Match events on their mobile phones, and so a dark colour scheme will ensure that viewing the website while near a pool table will reduce the risk of Player distraction.”

#### User Stories ####
> - [x] “I want to learn about what the CPC is.”
> - [x] “I want to be able to view the current League Table.”
> - [x] “I want to be able to register and sign-up to join the CPC.”
> - [x] “Once I'm sined-up and logged in, I want to be able to view my personal League statistics - my League Points, and my Matches Won/Lost.
> - [x] “If I act as a Referee for a League Match, I want to be able to record the Match result and update the current League Table.”
> - [x] “I want to be able to edit and update my Account information."
> - [x] “I want to be able to find contact infromation for the CPC, and be able to send a message to the CPC organisers."

#### [Back To Top ^ ](#top-of-page) ####

<br>

## 3. <a name="code-validation">Code Validation</a> ##

I ran the website through the W3C validators for [HTML](https://validator.w3.org/) and [CSS](https://jigsaw.w3.org/css-validator/). I also ran my JavaScript code through the [JSHint.com](https://jshint.com/) code checker, and used the PEP8 checker at [PEP8online.com](http://pep8online.com/) to check my Python code for PEP8 compliance.  

#### HTML ####

The validator highlighted the followings errors across index.html and contact.html.

* The aria-controls attribute must point to an element in the same document.
* The aria-describedby attribute must point to an element in the same document.
* The aria-describedby attribute must point to an element in the same document.
* Illegal character in path segment: space is not allowed.
* An img element must have an alt attribute, except under certain conditions.
* Element h3 not allowed as child of element span in this context. 
* Attribute row not allowed on element div at this point.

All errors were fixed by making neccessary changes.

#### CSS ####

The W3C CSS Validation Service

The validator highlighted the following errors in style.css;

* 44	.close:hover	Parse Error (1.3)
* 51	.close i:hover	Parse Error (1.3)
* 176	.btn-danger:hover	Parse Error (1.2)
* 275	.navbar button:hover	Parse Error (1.2)
* 357	.button.nav-link.mymenu:hover	Parse Error (1.2)

All errors were fixed by making necessary changes.

The validator also highlighted 2 x Errors and 768 x Warnings relating to the bootstrap.min.css style sheet. I queried this with Student support and was advised that as I have no control over the Bootstrap style sheet as I am using a CDN to access the file, these were acceptable issues.

#### JavaScript ####

I ran the following files though the JSHint validator;

store.js
maps.js
emailjs-homepage-request-a-quote.js
emailjs-contact-page-contact-form.js
bootstrap-form-validation.js

Once I configued the validator to accept jQuery and JavaScript ES6, no Errors were listed.

#### Python ####
......

#### [Back To Top ^ ](#top-of-page) ####

<br>

## 4. <a name="manual-testing">Manual Testing</a> ##

I manually tested all website elements/components under the following headings;

### Homepage ###

#### Navbar ####
* When I click on the party Chef Logo in the navbar it loads index.html as expected.
* The Home link button on the navbar shows an active status (button border) as expected.
* When I hover over the Contact button in the navabr it changes color as expected.
* When I click on the Contact button it opens contact.html as expected.
* When I click on the MyMenu button it opens the MyMenu Modal as expected.

#### Hero Image ####
* When I hover over the button on the hero images (Jumbotron) it hovers and grows as expected.
* When I click on the hero image button it opens contact.html as expected.

#### Menus Section ####
* When I hover over any/all menu accordion heading button it changes color and grows as expected.
* When I click on the menu heading button it opens the menu accordion as expected.
* When I click inside the open accordion the list of items scroll up/down as expected.
* When I hover over the 'Add To MyMenu' button it grows as expected.
* When I click on the 'Add To MyMenu' button it and alert appears to say 'Menu item added to your MyMenu' as expected.
* When I close the alert the item quantity indicator on the MyMenu button increases by one as expected.
* When I click on the MyMenu button the MyMenu modal opens and my item is listed as expected.
* When I add multiple items to MyMenu they all appear as expected.

#### Gallery Section ####
* When I hover over the gallery section image it grows as expected.
* When I click on the gallery section image it opens the gallery modal showing photo number one as expected.
* When I click the 'next' carousel control icon the next photo appears as expected.
* When I keep clicking the next carousel control button all images appear correctly as expected.
* When I click the previous carousel control button the previous photo appears as expected.
* When I click the close button on the modal the modal closes as expected.
* When I open the gallery carousel and click anywhere on the page outside the modal the modal closes as expected.

#### Footer ####
* When I hover over the Home and Contact Us navigation buttons they change colour as expected.
* When I click on the Home button it reloads the homepage as expected.
* When I click on the Contact Us button it loads contact.html as expected.
* When I hover over the social media icons they grow as expected.


### MyMenu Modal ###

#### Modal ####
* When I click on the MyMenu button in the nabar the MyMenu modal opens as expected.
* When I click the close button on the modal the modal closes as expected.
* When I open the MyMenu modal and click anywhere on the page outside the modal the modal closes as expected.

#### MyMenu Item List ####
* When I add an item to the MYMenu modal it appears in the list which a default quantity of 1 as expected.
* When I add an item to the MyMenu modal the 'Total' price figure updates correctly as expected.
* When I try to reduce the item quantity using the quantity controls I am stopped from reducing the quantity to zero as expected.
* When I increase the item quantity using the quantity controls the Total price increases correctly as expected.
* When I reduce the item quantity the Total price figure reduces correctly as expected.
* When I click on the remove item buttom the item disappears and an alert appears.

#### Reast-A-Quote Form ####
* When I click on the Contact Us link in the Request A Quote introduction section contact.html loads as expected.
* When I hover on the 'Lets Party' button it changes color and grows as expected.
* When I enter details in all fields correctly and hit the 'Send Request' button on the form, the Bootstrap validation highlights the fields in green as           expected.
* When I enter details in all fields correctly and hit the 'Send Request' button on the form, an Alert appears to notfy me my message has been sent.

### Contact Page ###
#### Navbar ####
* When I click on the party Chef Logo in the navbar it loads index.html as expected.
* The Contact link button on the navbar shows an active status (button border) as expected.
* When I hover over the Home button in the navbar it changes color as expected.
* When I click on the Home button it opens index.html as expected.

#### Google Map ####
* When Google Map controls work expected - Pan, Zoom in/out, Pegman, Map/Satellite views, and Full screen mode.
* When Click on a Party Chef marker and InfoWindow pops up with kitchen contact details as expected. All markers worked as expected.
* When I click on a new marker while an InfoWindow is already open, the existing InfoWindow closes and the new one opens as expected.

#### Social Media Section ####
* When I hover over a social media icon it grows as expected.
* When I click on a social media icon it launches the social media website in a new tab/page.

#### Contact Form ####
* When I complete the form correctly the fields are highlighted in green as expected.
* When I complete the form correctly and hit the 'Send Message' button I get a 'Message Sent Successfully' alert.
* When I close the 'Message Sent Successfully' alert the form clears as expected.
* When I complete the form correctly and hit the 'Send Message' button I receive an email to the Party Chef email and my personal email address as expected.

#### Footer ####
* When I hover over the Home and Contact Us navigation buttons they change colour as expected.
* When I click on the Home button it loads the index.html as expected.
* When I click on the Contact Us button it reloads contact.html and sends me to the top of the page as expected.
* When I hover over the social media icons they grow as expected.

#### [Back To Top ^ ](#top-of-page) ####

<br>

## 5. <a name="browser-testing">Browser Testing</a> ##

I completed the above manual testing on the following browsers. Please see results below.

### Chrome ###
* All tests ran OK.

### Firefox ###
* All tests ran OK. 

### Safari ###
* Safari date picker

#### [Back To Top ^ ](#top-of-page) ####


