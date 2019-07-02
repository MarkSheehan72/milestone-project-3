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
    recipes.insert(
    {
        'recipe_title': request.form.get('recipe_title'),
        'recipe_description': request.form.get('recipe_description'),
        'recipe_cuisine': request.form.get('recipe_cuisine'),
        'user': 
            {'name': request.form.get('user_name'),
            'country': request.form.get('user_country')},
        'ingredients': 
            {'name': request.form.getlist('ingredient_name'),
            'amount': request.form.getlist('ingredient_amount'),
            'allergen': request.form.getlist('ingredient_allergen')},
        'method': request.form.get('recipe_method'),
        'image': request.form.get('image')
    })
    return redirect(url_for('thanks'))


@app.route('/thanks')
def thanks():
    return render_template("thanks.html")


@app.route('/get_recipes') 
def get_recipes():
    recipes=mongo.db.recipes.find()
    categories=mongo.db.categories.find()
    return render_template("recipes.html", recipes=recipes, categories=categories)


@app.route('/search_category/<category_id>')
def search_category(category_id):
    the_category = mongo.db.categories.find({'_id': ObjectId(category_id)})
    all_categories = mongo.db.categories.find()
    recipes=mongo.db.recipes.find()
    return render_template("search_category.html", recipes=recipes, category=the_category, categories=all_categories)
    
    
@app.route('/search_recipes/<category_id>', methods=['POST'])
def search_recipes(category_id):
    the_category = mongo.db.categories.find({'_id': ObjectId(category_id)})
    all_categories = mongo.db.categories.find()
    recipes=mongo.db.recipes.find()
    search = request.form.get('search_recipes')
    title_search = mongo.db.recipes.find({"recipe_title": {"$regex":search}})
    cuisine_search = mongo.db.recipes.find({"recipe_cuisine": {"$regex":search}})
    ingredients_search = mongo.db.recipes.find({"ingredients": {"$regex":search}})
    return render_template("search_recipes.html", recipes=recipes, category=the_category, categories=all_categories, title_search=title_search, cuisine_search=cuisine_search, ingredients_search=ingredients_search)


@app.route('/search_username')
def search_username():
    recipes=mongo.db.recipes.find()
    return render_template("search_username.html", recipes=recipes)


@app.route('/search_recipes_by_username', methods=['POST'])
def search_recipes_by_username():
    recipes=mongo.db.recipes.find()
    search = request.form.get('search_recipes_by_username')
    username_search = mongo.db.recipes.find({"user.name": {"$regex":search}})
    return render_template("search_recipes_by_username.html", recipes=recipes, username_search=username_search)

    

    
# @app.route('/cuisine', methods=['POST'])
# def cuisine():
#     return render_template("cuisine.html", recipes=mongo.db.recipes.find(), cuisine=mongo.db.recipes.cuisine.find(), categories=mongo.db.categories.find())


# @app.route('/cuisine_recipes/<cuisine_choice>', methods=['POST'])
# def cuisine_recipes(cuisine_choice):
#     the_cuisine = mongo.db.recipes.find({'cuisine': ObjectId(cuisine_choice)})
#     return render_template("cuisine_recipes.html", cuisine=the_cuisine, recipes=mongo.db.recipes.find(), categories=mongo.db.categories.find())

   
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
    port=int(os.environ.get('PORT')), 
    debug=True)  