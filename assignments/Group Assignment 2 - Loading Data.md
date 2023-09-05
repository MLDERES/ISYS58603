# Group Assignment 2 - Loading Data

## Goal
The purpose of this assignment is to help students understand how to load data into a database using Python.

## Deliverable
There are two parts to this assignment.  One for the group to complete, and one part which is to be completed by every individual in the team.  All of the components should be a part of the single group repository which will be submitted to Blackboard.  <span style="color:red">**NOTE: If your repository is private, you'll need to invite the professors **</span> 

- **As a group**
  - A GitHub repository which all members of the group are contributors
  - A structured, semi-structured, or unstructured files containing the data  
  - A SQLite database with the data 
  - A README.md (markdown format) file with an overview of the application
  - A description of the data in the database (i.e. data dictionary). This could be part of the README.md or another file
    - OPTIONALLY: An entity diagram
  
- **Each Individual**
  - Three queries (one query can satisfy one or more of the conditions)
    - At least one includes two or more tables (via join or relationship) 
    - At least one with parameterized input
    - At least one which includes aggregated data (group by or single aggregation)
    - These queries should be included in the repository.  Defining what these queries do will be helpful in the README.md or other *markdown* documentation as appropriate to your repository.
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
            

