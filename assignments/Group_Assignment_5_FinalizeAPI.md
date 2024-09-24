# Group Assignment 5 - Finalize the API

## Goal
The purpose of this assignment is to stamp your API complete for use by someone else.  You will need to ensure that your API is documented and that it is easy to use.

## Deliverable
Submit the GitHub URL of your repository containing all code, dependencies, and a README with instructions for running the application. The application will be evaluated based on the effective use of the API, correctness, completeness (utilization of various API endpoints), and creativity.

***<span style="color:red">NOTE:</span> Be sure to TAG the commit that you want to be graded with `v1.0`, `GA5` or similar so that it's clear what you want to be evaluated***
## Background
Remember, the API you've built has several purposes, such as data exchange, modularity, and reusability. Think about how these aspects can influence your front-end. For example, if your API focuses on data exchange, you might build a data visualization front-end.

## Help and Hints
Clear and clean documentation are super important for this part of the project.  Think about how you want to document your API.  Make sure that you are exposing all the information that someone would need to use your API.  This includes:
- What is the base URL for your API?
- What are the paths for your API?
- What are the parameters for each path?
- What are the verbs for each path?
- What are the responses for each path?
- What are the data types for each parameter?
- What are the data types for each response?
- What are the data types for each query parameter?
- 

If you haven't already done so, ensure that you are not using fully-qualified paths or at least make them configurable.  This will make it easier for someone else to use your API.  This means don't have a path like `C:\Users\johndoe\Documents\GitHub\api\api.db` in your code.  Instead, make it configurable or relative.  For example, you could have a path like `./api.db` or `../api.db` or `~/api.db` or `/var/lib/api/api.db` or `C:\Users\johndoe\Documents\GitHub\api\api.db` and then make that configurable via a variable.  This way, someone else can clone your repository and run your API without having to change your code.
