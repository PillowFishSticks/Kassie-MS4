# Kassie - Testing details

[Main README.md file](README.md)

[View website on Heroku](https://kassie-ms4.herokuapp.com/)

## Table of Contents

1. [Automated Testing](#automated-testing)
    - [Validation](#validation)
2. [User Stories Testing](#user-stories-testing)
3. [Manual Testing](#manual-testing)
    - [Testing undertaken on desktop](#testing-undertaken-on-desktop)
    - [Testing undertaken on tablet and phone devices](#testing-undertaken-on-tablet-and-phone-devices)
4. [Bugs discovered](#bugs-discovered)
    - [Solved bugs](#solved-bugs)
    - [Unsolved bugs](#unsolved-bugs)
5. [Further Testing](#further-testing)

## Automated Testing

### Validation

CSS - Validated using [Jigsaw](https://jigsaw.w3.org/css-validator/) with no errors found.

| Page | Test | 
--- | --- | 
base.css | PASS
checkout.css | PASS
profile.css | PASS

HTML - Validated using [W3C](https://validator.w3.org/#validate_by_input) 
- With an error found in reviews.html - a duplicate id, Reviews, was found in reviews.html. If one id is removed or changed, the content in that div is not displayed. I decided to leave tackling this bug for a future release. 
- With an error found in manage_inspo_items.html - a duplicate id 'deleteInspoItem' was found. It occurs because there are six inspos in the manage inspo page and each of then as a delete modal with an id of 'deleteInspoItem'. This would mean each inspo would need a seperate id for the delete modal, thus I decided to leave it as is for the time being. 

| Page | Test | 
--- | --- | 
index.html |PASS
items.html | PASS
item_detail.html | PASS
add_item.html | PASS
edit_item.html | PASS
profile.html | PASS
reviews.html | PASS
checkout.html | PASS
checkout_success.html | PASS
cart.html | PASS

Javascript - Validated using [JSHint Validator](https://jshint.com/) with no errors found.


Python - Validated using [PEP 8](http://pep8online.com/) with no errors found with one exception: - ```settings.py``` (the Django settings file has a known issue, but is acceptable to not force a line break) - line too long (> 79 characters) - ```AUTH_PASSWORD_VALIDATORS = [{}]``` x 4

## User Stories Testing

The following section goes through the user stories identified in the [Ux section of README.md](README.md#UX) to check that the site meets those needs.

**As a visitor to The House of Mouse website I expect/want/need:**

1. **To easily find what I am looking for, I want the layout of the site to make sense so I am not confused or put off using it.**
    - Arrangement of site elements such as navbar, footer, icons, carousels, search, and forms conform to expected placement. Tag buttons are provided on pages where the user has moved deeper into the hierarchical data structure of the website to make it easier for the user to tell where they are.
    - The key pages of the site can be accessed from both the navigation bar and the footer, which can be found on all pages of the site.

1. **The ability to search through small amounts of information to find what I need, and then be able to easily click to get more detailed information when I need it.**
    - Some points for this already covered in previous user story details.
    - Once the user moves to an item detail page the user can access more detailed information on that item.
    - Product pages can be sorted by name A-Z or Z-A, category A-Z or Z-A, price high to low or price low to high.
    - The search bar allows the user to run a text search through all product titles, descriptions and tags to find what they are looking for.

1. **The site to be easily navigable from any device, desktop, tablet or phone. For the content to look good and be useable on all of these devices.**
    - The use of the site has been extensively tested on desktop, tablet and phone size screens.
    - The user can load the website on mobile, tablet, and desktop devices.
    - All elements have been given a responsive design, so nothing to too squashed, squeezed or hard to read on any screen size a user might be using.
    - The navbar has a collapsed menu for tablet and mobile viewing, this makes navigation easier for smaller devices.  

1. **To be able to add products to a wishlist that I wish to purchase at a later time.**
    - A heart appears next to each product on both the product page and product detail page, when clicked on, it adds
    the product to th users wishlist. 

1. **To be able to read reviews of items bought from previous customers, to build trust in my purchase.**
    - All previous product reviews can be seen at the bottom of each product page.

1. **Leave a review on a product so that I can inform other shoppers about whether it was a good purchase or not.**
    - Users can leave a review using the "Write a review" tab at the bottom of each product page
    - This feature is only available to logged in users, and if a user is not logged in they will be prompted to either log in or sign up.
    - Upon submission of the review form, the product page will reload and the user will be able to see their review in the reviews tab.
    - Users are also able to edit and delete their reviews once written. 

1. **For all information and images to be laid out in a clear and easy to understand way, on whatever size screen I am viewing the website on.**
    - Attention has been paid to ensuring product images are clean,professional and responsive, never squashed or squeezed and that the users operation of the site pages work on all devices. Text is never too large or too small, buttons are always large enough to click with a finger easily on touch screen devices.

1. **To be able to easily find out all the information I need to make an informed purchase. I expect information about the description, ingredients, and instructions where necessary.** 
    - Information about the products description and dimensions are available on the products page, in a tab, below the image and add to bag section. The Tab displays information relevent to that product. 

1. **A text search function so that I can quickly narrow down my search when looking for something specific.**
    - A text search is available in the navbar. It searches through the product titles, description and tags to find the results for the user.

1. **To be able to see a summary of my order during the checkout process.**
    - Users can see full detail of all products in their bag, as well as a bag total by clicking on the bag icon in the navigation bar which will redirect them to the bag page.

1. **That once I am logged in I can access my delivery details and update them if I need to.** 
    - The profile page gives the logged in user the ability to update their default delivery information.

1. **To be able to find information on my past orders.**
    - The profile page provides a list of all the users previous purchases, with full details of their order, date it was placed, products, quantities and total amount paid.

1. **To be able to connect to the businesses social media channels, to keep up to date with new items and deals on the site.**
    - Facebook, Instagram, Twitters, and Pinterest icons can be found in the footer on every page. 

1. **To be able to easily get in contact with the shop owner via a telephone number or email.**
    - The Kassie contact number and email address can be found in the footer on every page. 

1. **Feedback from the website I am using when I interact with it, I expect pop ups and modals to inform me when my forms have been completed and sent correctly. Or to let me know when an error has ocurred and what to do next.**
    - Popups appear to inform the user when their forms are completed, when products are added to their bag, when they checkout successfully, as well as if there are any errors when checking out. 
    - Error messages are also returned to the user when there is a problem with the site's functionality.

## Manual Testing
Below is a detailed account of all the manual testing that has been done to confirm all areas of the site work as expected. 

### Testing undertaken on desktop

All steps on desktop were repeated in browsers: Firefox, Chrome and Internet Explorer and on two different desktop screen sizes.

#### Elements on every page

1. Navbar 
    - Clicked each link in the navbar to confirm that it leads to the correct page.
    - Confirm that when logged out the options "Register" and "Log in" are visible and that "Log out" is not.
    - Log into the site, confirm that "Log out" is visible and that "Register" and "Log in" are not.
    - Click the "Shop" link in the navbar, confirm that all sections of the shop are listed in the dropdown menu.
    - Add a product to the users bag, confirm that the grand total appears under the shopping bag icon with the correct grand total. 
    - Delete all products from the users bag, confirm that the grand total is no longer visible in the navbar.

2. Search bar
    - Enter a search word that applies to many products. 
        - Confirm that the products returned match the products. Confirm that the message "0 products found for (product)" is displayed when hitting enter.

3. Footer
    - Hover over links in the footer, confirm the animation works as expected.
    - Click all links in the footer, confirm that they take the user to the relevant pages within the site.
    - Click the social icons, confirm that they open a new tab and take the user to the correct page.
    - Check date of copyright information, confirm year displayed matches the current year.

#### Home Page

1. Home banner
    - Click the 'Shop Now' button to ensure it takes the user to all products page.
    - Adjust width of browser window, confirm image is responsive and disappears on mobile devices.

2. Inspo section
    - Click on each of the inspo titles to ensure it takes the user to the correct inspo page.
    - Check that an extra inspo is added on medium and small devices to help with styling. 

3. On sale section
    - Click the 'Shop Now' button to ensure it takes the user to all specials page.
    - Adjust width of browser window, confirm image is responsive and disappears on mobile devices.

4. Shop by furniture
    - Click each of the buttons to ensure the user is taken to the correct products display page. 

#### Furniture pages

1. Types of products
    - Click tag buttons, confirm they work and go to the correct locations.
    - Click each of the dropdown links, confirm they go to the correct location. 
    - Click the All products link, confirm all products for that category are displayed. 
    - Confirm that the image and prices displayed are correct.
    - Click multiple products, confirm that the user is taken to the correct products detail page.

2. Sorting options
    - Select the different sorting options from the menu one by one, confirm that the iteems are sorted in the orders selected.

#### On Sale Page

1. Prices 
    - Ensure that the original price is displayed in grey, with a line through it. 
    - Ensure the on sale price is displayed in red. 
    - Check that the on sale price is used when the product is added to the bag. 

#### Inspo Page

1. Inspo Management
    - Ensure the inspo management table loads correctly on all device sizes. 
    - Click on the edit button and check that it takes you to the edit page for that inspo. 
    - Click the delete button and check that the delete modal appears, asking the superuser if they are sure they
    want to delete the inspo.  

2. Inspo pages           
    - Click on each of the inspo titles and check that they go to the correct inspo pages.
    - Try and delete an inspo and check that the delete modal appears, asking the superuser if they are sure they
    want to delete the inspo.  

#### Register Page

- Log out then go to the register page again. Confirm that the register form is displayed as expected.
- Fill in the form with a username already in the database, confirm that the user is informed that they must use a unique username.
- Fill in the email input with a non-email address, confirm the user is shown an error asking the to use an email address.
- Fill in the form with two different passwords, confirm the error is caught again and the user is informed of their mistake.

#### Login Page

- Attempt to log in with a username not in the database, confirm the relevant error message is shown.
- Attempt to log in with a correct username but wrong password, confirm the relevant error message is shown.
- Log in with a correct username and password, confirm that the user is logged in and that they are redirected to the home page. 

#### Account Page

- Go to the account page of a newly created user. Confirm that te profile info form is populated with the users username and email address.
- Confirm that the first name and last name fields are also available.
- Fill in the form with a non-email address, confirm that the applicable error is shown to the user
- Fill in the form correctly, confirm that the "Your account info has been updated." message is shown to the user and that the reloaded form is now populated with the new data.
- Confirm that a user with no previous orders has the "no orders to show" text in the Orders section.
- Make 2 separate orders on the website. 
- Return to the account page, confirm that the orders are displayed in the Orders section of the account page. With the top order being the most recent and open to show the full details. Confirm that all orders after it in the list are closed accordions, but that can be opened with a click.
- Confirm that all data in the orders on the account page is accurate.
- Go into the admin panel, mark one of the orders as shipped. Confirm that the information to the user in their account page is updated to show that the order selected has been shipped.

#### Log Out Page

- Attempt to log out and ensure the the user is taken to the log out page, asking if they are sure they want to log out.
- Click cancel, and ensure that the user is redirected to the home page. 
- Log out and and ensure that the user is redirected to the home page. 

#### Bag Page

- Log in and go to the bag page with nothing in the bag. Confirm that the message "Your bag is empty!" is shown and the call to action button "Keep shopping" is provided and that the checkout button is not displayed. 
- Click the button and confirm it takes the user to the all products page.
- Add products to the bag and return to the bag page, confirm that all products in the bag are displayed correctly, with the correct amounts requested by the user.
- Adjust the quantity field, confirm that the shopping bag subtotal is updated to reflect the change.
- Click the delete button on an product, confirm that the product is removed from the bag.
- Delete all products from the bag, confirm that the bag is empty. 

#### Checkout Pages

- Go to the checkout page when not logged in to the site, confirm that the user is taken to the login page to sign in.
- Confirm that the products are displayed correctly in the order summary, that the quantity, subtotal, and grand total are correct
- Try to send the form without all the required fields filled in. Confirm that the appropriate error message is given to the user.
- Return to the payment page , use the stripe checkout test [card numbers](https://stripe.com/docs/testing) to check the various responses to different errors.
- Make a successful payment. Confirm that the user is returned to checkout success page.
- Check that the checkout success page loads all item and delivery information correctly. 

### Testing undertaken on tablet and phone devices
All steps below were repeated to test mobile and tablet specific elements on my Samsung phone and tablet, in both the firefox browser and samsung internet browser.

Responsive design was also tested in the Chrome Developer Tools device simulators on all options and orientations.

#### Elements on every page

1. Navbar 
    - Open the website on mobile, confirm that the navbar is collapsed into a burger icon
    - click the burger icon, confirm that the navbar list appears are expected.
    - Add something to the bag, confirm that the user shopping bag grand total appears and displays correctly.

2. Footer
    - Scroll to the bottom of the page, confirm that the footer contents is displayed as expected with the bootstrap grid.
    - No content squashed or squeezed or disproportionate in size.
    - Confirm that all links and buttons in footer are easy to click with a finger on the smallest screen sizes.

3. Product pages
    - Confirm that the item list is displayed one on top of each other on mobile, and 3 or 2 to a row on tablet, depending on its size.
    - Confirm that all clicks and swipes operate as expected on touch screen.

4. All pages
    - Navigate to all pages on the site, check that the layout is as expected for the screen size.
    - Check that all buttons, menus, forms and other elements are the correct proportions and easily clickable with a finger.

## Bugs discovered: 
### Solved bugs

1. **Was getting the following error on the console**

<div align="center">
    <img src="/static/images/readme/console-error.png" target="_blank" rel="noopener" alt="console error"               aria-label="console error"/>
</div>


    ```js
    document.getElementById("defaultOpen").click();
    }
    ```

    was changed to


    ```js
    if (document.getElementById("openDefault")) {
        const element = document.getElementById("defaultOpen").click();
    }
    ```

2. **Secret keys were not being read by gitpod** 
    - Secret keys were not being read by gitpod, despite being added as gitpod variables. 
    - Created an env.py file to store the secret keys in. 

3. **Tab in item details was not changing tabs** 
    - Tab in items details was not changing tabs, all content was displaying the the first tab. 
    - JS was in a link tag and loading as a style sheet as follows:


    ```html
    <link rel="stylesheet" href="{% static 'js/scripts.js' %}">
    ```

    was changed to 


    ```html
    <script src="{% static 'js/scripts.js' %}"></script>
    ```

4. **Reptile tag buttons were not displaying at the top of the reptile page**
    - This was because friendly_name and Name were written incorrectly. 


### Unsolved bugs

1. **Duplicate id in reviews.html**
    - A duplicate id, Reviews, was found in reviews.html. If one id is removed or changed, the content in that div is not displayed. 
    - I decided to leave tackling this bug for a future release.

## Further testing: 
1. Asked friends and family to look at the site on their devices and report any issues they found.
2. Kassie viewed on all devices and orientations available in Chrome DevTools. 