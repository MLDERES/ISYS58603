# Group Assignment 3 - Creating the API

## Goal
The purpose of this assignment is to give students the opportunity to design and develop an API which will be able to interact with the database.

## Deliverable
This assignment will be assessed in two stages:
1. The design for the API will be developed
2. The queries connected to the design will be developed.

The design for the API should meet all of the requirements outlined here.  The implementation should be complete (it works completely) for at least one of the GET methods.  The other methods can be defined with placeholders.

GET - at least one for every table (not mapping tables)
- Get all (must have a filter) LIMIT
- Get one by one
- Get that spans multiple times

One for each table
POST
PUT
DELETE

Sample documentation for each call


## Background

## Instructions
Rather than give an explicit list of instructions here.  A general outline of activities is listed which you may execute in whatever order makes sense.  Also a few hints to the structure of the repository are also offered.

* Create a group repository on GitHub.  Ensure all members have access.
* One member creates the basic structure of the repository.  
  * Have a look through GitHub for some ideas of good structures.
  * OR, follow Peter's example structure
  * OR, ask one of your favorite GenerativeAI tools to give you an example
  * OR, check out the documentation for Flask 
* Be sure to add the common files.This includes:
  * README.md
  * File with the scripts to import the data into the database
  * The newly created database file (from the scripts)
  * The raw data used to create the database
  * Anything else that seems appropriate
* Each team member pulls the latest and creates a feature branch
* Push the feature branch to the remote repository
* Each team member develops and commits their changes locally
* When ready, push the commits to the server and open a pull request
* Another team member *should* (not required) review the changes and complete the pull request
* Team members pull the latest changes to the local environment
            
## Help and Hints

* There is tons of publicly available data, though not much of it is in a relational format.  For instance, [this data](https://github.com/MLDERES/Py4Analytics/tree/main/book/data) is collected from publicly available sources.  Additionally, you could use a site like [mockaroo](https://mockaroo.com/) to generate portions or all of your data.  If you are really adventurous, you can use a library like [mimesis](https://mimesis.name/en/master/index.html) to get exactly what you want and skip the part about having to save it to a flat file.
* There haven't been examples provided for putting data into a database.  You are welcome to use any methods you've seen so far (e.g. SQL inserts, Pandas or SQLAlchemy).  
  * **Extra hint**:  If you do SQLAlchemy for inserts now, it will help you do the queries and the API later.