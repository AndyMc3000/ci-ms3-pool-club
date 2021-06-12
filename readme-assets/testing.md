<a name="top-of-page">![Cill na Martra Pool Club (CPC) Logo created using Canva.com and Clipart.com](/readme-assets/cpcp-logo-readme-header.png)</a>


# Cill na Martra Pool Club - Testing Document :microscope: #  

<br>

## Table of Contents ##
1. [Development Testing](#development-testing)
1. [User & Client Stories Testing](#user-client-stories-testing)
1. [Code Validation](#code-validation)
1. [Manual Testing](#manual-testing)
1. [Browser Testing](#browser-testing)
1. [Bugs Discovered](#bugs-discovered)

### Testing User Accounts ###

Both Admin and Player views on the CPC site can be tested by using the following user accounts;

#### Admin User: Steve "The Ginger Magician" Davis ####
* Username/Email: steve@cpc.ie
* Password: theginger

#### Player User: Ding "Pot Noodle" Junhui ####
* Username/Email: ding@cpc.ie
* Password: potnoodle
* 
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
* Exception Handling. I added to Python functions to my app.py file to manage any erros which may happen while a usr is using the site. One function manages 404/'Page not Found' type erros, and the other manages all other exceptions/errors. In both cases a user should be directed to one of two pages which explain that an error occurred and which offer a button to direct a user back to the Homepage. I test this cand it worked as expected.
* Python and JavaScript functions testing are detailed under the Manual Testing section below.


#### [Back To Top ^ ](#top-of-page) ####

<br>

## 2. <a name="user-client-stories-testing">User & Client Stories Testing</a> ##

I tested each of the Client and User stories which were used to determine the features, functions and styling of the CPC website. See the results of these tests here; 

#### Client Stories ####
> - [x] “One of the main goals of the website is to grow the membership of Cill na Martra Pool Club, and to provide value to visitors in the information is provides about the CPC.” - TEST RESULT: The site describes what the club is, what the benefits are of being a member, and how leagues operate.
> - [x] “The website must give Club organisers a place to add new members and create and edit Leagues. - TEST RESULT: Admins can create new leagues, edit leagues, and add new members from functions listed on the Admin Homepage.
> - [x] “The website must allow users on the site to view the current League Table.” - TEST RESULT: A League Tabel can be accessed via a button on the Homepage. 
> - [x] “The website must allow new members to register and join the Club.” - TEST RESULT: The site has a Registration page where users can sing up abd join the club.
> - [x] “The website must provide an area where club members can view their current League statistics.” - TEST RESULT: A club member can view thier Points, Matches Won, and Matches Lost statistics by clicking a 'My League Stats' buttton on the Player Homepage.
> - [x] “The website must provide an area where club members can add a Match result when they have acted as a Match Referee. Adding a match must update the League Table and a members League statistics appropriately.” - TEST RESULT: A member can add a match result by clicking on a 'Add Match Result' button on the Player Homepage. Once a member submist the Add Match Result form, a Python function calculates the additional points accrued by each Player in the Match, and also increments either their Matches Won or Matche Lost total.
> - [x] “The website must provide an area where club members can edit and update their Account information.” - TEST RESULT: A member can update their Account details by clicking on an Edit My Account button on the Player Homepage.
> - [x] “The website must provide an area where site Admininstrators can add a new League." - TEST RESULT: An Admin can add a new League by clicking on an Add League button on the Admin Homepage.
> - [x] “The website must provide an area where site Admininstrators can add a new Player/Member." - TEST RESULT: An Admin can add a new Player by clicking on an Edit League button on the Admin Homepage. 
> - [x] “The website must provide an area where site Admininstrators can edit or delete a League." - TEST RESULT: An Admin can edit a League, or delete it by clicking on an Add League button on the Admin Homepage. When they click the button they are taken to a 'Select a League' page. Once they selct a league and 'Edit League page opens.
> - [x] “The website must allow users to find contact details for Club organisers and include a Contact Us form.” - TEST RESULT: A Contact section on index.html lists a telephone number and an email address which can be used to contact CPC organiser. A Contact From in the same section allows a user to send a message to CPC organisers (they will also receive a copy of their message by email).
> - [x] “The website must have a section showing banner adverts for CPC sponsors.” - TEST RESULT: All pages on the CPC site have a banner carousrel at the bottom of the page showing rotating banners for club sponsors.
> - [x] “The website must be mobile-friendly.” - TEST RESULT: The CPC site is responsive to tablet and mobile devices.
> - [x] “The website colours must be dark. The website will be used by Players at Match events on their mobile phones, and so a dark colour scheme will ensure that viewing the website while near a pool table will reduce the risk of Player distraction.” - TEST RESULT: Dark backgroundcolours have been used in the design of the CPC site.

#### User Stories ####
> - [x] “I want to learn about what the CPC is.” - TEST RESULT: The index.html page has an introduction sections which outlines who the CPC are and how they operate.
> - [x] “I want to be able to view the current League Table.” - TEST RESULT: A user can view the current league table by clicking a button in the Leagues Table section section on index.html
> - [x] “I want to be able to register and sign-up to join the CPC.” - TEST RESULT: A user can acces a registration page/form from a link in the navbar on index.html, or from button on the carousel and in the introduction section on index.html.
> - [x] “Once I'm sined-up and logged in, I want to be able to view my personal League statistics - my League Points, and my Matches Won/Lost. - TEST RESULT: A user can view their personal league stats by clicking a 'My League Stats' buttton on the Player Homepage.
> - [x] “If I act as a Referee for a League Match, I want to be able to record the Match result and update the current League Table.” - TEST RESULT: A registered member can add a match result by clicking on an Add Match Result button on the Player Homepage.
> - [x] “I want to be able to edit and update my Account information." - TEST RESULT: A User can edit their Account detilas by clicking an 'Edit My Account' button on the Player Homepage.
> - [x] “I want to be able to find contact information for the CPC, and be able to send a message to the CPC organisers." - TEST RESULT: A user can find contact details (telephone and email) for the CPC organisers on a Contact section on index.htmk. A user can also send a message to CPC organisers using a contact form in the Contact section on index.html. A copy of their message is sent to the user via email. 

#### [Back To Top ^ ](#top-of-page) ####

<br>

## 3. <a name="code-validation">Code Validation</a> ##

I ran the website through the W3C validators for [HTML](https://validator.w3.org/) and [CSS](https://jigsaw.w3.org/css-validator/). I also ran my JavaScript code through the [JSHint.com](https://jshint.com/) code checker, and used the PEP8 checker at [PEP8online.com](http://pep8online.com/) to check my Python code for PEP8 compliance.  

#### HTML ####

The W3C CSS Validation Service. The validator highlighted the following warning for index.html. No other errors or warnings were found.

* "Warning: Section lacks heading. Consider using h2-h6 elements to add identifying headings to all sections." - I decide not to 'fix' the issue this warning relates to. It relates to the title of the introduction section which is a h1 title. I decide to leave it as a h1 as it looks better like this when underneath the 'hero' carousel.

#### CSS ####

The W3C CSS Validation Service. The validator found the following errors. No toher warnings or erros were found.

* The validator highlighted 18 Errors and 768 Warnings relating to the bootstrap.min.css style sheet. I queried this with Tutor Support and was advised that these were acceptable issues as I have no control over the CDN-delivered Bootstrap style sheet.

#### JavaScript ####

I ran my script.js file through the JSHint validator;




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


## 6. <a name="bugs-discovered">Bugs Discovered / Remedies</a> ##

While developing and testing the site I discovered the below bugs/issues. If I founc a remedy to a bug I have listed this below.

#### Bugs Discovered / Remedies ####
1. Bootstrap form validation - When I tried to validate the JavaScript code I got from Bootsrap on JSHint.com, it thrw back warnings saying the code was missing semi-colons. So, I added them to my code. However this stopped the vaidation so I had to revert to the original code.
1. CSS animation error - I added the animation property to my style.css along with the required vendor prefixes and @keyframe syntax. When I ran my code through the W3 Jigsaw validator, it threw errors for my animation code. I did some research and it seems that W3/CSS specification don't yet recognise vendor prefixes. As such I removed the animation code to ensure I ran no errors.
1. Bootstrap CSS errors. When I ran my site through the W3 Jigsaw CSS validator it through multiple warnings and erros for the Bootstrap CDN-linked CSS file in my base.html. I discussed this with Student Support and was advised that as it was a Bootstra file (and I have no control over it), it was acceptable to leave this as is. 
1. EMailJS Console error - The EmailJS JavaScript code produces and 'AddEventListener' error in the console. I didn't have time to find a solution to this.
1. HTML validator warning - The W3 HTML validator produced a Warning in regard to a section not having an accetable heading. It relates to the Introduction section on index.html. I decided to leave this issue as is, as it looks better on the page to have a H1 there instead of a H2 to H6 version of the text.
1. Floating Footer - When I initally created my base.html and index.html templates and added a navbar and footer, the footbar did not behave itself. It was 'floating' up from the bottom of the page and hugging the bottom of the last container on the page. I did some research and found that I could fix it by applying some CSS to it. I added the 'Margin-Top: auto' property and value and it fixed the issue.
1. On a previous project I had a bug with form submission where Bootstrap was validating a contact form after it had been 'submit' and 'reset'. As the form had been reset, this resulted in Bootstrap validation errors appearing on the blank form after form submission. This may give a user the impression that their message/form had not been sent, even though an Alert had been sent to the browser to confirm that the message had been sent. This is a known issue with Bootstrap. With help from Tutor support and a Google search I found some jQuery code on a GitHub chat thread which fixed the problem. When I added the code to my EmailJS JavaScript code on script.js it fixed the problem. See that GitHub thread here - ['Resetting form doesn't clear validation errors'](https://github.com/1000hz/bootstrap-validator/issues/68). 
1. Safari datepicker. I found that Safari does not HTML datepicker. I found a jQuery-based solution on [StackOverflow](https://stackoverflow.com/questions/35682138/html5-date-picker-doesnt-show-on-safari), but didn't have time to implement/test it.

#### [Back To Top ^ ](#top-of-page) ####

<a name="top-of-page">![Cill na Martra Pool Club (CPC) Logo created using Canva.com and Clipart.com](/readme-assets/cpcp-logo-readme-header.png)</a>
