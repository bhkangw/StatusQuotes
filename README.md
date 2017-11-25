## Synopsis
This is a complete CRUD app built using Django that allows a user to access a Quotes wall after logging in or creating a new account. Once verified, the user has access to the community's list of famous quotes and the ability to add their own. They can also favorite specific quotes - which separates the quote into their own personal list. The goal of this app is to give the user a dashboard where they can interact with a community by adding their favorite quotes and 'bookmarking' liked quotes submitted by other users.

## Motivation
This app was built exam-style, from-scratch, timed in 4.5 hours in order to test proficiency of Python using the Django framework. Received a score of 10.0 out of 10.0.

## Features
- Appointments & Login app has full validations on all form fields ie. password, birthday, name, email, appointment dates, quotes content, etc.

- Users' passwords encypted using bcrypt.

- Each user has a page displaying their contributed quotes and contribution count.

- Connected to backend database using django SQLite for all Quotes and User data. Saves quotes per user independent of sessions.

- Utilizes a many to many model relationship in order to display a user's favorited quotes separately from the default list.

- Used Twitter Bootstrap for basic styling on both login page and Quotes dashboard.

## Skills/Concepts Practiced
- OOP / ORMs
- Client/Server Communication
- Django
- Models/Migration/Relationships
- Password Hashing
- Backend Database connections
- SQL Queries
- RESTful Routing
- Deployment through AWS
