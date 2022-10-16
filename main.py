
from flask import Flask,jsonify,request
import csv
all_movies=[]
with open ('movies.csv',encoding='utf-8') as f:
    reader=csv.reader(f)
    data =list(reader)
    all_movies=data[1:]
liked_movies=[]
notliked_movies=[]
notwatched=[]
app=Flask(__name__)
@app.route('/get-movie')
def get_movie():
    return jsonify({
        'data':all_movies[0],
        'status':'success'
    })
@app.route('/liked-movies',methods=['POST'])
def liked_movie():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        'status':'success'
    }),201
@app.route('/unliked-movies',methods=['POST'])
def unliked_movie():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    notliked_movies.append(movie)
    return jsonify({
        'status':'success'
    }),201
@app.route('/didnotwatch-movies',methods=['POST'])
def notwatched_movie():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    notwatched.append(movie)
    return jsonify({
        'status':'success'
    }),201    
if __name__=='__main__':
    app.run()
