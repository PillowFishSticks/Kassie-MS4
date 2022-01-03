<div align="center">
    <img src="/media/readme/mock-up.png" target="_blank" rel="noopener" alt="Kassie" aria-label="Kassie"/>
</div>


[Kassie](https://kassie-ms4.herokuapp.com/) is an e-commerce site, built using HTML, CSS, JavaScript, Python, and Django. The shop sells a range of furniture.

DISCLAIMER: This website is for educational purposes only and uses products and content from existing brands. Please see the credits section for full information.

Test card details:
* Card Number: 4242 4242 4242 4242
* Expiration Date: 04 / 24
* CVC: 424
* ZIP: 42424

## Table of Contents

1. [Project Summary](#project-summary)
	- [Site Purpose](#site-purpose)

2. [UX](#ux)
    - [Goals](#goals)
        - [Site Owner Goals](#site-owner-goals)
        - [Site User Goals](#site-user-goals)
    - [User Stories](#user-stories)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)

3. [Features](#features)
    - [Common Features](#common-features)
    - [Page Features](#page-features)

5. [Information Architecture](#information-architecture)
    - [Database choice](#database-choice)
    - [Data Models](#data-models)

6. [Technologies Used](#technologies-used)
    - [Tools](#tools)
    - [Databases](#databases)
    - [Libraries](#libraries)
    - [Languages](#languages)

7. [Testing](#testing)
    - See separate [TESTING.md](TESTING.md) file.

8. [Deployment](#deployment)
    - [How to run this project locally](#how-to-run-this-project-locally)
    - [Heroku Deployment](#heroku-deployment)

9. [Credits](#credits)
    - [Content](#content)
    - [Images](#images)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

----

# Project Summary 

This project is my fourth and final milestone project (Full Stack Frameworks With Django) for the Code Institute Diploma in Software Development.

The purpose of the project is to build a full-stack site based around business logic used to control a centrally-owned dataset , setting up an authentication mechanism and providing paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.

## Site Purpose 

The purpose of the site is to sell furniture items on an online store called Kassie. Customers can purchase items and user engagement is encouraged through the ability to leave reviews and comments and to create user profiles.

The site is intended to be visually appealing, and easy to navigate. It has a responsive design so that it can be viewed easily on mobile and desktop.

# UX

## Goals

### Site Owner Goals

As a site owner I want to be able to:

- Create a visually appealing site with a strong brand identity.
- Add products on the website so I can add new items to my stores.
- Edit existing products in my store so I can change product prices, descriptions, images and other product information.
- Delete products on the website so I can remove items from my store.
- Have links that direct users to our social sites for further engagement.
- Keep track of sales data to inform future product choices.

### Site User Goals

The central target audience for Kassie are:

- People who would like to shop for furniture. 
- People who would like to own quality furniture. 
- People who would like the ease of shopping online for furniture.
- People who value door to door delivery.

As a site user I want to be able to:

- Find furniture needed for my home. 
- Enjoy browsing all the furniture products.
- Be able to navigate the shop easily, find what I need and make a safe and secure purchase.
- Buy from a trustworthy online shop. 

## User Stories

As a visitor to the Kassie website I expect/want/need:

1. To easily find what I am looking for, I want the layout of the site to make sense so I am not confused or put off using it. 

1. The ability to search through small amounts of information to find what I need, and then be able to easily click to get more detailed information when I need it.

1. The site to be easily navigable from any device, desktop, tablet or phone. For the content to look good and be useable on all of these devices.

1. To be able to add products to a wishlist that I wish to purchase at a later time. 

1. To be able to read reviews of products bought from previous customers, to build trust in my purchase.

1. Leave a review on a product so that I can inform other shoppers about whether it was a good purchase or not.

1. For all information and images to be laid out in a clear and easy to understand way, on whatever size screen I am viewing the website on.

1. To be able to easily find out all the information I need to make an informed purchase. I expect information about the description, ingredients, and instructions where necessary. 

1. A text search function so that I can quickly narrow down my search when looking for something specific

1. To be able to see a summary of my order during the checkout process.

1. That once I am logged in I can access my account details and update them if I need to. 

1. To be able to find information on my past orders. 

1. To be able to connect to the businesses social media channels, to keep up to date with new items and deals on the site. 

1. To be able to easily get in contact with the shop owner via a telephone number or email.

1. Feedback from the website I am using when I interact with it, I expect pop ups and modals to inform me when my forms have been completed and sent correctly. Or to let me know when an error has ocurred and what to do next.

## Design Choices

### Fonts

- The primary and only font 'Roboto' was chosen for the text of the site because of it clear readability and clean style. 

### Colors
- The colour scheme for this site was rendered on [Cooler](https://coolors.co/) and can be seen below:

<div align="center">
    <img src="/media/readme/color-palette.png" alt="Colors used in the Kassie website" aria-label="Colors used in the Kassie website"/>
</div>

- Black: #000000
- Eerie Black: #222222
- Ming: #036A78
- Cultured: #F6F6F6
- White: #FFFFFF

- The Ming blue was chosen as the brand color for Kassie, as it provides a strong presence and is a fun color. 

- The blacks were chosen for most text and buttons, as it is neutral and compliments the greys. 

- The greys were chosen for this project to provide a neutral background color to information, making a clear seperation from the white background. 