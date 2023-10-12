# Group Assignment 3 - Creating the API

## Goal
The purpose of this assignment is to give students the opportunity to design and develop an API which will be able to interact with the database.

## Deliverable
This assignment will be assessed in two stages:
1. The design for the API will be developed
2. The queries connected to the design will be developed.

The design for the API should meet all of the requirements outlined here.  The implementation should be complete (it works completely) for at least one of the GET methods.  The other methods can be defined with placeholders.  Documentation needs to be provided for each of the paths

GET - at least one for every table (except mapping tables)
- Get all (must have a filter) LIMIT
  - (e.g. https://localhost:5000/customers?limit=10)
- Get one by one
  - (e.g. https://localhost:5000/customers/1)
- Get that spans multiple tables

These don't have to be for every table, only the tables where it makes sense
* POST - Create a new entity for your database (can be a single table or multiple tables)
* PUT - Update an entity in your database
* DELETE - Remove an entity from your database

***Note be sure to TAG the commit that you want to be graded with `v2.0`, `GA3` or similar so that it's clear what you want to be evaluated***

## Background
You are building an API to access the data in the database you have developed.  Your API can be **focused** on getting data into the database or out of the database (most likely out of the database).  Strongly consider what kinds of queries will be useful and plan ahead so that your API will offer a consistent and easy to use interface.

For example consider the following:
* You have a table of `students` and a table of `courses` and a table of `grades`.  You want to be able to get the grades for a student in a course.  You could do this in a couple of ways:
  * You could have a path that is `/students/{student_id}/courses/{course_id}/grades` which would return the grades for the student in the course
  * You could have a path that is `/grades` and you would pass in the student_id and course_id as parameters to the query such as `/grades?student_id=1&course_id=2`
  * You could have a path that is `/students/{student_id}/grades` and you would pass in the course_id as a parameter to the query such as `/students/1/grades?course_id=2`

All of these are valid approaches.  The first one is the most RESTful, but it is also the most complicated to implement.  The second one is the least RESTful, but it is the easiest to implement.  The third one is a compromise between the two.

Whichever approach you choose, you should be consistent so that the user experience is consistent.  A couple things to consider:
* Use query strings for optional parameters and also for parameters that would difficult in the path (like strings with spaces or special characters)
* Use path parameters for required parameters
* Use the same parameter names across all of your paths
* Use the same HTTP verbs for the same kinds of operations (e.g. use GET for all of your queries, use POST for all of your inserts, use PUT for all of your updates, use DELETE for all of your deletes)

### Testing the API
While not required for this assignment, it is strongly recommended that you use a tool like [Postman](https://www.postman.com/) to test your API.  This will allow you to test the API without having to write a client for it.  You can also use the browser to test the API, but it is not as flexible as Postman.

## Instructions
Rather than give an explicit list of instructions here.  A general outline of activities is listed which you may execute in whatever order makes sense.

* Develop your plan.  
  * Which tables are going to be static and should only need to be queried?            
  * Which tables/entities are going to make sense for updating and deleting?
  * How do you want to expose queries for the different entities?
* Document your paths in your README.md or HOWTO.md and in the comments (using [docstrings](https://www.programiz.com/python-programming/docstrings) and/or the [OpenAPI](https://swagger.io/docs/specification/about/) specification)
* Create your paths and the associated functions in the controller
  * If you just create the shell of the function, then the content can be `pass` to make it a syntactically correct python.  This can be used as a placeholder until you are ready to implement the function.
  ```python
  @app.get(/items/{item_id})
  def collect_item_by_id(item_id):
    pass
  ```
* Connect the methods associated with the paths to the queries you have built in the `model`

## Help and Hints
We have created a few examples to help you visualize how to go about developing your application.  These examples are not complete, but they should give you a good idea of how to get started.  Make sure to consult the README.md in the examples folder for more information.

In the examples folder
- **basic-flask.py** - This is a very basic example of how to use Flask to create an API.  It connects to the database and shows the basic examples for each of the 4 verbs (GET, POST, PUT, DELETE)
- **advanced-flask.py** - this is a more advanced Flask example.  Providing more examples of how to use the different verbs and how to use parameters in the path and in the query string.
- **fast-api.py** - this is an example of how to use FastAPI to create an API.  It connects to the database and shows the basic examples for each of the 4 verbs (GET, POST, PUT, DELETE), but it leverages the SQLAlchemy ORM to make it easier to work with the database.

If you are finding the folder structure complex, this is a simplified version of the folder structure that you can use:
```bash
.
├── app.py            # this is where you would put your main application
├── config.py         # this is where you would put your configuration information
├── controller.py     # this is where you would put your paths
├── data              # this is where you would put your data files
│   ├── customers.csv
│   └── customers.db
├── database.py       # this is where you would put your database connection
├── model.py          # this is where you would put your queries
├── README.md
├── static            # this is where you would put your static files like images, css, javascript, etc.
└── requirements.txt  # this is where you would put your python dependencies

```

