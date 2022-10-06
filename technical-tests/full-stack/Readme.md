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

...


## Assumptions

...

## Notes

...
