import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = "mongodb://root:r00tUser@myfirstcluster-shard-00-00.w52aw.mongodb.net:27017,myfirstcluster-shard-00-01.w52aw.mongodb.net:27017,myfirstcluster-shard-00-02.w52aw.mongodb.net:27017/cook_book?ssl=true&replicaSet=atlas-n79620-shard-0&authSource=admin&retryWrites=true&w=majority"

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)