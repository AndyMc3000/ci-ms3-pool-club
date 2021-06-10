##### <br> #####
<a name="top-of-page">![Cill na Martra Pool Club (CPC) Logo created using Canva.com and Clipart.com](/readme-assets/cpcp-logo-readme-header.png)</a>
# Cill na Martra Pool Club (CPC) :8ball: #
## A web application for managing the members and leagues of a fictional Pool Club ## 
### Purpose: Backend Development Project (Milestone Project 3) for the Diploma in Software Development course at [Code Institute](https://codeinstitute.net/) ###
### Developer: Andrew McDonald - Contact me on GitHub :octocat: @ <a href="https://github.com/AndyMc3000"><strong>AndyMc3000</strong></a> ###
### Website deployed on an Heroku App: [Click Here](https://pool-club.herokuapp.com/) ###
<hr>
<img src="/readme-assets/cpc-am-i-responsive-readme-screenshot.png" width="1100">
<hr>

# Table of Contents #
1. [Introduction](#introduction-heading)
1. [User Experience Design (UX)](#user-experience-design)
1. [Development Process](#development-process)
1. [Website Features](#website-features)
1. [Technologies Used](#technologies-used)
1. [Testing & Bugs](#testing)
1. [Deployment](#deployment)
1. [Credits](#credits)
<br>
<hr>

#### <br> ####
## 1. <a name="introduction-heading">Introduction</a> ##
#### <br> ####
<hr>

The Cill na Martra Pool Club (hereafter called CPC) website is my Milestone 3 (MS3) project for the Diploma in Fullstack Software Development course at Code Institute. The underlying goal of the project is to meet and exceed the requirements laid out for the MS3 project by Code Institute. The high-level requirement of the MS3 project is to "..build a full-stack site that allows your users to manage a common dataset about a particular domain. Users make use of the site to share their own data with the community, and benefit from having convenient access to the data provided by all other members." 

This README refers to CPC as a fictional client of mine, where I have been hired to develop a website for CPC to meet certain criteria (see the User Experience Design section below). CPC is a small Pool Club with members based around a number of parishes close to Cill na Martra in Co.Cork, Ireland. Club members meet weekly at a number of local pubs to play pool. Membership numbers fluctuate between roughly 25 to 50 players. CPC runs a Pool League twice yearly. Members arrange to meet at a venue to play league matches, which comprise of playing a 'best of 5' games format. A Referee must also be present at league matches. Any other member can referee a match.

Club member management and pool league data was traditionally paper-based, and was a headache for those members who were 'voluntold' to manage that job. The club want a simple web-based application to make it easy for members to; 
* Manage a league table.
* To allow members to get real-time match/league result information.
* To allow members to record match results and calulate league points in real-time for a league table hosted on the site.

The principle languages used in the development of the site are; HTML5, CSS3, JavaScript, and Python.

Other technologies include; 
* The Bootstrap front-end CSS framework.
* The jQuery JavaScript library.
* The Flask Python web framework.
* The Jinja templating language for Python.
* The MongoDB NoSQL database program.
* The Heroku cloud Platform-as-a-Service.
* The EmailJS email service.

#### [Back To Top ^ ](#top-of-page) ####

<hr>

#### <br> ####
## 2. <a name="user-experience-design">User Experience Design (UX)</a> ##
#### <br> ####
<hr>

The design of the CPC website was determined by assessing and quantifying the goals and objectives of the club organisers ('client stories'), as well as the requirements of players who will visit and use the site ('user stories'). Following the determination of client and user stories and their subsequent technical requirements, the site was designed using the principles of Jesse James Garrett's '5 Planes of UX Design'. The outcome or tasks created for each of the 5 design planes is outlinined below.

### 1. The Strategy Plane ###

The Strategy Plane, as defined by Jesse James Garrett "..incorporates not only what the people running the site want to get out of it but what the users want to get out of the site as well." 

Please see below details of the 'Client Stories' to detail the requirements of the CPC, and the 'User Stories' which highlight the requiremnts of club members/players.

#### Client Stories ####
> - [x] “One of the main goals of the website is to grow the membership of Cill na Martra Pool Club, and to provide value to visitors in the information is provides about the CPC.”
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

#### League Ranking & Points Calculations ####
In order to complete the above requirements it is important to understand how the League ranking sytem works. When adding a Match Result to the CPC site, the below rules will determine how calculations should be made.

1. A League Match consists of a series of games where the winner is the first to win three games ( a 'best of 5 games' format).
1. The Rank of a Player in the League is determined by how many points they have accrued. Rank #1 is the Player with the most points, Rank #2 has the second most points, and so on. This ranking detemines how the League Table should be presented.
1. When a Match is played, Players accrue points for winning games. Where;
  * Winning 0 games in a Match scores 1 point
  * Winning 1 game in a Match scores 2 points
  * Winning 2 games in a Match scores 3 points
  * Winning 3 games in a Match scores 4 points
1. In addition to scoring points a Players statistics also include a Matches Won and Matches Lost record.
1. When a Match is played, Players also increment their Matches Won or Matches Lost tally by 1. Where;
  * Winning 0 games in a Match adds 1 to their Matches Lost tally
  * Winning 1 games in a Match adds 1 to their Matches Lost tally
  * Winning 2 games in a Match adds 1 to their Matches Lost tally
  * Winning 3 games in a Match adds 1 to their Matches Won tally

### 2. The Scope Plane ###

Based on the outcomes from the Strategy Plane, The Scope Plane determines what features, functionality, and types of content should be included within the scope of the project. Listed below are the functional specifications and content requirements decided on for the CPC website. 

#### Functional Specifications: ####
* Build a responsive Website with 3 main pages - a Homepage, a Player Homepage, and an Admin homepage. 
* Each of these pages should have a selection of 'feature views'/pages linked from them. The Homepage should have 3 page views linked from it, those being; 'Login', 'Current League Table', and 'Register'. 
* The Player Homepage should have 3 page views linked from it, those being; 'My League Stats', 'Add Match Result', and 'Edit My Account'. 
* The Admin Homepage should have 6 page views linked from it, those being; 'Add League', 'Add Player', and 'Edit League'.  

* All Pages:  
   * All pages should include a Navigation bar to highlight the currently accessed page. The Navigation bar should have 3 different views; One for a non-logged in user, one for a logged in registered player, and one for an Admin user.
   * All pages should include a carousel with scrolling banners adverts for CPC sponsors at the bottom of the page.
   * All pages should include a Footer section which simply has a CPC logo which links to the Homepage, and copyright information. 
* Homepage, Registration page, Login page, and League Table page:  
   * The Homepage should include and introduction section and a 'why join us?' section, which should introduce the club and promote the benefits of joining it. 
   * The Homepage should also have an 'Our Leagues' which describes what the Leagues are and how often they are run. This section should also include a button linking to the current League Table.
   * The Homepage should include a Contact Us section to show name, telephone, and email contact information for the CPC organisers, as well a contact form where user ccan send a message.
   * The Register page should have a form which allows a new member to input their; First Name, Nickname, Surname, Telephone Number, Email Address, a Password, and it should also include a Confirm Password field. On clicking a Register button, a user will create a new document in a 'user' collection of a MongoDB database. This document will also contain default values (hidden from the form) for Points, Matches Won, Matches Lost, Games Won, Games Lost, Matches Remaining, and Leagues Entered.
   * The Login page should have a form where a User can input their email address and password. On clicking a "log In' button, the user should be redirected to their Player Homepage.
   * The Current League Table should show a table showing up-to-date data for all members in the current League. This table should include columns with headings for; Rank, Player Name, Points, Matches Won, and Matches Lost.
* Player Homepage:
   * The 'My League Stats' page should include a table which shows a Players individual current League statistics including their: Points, Matches For, and Matches Against.
   * The 'Add Match Result' page should contain a form where a Player can record the results of a Match for the current League. The form should contain the following fields; Match Date, Match Referee, Player One, Player One Frames Won, Player Two, and Player Two Frames Won. On clicking a 'Add Result' button, the Player would then create a new Match document in the Matches collection on a MongoDB database. This action would also calculate the Points and Matches Won or Matches Lost for each Player. The League Table would should also be updated with the appropriate increase in Points and Matches Won/Lost for each Player.
   * The 'Edit My Account' page should include a form which pre-populates with a Players Account information. A Player can edit the details on the form. These details being; First Name, Nickname, Surname, Telephone Number, Email Address, and Password. On clicking a update details button, a user will update their document in the user collection on MongoDB.
* Admin Homepage:
   * The 'Add League' page should contain a form where an Admin can input; League Name, League Description, Start Date and End Date.
   * The 'Add Player' page should contain the same form as in the Register page. This feature may be required when a person wants to join the club but is not computer savvy. And so an Admin can then register the user on their behalf.  
   * The 'Select League' page should contain a dropdown where an Admin can select a League. After selecting a league by clicking a button, the Admin will be redirected to the Edit League page where a form will be populated containing the following data about that League; League Name, League Description, Start Date and End Date. An Admin can then edit the League details. On clicking a "Update League' button an Admin can then update a Leagues document in the league collection of a MongoDB database. Alternatively an Admin can also click a 'Delete League' button which will delete a League document from the league collection in a MongoDB database.  
   
#### Content Requirements: ####
* The images used on the Homepage Carousel should show people playing pool. The images should be colourful and 'exciting', in order to entice new members to join the club. 
* The 'Why Join' section on the Homepage should briefly, but completely, convey what the benefits are of joining the Club. 
* The 'Why Join' section should also contain appropriate images and texts contained within Bootstrap cards to reinforce the 'Why Join' messaging.
* The 'Our Leagues' section on the Homepage should briefly, but completely, describe what the Club Leagues are and how often they are run. 
* This 'Our Leagues' section should also contain Bootstrap cards which contain images, texts, and a link button which links to the current League Table page.
* The Contact Us section should include text to describe how the Club can be contacted, including a telephone munber and an email address, which should be placed above a Contact Form.
* The 'Visit our Sponsors' scrolling carousel section should contain a selection of attractive sponsor marketing banners, and include links to the external sponsor websites.
* The Footer section should contain a single CPC logo which also serves as a link to the Homepage.

### 3. The Structure Plane ###

#### Interaction Design: ####

Interaction design is defined as the "..development of application flows to facilitate user tasks, defining how the user interacts with site functionality". Inline with this principle, the pages were designed as follows;

* The Homepage and linked pages/views;
* It should have a navigation bar with individual links to the Registration and Login pages. The navigation bar should also be fixed to the top of the page view.
* The 'hero' carousel banners at the top of the Homepage should include a link button linking to the Registration page.
* The 'Why Join' section should also contain a link button linking to the Registration page.
* The 'Our Leagues' section should contain a button should linking a user to the current League Table page.
* On completion and submission the Contact Form should send an email (cc'ing the user) to a CPC organiser using the EmailJS email service. 
* The sponsor carousel banners in the 'Visit our Sponsor' section should be clickable and link a user to an external sponsor website, where that page opens in a new browser window/tab.
* The Current League page should have back buttons above and below the League Table container and link a user back to the Homepage.
* The Login page should have back buttons above and below the Log In form container and link a user back to the Homepage.
* The Registration page should have back buttons above and below the Registration From container and link a user back to the Homepage.

* The Player Homepage and linked pages/views;
* Once a Player is logged in and is rerouted to their Player Homepage, the navigation bar should change and show individual links for; Home (Homepage), MyHome (Player Homepage), and Log Out (which reroutes a user to the Login page).  
* The Player Homepage should have individual Bootstrap cards with clearly visible link buttons for each function a user can perform there.
* Each function listed on the Player Homepage should have its own page.
* Each of the function pages should have a 'Back' button positioned both below and above the content area, returning a Player to their Player Homepage. The function pages to be included are: 'My League Stats', 'Add Match Result', and 'Edit My Account'.

* The Admin Homepage and linked pages/views;
* If a Player is also an Admin, and once that Player is logged in and is rerouted to their Player Homepage, the navigation bar should change and show individual links for; Home (Homepage), MyHome (Player Homepage), Admin (Admin Homepage) and Log Out (which should reroute a user to the Login page). 
* The Admin Homepage should have individual Bootstrap cards with clearly visible link buttons for each function a user can perform there.
* Each function listed on the Admin Homepage should have its own page.
* Each of the function pages should have a 'Back' button positioned both below and above the content area, returning an Admin to their Player Homepage. The function pages to be included are: 'Add League', 'Add Player', and 'Edit League'.

#### Information Architecture: ####

Information Architechture is defined as; "The structural design of the information space to facilitate intuitive access to content" (Copyright 2000 James Garrett).

With this in mind, please see details below about the CPC sitemap, how data is stored and managed, and about navigation and security considerations.

* ##### Sitemap #####
The structure of the website is outlined in the Sitemap. Click here to view the <a href="readme-assets/cpc-sitemap.png"><strong>Sitemap.</strong></a>

* ##### Navigation & Security #####
* The CPC website should also be designed to allow users to easily and securely navigate throughout the site. For example, the navigation bar should be fixed to the top of the page view so that it is always immediately accessible. 
* Buttons and links should be clearly visible and communicate their purpose in an unambiguous way. 
* Function pages should have 2 'Back' buttons situated at the top and bottom of the page view to allow for an easy back and forth between pages.
* The site should not all users to access areas without privileges. For example, a user should not be able to access another users Player Homepage or be able to edit another players account details. Or, A non-Admin should not be able to edit matches or access the Admin Homepage.
* MongoDB Atlas access credentials should not be visible anywhere on the site.
* A user should not be able to access another users password. 

#### Data & Database Schema ####
The CPC website should be designed to allow a user to create, read, update, and delete data intuitively and quickly. CPC will use a NoSql MongoDB Atlas database to store all data. The database will be called 'pool_club'. It will store data in four Collections named: 'user', 'league', and 'matches'. Each Collection will contain documents with unique 'id's, storing key:value pairs of relevant information. The user functions/actions on the CPC site will interact with and/or populate the documents with relevant values.

* The 'user' collection should store information relating to registered club members, or Players. The keys in this collection will be;
  * 'first_name', 'nickname', 'surname', 'email', 'telephone', 'password', 'admin', 'points' 'matches_played', 'matches_won', 'matches_lost', 'games_won', 'games_lost, and 'entered_leagues'. * Please note that some keys will store data for future features - please see the future features section below for more details about future relases.  

* The 'league' collection should store information relating to the current league (the current league is that which has an end date in the future but a start date in the past). The keys in this collection will be;
  * 'name', 'description', 'start_date', 'end_date', and 'participating_players'. * Please note that some keys will store data for future features - please see the future features section below for more details about future relases.   
  
* The 'matches' collection should store information relating to individual matches played. The keys in the documents of this collection will be;
  * 'player_one', 'player_two', 'player_one_won', 'player_two_won', 'date', 'league', 'created_by', and 'referee'. * Please note that some keys will store data for future features - please see the future features section below for more details about future relases.  
  
The Data Types for each value in the Collections can be seen in the Database Schema <a href="readme-assets/cpc-database-schema.md"><strong>Here.</strong></a>

### 4. The Skeleton Plane ###

Following on from the tasks decided upon in the Structure Plane, the Skeleton Plane is defined as follows; ".. The skeleton is designed to optimize the arrangement of these elements (such as the placement of buttons, tabs, photos's and blocks of text) for maximum effect and efficiency..".

With this in mind I created the below wireframes, to detail the layout of the website pages and individual sections/containers etc. Due to the number of pages involved, I created multiple and split them into groups. I created 2 wireframes for the Homepage and the pages directly linked from the Homapgae. I created 2 wireframes for the Player Homepage and the pages directly linked from the Player Homepage. And I created 2 wireframes for the Admin Homepage and the pages directly linked from the Admin Homepage. Please click on the the links below to view these wireframes. * Please note that these wireframes include references to features not yet available.

##### Wireframes #####
* Wireframes for the Homepage and related pages;
1. <a href="readme-assets/cpc-homepage-and-linked-pages-wireframes-large.png"><strong>Homepage on Large Screen Devices</strong></a>
1. <a href="readme-assets/cpc-homepage-and-related-pages-wireframes-mobile.png"><strong>Homepage on Mobile Devices</strong></a>

* Wireframes for the Player Homepage and related pages;
1. <a href="readme-assets/cpc-player-homepage-and-linked-pages-wireframes-large.png"><strong>Player Homepage on Large Screen Devices</strong></a>
1. <a href="readme-assets/cpc-player-homepage-and-linked-pages-wireframes-mobile.png"><strong>Player Homepage on Mobile Devices</strong></a>

* Wireframes for the Admin Homepage and related pages;
1. <a href="readme-assets/cpc-admin-homepage-and-linked-pages-wireframes-large.png"><strong>Admin Homepage on Large Screen Devices</strong></a>
1. <a href="readme-assets/cpc-admin-homepage-and-linkeded-pages-wireframes-mobile.png"><strong>Admin Homepage on Mobile Devices</strong></a>


### 5. The Surface Plane ###

Having completed the previous 4 stages in the UX design process, I moved on to making decisions around the design and styling of the website. The Surface Plane focuses on the styling of images, backgrounds, fonts, and colours used on a website. The details of these decisions are listed here;

1. Colours - The color scheme for the website was chosen from a selection of colours I considered when using the tools on the [Coolors.co](https://coolors.co/) website. I only used 2 dark site colours in order to meet the requirement that the site have dark background colours. I found a suitable dark colour and then found a related tint of that colour to use for the background colours. The colours chosen, along with their HEX values, are shown here;
<img src="readme-assets/cpc-coolors-colour-pallette.png" width="500">

1. Font - I used the Google Fonts website to help me decide on a font to use for site texts. I decided on a font called 'Audiowide' for all texts. I also used the Canva.com free trial service to help me find a font for my logo (I sourced the image part of the logo elswhere). On Canva I found and used a font called ARCHIVE (Designed by Slava Kirilenko – a graphic designer from Almaty, Kazakhstan) for the logo. Please see an example of both fonts here;  
<img src="readme-assets/cpc-fonts.png" width="600">

1. Logo Design - I created the CPC logo using tools on [Canva.com](https://www.canva.com/). The logo contains an image and some text. I got the image from Clipart.com and then uploaded it to Canva where I used its editor to add text and produce the final logo.

1. Images - I mainly used free photos taken from the [Unsplash.com](https://unsplash.com/) website. On Unspalsh.com I was able to create a collection of relevant phtotos. The naming convention for each photograph includes a referenece to the photographer name and the Unsplash item code. The Alt attribute for each photograph also includes the photographer name. All other images use the providers naming convention along with a CPC prefix, e.g. 'cpc-feature-<provider filename>.png.

1. Icons - I used [Font Awesome](https://fontawesome.com/) icons to add icons to section headings. 

1. Favicons - I use the Real Favicon Generator online service to create browser, desktop, and mobile favicons for the site. I uploaded a single favicon image to the Real Favison Generator service, and it generated a package of individual files for different devices and browser which I then downloaded. I then uplodaed these files to a favicon directory in my repository, and added a list of links to the header of my base.html page. These links then served the correct favicon to the appropriate device or browser. You can learn more about this service here: [RealFaviconGenerator](https://realfavicongenerator.net/)

#### [Back To Top ^ ](#top-of-page) #### 

<hr>

#### <br> ####
## 3. <a name="development-process">Development Process</a> ##
#### <br> ####
<hr>

I drew up a process to follow for developing the CPC website. This is listed in sequence below.

1. Design - I firstly designed the site based on the Client/User Stories requirements, and by creating wireframes/sketches etc.
2. Setup - I then setup my GitPod IDE by creating a python (.py) file, and by installing Flask, PyMongo, flask-pymongo, and dnspython. I then created a new Database on MongoDB and added new Collections to it. I also created a new app on Heroku. I then created an env.py file for my sensitive environment variables, and listed that file in my .gitignore file so that it would not be pushed(or published) to my public GitHub repository. I created a requirements.txt file so that Heroku would understand what the site/app requirements are. I also added my environment variables to Heroku, and integrated Heroku with my GitHub repository for automatic updates (so that when I push changes to GitHub, the changes are also automatically picked up and deployed by Heroku too.  
3. HTML & CSS - I then used Flask and Jinja to create template pages for the site. I then added HTML to a base.html template page, and then all other pages for the site. I also add CSS styling as I went along.
4. Flask & Python - I then added Flask routes and Python functions to my app.py file to create relevant functionality for each page. Site functionality mainly revolves around CRUD operations with my MondoDB Atlas database. 
5. JavaScript/jQuery - I added JavaScript and jQuery to my script.js file for functions such as Bootstrap Form Validation, Bootstrap Data Table functionality, and for the EMailJS email service functionality for the Contact Us form. I also added a jQuery script to the select-league.html page.
5. Resonsiveness - I made sure all texts/headings, images, and container elements transform approprately and look good when viewed on different devices such as: mobile phones, tablets, laptops, large screen PC's, and large TV's. 
7. Code validation - I validated all code using appropriate validators - W3.org validators, JSHint.com, and PEP8online.com
8. Documentation - I added relevant documentation and information to my README.md file.
9. Testing - I tested functionality of site elements across a range of different devices and browsers, and fixed any bugs found. I documented this activity in my Testinh.md file.

#### [Back To Top ^ ](#top-of-page) ####

<hr>

#### <br> ####
## 4. <a name="website-features">Website Features</a> ##
#### <br> ####
<hr>

The CPC site employs the following features/functionality;

* Bootstrap Navigation Bar on all pages.
* Bootstrap 'Hero' Carousel on index.html, and Carousels for sponsor banner adverts on all pages.
* Bootstrap Cards on all pages to contain content sections.
* Bootstrap Responsive Grid system.
* JavaScript for Bootstrap validation.
* JavaScript for EmailJS for sending contact form data by email.
* JQuery code for resetting the contact form following submission.
* Python CRUD operations with the MongoDB Atlas database.
* Page Footer on all pages.

#### Future Features ####
Unfortunately I ran out of time to implement all of the site features which I had planned to implement at the beginning of the project. These items can be seen in the site Wireframes, in routes/function in the app.py file, and in HTML pages in the Templates folder. These and other additional possible features are listed below. I wss advised to leave the HTML pages and Flask/Python code for these features in place to show the intended 'direction of travel' for the site.

1. A 'League Archive' which can be accessed from the Homepage. This would allow a user to select an historical League from a droppdown listand view the final Table for that League. An Archived League would be created when a current/active league is deleted from the edit-league.html page. It would capture all the league stats for the users in the current league and create a new document in a MongoDB 'archive' collection. There is a 'Coming Soon' section on index.html to show where this feature would be positioned/accessed from.
1. A 'Find a Player' feature. Accessible from the Player Homepage, this would allow a registered user to search for and find information about another player. This infromation would include a players contact details (telephone & email), and would also show the current League statistics for that user. This would enable to player to get in touch with another member in order to organise a league match, and to understand where that player sits in the League Table without having to search through the League Table on the Homepage. 
1. A 'My Match List' feature. Accesible from the Player Homepage, this would allow a user to see a list of all League participants, along with the number of matches they have played against each player. 
1. A 'My League History' feature. Acceesible from the Player Homepage, this would allow a user to select an Archived league and view what their final statistics were in that League.
1. An 'Add Admin' feature. Accessible from the Admin Homepage, this would allow an Admin to select a member from a dropdown list, and enable them to make that memeber an Admin by updating a boolean Admin value in that members user document in MongoDB. 
1. An 'Edit a Match' feature. Accessible from the Admin Homepage, this would allow an Admin to select a Match from a dropdown list and then edit and update the values of that Match document. It would also allow an Admin to delete a Match record.
1. An 'Edit a Player' feature. Accessible from the Admin Homepage, this would allow an Admin to select a Player from a dropdown list and then edit and update the values of that Player document. It would also allow an Admin to delete a Player record.
1. The Club may decide it wants to charge members an annual membership fee. The CPC site could be used to collect this fee from members. This would require the integration of a billing system.
1. The Club may want to run a Pool Championship (a knockout tournament) in addition to Leagues, at particular times, e.g an Xmas Pool Championship. The site could be updated to add logic and a data schema for a Championship bracket system.
1. The Club may want to sell merchandise in order to raise funds for prizes and tours. The site could be updated to add a shop selling Club themed merchandise. 

#### [Back To Top ^ ](#top-of-page) ####

<hr>

#### <br> ####
## 5. <a name="technologies-used">Technologies Used</a> ##
#### <br> ####
<hr>

<img src="readme-assets/cpc-technologies-used-logos.png" width="630">

I used the following technologies, services, and devices to develop, style, deploy, and test the CPC website;
<br>
* HTML5 - The site pages were developed using HTML5 markup language.
* CSS3 - The site was styled and in some cases made responsive using CSS3.
* Python - CRUD functionaiity with a MongoDB Atlas database was done using Python functions.
* Flask - I used the Flask framework along with the Jinja template engine and the Werkzeug toolkit to develop the CPC web app.
* JavaScript & jQuery - I used JavaScript and jQuery for functioonality around Bootstrap validation, the EMailJS email service, and the Bootstrap Data Tables table sorting functionality.
* Bootstrap - I used the Bootstrap framework for many of the HTML elements, including the Navbars, container Cards, the Carousels, the Forms, and the Tables. 
* EmailJS - I used the EmailJS email service to send Contact Us Form data by email to the CPC organisers and the user.
* GitHub - I set up a free repository on GitHub.com to maintain a master of all website files, content, and resources.
* GitPod - I used the free GitPod.io Integrated Development Environment to write and develop the code for the website.
* MongoDB Atlas - All data is stored in a MongoDB Atlas database. The Pythons functions used to create site operations/functionality interact with the Collections in the MongoDB Atlas database. The functions complete one of four database CRUD operations; Create documents in a Collection, Read documents in a Collection, Update documents in a Collection, or Delete documents in a Collection.    
* Heroku - I used the Heroku cloud-based and container-based platform-as-a-service to host and deploy the CPC web app.
* Balsamiq - I used the Balsamiq application to create the website sitemap, and to create the page wireframes for PC & Tablet/Mobile views.
* W3C validators - I used the W3C HTML5 and CSS3 code validators to validate my HTML and CSS.
* JSHint - I used jshint.com to validate my JavaScript code.
* PEP8Online.com - I used the PEP8 checker at Pep8online.com to check my Python code for errors.
* Responsive Viewer - I used a Chrome Browser Extension called Responsive Viewer to emulate the presentation of the website on multiple device sizes and types.
* AmIResponsive - I used the [AmIResponsive](http://ami.responsivedesign.is/) webpage to view site responsiveness across devices.
* Apple Preview - I used the Apple Preview image editor application to crop and resize photo's and images, and to create some of the readme assets. 
* Apple Pages - I used the Apple Pages word processor to manage and edit text content for the website. 
* Apple Keynote - I used Apple Keynote as a sketch pad to test content and review/edit content/images.
* Apple Hardware - I used a MacBook Pro to develop the site. I also used an Apple iPhone, Apple TV, iPad and iPad Mini for testing the website.

#### [Back To Top ^ ](#top-of-page) ####

<hr>

#### <br> ####
## 6. <a name="testing">Testing</a> ##
#### <br> ####
<hr>

Testing was completed under the below headings. A detailed testing document can be seen <a href="readme-assets/testing.md"><strong>Here</strong></a>

#### Testing Headings ####
1. Development Testing
1. User & Client stories Testing
1. Code Validation
1. Device Testing
1. Browser Testing

# TO DO #
  
#### Bugs Discovered / Remedies ####
1. Bootstrap form validation
1. CSS animation error
1. console error
1. Admin link visibility
1. Floating Footer
1. On a previous project I had a bug with form submission where Bootstrap was validating a contact form after it had been 'submit' and 'reset'. As the form had been reset, this resulted in Bootstrap validation errors appearing on the blank form after form submission. This may give a user the impression that their message/form had not been sent, even though an Alert had been sent to the browser to confirm that the message had been sent. This is a known issue with Bootstrap. With help from Tutor support and a Google search I found some jQuery code on a GitHub chat thread which fixed the problem. When I added the code to my EmailJS JavaScript code on script.js it fixed the problem. See that GitHub thread here - ['Resetting form doesn't clear validation errors'](https://github.com/1000hz/bootstrap-validator/issues/68). 

#### [Back To Top ^ ](#top-of-page) ####

<hr>

#### <br> ####
## 7. <a name="deployment">Deployment</a> ##
#### <br> ####
<hr>

The deployment of the CPC site was dependent on the setup of, and integration between, a number of platforms/frameworks/tools and a NoSQL MongoDB database.
  
This site was deployed by firstly setting up a GitHub repository to store the website files. GitHub is a free online code hosting platform for websites or web applications, which enables version control and collaboration during the development of a project. A repository on GitHub containes all of a project's files and each file's revision history. You can learn more about GitHub and repositories here: [Click here to go to GitHub](https://docs.github.com/en/free-pro-team@latest/github)

I then used the online GitPod Integrated Development Environment (or GitPod IDE) to write the code for the website. Once I was happy with a section of new code I commited or saved that to a staging area. Then, on a regular basis, I commited changes to the working version of the website on GitPod. These commits included a short description of what the changes do. I would then 'push' those changes from the GitPod IDE to my GitHub repository where the master set of files was updated. You can learn more about GitPod here: [Click here to go to GitPod](https://docs.github.com/en/free-pro-team@latest/github)

Early on in the development process I also deployed the website to a live web address using Heroku. Heroku is a container-based cloud Platform as a Service (PaaS). Developers use Heroku to deploy, manage, and scale modern apps. The Heroku platform is elegant, flexible, and easy to use, offering developers an easy path to getting their apps to market. Once setup, any changes I made on my GitPod IDE (and which were subsequently 'pushed' to my GitHub repository), were automatically pushed to my Heroku app.

The CPC site uses the Flask Python framework, a MongoDB database, a GitHub repository (including a main Python application file), and the Heroku platform. I had to ensure that all these components worked in sync in order to deploy the site successfully.

Here are the steps I took to deploy the website on Heroku;

**** Install Flask & add additional files ****

1. Added Python application file (app.py).
1. Added environment variables file (env.py).
1. Added env.py to .gitignore file so that it would not be pushed to my public repository (it was done by default when using the Code Institute GitHub template).
1. Imported Flask and associated libraries (see requirements.txt file below for a list of requirements).
1. Tested that Flask was working by outputting Hello World to GitPod preview browser. 
1. Added requirements.txt to tell Heroku what tools, frameworks, and library versions the app requires to run. in this case, these requirements are;
    * click==7.1.2
    * dnspython==2.0.0
    * Flask==1.1.2
    * Flask-PyMongo==2.3.0
    * itsdangerous==1.1.0
    * pymongo==3.11.0
    * Werkzeug==1.0.1
1. Added Procfile to tell Heroku what command to run to operate the app.

**** Create a MongoDB Database ****

1. Created a free MongoDB Atlas account.
1. Created a new database on MongoDB called pool_club. 
1. Added three collections to the database - 'league', 'user', and 'matches' - see the Database Schema <a href="readme-assets/cpc-database-schema.md"><strong>Here.</strong></a>
1. Manually added some test documents to the user collection.

**** Create app on Heroku ****

1. Created a new App on Heroku.
1. Added config variabless to the Heroku app.
1. Enabled automatic deploys from my GitHub repository (the Master branch) to the Heroku app. 
1. Tested the connection with Heroku and got Hello World! when I opened the Heroku app.

**** Final Steps ****
1. Connected app.py to Mongodb.
1. Imported flask_pymongo and bson.objectid tools in order to be able to interact with MongoDB Objects. 
1. Tested connections between App.py-MongoDB-Heroku by adding a Flask route and Python function to app.py. The function asked to find all the documents in th collection 'user' and return it to the index route (render the template index.html). 
1. I then committed and pushed my changes to my GitHub repository. 
1. When I refeshed my Heroku app url, the list of test user documents which I created previously displayed on the index.html page correctly.

I deployed the website early on in the development process as it useful to be able to test examine developing features on the website and on various physical devices in its live state. Also, while the GitPod IDE has the ability to show a preview of real-time changes to a project, sometimes that does not pick up or display issues which would appear on the live site. By having the deployed site up and running during development, I was able to address and correct any bugs early in the development process.

The live version of the CPC website deployed via Heroku can be seen: [Here!](https://pool-club.herokuapp.com/)

#### [Back To Top ^ ](#top-of-page) ####

<hr>

#### <br> ####
## 8. <a name="credits">Credits</a> ##
#### <br> ####
<hr>

1. Coding Websites - I regularly used a number websites to help me learn how to code certain elements/features. These websites include; 
* [GetBootstrap.com](https://getbootstrap.com/)
* [W3Schools.com](https://www.w3schools.com/)
* [Flask Documentation Website](https://flask.palletsprojects.com/en/1.1.x/)
* [Mozilla MDN Web Docs](https://developer.mozilla.org/)
* [YouTub.com](https://youtube.com/)
* [GitHub.com](https://github.com/)
* [EDUCBA Website](https://www.educba.com/)
* [StackOverflow.com](https://stackoverflow.com/)
* [CSSTricks.com](https://css-tricks.com/)

* TO DO *
  
1. Code Institute Course Material - I referred to and used Code Instiute course material

1. jQuery code used to stop Bootstrap form validation after a form was submitted in emailjs-contact-page-contact-form.js - I had a bug with form submission where Bootstrap validated the form again after 'submit' and 'reset'. As the form had been reset, this resulted in validation errors appearing on the blank form. I found some jQuery code on a GitHub issues thread which fixed the problem when I applied the code to my EmailJS JavaScript file. This thread was owned by a GitHub user called Cina Saffary. See the GitHub thread here - ['Resetting form doesn't clear validation errors'](https://github.com/1000hz/bootstrap-validator/issues/68).

1. EmailJS code - I copied relevant JavaScript code from the EmailJS website in order to send emails from my Contact Form on index.html.

1. Colours - I used the Coolors.co website to help me decide on a colour scheme for the webite. This website allows you to create your own colour palettes or to use one of thiers. See more about the Coolors.co palette catalogue and tools here: [Coolors.co](https://coolors.co/). 

1. Font - I used Google Fonts for the fonts on the website. See more at: [GoogleFonts.com](https://fonts.google.com/)

1. Icons - I used FontAwesome and Favicon for all icons on the website. See more at: [FontAwesome.com](https://fontawesome.com/)

1. Design Principles - The design of this website employed the principles of 'The 5 Planes of UX design', which was created by Jesse James Garrett in his book; The Elements of User Experience: User-centered Design for the Web (2002). See more at; [Jjg.net](http://www.jjg.net/elements/)
  
1. Company Logo - The Party Chef logo was created using tools on the FreeLogoDesign.org website. See more at; [FreeLogoDesign.org](https://www.freelogodesign.org/)



### Acknowledgements ###

In order to get design ideas, I took inspiration from a number of industry relevant websites.
These websites are;

No. | Business     | Website     | Description |
--- | ------------ | ----------- | ----------- |
1 | **The UK Premier League(EPL)** | [PremierLeague.com](https://www.premierleague.com/) | Wikipedia describes the Premier League as; "The Premier League, often referred to exonymously as the English Premier League or the EPL, is the top level of the English football league system. Contested by 20 clubs, it operates on a system of promotion and relegation with the English Football League.
2 | **World Pool-Billiard Association (WPA)** | [WPAPool.com](https://wpapool.com/) | Wikipedia describes the World Pool-Billiard Association as; "The World Pool-Billiard Association is the international governing body for pool. It was formed in 1987, and was initially headed by a provisional board of directors consisting of representatives from Japan, the United States, Sweden, and Germany. as of February 2019, the WPA president is Ian Anderson of Australia."
3 | **American Poolplayers Association (APA)** | [WPAPool.com](https://poolplayers.com/) | The American Poolplayers Association (APA) website describes themselves as; "The American Poolplayers Association (APA) is the World's Largest Amateur Pool League. With nearly 250,000 members throughout the United States, Canada and Japan, the APA awards nearly $2 Million in guaranteed prize money every year during the APA Championships in Las Vegas! In the APA, Everyone Can Play… Anyone Can Win – even you!"
3 | **BBC SPORT** | [BBC.com](https://www.bbc.com/) | Wikipedia describes BBC SPORT as; "BBC Sport is the sports division of the BBC, providing national (UK) sports coverage for BBC Television, radio and online. "
 

### Additonal Support ###

I also received help and support from;
* Reuben Ferrante - Code Institute Mentor - Slack Username: [reubenfer_mentor](https://code-institute-room.slack.com/team/UKD9L615F) - Reuben is my new Mentor and was hugely helpful with helping me with my JavaScript code, having jumped in at a late stage in the project. Reuben also helped me with fixing issues for the resubmission of my project.
* Anna Greaves - Full Stack Developer and Content Developer at Code Institute - GitHub profile here: [@AJGreaves](https://github.com/AJGreaves)
 - I took inspiration from Anna's Family Hub project on GitHub. In particular I found Anne's README.md and Testing.md files very helpful. See that repository here: [FamilyHub](https://github.com/AJGreaves/familyhub)
* The Student Support team at Code Institute.
* The Tutor team at Code Institute.

#### [Back To Top ^ ](#top-of-page) ####

<a name="top-of-page">![Party Chef Logo created using FreeLogoDesign.org](/assets/readme-assets/party-chef-logo-readme.png)</a>
