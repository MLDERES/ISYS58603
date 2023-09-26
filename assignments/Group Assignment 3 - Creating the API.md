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
- Get one by one
- Get that spans multiple times

These don't have to be for every table, only the tables where it makes sense
* POST - Create a new entity for your database (can be a single table or multiple tables)
* PUT - Update an entity in your database
* DELETE - Remove an entity from your database

## Background
You are building an API to access the data in the database you have developed.  Your API can be **focused** on getting data into the database or out of the database (most likely out of the database).  Strongly consider what kinds of queries will be useful and plan ahead so that your API will offer a consistent and easy to use interface.

For example consider the following:
* You have a table of `students` and a table of `courses` and a table of `grades`.  You want to be able to get the grades for a student in a course.  You could do this in a couple of ways:
  * You could have a path that is `/students/{student_id}/courses/{course_id}/grades` which would return the grades for the student in the course
  * You could have a path that is `/grades` and you would pass in the student_id and course_id as parameters to the query such as `/grades?student_id=1&course_id=2`
  * You could have a path that is `/students/{student_id}/grades` and you would pass in the course_id as a parameter to the query such as `/students/1/grades?course_id=2`

All of these are valid approaches.  The first one is the most RESTful, but it is also the most complicated to implement.  The second one is the least RESTful, but it is the easiest to implement.  The third one is a compromise between the two.

Whichever approach you choose, you should be consistent so that the user experience is consistent.

### Testing the API
While not required for this assignment, it is strongly recommended that you use a tool like [Postman](https://www.postman.com/) to test your API.  This will allow you to test the API without having to write a client for it.  You can also use the browser to test the API, but it is not as flexible as Postman.

## Instructions
Rather than give an explicit list of instructions here.  A general outline of activities is listed which you may execute in whatever order makes sense.

* Develop your plan.  
  * Which tables are going to be static and should only need to be queried?            
  * Which tables/entities are going to make sense for updating and deleting?
  * How do you want to expose queries for the different entities?
* Document your paths in your README.md or HOWTO.md and in the comments (using [docstrings](https://www.programiz.com/python-programming/docstrings))
* Create your paths and the associated functions in the controller
  * If you just create the shell of the function, then the content can be `pass` to make it a syntactically correct python
  ```python
  @app.get(/items/{item_id})
  def collect_item_by_id(item_id):
    pass
  ```
* Connect the methods associated with the paths to the queries you have built in the `model`

## Help and Hints
The code below shows how to use the flask package to develop your API.  The code below is a simple example of how to create a path that will return a list of all of the students in the database.

```python
from flask import Flask
from flask import jsonify
from flask import request
from controller import get_all_students, select_student_by_id
app = Flask(__name__) 

@app.route('/students', methods=['GET'])
def get_students():
    # Get the list of students from the database
    # Return the list of students as a JSON object
    return jsonify(get_all_students())

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    # Get the student from the database
    # Return the student as a JSON object
    return jsonify(select_student_by_id(student_id))
``` 