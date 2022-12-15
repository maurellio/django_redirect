# django_redirect

<h3>What is about?</h3>
It's a small web app that provides link shortener service.

<h3>Functions</h3>
+ Authorization and authentication
<br>+ Profile with shorted links
<br>+ Create links
<br>+ Delete links
<br>+ Get the information about ammount of clicks per link
<br>+ DRF API for create / get / update links
<br>+ Slugger based API documentation

<h3>How to run</h3>
1. Change the host in file "django_redirect/core/redirection/models.py"
<br>2. Create docker container "docker build --tag python-django . "
<br>3. Run docker container "docker run --publish 8080:8080 python-django"
<br> The server will starts on 8080 port. If it's already taken, you should as well change the port in Dockerfile
