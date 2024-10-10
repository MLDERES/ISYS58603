# Group Assignment 2 - Loading Data

## Goal
The purpose of this assignment is to help students understand how to load data into a database using Python.

## Deliverable
There are two parts to this assignment.  One for the group to complete, and one part which is to be completed by every individual in the team.  All of the components should be a part of the single group repository which will be submitted to Blackboard.  

***<span style="color:red">NOTE:</span> If your repository is private, you'll need to invite the professors***

***<span style="color:red">NOTE2:</span> Be sure to TAG the commit that you want to be graded with `v0.1`, `GA2` or similar so that it's clear what you want to be evaluated***.  This will also allow you to continue working on your repo without worrying about it being graded in a state of flux.

- **As a group**
  - A GitHub repository which all members of the group are contributors
  - A structured, semi-structured, or unstructured files containing the data  
  - A SQLite database with the data
    - The database must have _at least_ two related tables 
  - A README.md (markdown format) file with an overview of the application
  - A description of the data in the database (i.e. data dictionary). This could be part of the README.md or another file
    - OPTIONAL (but highly encouraged): An entity diagram
  
- **Each Individual**
  - Three queries (one query can satisfy one or more of the conditions)
    - At least one includes two or more tables (via join or relationship) 
    - At least one with parameterized input
    - At least one which includes aggregated data (group by or single aggregation)
    - These queries should be included in the repository.  Define what these queries do in the README.md (or similar file) using *markdown* documentation.
  - GitHub history of commits will be used as evidence of individual work.

## Background
The intent of this exercise is practice working on a team repository and also to practice adding data to a database.  For this set of exercises we are using SQLite3 because it is ubiquitous and it can be moved around like a simple file, which means it can be added to GitHub and managed using the tools we've learned in Git hub.

The goal of this exercise is to begin to build a team repository with appropriate folders for the raw data, the database, documentation and (eventually though not in this exercise) the objects and endpoints for the API calls.

Teams/individuals are strongly encouraged to use feature branches and pull requests to integrate changes from members of the team and to keep all commit history public, by pushing all the local commits to the shared repository on GitHub.  

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

* When all the pulls and syncs are complete, add a tag to the commit that you want to be graded.  This will be the commit that is graded.
  
## Help and Hints

* There is tons of publicly available data, though not much of it is in a relational format.  For instance, [this data](https://github.com/MLDERES/Py4Analytics/tree/main/book/data) is collected from publicly available sources.  Additionally, you could use a site like [mockaroo](https://mockaroo.com/) to generate portions or all of your data.  If you are really adventurous, you can use a library like [mimesis](https://mimesis.name/en/master/index.html) to get exactly what you want and skip the part about having to save it to a flat file.
* There haven't been examples provided for putting data into a database.  You are welcome to use any methods you've seen so far (e.g. SQL inserts, Pandas or SQLAlchemy).
  * The absolute simplest way to do this is to use the `sqlite3` library and write SQL statements to insert the data.  This is not the most efficient way, but it is the simplest.
  * The next easiest way is to use Pandas to read the data and then use the `to_sql` method to write the data to the database.  This is a little more complicated, but it is more efficient.  
* Queries should be written **as functions** in the model, therefore multiple queries can be stored in a single file.  These functions should be called from the controller.  The controller should be called from the main application.  This is the MVC pattern.  It is not required, but it is strongly encouraged.
  * **Extra hint**:  If you do SQLAlchemy for inserts now, it will help you do the queries and the API later.

## Sample project structure
Students have said that it is helpful to understand how a project of this type can be structured.  Here is a simple example of how the project could be structured.  This is not the only way to structure the project, but it is a way that has worked for many students in the past.

```
project_root/
│
├── api/
│   ├── __init__.py               # Package initializer for the 'api' directory
│   ├── models.py                 # Database models/classes
│   ├── routes.py                 # API route definitions
│   └── services.py               # Service functions, handling business logic, and database operations
│
├── data/
│   └── movie_data.db             # SQLite database file 
│
├── docs/
│   ├── api_documentation.md      # Documentation for API usage
|   └── data_dictionary.md        # Data dictionary for the database
│
├── tests/                        # Optional directory for unit tests
│   ├── __init__.py               # Package initializer for 'tests'
│   ├── test_db.py                # Unit tests for database operations
│   ├── test_routes.py            # Unit tests for API routes
│   └── test_services.py          # Unit tests for service layer
│
├── utility/
│   ├── helpers.py                # Utility functions used across the project
│   └── config.py                 # Configuration settings for the application
│
├── .gitignore                    # Specifies files and folders to be ignored by Git
├── LICENSE                       # License information for the project
├── README.md                     # General overview and setup instructions for the project
└── run.py                        # Entry point script to start the Flask application
```

There are a few challenges to putting the files together in this way, so you can take a look at [this project](https://github.com/ISYS58603/MovieRatings) to see examples of how libraries are referenced, how the data is loaded, and how the queries are written.  This is a simple example, but it should be enough to get you started.  If you have questions, please ask.