# Precog_Intern_Assignment

## Running the Application locally
In order to run the application locally you need to have Docker installed on your local system.Type
```terminal
docker --version
```
If you get Docker version 18.09.1, build 4c52b90 ,then Docker is installed otherwise go to <a href="https://docs.docker.com/docker-for-mac/install/">this link</a> to install Docker Desktop
After Downloading,copy the below given instructions to run the application locally.
```terminal 
$git clone https://github.com/avinsit123/Precog_Intern_Assignment.git
$cd Precog_Intern_Assignment
$docker build -t Movie_recco .
$docker run -d -p 5000:5000 Movie_recco
```
Open http://0.0.0.0:5000/ to start the web application and start using it.

## Approach Followed
I have intended to examine Movie recommender systems through different methods mainly User-User Collaborative Filtering,Item-Item Collaborative Filtering and Rank Matrix factorization 

## Dependencies
<ul>
<li>Numpy,Pandas to help with all the Numerical Calculations and datasets manipulations.</li>
<li>Pymongo to connect with online Mongo Atlas Cluster and retreive and add information to it.</li>
<li>WhiteNoise to help web app to serve its own static files and make external deployment on Heroku easy.</li>
<li>Gunicorn to help with web app deployment and setting up an external web server on Heroku.</li>
</ul>
## Directory Structure
```terminal
.
├── Dockerfile
├── Main
│   ├── Database_connector.py
│   ├── Externals
│   │   └── ratings.csv
│   ├── Reccomending_functions.py
│   ├── __pycache__
│   │   ├── Database_connector.cpython-35.pyc
│   │   ├── Database_connector.cpython-36.pyc
│   │   ├── Reccomending_functions.cpython-35.pyc
│   │   └── Reccomending_functions.cpython-36.pyc
│   ├── bakend.py
│   ├── static
│   │   ├── graeat.js
│   │   └── movie_beauty.css
│   ├── templates
│   │   ├── Display\ Recommendations.html
│   │   └── Display_movies.html
│   └── wsgi.py
├── Procfile
└── requirements.txt

```
## Codebase
<ol>
  <li> <h4>Procfile</h4> Helps heroku server in setting up a web dyno and running the application on a web server</li>
  <li> <h4> Requirements.txt</h4> Contains list of all Dependencies needed to run the application</li>
  <li> <h4> Static </h4> Contains CSS and JS files needed to render style on the webpage</li>
  <li> <h4> Templates </h4> Contains HTML files </li>
  <li> <h4> bakend.py </h4> The Main Backend python file which helps in routing amongst various webpages.I have used a Flask Backend. </li>
  <li> <h4>Externals</h4>  Contains Ratings.csv which has all the ratings of the dummy users and their ratings.We have taken the first 46 users and first 300 movies.</li>
  <li> <h4>Database_connector.py</h4> This script helps in fetching data from MongoDB database given a list of movies and packaging it in the form of a class and returning this class.</li>
  <li> <h4>Recommending functions</h4> Contains all the functions for performing rank-matrix factorization,user-user and item-item collaborative filtering </li>
  <li><h4>Dockerfile</h4> File to help Docker hub build a Docker Image</li>
</ol>

