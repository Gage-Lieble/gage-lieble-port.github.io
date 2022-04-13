Gage Lieble's Personal Portfolio

This site will allow possible employers and online users to see my skill sets, past cases, and a way to get ahold of me. My portfolio
was built in HTML and CSS using Bootstrap and Flask. As of now (VERSION 1) my nav bar needs some work such as closing when the user scrolls.
My site is also only built for mobile screens so my nexct goal in version 2 is to create a responsive design.


View the wesbite at: www.gagelieble.com


HOW TO RUN LOCALLY
DJANGO: <---- Main Files for gagelieble.com
You must be in the file directory that contains 'manage.py' inorder to run this project locally. The 'portfolio_proj', 'portfolio_app', 'templates', and static files must also be present in this directory. After installing djanog on your machine you can enter the following into your terminal.
-WINDOWS: py -m manage runserver
-MAC: manage.py runserver
-Shift click on 'http://127.0.0.1:8000/' in your terminal
This will open a tab in your default broswer with this project!

FLASK: <---- Version 1 of gagelieble.com - No longer the Main Files
In order to view the site you must have the app.py file in the directory. inside the directory you must also have a 'templates' folder and a 'static' folder. Place the HTML files in the template folder. Inside the static folder, place the 'Images' folder and the 'style' folder. the 'style' folder must include style.css and bootstrap.css.
- In the terminal type 
- WINDOWS: "$env:FLASK_APP = "app.py"
- MAC: "export FLASK_APP=app.py"
- next you must type
- WINDOWS: "py -m flask run"
- MAC: "flask run"
Lastly once the server is running, Shift click the Local Host Server 5000
and it will open in the deafault browser


