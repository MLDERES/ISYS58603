# Group Assignment 4 - Putting a front-end on the API

## Goal
The purpose of this assignment is to transition your API into a functional application—essentially moving from the abstract to the concrete. Your application could be a web-based front-end, a command-line interface, or even a data visualization tool.

## Deliverable
Submit the GitHub URL of your repository containing all code, dependencies, and a README with instructions for running the application. The application will be evaluated based on the effective use of the API, correctness, completeness (utilization of various API endpoints), and creativity.

***<span style="color:red">NOTE:</span>be sure to TAG the commit that you want to be graded with `v0.3`, `GA4` or similar so that it's clear what you want to be evaluated***
## Background
Remember, the API you've built has several purposes, such as data exchange, modularity, and reusability. Think about how these aspects can influence your front-end. For example, if your API focuses on data exchange, you might build a data visualization front-end.

## Help and Hints
We've provided some example code in the [examples folder](examples/README.md) to help you get started. Check the README in that folder for more information. Consider also looking into best practices for API and front-end development to ensure your application is efficient.

**While we have provided examples in the same repository as our API, you are not required to do so. You may create a separate repository for your front-end application.  As a matter of fact, you may find this easier to manage.**

In the [examples folder](examples/README.md)
- **basic-flask.py** - This is a very basic example of how to use Flask to create an API.  It connects to the database and shows the basic examples for each of the 4 verbs (GET, POST, PUT, DELETE)
- **advanced-flask.py** - this is a more advanced Flask example.  Providing more examples of how to use the different verbs and how to use parameters in the path and in the query string.
- **fast-api.py** - this is an example of how to use FastAPI to create an API.  It connects to the database and shows the basic examples for each of the 4 verbs (GET, POST, PUT, DELETE), but it leverages the SQLAlchemy ORM to make it easier to work with the database.

The applications which use the APIs are in the [views](examples/views) folder.  These are the front-end applications that use the APIs.  They are very basic, but they should give you an idea of how to get started.
- **basic-flask.ipynb** - This is an example Jupyter notebook which connects to and uses the basic-flask.py API.  Once the basic-flask API is started the notebook walks through how to use the API and how to use the different verbs.
- **fastapi.hmtl** - This is an example HTML page which connects to and uses the fast-api.py API.  Once the fast-api API is started the page walks through how to use the API and how to use the different verbs.  It is a bit more complex, in that it uses JavaScript to make the API calls, but it should give you an idea of how to get started.
