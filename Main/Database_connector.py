from pymongo import MongoClient
from Reccomending_functions import user_user_cf
import numpy as np

class Details:
    def __init__(self,Name, Overview, img_link,source_link,movieid):
        self.Name = Name
        self.Overview = Overview
        self.img_link = img_link
        self.source_link = source_link
        self.movieid = movieid

def fetch_from_database(movie_list):
    client = MongoClient("mongodb://avi123:123itrocks@movierecommend-shard-00-00-tgqzh.mongodb.net:27017,movierecommend-shard-00-01-tgqzh.mongodb.net:27017,movierecommend-shard-00-02-tgqzh.mongodb.net:27017/test?ssl=true&replicaSet=MovieRecommend-shard-0&authSource=admin&retryWrites=true")
    db = client.movies.movie_details
    movie_details_list = []
    
    for pos,i in enumerate(movie_list):
        cursor=db.find()[i-1]
        mo_detail = Details(cursor["Name"],cursor["Overview"],cursor["Image Link"],cursor["Profile Link"],"movie"+str(pos+1))
        movie_details_list.append(mo_detail)
    return movie_details_list


if __name__=="__main__":
    heee = 0