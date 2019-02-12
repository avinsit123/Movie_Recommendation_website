from flask import Flask,request,render_template
import numpy as np
from Reccomending_functions import item_item_cf,user_user_cf,rank_matrix_factorize
from Database_connector import fetch_from_database
import random
#ML Packages
asd = []
app = Flask(__name__)
@app.route('/')
def index():
    global asd
    randindex = [x for x in range(1,301)]
    random.shuffle(randindex)
    movies_list = randindex[0:12]
    asd = movies_list
    display_list = fetch_from_database(movies_list)
    return render_template("Display_movies.html",display_list=display_list)

@app.route('/recommendations',methods=['POST','GET'])
def recommend():
    
    if request.method != 'POST':
        return "Bye-Bye"
    movies_list = asd
    user_ratings = np.zeros((1,301))
    for i in range(len(movies_list)):
        user_ratings[0][movies_list[i]]=request.form['movie'+str(i+1)]
    if request.form['recco_method']=="uucf":
        recommendend_movies_list = user_user_cf(user_ratings,movies_list)
    elif request.form['recco_method']=="iicf":
        recommendend_movies_list = item_item_cf(user_ratings, movies_list)
    elif request.form['recco_method']=="rf":
        recommendend_movies_list = rank_matrix_factorize(user_ratings,movies_list)
    print(user_ratings)
    recommendend_movies_list = list(recommendend_movies_list)
    sasa =[]
    for i in recommendend_movies_list:
        sasa.append(int(i))
    movie_details = fetch_from_database(sasa)
    return render_template("Display Recommendations.html",movie_details=movie_details)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
