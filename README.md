
# Webd2decoder
This project is based on the project [LaBot](https://github.com/louisabraham/LaBot). Its purpose is to provide web APIs for the module LaBot-decoder. The final goal is to provide a module that can help build tools for Dofus 2.  
The origin of this project is that it is quite time-consuming to build a stack to understand the messages exchanged between Dofus' client and server. By providing web APIs to LaBot-decoder, we can have a standard application dedicated to Dofus' messages understanding. Thus, any tool, whatever the technologies powering it, can delegate the message reading function to this app.
![
](/docs/webd2decoder.JPG)
## APIs
There is 2 way to use this app. You can use it through http calls or through websocket **(do not confuse with socketio)**. Endpoints are described below.
### 1. Webservices
See postman collection (TODO) for examples. 
 1. **[POST]** /decoder/fromclient mediatype: text/plain
 Decode a message produced by the client. The body is the raw message in hexadecimal format.
 3. **[POST]** /decoder/fromserver mediatype: text/plain
Decode a message produced by the server. The body is the raw message in hexadecimal format.
### 2. Websocket endpoint
**wss://hostname/decoder**

This endpoint can decode messages procuded by both client and server. You still have to indicate from which actor the messages has been produced. The message format for this endpoint is a simple JSON with 2 fields :

{
"data" : "4ED5454CDA...",
"fromclient": true
}

Data is the raw message in hex format. 
The fromclient field has to be set to true to decode a message from client and to false if the message is from the server.

## Start the app
Following commands  consider the working directory is the project root.
### 1. Python 
Install dependencies :
````
pip3 install -r requirements.txt
````
Run the app :
````
python3 webapi.py
````

App listens to port 5000 by default.
You can check if the app is running at http://localhost:5000/ , it should return :

> app is running !
### 2. Docker
You can also use docker to start the app.  

Build docker image from Dockerfile :
**This step might take a while, don't worry if the image building seems stuck on "Building wheel for gevent..."**
````
docker build -t webd2decoder .
````

Create a container from the built image :
````
docker run -p 8080:5000 webd2decoder
````
Here the app should be available at http://localhost:8080/. If you're using docker toolbox, you will need to use docker VM's IP address instead of localhost. 
## Demo
A demo is available here : https://webd2decoder.herokuapp.com
Endpoints are the following :

 - https://webd2decoder.herokuapp.com/decoder/fromclient
 - https://webd2decoder.herokuapp.com/decoder/fromserver
 - wss://webd2decoder.herokuapp.com/decoder

Use the demo app might take some time for the first call as it is hosted on a heroku free plan, which means that the app needs to be started first if it hasn't been used for a while.

A postman collection is also available here : 
https://www.getpostman.com/collections/435c144a67de71210ba5

## Protocol builder
In this project you'll also find a protocol builder which job is to convert AS3 classes to JSON. It also comes from  [LaBot](https://github.com/louisabraham/LaBot project. Some minor modifications have been done just to make the output file readable by the decoder.

Here's how to use it :

