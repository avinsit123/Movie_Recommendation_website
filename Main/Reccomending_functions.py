#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 18:29:08 2019

@author: r17935avinash
"""
import pandas as pd
import numpy as np
import sys
import os



def normalized(ar):
    return ar - np.average(ar)

def cosine_similarity(ar1, ar2):
    numerator = np.sum(ar1 * ar2)
    denominator = np.sqrt(np.sum(ar1 * ar1) * np.sum(ar2 * ar2))
    if denominator != 0:
        return numerator / denominator
    else:
        return 0


######################################################################################
###########Collaborative filtering user by user#######################################

def find_similar_users(user_id, curated_ratings):
    fake_ratings = np.zeros((1, 301))
    sum_weight = 0
    for i in range(3,47):
        if i != user_id:
            weight = cosine_similarity(normalized(curated_ratings[user_id]), normalized(curated_ratings[i]))
            sum_weight = sum_weight + weight
            fake_ratings = fake_ratings + weight * normalized(curated_ratings[i])
    fake_ratings = fake_ratings / sum_weight
    fake_ratings = fake_ratings[0]
    fake_ratings = fake_ratings + np.average(curated_ratings[user_id])
    return fake_ratings.argsort()[-24:][::-1]


def user_user_cf(input_ratings, movies_list):
    curated_ratings = np.zeros((48, 301))
    ratings = pd.read_csv("Main/Externals/ratings.csv")
    for i in range(len(ratings[ratings['userId'] <= 45])):
        if ratings['movieId'][i] <= 300:
            curated_ratings[ratings['userId'][i]][ratings['movieId'][i]] = ratings['rating'][i]
    for i in range(301):
        curated_ratings[47][:] = input_ratings[0][:]

    top_k = find_similar_users(47, curated_ratings)
    recommended_movies = []
    for i in range(16):
        if top_k[i] not in movies_list:
            recommended_movies.append(top_k[i])
    recommended_movies = np.array(recommended_movies)
    return recommended_movies[0:12]


############################################################################################
##################### Item - Item Collaborative filtering ###################################

def find_similar_movie(user_id, curated_ratings):
    fake_rating = np.zeros((48, 301))
    curated_ratings = curated_ratings - curated_ratings.mean(axis=1,keepdims=True)
    for i in range(301):
        sum_weight = 0
        for j in range(301):
            if i != j:
                weight = cosine_similarity(curated_ratings[:, i], curated_ratings[:, j])
                fake_rating[:, i] = fake_rating[:, i] + weight * curated_ratings[:, j]
                sum_weight = sum_weight + weight
        # print(sum_weight)
        if sum_weight != 0:
            fake_rating[:, i] = fake_rating[:, i] / sum_weight

    return fake_rating[user_id].argsort()[-24:][::-1]


def item_item_cf(input_ratings, movies_list):
    curated_ratings = np.zeros((48, 301))
    ratings = pd.read_csv("Main/Externals/ratings.csv")
    for i in range(len(ratings[ratings['userId'] <= 45])):
        if ratings['movieId'][i] <= 300:
            curated_ratings[ratings['userId'][i]][ratings['movieId'][i]] = ratings['rating'][i]
    for i in range(301):
        curated_ratings[47][:] = input_ratings[0][:]
    top_k = find_similar_movie(47, curated_ratings)
    recommended_movies = []
    for i in range(24):
        if top_k[i] not in movies_list:
            recommended_movies.append(top_k[i])
    recommended_movies = np.array(recommended_movies)
    return recommended_movies[0:12]

#################################################################################################
##################### Rank Matrix Factorization #################################################

# value of k for rank matrix factorization for has been taken 40 as it was observed to achieve a very low RMSE
# We consider 40 features for after svd
def Decompose_Matrix(user_id,curated_ratings):
    k = 40
    u,s,vh = np.linalg.svd(curated_ratings)
    fake_ratings = np.dot(u[user_id,0:k],vh[0:k,user_id])
    return fake_ratings.argsort()[-24:][::-1]

def rank_matrix_factorize(input_ratings,movies_list):
    curated_ratings = np.zeros((48, 301))
    ratings = pd.read_csv("Main/Externals/ratings.csv")
    for i in range(len(ratings[ratings['userId'] <= 46])):
        if ratings['movieId'][i] <= 300:
            curated_ratings[ratings['userId'][i]][ratings['movieId'][i]] = ratings['rating'][i]
    for i in range(301):
        curated_ratings[47][:] = input_ratings[0][:]
    top_k = find_similar_movie(47, curated_ratings)
    recommended_movies = []
    for i in range(24):
        if top_k[i] not in movies_list:
            recommended_movies.append(top_k[i])
    recommended_movies = np.array(recommended_movies)
    return recommended_movies[0:12]


