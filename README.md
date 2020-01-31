# Docker and Kubernetes: The Complete Guide

I'm following the Udemy course [Docker and Kubernet: The Complete Guide](https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/) and keep track of my progress here.
The end-goal of the course is to build a simple dockerized Node.js web application that runs on AWS including an CI/CD pipeline running on Github and Travis CI.
Instead of Node.js I will be using Flask to create the web server backend.

The code in this project is organized as follows:

````
- 0.web_simple
- 1.web_visit_counter
````
 

## Web Simple

Section 4 of the course covers building a single-container docker application that simply prints 'Hi there'.</br>
Run the below commands to boot up the application.

```
cd 0.web_simple
docker build -t <image_name> .
docker run -p 8080:5000 -e FLASK_APP=index.py <image_name>
```

You can then browse to <http://127.0.0.1:8080/> where 'Hi there' is printed.

## Web Visit Counter

Section 5 covers building a multi-container docker application that counts the number of times a web app was visited.
The application consists of a Python Flask app container as a web-server and a Redis container for storing the counter.
Run the below commands to boot up the application.

```
cd 1.web_visit_counter/
docker-compose up -d
```

You can then browse to <http://127.0.0.1:8080/> and refresh the page to update the visit counter.
To stop the application execute
```
docker-compose down
```

## Nginx with Flask integration

Section 6 introduces volumes which allows for quick development because your code changes are immediately visible 
in the running Docker container. 
Furthermore, we introduce a production style setup where we integrate Flask with Nginx.
 
```
cd 2.nginx_flask_integration/
docker-compose up -d
```

You can then browse to <http://127.0.0.1:8080/> where it shows the message from the text file

```
2.nginx_flask_integration/services/web/message.txt
```

By editing this file, you can control the text that is displayed on your web browser.</br>
Simply refresh the browser to see your new message.

To stop the application execute
```
docker-compose down
```