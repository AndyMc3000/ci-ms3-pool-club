<a name="top-of-page">![Cill na Martra Pool Club (CPC) Logo created using Canva.com and Clipart.com](/readme-assets/cpcp-logo-readme-header.png)</a>


# Cill na Martra Pool Club - Testing Document #



## 1. Development Testing ##

During the development process I manually tested elements and components after I added them to the website. If I encountered an issue or bug in most cases I worked to resolve it straight away. I have listed the tests I did including those where I encountered bugs here;

#### Tests ####

* Added Bootstrap Navbar to index.html and contact.html. Tested navigation links - Home, Contact, and Logo. All worked as expected. 
* Tested Sticky Navbar functionality. I had to add a large image to the body to test this, and once done it worked as expected.
* Added Jumbotron to index.html and contact.html. Tested button on index.html jumbotron. It worked as expected and directed me to contact.html.
* Added photo gallery section and bootstrap modal gallery. Tested ‘Open Gallery’ button (I removed this button subsequently), and tested clicking on photo to open the modal gallery. Both opened the modal carousel gallery as expected. The carousel controls on the modal gallery also worked as expected.
* Added Testimonial and Footer sections. Tested responsiveness of both and they reacted as expected.
* Add Google Map using Google Maps API. Map worked as expected.
* Added test marker to Google Map. Marker worked as expected.
* Added second test marker to Google Map in order to test marker clustering functionality. Clustering worked as expected. I subsequently removed clustering as I decided to use custome markers with InfoWindows, and I could not find a way to cluster custom markers.
* Added Google Maps ‘Info Window’ functionality. So if a user clicks on a marker an Info Window will pop-up to show contact details for a local Party Chef kitchen/office. This worked as expected.
* Added custom markers to Google Maps. They worked as expected (however as mentioned above, I could not find a solution to cluster these markers).
* Added code for Info Window so that if a second marker is clicked on, the previous Info Window will close and the new one will open. Tested this and it worked as expected.
* Styled content appearing in InfoWindow on Google Map. Tested this and it rendered as expected.
* Added additional locations to Google Maps. Tested each location marker as I saved the location data to maps.js.
* Tested Email links on InfoWindows on Google Map to check if they opened my desktop email client once clicked. They all worked as expected.
* Created a modal to contain the MyMenu 'shopping cart' system. That opened as expected.
* Added ‘Add to cart’ button to index.html to test WebDevSimplified JavaScript shopping cart code. I then added a store.js file to contain JavaScript code from the plugin. I then added a div with an ID to call the JS code to the modal. I then tested adding an item to the MyMenu modal/cart and it worked as expected.
* Tested increasing/decreasing quantities of items in the MyMenu, and removing items from MyMenu. Both worked as expected.
* Added EmailJS javascript file for 'Request a quote' form code on MyMenu/Cart. Tested it and it worked as expected.
* Added Bootstrap form validation to form on MyMenu. Tested it and it worked as expected.
* Added content to menu items. I tested ‘Add to MyMenu’ button functionality for each item as I added items. All worked as expected.
* Added images to Bootsrap gallery. I tested calling the gallery and the modal controls. All worked as expected.
* Added EmailJS Contact Form send functionality. Tested it and it worked as expected.
* Added MyMenu cart item indicator to MyMenu button in navbar. Tested it and it worked as expected. 


#### Tests with Bugs ####

* Added Bootstrap menu accordions to index.html. Found a bug where all accordions open and close at the same time. I realised I needed to give each accordion * unique control ID’s. That fixed the bug.
* On one occassion I had an issue with launching the project master instance on GitPod. It wasn't loading completely (see screenshot). When trying to resolve the issue I somehow ended up working on a branch of my Master. I found that the simplest course of action was to delete my GitPod instances (branch & master) and create an new instance by launching the site afresh from GitPod.
     <img src="/assets/readme-assets/gitpod-error-instance-not-loading.png">

* I tried implementing a Javascript shopping cart plugin for the MyMenu system but couldn’t get it to work. See GitHub and the following repository for that code: [Asraf-Uddin-Ahmed /jquery.mycart](https://github.com/Asraf-Uddin-Ahmed/jquery.mycart). I decided to use a simpler alternative solution instead. See the following for that code: [Introduction to JavaScript Lesson 1](https://github.com/WebDevSimplified/Introduction-to-Web-Development/tree/master/Introduction%20to%20JavaScript/Lesson%201). 
* I had a bug with form submission. The EmailJS code was executing (sending an email) before Bootstrap validation was taking place. I got help from Tutor support to resolve this.
* I had a bug with form submission where Bootstrap validated the form again after 'submit' and 'reset'. As the form had been reset, this resulted in validation errors appearing on the blank form. This may have given a user the impression that their message/form had not been sent, even though an Alert was sent to the browser to confirm the message had been sent. This is a known issue with Bootstrap. With help from Tutor support and a Google search I found some jQuery code on a GitHub issues thread which fixed the problem. When I added the code to my EmailJS JavaScript file it fixed the problem. See that GitHub thread here - ['Resetting form doesn't clear validation errors'](https://github.com/1000hz/bootstrap-validator/issues/68).  
* I had an issue on the MyModal form with here I couldn't put a placeholder in for the 'options' dropdown input (the last form field). The first option in the list, 'Choose and option', was acting as the placeholder but was also selectable, which doesn't make sense. I eventually found a solution on StackOverflow which allowed me to add a class to the first option so that it would not be selectable.


## 2. User & Client Stories Testing ##

#### Client Stories ####
> - [x] “One of the main goals of the website is to grow the membership of Cill na Martra Pool Club, and to provide value to visitors in the information is provides about the CPC.”
> - [x] “The website must also give Club organisers a one-stop-shop to create and manage Pool Leagues, League Matches, and Players/Members.”
> - [x] “The website must allow users on the site to view both current and archived League Tables.” 
> - [x] “The website must allow new members to register and join the Club.” 
> - [x] “The website must provide an area where club members can view their current League statistics/progress.”
> - [x] “The website must provide an area where club members can view a list of the current League Matches they have played, and which matches are yet to be played (depending on active membership numbers, a player can expect they will need to play each other player twice in a given League).”
> - [x] “The website must provide an area where club members can add a Match result when they have acted as a Match Referee.”
> - [x] “The website must provide an area where club members can find contact details of another Player in order to arrange a Match date/time/venue.”
> - [x] “The website must provide an area where club members can view their League statistics for previous (archived) Leagues.”
> - [x] “The website must provide an area where club members can edit and update their Account information.”
> - [x] “The website must provide an area where site Admininstrators can add a new League."
> - [x] “The website must provide an area where site Admininstrators can add a new Player/Member."
> - [x] “The website must provide an area where site Admininstrators can make a Player/Member an Administrator."
> - [x] “The website must provide an area where site Admininstrators can edit or delete a League."
> - [x] “The website must provide an area where site Admininstrators can edit or delete a Player."
> - [x] “The website must provide an area where site Admininstrators can edit or delete a Match."
> - [x] “The website must allow users to find contact details for Club organisers and include a Contact Us form.”
> - [x] “The website must have a section showing banner adverts for CPC sponsors.”
> - [x] “The website must be mobile-friendly.”
> - [x] “The website colours must be dark. The website will be used by Players at Match events on their mobile phones, and so a dark colour scheme will ensure that viewing the website while near a pool table will reduce the risk of Player distraction.”

#### User Stories ####
> - [x] “I want to learn about what the CPC is.”
> - [x] “I want to be able to view current and archived CPC League Tables.”
> - [x] “I want to be able to register and sign-up to join the CPC.”
> - [x] “Once I'm sined-up and logged in, I want to be able to view my personal League statistics - current League Rank, current League Points, current Matches won/lost, current Games won/lost, current Matches played, and Matches remaining.”
> - [x] “I want to be able to view my personal League statistics - League Rank, League Points, Matches won/lost, Games won/lost, Matches played, and Matches remaining.”
> - [x] “If I act as a Referee for a League Match, I want to be able to record the Match result and update the current League Table.”
> - [x] “I want to be able to view my list of Leagues Matches, both those Matches Played and those Matches yet to be played."
> - [x] “I want to be able to find contact details for other players so that I can arrange my Matches as/when required."
> - [x] “I want to be able to edit and update my Account information."


## 3. Code Validation ##

I ran the website through the W3C validators for HTML and CSS. I also ran my JavaScript code through the JSHint.com code validator.

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

## 3. Manual Testing ##

I manually tested all website elements/components under the following headings;

### Homepage ###

#### Navbar ****
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
* 

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

## 5. Browser Testing ##

I completed the above manual testing on the following browsers;

### Chrome ###
* All tests ran OK.

### Firefox ###
* All tests ran OK. 

### Safari ###
* All tests ran OK. 



