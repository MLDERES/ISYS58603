# Exercising the API 

In order to access the API for something useful, from a front-end, we need to start the API to listen on the network.  The API can be started using the one of the following commands:
```bash
python basic-flask.py
```
or 
```bash
python advanced-flask.py
```
or
```bash
uvicorn fastapi:app --reload
```

<span style="color:red; font-weight:bold; font-style:italic">Each of the three APIs offer different endpoints, so you'll need to use the correct endpoint for the API you are using.
</span>In most cases, your code will be implemented in a single API so there won't be this concern.


## Using a webpage

In this project there is a sample HTML file which will access the API.  To use this file, you'll need to start the API and then open the file in a web browser.  The file is located at: examples/views/fastapi.html.  In reality, it doesn't matter which backend is being used, the HTML file would work with any of the backends, if all the endpoints are supported.  

## Exercising the API using Python
Also in this project there is a Jupyter notebook which can be used to access the basic-flask API.  The notebook is located at: `examples/views/basic-flask.ipynb`.  Once again, there are different endpoints supported by the different APIs so you have to start the right API to connect.  The notebook assumes that you have started the **basic-flask** api.