# Code Jam Submission by Team Adventurous Anteaters

- The original ambitious project was to create a "Decentralized Social Network.", something like FidoNet.
- The idea sprouted from the fact that the theme is "Early Internet".
- Back in the day, not everything was on a single central server, and many networks were not even part of the WWW because it was that new. 
- So, we wanted to create something, that would have one or two parent servers, and rest of the servers could be spawned by anyone. 
- Each spawned server would host their own set of Users, and if the servers had access keys to each others, those users would be able to interact with each other as well. 

## However, we are NOWHERE NEAR THAT! So, if someone sees this and wants to try, you have our blessing :) 

#Setup:
1. git clone the project
2. Install Requirements: pip install -r requirements.txt
3. make the migrations: py manage.py makemigrations
                       py manage.py migrate
4. run server: py manage.py runserver


### Flow of the Project: 

- The home page is the profile page, which requires you to be logged in. 
- There's boilerplate check to see if user is logged in, if not, redirect to login page.
- From here, user can register as well if no account is present.
- Once that is done, user will be redirected to Profile page
- Here, he can see the button to "Post a Tweet"
- Clicking on it shows two text boxes, one is the title of the tweet, and the other is the content. 
- Once posted, the user can see all the posted tweets
- There is some small functionality added in the icon bar in header, however, most of it is just for the retro feel. 

### The Following endpoints are active:
- /profile
- /post
- /posted
- /view_tweet
- /register


# What we Learned from participating in the Jam.
- GIT
- HTML/CSS/JS
- Django basics
- Templating (Jinja Templating)
- Team Work
- Time Management (yeah, right!)

[WE EVEN MADE A SHEET](https://docs.google.com/spreadsheets/d/1txXqRkj4V4D4RS1sVEganfGJPK0br0lnWWaH3P1boUM/edit#gid=873896706)
