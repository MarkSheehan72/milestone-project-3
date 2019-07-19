# Cook Book 

Deployed app: https://cook-book-milestone-project.herokuapp.com/

**The brief for this project is as follows:** 
>CREATE AN ONLINE COOKBOOK:
>
>Create a web application that allows users to store and easily access cooking recipes.
>
>Put some effort into designing a database schema based on recipes, and any other related properties and entities (e.g. views, upvotes, ingredients, recipe authors, allergens, author’s country of origin, cuisine etc…). Make sure to put some thought into the relationships between them, and use either foreign keys (in the case of a relational database) or nesting (in the case of a document store) to connect these pieces of data.
>
>Create the backend code and frontend form to allow users to add new recipes to the site (at least a basic one, if you haven’t taken the frontend course).
>
>Create the backend code to group and summarise the recipes on the site, based on their attributes such as cuisine, country of origin, allergens, ingredients, etc. and a frontend page to show this summary, and make the categories clickable to drill down into a filtered view based on that category. This frontend page can be as simple or as complex as you’d like; you can use a Python library such as matplotlib, or a JS library such as d3/dc (that you learned about if you took the frontend modules) for visualisation.
>
>Create the backend code to retrieve a list of recipes, filtered based on various criteria (e.g. allergens, cuisine, etc…) and order them based on some reasonable aspect (e.g. number of views or upvotes). Create a frontend page to display these, and to show some summary statistics around the list (e.g. number of matching recipes, number of new recipes. Optionally, add support for pagination, when the number of results is large.
>
>Create a detailed view for each recipes, that would just show all attributes for that recipe, and the full preparation instructions.
>
>Allow for editing and deleting of the recipe records, either on separate pages, or built into the list/detail pages.
>
>Optionally, you may choose to add basic user registration and authentication to the site. This can as simple as adding a username field to the recipe creation form, without a password (for this project only, this is not expected to be secure).

As such, I set about creating an app which served two main functions: finding recipes already existing on the linked database, and adding recipes to the linked database.

 

# UX 

This app has two primary parties involved –  users who want to add recipes to the site for storage purposes/future reference/to share with others, and users who want to search for recipes. The user stories for these parties are as follows:

**Users adding recipes:** 
* We want to easily add recipes to the site's database.
* We want to access these recipes in future easily, perhaps through a username.
* We want to be albe to see if the recipe has been received favourably, either through likes or view numbers.
* We want to be able to edit and delete recipes on the site.

**Users searching for recipes:**  
* We want to be able to easily access recipes based on various search criteria (perhaps the title, cuisine or an ingredient in the recipe).
* We want to be able to get a summary of search results to make it easier to decide which search result recipe best fits what we are looking for.
* We want search result recipes to be ordered by some manner of popularity (either likes or views) to see the most popular recipes which match our search.
* We want the recipe to be clear and concisely presented, in an easily understandable format.

 
# Wireframes
Please see the [*Wireframes*](https://github.com/MarkSheehan72/milestone-project-3/tree/master/wireframes) directory in the project for wireframes of various pages/aspects of the project. 

# Features 

**Existing Features** 

* Parallax: Parallax is an effect where the background content or image in this case, is moved at a different speed than the foreground content while scrolling. Here, it is used for the hero image on the home page.

* Cards: A convenient means of displaying content composed of different types of objects. Here, these are used to section off content in a visually pleasing manner.

* Carousel: Allows users to easily swap between recipe cards on the home page.

* Dropdown: Used for the "Find a recipe" part of the navbar, to allow users to select which category they would like to use to search. 

* Buttons: Used for specific actions for user interaction.

* Forms: Used as front-end methods to add and edit recipes on the site.

* Card Reveal: Used to reveal the recipe description of search results, and also the link to the recipe itself once users have decided that is the recipe they wish to view.

* Delete Modal: When users hit the delete button on the recipe page, a modal pops up asking if users are sure they wish to delete the recipe. This allows for a "second chance" in case of accidental clicks of the delete button.

**Features Left to Implement** 

* Adding the ability for users to create their own profile. As a result of this, users would have their own page with their recipes, and deleting recipes would be locked to the owner of the recipe only.


# Technologies Used 

**HTML** 

The project uses [HTML](https://en.wikipedia.org/wiki/HTML5) to structure the site. 

**CSS** 

The project uses [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) to style the site. 

**Javascript**

The project uses [Javascript](https://en.wikipedia.org/wiki/JavaScript), in particular JQuery, for interactive elements on various pages. 

**Materialize** 

The project uses [Materialize](http://archives.materializecss.com/0.100.2/) to aid in both the styling (Materialize CSS, Components and Javascript) and structure (Grid System) of the site, as well as aiding to create a responsive design (also through the Grid System). 

**FontAwesome** 

The project uses [FontAwesome](https://use.fontawesome.com/releases/v5.6.3/css/all.css) icons on various pages of the app.

**Python**

The project uses [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) for logic elements of the project.

**Flask**

The project uses the [Flask Framework](https://en.wikipedia.org/wiki/Python_(programming_language)).

**MongoDB**

The project uses [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/lp/general/try?utm_content=070819_Ad_ConFree_V1&jmp=search&utm_source=google&utm_campaign=GS_Footprint_ROW_Search_Brand-AtlasTerms_Atlas_Desktop&utm_term=mongodb%20atlas&utm_device=c&utm_network=g&utm_medium=cpc_paid_search&utm_matchtype=e&utm_cid=2037898761&utm_asagid=74623183880&utm_adid=356073073825&gclid=EAIaIQobChMIlLzMwb284wIVQ4fVCh3L7QkuEAAYASAAEgJ12_D_BwE) as a non-relational database for the project's data.

**Jinja2**

The project uses the [Jinja2](http://jinja.pocoo.org/docs/2.10/) templating language.



# Testing 

### Scenarios: 

##### User Story 1 - Users adding recipes: 

*Easily add recipes to the app's database:* 

* Go to the add recipe page (either through the navbar link or by the add recipe card on home page).

* Insert random values into the form elements and click the "Add Recipe" button at the bottom of the page.

* Users will see that they have added a recipe with a thank you message and link back to the site's home page.

* Search for the recipe using one of the categories to see if it was added.

* Can visually confirm that this works. As the site developer, I can see that this has been added to the database on MongoDB Atlas.



*Access these recipes in future easily, perhaps through a username:* 

* Add a recipe. Recall the username submitted with this recipe.

* Go to the 'search recipes by username' page either through the navbar dropdown (Find a recipe) or by going to the category page (recipes.html) via the link on the home page.

* Enter the username into the search field and click the search button.

* The recipe will appear in the search results page.

* This test can be repeated for any of the search categories.

 

*See if the recipe has been received favourably, either through likes or view numbers:* 

* With all recipe cards, the number of views the recipe has is visible either next to the word "views" or next to the views icon: `<i class="material-icons">visibility</i>`. 

* As a test, search for a recipe (use "test" as the title for this example).

* Users will see the recipe in the search results, and the number of views can be clearly seen on the recipe card.


*Edit recipes on the site:*

* Search for a recipe (use "test" as the title for this example).

* Click on the resulting recipe's card and click on the link from the card reveal.

* At the bottom of the recipe page, click the "Edit Recipe" button.

* Users will see a form like the "Add Recipe" form, but with the information from the recipe filled in.

* Edit a field(s) of the recipe and click the "Edit Recipe" button at the bottom of the page.

* Users will see that they have edited the recipe with a thank you message and link back to the site's home page.

* To ensure this recipe was edited, they can repeat the search procedure above and go to the recipe's page.

* The user will now see that the fields they changed have been changed in the recipe. As the site developer, I can see that this has been edited in the database on MongoDB Atlas.


*Delete recipes on the site:*

* Search for a recipe (use "test" as the title for this example).

* Click on the resulting recipe's card and click on the link from the card reveal.

* At the bottom of the recipe page, click the "Delete Recipe" button.

* Users will see a modal pop up, asking them if they are sure they wish to delete the recipe.

* Click the "Delete Recipe" button in the pop-up.

* Users will be redirected to the home page.

* To see if the recipe was in fact deleted, users can repeat the search process, and will find that the recipe does not appear in the search results as it has been deleted. As the site developer, I can see that this has been deleted from the database on MongoDB Atlas.
 

##### User Story 2 - Users searching for recipes: 

*Easily access recipes based on various search criteria (perhaps the title, cuisine or an ingredient in the recipe):* 

* See "User Story 1" point on "Access these recipes in future easily, perhaps through a username".  


*Get a summary of search results to make it easier to decide which search result recipe best fits what we are looking for:* 

* Search for a recipe (use "test" as the title for this example).

* Users will see the number of recipes in the database which match their search criteria at the top of the search results page.

* Users will be presented with a card for each recipe matching their search criteria. Initially, these just have the title, author, number of views and an image (if provided - if not, they are given a default image stating no image exists for the recipe). 
  On clicking the card, they will then receive a more detailed description of the recipe, as well as the link for the recipe. This graduated release of information allows users to more easily filter through recipes, only getting more information on recipes which appeal to them.  


*Search result recipes to be ordered by some manner of popularity (either likes or views) to see the most popular recipes which match our search:* 

* Search for a recipe (use "test" as the title for this example).

* Users will see that the search results are returned in descending order of the number of views they have (i.e. the recipes with the most views will appear first).


*The recipe to be clear and concisely presented, in an easily understandable format* 

* Search for a recipe (use "test" as the title for this example).

* Click on a search result and click the link from the card reveal.

* Users will see a page with all of the recipe information, arranged in a logical fashion and divided into different sections for easy following.


### Responsiveness of site: 

To aid in creating a responsive site, I used Materialize’s Grid System. Through the creating process of this app, I would check the various break points to see if the column sizes worked with the design on various device screen sizes, using Chrome Dev Tools, my own iPhone 8 and an iPad Pro (10.5).


**Navbar:** For mobile views for the project, users will see that the full desktop navbar is reduced to just the logo and a burger button, which activates the side nav containing the navbar elements.

**Sections:** The Grid System aided me greatly in arranging the sections for each page. 
As I was creating each section, and the elements in each (e.g. cards, images, text, etc.), I experimented with various column sizes for each breakpoint to get an appealing layout appropriate to the screen size it is being viewed on.

**Elements/Cards/Carousel/etc.:** As above with the sections, I experimented with various col sizes to achieve a layout of the various elements throughout the site which was visually appealing and appropriate to the screen size it would be viewed on.

**The Recipe View:** The layout of the first card on the page (containing the title, username, views, image and description) changes in the mobile view, where the image goes from the side to being quite prominent within the card.


### Debugging:

**Edit Page:** For the "Ingredients" section of this form, initially, although the page was displying all of the data correctly in the form, it would not display as I wanted in mobile view (as it was three divs, looping through three seperate lists - ingredient name, amount and allergen).
I tried various positions for the loops and tried nesting loops, but this caused more problems without solving the initial problem. With a bit of guidance from Anna Greaves on Slack, reworking the structure of the data for the Ingredients part of my [schema](https://github.com/MarkSheehan72/milestone-project-3/blob/master/schema/schema_sample.png), I was able to loop successfully, achieving the visual layout I wanted.
However, this then led to me having to rework my edit function in relation to sending the edited data to the database. With some more guidance from Anna (although how I went about debugging the problem was differnet to how she suggested), I came across the zip() function, allowing me to loop simultaneously through lists.
As such, I was able to retrieve the data from the form as three seperate lists:

```python
  ingredients_name = request.form.getlist('ingredient_name')
  ingredients_amount = request.form.getlist('ingredient_amount')
  ingredients_allergen = request.form.getlist('ingredient_allergen')
```

create a blank object, and use the zip function to loop through the three lists and the insert them into this blank object, which I then inserted into a blank array (ingredients_array), which could then be sent to the database:

```python
ingredients_array = []
    for name, amount, allergen in islice(zip(ingredients_name, ingredients_amount, ingredients_allergen), 0, None):
        temporary_object = {}
        temporary_object.update({'name': name.lower()})
        temporary_object.update({'amount': amount.lower()})
        temporary_object.update({'allergen': allergen.lower()})
        ingredients_array.append(temporary_object)
```

# Deployment 

I created a repository on GitHub, linking my project on Cloud9 to it. I committed and pushed content to this repository at various stages of the project (e.g. when I had a section fully structured and styled, or when I had coded a certain function to function in the desired manner). 

I then created the app on Heroku, created a requirements.txt file (with the project's required applications) and a Procfile (specifying the app is a Python web app).

I then pushed to Heroku. Having done this, I then specified the IP and PORT. 

I pushed to heroku whenever I pushed to Github. This was incredibly useful in testing the site, as outlined above, especially in testing it on various screen sizes.

# Credits 

### Content 

* Some of the basic functionality (although edited in various places), for example the add and delete functions, was obtained from the Data Centric Milestone Project.

* The icons not sourced from Materialize's own icon library were sourced from [FontAwesome](https://fontawesome.com/icons/arrow-circle-down?style=solid). 

* Aid for the data structure for the ingredients object in the schema, the syntax for sort(), and guidance on the edit function was obtained on Slack from Anna Greaves. 


# Media 

* All images for this project were obtained from Google Images.

# Acknowledgements 

* I received some inspiration for this project from the dashboard project which was part of the Data Centric Development Module.