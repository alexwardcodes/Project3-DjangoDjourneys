# Project 3 - Django Djourneys

## Description

This project was assigned at the end of the eighth week of General Assembly’s 3-month SEI (Software Engineering Immersive) course, which teaches people who don't know how to code the basics of software engineering with a view to launching a career in the tech sector. The aim of this project was to design an app in Python using the Django framework over the course of one week. This project was a group project together with two other students on the course.

## Deployment link

[You can find Django Djourneys deployed on this link](https://djangodjourney.herokuapp.com/). Take the quiz and see where your next journey should take you!

<img width="1919" height="1007" alt="Image" src="https://github.com/user-attachments/assets/00c2d3fb-301f-4bf2-bed0-51ef3b35d8d3" />

## Getting Started/Code Installation

### Instructions

#### Deployed app

There are no specific installation requirements for this app since Django Djourneys runs in the browser. Simply create an account or take our four-part quiz to get started!

## Timeframe & Working Team

We worked as a team of three over the course of a week to deliver this project. We split tasks equally to ensure we were all contributing to the project at the same level. We were an especially effective team on this project! I took the lead to manage the project and track tasks to ensure we remained on target for delivery.

## Technologies Used

We built this project in Python and HTML within the Django framework, with CSS for the styling. We used Multer for image upload, PostgreSQL for database storage/retrieval and deployed our app on Heroku.

## Brief

Our brief for this project was to build an app from scratch in Python as a team using the Django framework, and then to deploy this on Heroku. Our criteria were as follows:

- Create the application using at least 2 related models, one of which should be a user
- Manage team contributions and collaboration using a standard Git flow on GitHub
- Include all major CRUD functions for at least one of your models
- Add authentication AND authorization (page protection) to restrict access to appropriate users
-   User must be able to sign up or login
-   Signed in user must be able to change password and logout
-   change password and logout must only be available to logged in users
- Layout and style your front-end with clean & well-formatted CSS, with or without a framework
- Deploy your application online so it's publicly accessible

Some of the possible stretch goals we could achieved included:

- Allow users to change website theme, Dark mode etc.
- Include Pagination
- Utilise 3rd party APIs
- Send verification email upon registration
- Allow users to upload image files
- Password reset using an email

At the end of the project we had to present our project while covering the points below:

- What is the app about?
- How does your app work?
- What bits of code are you most proud of?
- What was your favourite part to work on?
- What issues did you encounter?
- What would you add next?

## Planning  

### Development Overview  

As team leader, I worked with my teammates to come up with a clear development process that we could follow and track our progress over the course of project:

1. Brainstorm
2. Pick an idea
3. Wireframe, ERDs and user stories
4. Create repo and starting files (.js, .css., .html)
5. Break the process down by requirements
6. Basic layout
7. Structure logic and begin working on functions
8. Test functions
9. Touch up styling
10. Test site
11. BONUS: Add extras

### Team leadership  

Speaking to the team, we agreed that I would be team leader and handle management of the project and development flow. As in previous projects, we collaborated to set out a clear development overview that would allow us to remain accountable, on target and achieve our goals for this app. We established minimum deliverable functionalities as well as stretch goals, and as the project progressed, I ensured that we all stuck to these as a team. Wherever issues arose, we worked together to resolve these and I periodically checked in with my teammates to see if they needed help, feedback or support with bugs. We used Zoom and Slack to stay in constant communication throughout the project.

### Task management  

I created a public Trello board which all of our team could access in order to track, assign and manage tasks. This really helped us work collaboratively and we reviewed the Trello board on a daily basis each day to make sure we stayed up to date on what had been done, what needed to be assigned, and what hadn't been started yet.

We delegated functions by feature to each of the members of our team:
- I would work on creating user accounts, user profiles, the list of destinations and the main quiz function
- One teammate would work on our search function and APIs for displaying destinations
- One teammate would work on user review functionality, ratings, site styling/pagination and 3rd party APIs

You can find the link to our Trello board [here](https://trello.com/b/OvjiXE35/project3-django-djourney).

<img width="1907" height="1032" alt="Image" src="https://github.com/user-attachments/assets/8da7e68f-c6ec-4cff-8cf8-62ebce0daa44" />

## Build/Code Process

Documented below are the stages we went through in order to build the code for our project.  

### Stage 1: Brainstorming  

We started by brainstorming ideas for our app. Initial ideas included a World Cup 2022 match fixture tracker, a sports venue booking system and one or two other ideas related to sporting events. After some initial research, we decided to rule these out and went with our final, very appealing idea.

### Stage 2: Pick an idea  

My team were all quite ready for a holiday and taking inspiration from the perfume brand Penhaligon's website, where users can take a test to build a "fragrance profile" and be matched to the best fragrances for them, we thought: "Wouldn't it be great if you could have an app that tells you what your next holiday destination should be?". The idea struck a chord with all of us and we decided to build a quiz that users can take to be matched to a list of potential holiday destinations.

### Stage 3: Wireframe, ERD and user stories  

#### ERD

We started by drawing up an ERD to map out the relations between all of our models and functionalities.

<img width="733" height="473" alt="Image" src="https://github.com/user-attachments/assets/b83ff5e1-3fcb-4afd-aaa3-9e24eea8ce5b" />

#### Wireframes

We then got to work on wireframing our site page by page:  

<img width="500" height="350" alt="Image" src="https://github.com/user-attachments/assets/1814d05c-fd17-4d61-8fd4-b5d53bc06f20" />
<img width="500" height="350" alt="Image" src="https://github.com/user-attachments/assets/d0ed07cb-3973-48da-ae0d-3de607007392" />
<img width="500" height="550" alt="Image" src="https://github.com/user-attachments/assets/b293796d-7c4d-40ff-a66e-5e9622267408" />
<img width="500" height="550" alt="Image" src="https://github.com/user-attachments/assets/8a802a6c-fe94-403e-9054-5e751bf78fd4" />

#### User Stories

We took time to think about the features and functionalities we wanted our users to have, and set out the following user stories:

- As an unregistered user, I want a function to sign up to the site  
- As an unregistered user, I want to know what the site is about  
- As a registered user, I want to be able to create a profile  
- As a user of the site, I want to be able to see a list of destinations  
- As a user, I want to be able to see details about those destinations
- As a user, I want to be able to edit my profile  
- As a user, I want to be able to take the quiz 
- As a user, I want to be able to see my quiz results and the destinations they match up with
- BONUS: As a registered user, I want to be able to leave reviews   
- BONUS: As a user, I want to learn about the creators of the site  
- BONUS: As a user, I want to add my own destinations    

### Stage 4: Creating GitHub repo and starting files  

Since I was the team leader on this project, I created a repo on GitHub and set up the initial file structure so that we could begin working. I communicated constantly with my team to make sure that we were always working in the dev branch, and helping them to resolve any issues with migrations, merges, etc. We experienced relatively few issues with conflicts during merges as a result and development ran more or less smoothly.

### Stage 5: Requirements  

We defined our basic requirements at the outset:

- Users should be greeted by a welcome page explaining the site and the quiz
- Users should have the option to take the quiz, or skip straight to a list of all destinations
- Users should be able to create an account
- Users should be able to see details on individual destinations
- Users should be able to leave reviews on destinations they have visited

### Stage 6: Basic layout  

Once we had set out our basic requirements, we got started on the basic layout of the site in line with our wireframes. I created a **templates** folder in our main app directory where all of our html files would be located. We started with **base.html**, which is the file that serves as the base template for our site, with imported 3rd-party APIs, jQuery library, fonts, Bootstrap, CSS. The header contains our links to navigate the site, with additional links in the footer, while the **main** element uses backend code to allow us to insert other html files as the user navigates the site: 

<img width="1575" height="987" alt="Image" src="https://github.com/user-attachments/assets/feb25dac-21c8-4f12-98b6-28f876ff4c6f" />
  
The first page users see is **home.html**:

<img width="628" height="452" alt="Image" src="https://github.com/user-attachments/assets/2bbadb5b-d0c8-47bb-8229-867437bcf922" />

The HTML in this file between **{% block content %}** and **{% endblock %}** is taken as a whole block of code and slotted into the **base.html** because we have added **{% extends 'base.html' %}** at the top of the file. In this way we began building the different pages for our site, with separate HTML files for the users' profile, user registration, and destinations both collectively as well as individually. We would later add separate files for our quiz, quiz results, and search functionality: 

<img width="1607" height="807" alt="Image" src="https://github.com/user-attachments/assets/f696cb69-427a-4bf5-927d-b461e39c0b0d" />

### Stage 7: Structuring logic and working on functions  

I started by looking for a suitable list of destinations to use for our database. I settled on a list of 250 destinations collated by Nghia Nhuyen and offered for use on her GitHub [here](https://github.com/nghia-t-nguyen/travel-bot-project/blob/main/Travel-Destinations.csv). I edited the spreadsheet to include the **Name** of the destination, my teammates entered the **Location** and updated the **Country**for each one, and I also added the **Currency**. Later, I would also add a list of specific **Keywords** to each destination, which would be use later on in our quiz function:

<img width="1598" height="286" alt="Image" src="https://github.com/user-attachments/assets/f2d343a1-bb9d-44c1-b0f0-53a55707cbd9" />

With our basic list of destinations completed, I exported this as a .csv file and imported it into our database in PostgreSQL, taking care to deselect the ID tag when specifying the columns to import:

<img width="1030" height="280" alt="Image" src="https://github.com/user-attachments/assets/3730d94f-84d1-4263-bc27-29bc710dc20d" />
<img width="706" height="548" alt="Image" src="https://github.com/user-attachments/assets/4bfeb431-633e-4d36-842c-daedcc8eb722" />

This allowed my teammate to begin working on creating the APIs to retrieve all destinations via our search function or when the user clicks on 'View All Destinations': 

<img width="901" height="596" alt="Image" src="https://github.com/user-attachments/assets/d6a67207-8930-45aa-8d22-7d4508588958" />

As well as rendering details for individual destinations:

<img width="890" height="89" alt="Image" src="https://github.com/user-attachments/assets/ddde5121-076d-4439-b5de-510c81391ca8" />
  
Next, I worked on the user creation functionality. Creating the user account was simple enough with the use of a **signup** API. I wrote this to capture the information the user enters during sign-up as a POST request, validate this and then save the information as a new instance of User. With their user account now created, the user is then redirected to the index page:

<img width="890" height="606" alt="Image" src="https://github.com/user-attachments/assets/23e5236f-af0d-4b5a-b631-8ab0025f8a25" />

The file **forms.py** contains a model for a form that allows the user to update their profile information: 

<img width="714" alt="Image" src="https://github.com/user-attachments/assets/471207166-30b1b7e4-aeb9-414a-9319-c6079d4e0aac">
  
This is mirrored on the frontend with the following form:

<img width="714" height="342" alt="Image" src="https://github.com/user-attachments/assets/30b1b7e4-aeb9-414a-9319-c6079d4e0aac" />

The form is populated with their existing information, and once they click on the submit button, the **profile_update** API is triggered. The information entered in the frontend form is sent as a request to the backend, validated against the structure of the user and profile update forms, and if valid, both the user and profile objects are updated in the database:

<img width="1142" height="814" alt="Image" src="https://github.com/user-attachments/assets/4dbe4c43-46d3-4d74-a58f-99295a216df1" />

### Favourite functions

#### User signup & profile creation

The trick on this project was to allow the user to sign up and simultaneously create a profile for the user in the background. 

With the sign up API already written, I created a **signals.py** file. This contains two signals that would cause two additional functions to be triggered on the creation of an instance of User, and when they update their information. This creates an instance of Profile, which stores information about the user. This is then displayed when they log into the website, and is based on the instance of User that has just been created. It was tricky to get working at first, but by using console.log on each line of my code, I was able to pinpoint my error, which was an incorrect import statement.

<img width="858" height="292" alt="Image" src="https://github.com/user-attachments/assets/b8196904-c9b1-4616-8da8-970b0f3cdc09" />

#### Destination Quiz (rango-query.js)

I wrote the quiz function - the main element of our site - using jQuery. The quiz is actually structured as a form with a hidden input tag that contains an empty value attribute. The quiz itself is composed of a series of four questions. The user has three options per round, one of which is entirely neutral. With each answer they click, a specific keyword is pushed to this empty value attribute, or no keyword if their answer is neutral. When the user then clicks on the "Find my holiday!" button at the end of the quiz, the string stored in the value attribute is then used as a "profile" to search the database of destinations and return a list of destinations.

Each destination in our database has a specific combination of keywords, meaning that only those destinations containing these keywords will be returned and made visible to the user, i.e. destinations matching their profile. jQuery is used to update the value attribute with each question answered, to make use of delay times and fade-out functionalities, thus providing a great experience for the person taking the quiz!

<img width="476" height="320" alt="Image" src="https://github.com/user-attachments/assets/7747446b-7de1-43c5-b0f4-0d8cc112971f" />

<img width="1488" height="964" alt="Image" src="https://github.com/user-attachments/assets/4f22dab9-22a8-429b-8e94-415758012bae" />

### Stage 8: Testing functions  

Testing functions along the way is how we managed to stay on track for delivery and ensure we minimised the risk of bugs. We used a lot of console.logs to capture the information we were generating and see what extra code was needed to achieve the functionality we wanted. We also got the other members of our team to test our code and look through it to make sure we didn't miss anything critical.

### Stage 9: Styling  

We knew from the start that we wanted our site to be responsive, simple, clean and easy on the eyes. We drew inspiration from Skyscanner, Trip Advisor and other sites to style our website, with destinations presented as cards: 

<img width="859" height="493" alt="Image" src="https://github.com/user-attachments/assets/b1ba01b0-74f0-4129-b681-b9f78d844fcf" />

When all destinations are displayed on the **destinations/index.html**, we first start with a div that has the classes of **"row card-group"**. A separate **card** div is then created for each destination, containing the destination image, name, review, and other details:

<img width="1919" height="1039" alt="Image" src="https://github.com/user-attachments/assets/079efa1e-48fd-48d6-aa6e-2aadf0cc9dfb" />

Providing feedback as a team, our teammate who focused on styling the site to make it fully mobile responsive when the width of 428px is reached:

<p float="left">
<img width="337" alt="Image" src="https://github.com/user-attachments/assets/c989051d-f387-4e5b-847c-67289c02a90d" />
<img width="337" alt="Image" src="https://github.com/user-attachments/assets/28874a80-d96d-4d41-8280-4ab427f510a2" />
</p>

This means e.g. that the two divs that make up our quiz are displayed one above the other instead of side-by-side on a computer, and the font size is reduced to fit within the respective divs throughout the site:

<img src="https://github.com/user-attachments/assets/30ed6e62-2422-4e97-84be-4876a7910953" height="500" width="250">

### Stage 10: Testing the site  

We tested our quiz repeatedly to adjust timings and fadeouts, and tested the destination list, user signup, profile creation and API calls to make sure these were all working the way we wanted. We used plenty of console.logs to check what our functions were doing precisely, and where the information we were getting was incorrect or the function was working differently than anticipated, we were able to correct this. We checked all of our links to make sure these were correct, and checked the database to ensure all of our API calls were creating, updating and deleting information correctly. We also got friends to test the quiz to ensure the user experience was seamless and working as we wanted.

<img width="904" height="988" alt="Image" src="https://github.com/user-attachments/assets/7b64c488-6c96-46df-afd3-6a367e5d1b93" />

### Stage 11: Bonus features  

The development of our project went so well that we were able to add additional functionality, such as the option for users to leave a review on destinations they have visited before. A form is shown to users on the detail page for the individual destination. Here users canleave a review on a destination:

<img width="1142" height="814" alt="Image" src="https://github.com/user-attachments/assets/9b75f110-b779-41df-b3ff-e9b121183894" />

When they click submit, the **add_review** API is triggered and information in the form is captured and validated against the review form model:

<img width="514" height="199" alt="Image" src="https://github.com/user-attachments/assets/7160eae8-e790-4aa1-95e9-a039aa18cb21" />
<img width="581" height="236" alt="Image" src="https://github.com/user-attachments/assets/964839a5-fdad-4a2e-a583-bfbeeaf84f20" />

If the content is valid according to the structure of the Review model, this is saved in the database as a new review and then listed on the individual destination.

## Challenges

We had a hard time with the search functionality of our app, but were able to get this working after extensive trial and error. We also found adding star ratings to be quite a challenge, and after testing several different methods to no success, came up with a solution that worked for us. We were also hampered by the number of API calls we could make to our 3rd party weather API, with just 50 calls permitted a day.

### Problem-solving  

We worked well as a team at investigating and resolving bugs as they came up. We maintained constant communication to resolve errors, and if teammates were currently too busy working on a specific functionality, I took the initiative as team leader to do additional research to resolve the bugs we were encountering. We went through each line of code one at a time to identify where issues were occurring and exactly what information we were getting back. I kept a log of all errors as they occurred so we could track issues and resolve them in a timely manner.

## Wins

The fact that our project is fully responsive is a big win:

<p float="left">
<img width="280" alt="Image" src="https://github.com/user-attachments/assets/6bda50a6-de3d-4e0e-b04e-3abf67dd962d" />
<img width="280" alt="Image" src="https://github.com/user-attachments/assets/3682adc5-1ee8-4903-9543-18e66bdb70e9" />
<img width="280" alt="Image" src="https://github.com/user-attachments/assets/1e98f4b8-a866-4dff-b81a-c4c99bbfe6e3" />
</p>
                                                                                                                            
I'm also very happy that with just a week or so of Python under our belts, we were able to produce an app of this caliber. I personally struggled with adjusting from JavaScript to Python in the beginning stages, but working with my team to build an app we could be proud of and resolving issues along the way, my confidence in the language grew and I am very proud of the product we were able to deliver.
                                                                                                                            
## Key Learnings & Takeaways

This project taught me that working in a team can be fun and seamless when you establish your criteria and process clearly from the outset. We worked so well as a team that our communication was always effortless, productive and led to us resolving issues collaboratively in a very short time. Although I personally prefer JavaScript, I learned that I can do a lot with Python, and this project gave me a much better understanding of the language. I feel more confident using Python after implementing it on this project.

## Bugs

Heroku periodically deletes images, so some images such as profile photos will not display properly. This could be rectified by using Cloudinary for image storage rather than using Multer.

## Future Improvements

In future versions of Django Djourneys, I want to allow users to be able to add destinations - subject to approval by an administrator. These would require checking to ensure multiple versions of the same destination do not get added to the database. I would also add in forwarding to e.g. Skyscanner to allow users to check and book flights to the destination of their choice.
