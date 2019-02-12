# Precog_Intern_Assignment

## Running the Application locally

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

## 
