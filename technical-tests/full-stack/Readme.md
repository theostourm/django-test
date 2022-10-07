# Oddbox - Full-Stack Technical Test

The Oddbox Full-Stack technical test is designed to test your fundamental understanding of building and using the django framework to expose data for web applications. 

## Task

Your task is to model and store blog post data, expose the data via an API, and consume it on the frontend.

1. Create django model(s) to represent the blog data found in `data/posts.csv`. 
2. Write a loader to import the blog post data into your database.
3. Expose the blog posts via an api that supports pagination
4. Create a react component to fetch data from the api you created in step 3 and display in a looping carousel [mockup](mockup.png)

Please download this repository, add your changes, and upload them to a private GitHub repository. Invite [oddbox-team](https://github.com/oddbox-team) as a collaborator.

Please update this readme with instructions and any assumptions you may have made.

Please do not spend longer than 4 hours on the task - we are looking to understand your approach rather than your ability to build something production-ready in a morning!

## Getting Started

Some boilerplate has been created to help you get started, including django and django-admin for the backend, and create react app on the frontend. It requires [docker](https://www.docker.com/).

Feel free to use the boilerplate or to create your own.

```
> docker-compose run backend python manage.py migrate
```

Will create the database `src/backend/db.sqlite3`.

```
> docker-compose run backend python manage.py createsuperuser
```

To create a superuser for django-admin

```
> docker-compose up
```

Frontend:  http://localhost:3000
Backend:  http://localhost:8000
Django Admin:  http://localhost:8000/admin



## Instructions

First, to install djangorestframework in the container, run:

> docker-compose build

Then, to create the sqlite3 database:

> docker-compose run backend python manage.py migrate

To create a superuser for django-admin:

> docker-compose run backend python manage.py createsuperuser

To have the containers up and running:

> docker-compose up

Then, create two new models and the associated tables in the db (Post, Tag, and the table linking them).

> python manage.py makemigrations
> python manage.py migrate

- Second, we will populate the database with the posts.csv file.

    - Let's check the posts in the database first, with a GET request, 
      The result should be an empty list (you can use Postman, or a similar tool to send a request): http://localhost:8000/posts/
  
    - Let's populate the database with a POST request, requesting the same URL: http://localhost:8000/posts/
    
    - Let's check again the posts in the database with a GET request: http://localhost:8000/posts/
      You should see the posts data!


## Assumptions

To make decision about the models used to store the data, I have had a look at the data in the csv.
the '/blog/' from the slug is not stored in the database, we keep only the slug which is the last part of the url (after the last '/')

I have created a second model Tag because I have seen that some of them are used multiple times, and could be re-used in the future.
Then in the database there is a third table linking the tags with the posts.

I could have done the same for the authors as they are used multiple times as well. I decided not to proceed because it would create tables with only a few (2?) entries.

## Notes

Some tests are available in /blog/tests.py, feel free to run them!
I have not written a lot of non-native Django function, thus not so many tests.

The POST method directly gets the data with the name of the csv file. In real life the csv could not be stored in the code, but in an AWS S3 bucket for example.
In this case we would connect to the bucket and get the data from there.

In the csv file, the pictures are stored online, we could also upload these pictures in an S3 bucket stored on company's cloud for security.

