import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo 
from bson.objectid import ObjectId 
from itertools import islice
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-chhcw.mongodb.net/cook_book?retryWrites=true&w=majority'

mongo = PyMongo(app)



#////////////////////////////////////////////////# Home Page
@app.route('/')
@app.route('/index')
def index():
    recipes=mongo.db.recipes.find().sort("views", -1)
    return render_template("index.html", recipes=recipes)


#////////////////////////////////////////////////# Add recipe page
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html")


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
            [
                {
                        'name': request.form.get('ingredient_name_1').lower(),
                        'amount': request.form.get('ingredient_amount_1').lower(),
                        'allergen': request.form.get('ingredient_allergen_1').lower()
                },
                {
                        'name': request.form.get('ingredient_name_2').lower(),
                        'amount': request.form.get('ingredient_amount_2').lower(),
                        'allergen': request.form.get('ingredient_allergen_2').lower()
                },
                {
                        'name': request.form.get('ingredient_name_3').lower(),
                        'amount': request.form.get('ingredient_amount_3').lower(),
                        'allergen': request.form.get('ingredient_allergen_3').lower()
                },
                {
                        'name': request.form.get('ingredient_name_4').lower(),
                        'amount': request.form.get('ingredient_amount_4').lower(),
                        'allergen': request.form.get('ingredient_allergen_4').lower()
                },
                {
                        'name': request.form.get('ingredient_name_5').lower(),
                        'amount': request.form.get('ingredient_amount_5').lower(),
                        'allergen': request.form.get('ingredient_allergen_5').lower()
                },
                {
                        'name': request.form.get('ingredient_name_6').lower(),
                        'amount': request.form.get('ingredient_amount_6').lower(),
                        'allergen': request.form.get('ingredient_allergen_6').lower()
                },
                {
                        'name': request.form.get('ingredient_name_7').lower(),
                        'amount': request.form.get('ingredient_amount_7').lower(),
                        'allergen': request.form.get('ingredient_allergen_7').lower()
                },
                {
                        'name': request.form.get('ingredient_name_8').lower(),
                        'amount': request.form.get('ingredient_amount_8').lower(),
                        'allergen': request.form.get('ingredient_allergen_8').lower()
                },
                {
                        'name': request.form.get('ingredient_name_9').lower(),
                        'amount': request.form.get('ingredient_amount_9').lower(),
                        'allergen': request.form.get('ingredient_allergen_9').lower()
                },
                {
                        'name': request.form.get('ingredient_name_10').lower(),
                        'amount': request.form.get('ingredient_amount_10').lower(),
                        'allergen': request.form.get('ingredient_allergen_10').lower()
                }
            ],
        'method': request.form.getlist('recipe_method'),
        'image': request.form.get('image')
    })
    return redirect(url_for('thanks'))


#////////////////////////////////////////////////Thank you page - users are sent to this page after they submit a recipe.
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
    username_search = mongo.db.recipes.find({"user.name": {"$regex":search}}).sort("views", -1)
    count = username_search.count()
    return render_template("search_recipes_by_username.html", recipes=recipes, username_search=username_search, count=count)
    
    
@app.route('/search_cuisine')
def search_cuisine():
    recipes=mongo.db.recipes.find()
    return render_template("search_cuisine.html", recipes=recipes)


@app.route('/search_recipes_by_cuisine', methods=['POST'])
def search_recipes_by_cuisine():
    recipes=mongo.db.recipes.find()
    search = request.form.get('search_recipes_by_cuisine').lower()
    cuisine_search = mongo.db.recipes.find({"recipe_cuisine": {"$regex":search}}).sort("views", -1)
    count = cuisine_search.count()
    return render_template("search_recipes_by_cuisine.html", recipes=recipes, cuisine_search=cuisine_search, count=count)


@app.route('/search_ingredient')
def search_ingredient():
    recipes=mongo.db.recipes.find()
    return render_template("search_ingredient.html", recipes=recipes)


@app.route('/search_recipes_by_ingredient', methods=['POST'])
def search_recipes_by_ingredient():
    recipes=mongo.db.recipes.find()
    search = request.form.get('search_recipes_by_ingredient').lower()
    ingredient_search = mongo.db.recipes.find({"ingredients.name": {"$regex":search}}).sort("views", -1)
    count = ingredient_search.count()
    return render_template("search_recipes_by_ingredient.html", recipes=recipes, ingredient_search=ingredient_search, count=count)


@app.route('/search_recipe_title')
def search_recipe_title():
    recipes=mongo.db.recipes.find()
    return render_template("search_recipe_title.html", recipes=recipes)


@app.route('/search_recipes_by_recipe_title', methods=['POST'])
def search_recipes_by_recipe_title():
    recipes=mongo.db.recipes.find()
    search = request.form.get('search_recipes_by_recipe_title').lower()
    recipe_title_search = mongo.db.recipes.find({"recipe_title": {"$regex":search}}).sort("views", -1)
    count = recipe_title_search.count()
    return render_template("search_recipes_by_recipe_title.html", recipes=recipes, recipe_title_search=recipe_title_search, count=count)


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
    
@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    
    #Get an array of each ingredient element: 
    ingredients_name = request.form.getlist('ingredient_name')
    ingredients_amount = request.form.getlist('ingredient_amount')
    ingredients_allergen = request.form.getlist('ingredient_allergen')
    
    #Loops through each array and creates an object containing each ingredient's name, amount and allergen info.
    #Then appends this collection of objects to an array (ingredients_array):
    ingredients_array = []
    for name, amount, allergen in islice(zip(ingredients_name, ingredients_amount, ingredients_allergen), 0, None):
        temporary_object = {}
        temporary_object.update({'name': name.lower()})
        temporary_object.update({'amount': amount.lower()})
        temporary_object.update({'allergen': allergen.lower()})
        ingredients_array.append(temporary_object)
    
    #Updates the recipe fields:
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_title': request.form.get('recipe_title').lower(),
        'recipe_description': request.form.get('recipe_description').lower(),
        'recipe_cuisine': request.form.get('recipe_cuisine').lower(),
        'user': 
            {'name': request.form.get('user_name').lower(),
            'country': request.form.get('user_country').lower()},
        'ingredients': ingredients_array,
        'method': request.form.getlist('recipe_method'),
        'image': request.form.get('image')
    })
    return redirect(url_for('thanks_update'))
    

#////////////////////////////////////////////////Thank you (update) page - users are sent to this page after they edit a recipe.
#////////////////////////////////////////////////This gives users assured feedback that their recipe has been edited.
@app.route('/thanks_update')
def thanks_update():
    return render_template("thanks_update.html")


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