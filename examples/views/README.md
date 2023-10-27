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


## Exercising the API using Jupyter
Also in this project there is a Jupyter notebook which can be used to access the basic-flask API.  The notebook is located at: `examples/views/customers_test.ipynb`.  Once again, there are different endpoints supported by the different APIs so you have to start the right API to connect.  The notebook assumes that you have started the **basic-flask** api.  Once you start the API, then you can work through the notebook, cell-by-cell, executing each end point provided by the API.  The notebook will walk you through how to use the API and how to use the different verbs.

## Exercising the API using Python
Not all front-ends are graphical or require a fancy user interface.  Check out the `playlist_creator.py` file in the `examples/views` folder.  This is a simple Python script which uses the API to create a playlist.  It is a very simple example, but it should give you an idea of how to get started.  In this case, we left the details of calling the API out of the mix and just put in placeholders.  Sometimes seeing a front-end without the complexity of the API calls can be helpful.

## Using a webpage
In this project there is a sample HTML file which will access the API.  To use this file, you'll need to start the API and then open the file in a web browser.  The file is located at: `examples/views/tracks_albums_test.html`.  In reality, it doesn't matter which backend is being used, the HTML file would work with any of the backends, if all the endpoints are supported.  

