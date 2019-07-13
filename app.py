import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo 
from bson.objectid import ObjectId 

app = Flask(__name__) 

app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-chhcw.mongodb.net/cook_book?retryWrites=true&w=majority'

mongo = PyMongo(app)


#////////////////////////////////////////////////# Home Page
@app.route('/')
@app.route('/index')
def index():
    recipes=mongo.db.recipes.find()
    return render_template("index.html", recipes=recipes)


#////////////////////////////////////////////////# Add recipe page
@app.route('/add_recipe')
def add_recipe():
    recipes=mongo.db.recipes.find()
    categories=mongo.db.categories.find()
    return render_template("addrecipe.html", recipes=recipes, categories=categories)


#////////////////////////////////////////////////# Function for inserting a recipe as a document in MongoDB. Once a user has added a recipe,
#////////////////////////////////////////////////# they will be redirecte to thanks.html, which is just a confirmation for the viewer that they
#////////////////////////////////////////////////# have successfully added a recipe to the app.
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert(
    {
        'recipe_title': request.form.get('recipe_title').lower(),
        'recipe_description': request.form.get('recipe_description').lower(),
        'recipe_cuisine': request.form.get('recipe_cuisine').lower(),
        'user': 
            {'name': request.form.get('user_name').lower(),
            'country': request.form.get('user_country').lower()},
        'ingredients': 
            {'name': request.form.getlist('ingredient_name'),
            'amount': request.form.getlist('ingredient_amount'),
            'allergen': request.form.getlist('ingredient_allergen')},
        'method': request.form.getlist('recipe_method'),
        'image': request.form.get('image')
    })
    return redirect(url_for('thanks'))


#////////////////////////////////////////////////Thanks you page - users are sent to this page after they submit a recipe.
#////////////////////////////////////////////////This gives users assured feedback that their recipe has been added.
@app.route('/thanks')
def thanks():
    return render_template("thanks.html")


#////////////////////////////////////////////////Page linked from pressing the "Find Recipe" button on index.html.
#////////////////////////////////////////////////Also linked from the "Find Recipes" option in the mobile side nav.
@app.route('/get_recipes') 
def get_recipes():
    recipes=mongo.db.recipes.find()
    categories=mongo.db.categories.find()
    return render_template("recipes.html", recipes=recipes, categories=categories)


# @app.route('/search_category/<category_id>')
# def search_category(category_id):
#     the_category = mongo.db.categories.find({'_id': ObjectId(category_id)})
#     all_categories = mongo.db.categories.find()
#     recipes=mongo.db.recipes.find()
#     return render_template("search_category.html", recipes=recipes, category=the_category, categories=all_categories)
    
    
# @app.route('/search_recipes/<category_id>', methods=['POST'])
# def search_recipes(category_id):
#     the_category = mongo.db.categories.find({'_id': ObjectId(category_id)})
#     all_categories = mongo.db.categories.find()
#     recipes=mongo.db.recipes.find()
#     search = request.form.get('search_recipes')
#     title_search = mongo.db.recipes.find({"recipe_title": {"$regex":search}})
#     cuisine_search = mongo.db.recipes.find({"recipe_cuisine": {"$regex":search}})
#     ingredients_search = mongo.db.recipes.find({"ingredients.name": {"$regex":search}})
#     return render_template("search_recipes.html", recipes=recipes, category=the_category, categories=all_categories, title_search=title_search, cuisine_search=cuisine_search, ingredients_search=ingredients_search)


#////////////////////////////////////////////////Search Views:
#////////////////////////////////////////////////The following views provide users with a search page for their desired search category, 
#////////////////////////////////////////////////and the search results from those pages.

@app.route('/search_username')
def search_username():
    recipes=mongo.db.recipes.find()
    return render_template("search_username.html", recipes=recipes)


@app.route('/search_recipes_by_username', methods=['POST'])
def search_recipes_by_username():
    recipes=mongo.db.recipes.find()
    search = request.form.get('search_recipes_by_username').lower()
    username_search = mongo.db.recipes.find({"user.name": {"$regex":search}})
    return render_template("search_recipes_by_username.html", recipes=recipes, username_search=username_search)
    
    
@app.route('/search_cuisine')
def search_cuisine():
    recipes=mongo.db.recipes.find()
    return render_template("search_cuisine.html", recipes=recipes)


@app.route('/search_recipes_by_cuisine', methods=['POST'])
def search_recipes_by_cuisine():
    recipes=mongo.db.recipes.find()
    search = request.form.get('search_recipes_by_cuisine').lower()
    cuisine_search = mongo.db.recipes.find({"recipe_cuisine": {"$regex":search}})
    return render_template("search_recipes_by_cuisine.html", recipes=recipes, cuisine_search=cuisine_search)


@app.route('/search_ingredient')
def search_ingredient():
    recipes=mongo.db.recipes.find()
    return render_template("search_ingredient.html", recipes=recipes)


@app.route('/search_recipes_by_ingredient', methods=['POST'])
def search_recipes_by_ingredient():
    recipes=mongo.db.recipes.find()
    search = request.form.get('search_recipes_by_ingredient').lower()
    ingredient_search = mongo.db.recipes.find({"ingredients.name": {"$regex":search}})
    return render_template("search_recipes_by_ingredient.html", recipes=recipes, ingredient_search=ingredient_search)


@app.route('/search_recipe_title')
def search_recipe_title():
    recipes=mongo.db.recipes.find()
    return render_template("search_recipe_title.html", recipes=recipes)


@app.route('/search_recipes_by_recipe_title', methods=['POST'])
def search_recipes_by_recipe_title():
    recipes=mongo.db.recipes.find()
    search = request.form.get('search_recipes_by_recipe_title').lower()
    recipe_title_search = mongo.db.recipes.find({"recipe_title": {"$regex":search}})
    return render_template("search_recipes_by_recipe_title.html", recipes=recipes, recipe_title_search=recipe_title_search)


#////////////////////////////////////////////////The recipe view:
#////////////////////////////////////////////////The page for the particular recipe picked by the user.
@app.route('/the_recipe/<recipe_id>')
def the_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find({'_id': ObjectId(recipe_id)})
    mongo.db.recipes.update({'_id': ObjectId(recipe_id)}, { '$inc': { 'views': 1 } })
    return render_template("the_recipe.html", recipe=the_recipe)


#////////////////////////////////////////////////Edit recipe view:
#////////////////////////////////////////////////Where users can edit the details of a selected recipe.
@app.route('/edit_recipe/<recipe_id>') 
def edit_recipe(recipe_id): 
    the_recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}) 
    return render_template('edit_recipe.html', recipe=the_recipe) 


#////////////////////////////////////////////////Delete recipe view:
#////////////////////////////////////////////////Where users can delete a selected recipe.
@app.route('/delete_recipe/<recipe_id>') 
def delete_recipe(recipe_id): 
    recipes = mongo.db.recipes
    recipes.remove({'_id': ObjectId(recipe_id)}) 
    return redirect(url_for('index')) 

   
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
    port=int(os.environ.get('PORT')), 
    debug=True)  