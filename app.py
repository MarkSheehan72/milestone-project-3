import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo 
from bson.objectid import ObjectId 

app = Flask(__name__) 

app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-chhcw.mongodb.net/cook_book?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", recipes=mongo.db.recipes.find(), categories=mongo.db.categories.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('index'))

@app.route('/get_recipes') 
def get_recipes():  
    return render_template("recipes.html", recipes=mongo.db.recipes.find(), categories=mongo.db.categories.find())

    
@app.route('/cuisine', methods=['POST'])
def cuisine():
    return render_template("cuisine.html", recipes=mongo.db.recipes.find(), cuisine=mongo.db.recipes.cuisine.find(), categories=mongo.db.categories.find())

@app.route('/cuisine_recipes/<cuisine_choice>', methods=['POST'])
def cuisine_recipes(cuisine_choice):
    the_cuisine = mongo.db.recipes.find({'cuisine': ObjectId(cuisine_choice)})
    return render_template("cuisine_recipes.html", cuisine=the_cuisine, recipes=mongo.db.recipes.find(), categories=mongo.db.categories.find())
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
    port=int(os.environ.get('PORT')), 
    debug=True)  