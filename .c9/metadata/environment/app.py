{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":129,"column":0},"end":{"row":129,"column":63},"action":"insert","lines":["@app.route('/search_recipes_by_recipe_title', methods=['POST'])"],"id":512}],[{"start":{"row":129,"column":13},"end":{"row":129,"column":43},"action":"remove","lines":["search_recipes_by_recipe_title"],"id":513},{"start":{"row":129,"column":13},"end":{"row":129,"column":14},"action":"insert","lines":["v"]},{"start":{"row":129,"column":14},"end":{"row":129,"column":15},"action":"insert","lines":["i"]},{"start":{"row":129,"column":15},"end":{"row":129,"column":16},"action":"insert","lines":["e"]},{"start":{"row":129,"column":16},"end":{"row":129,"column":17},"action":"insert","lines":["w"]},{"start":{"row":129,"column":17},"end":{"row":129,"column":18},"action":"insert","lines":["u"]},{"start":{"row":129,"column":18},"end":{"row":129,"column":19},"action":"insert","lines":["p"]}],[{"start":{"row":129,"column":19},"end":{"row":129,"column":20},"action":"insert","lines":["/"],"id":514}],[{"start":{"row":129,"column":20},"end":{"row":129,"column":21},"action":"insert","lines":["<"],"id":515},{"start":{"row":129,"column":21},"end":{"row":129,"column":22},"action":"insert","lines":[">"]}],[{"start":{"row":129,"column":21},"end":{"row":129,"column":22},"action":"insert","lines":["r"],"id":516},{"start":{"row":129,"column":22},"end":{"row":129,"column":23},"action":"insert","lines":["e"]},{"start":{"row":129,"column":23},"end":{"row":129,"column":24},"action":"insert","lines":["c"]},{"start":{"row":129,"column":24},"end":{"row":129,"column":25},"action":"insert","lines":["i"]},{"start":{"row":129,"column":25},"end":{"row":129,"column":26},"action":"insert","lines":["p"]},{"start":{"row":129,"column":26},"end":{"row":129,"column":27},"action":"insert","lines":["e"]}],[{"start":{"row":129,"column":27},"end":{"row":129,"column":28},"action":"insert","lines":["_"],"id":517},{"start":{"row":129,"column":28},"end":{"row":129,"column":29},"action":"insert","lines":["i"]},{"start":{"row":129,"column":29},"end":{"row":129,"column":30},"action":"insert","lines":["d"]}],[{"start":{"row":134,"column":46},"end":{"row":135,"column":0},"action":"insert","lines":["",""],"id":518},{"start":{"row":135,"column":0},"end":{"row":135,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":135,"column":12},"end":{"row":135,"column":16},"action":"remove","lines":["    "],"id":519},{"start":{"row":135,"column":8},"end":{"row":135,"column":12},"action":"remove","lines":["    "]},{"start":{"row":135,"column":4},"end":{"row":135,"column":8},"action":"remove","lines":["    "]}],[{"start":{"row":135,"column":4},"end":{"row":135,"column":64},"action":"insert","lines":["return render_template(\"the_recipe.html\", recipe=the_recipe)"],"id":520}],[{"start":{"row":131,"column":4},"end":{"row":132,"column":0},"action":"insert","lines":["",""],"id":521},{"start":{"row":132,"column":0},"end":{"row":132,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":131,"column":4},"end":{"row":131,"column":68},"action":"insert","lines":["the_recipe = mongo.db.recipes.find({'_id': ObjectId(recipe_id)})"],"id":522}],[{"start":{"row":129,"column":32},"end":{"row":129,"column":50},"action":"remove","lines":[", methods=['POST']"],"id":523}],[{"start":{"row":132,"column":4},"end":{"row":133,"column":0},"action":"insert","lines":["",""],"id":524},{"start":{"row":133,"column":0},"end":{"row":133,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":132,"column":4},"end":{"row":132,"column":5},"action":"insert","lines":["f"],"id":525},{"start":{"row":132,"column":5},"end":{"row":132,"column":6},"action":"insert","lines":["o"]},{"start":{"row":132,"column":6},"end":{"row":132,"column":7},"action":"insert","lines":["r"]}],[{"start":{"row":132,"column":7},"end":{"row":132,"column":8},"action":"insert","lines":[" "],"id":526},{"start":{"row":132,"column":8},"end":{"row":132,"column":9},"action":"insert","lines":["r"]},{"start":{"row":132,"column":9},"end":{"row":132,"column":10},"action":"insert","lines":["e"]},{"start":{"row":132,"column":10},"end":{"row":132,"column":11},"action":"insert","lines":["c"]},{"start":{"row":132,"column":11},"end":{"row":132,"column":12},"action":"insert","lines":["i"]},{"start":{"row":132,"column":12},"end":{"row":132,"column":13},"action":"insert","lines":["p"]},{"start":{"row":132,"column":13},"end":{"row":132,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":132,"column":14},"end":{"row":132,"column":15},"action":"insert","lines":[" "],"id":527},{"start":{"row":132,"column":15},"end":{"row":132,"column":16},"action":"insert","lines":["i"]},{"start":{"row":132,"column":16},"end":{"row":132,"column":17},"action":"insert","lines":["n"]}],[{"start":{"row":132,"column":17},"end":{"row":132,"column":18},"action":"insert","lines":[" "],"id":528},{"start":{"row":132,"column":18},"end":{"row":132,"column":19},"action":"insert","lines":["t"]},{"start":{"row":132,"column":19},"end":{"row":132,"column":20},"action":"insert","lines":["h"]},{"start":{"row":132,"column":20},"end":{"row":132,"column":21},"action":"insert","lines":["e"]},{"start":{"row":132,"column":21},"end":{"row":132,"column":22},"action":"insert","lines":["_"]},{"start":{"row":132,"column":22},"end":{"row":132,"column":23},"action":"insert","lines":["r"]},{"start":{"row":132,"column":23},"end":{"row":132,"column":24},"action":"insert","lines":["e"]}],[{"start":{"row":132,"column":24},"end":{"row":132,"column":25},"action":"insert","lines":["c"],"id":529},{"start":{"row":132,"column":25},"end":{"row":132,"column":26},"action":"insert","lines":["i"]},{"start":{"row":132,"column":26},"end":{"row":132,"column":27},"action":"insert","lines":["p"]},{"start":{"row":132,"column":27},"end":{"row":132,"column":28},"action":"insert","lines":["e"]},{"start":{"row":132,"column":28},"end":{"row":132,"column":29},"action":"insert","lines":[":"]}],[{"start":{"row":132,"column":29},"end":{"row":133,"column":0},"action":"insert","lines":["",""],"id":530},{"start":{"row":133,"column":0},"end":{"row":133,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":134,"column":4},"end":{"row":134,"column":8},"action":"insert","lines":["    "],"id":533}],[{"start":{"row":133,"column":6},"end":{"row":133,"column":7},"action":"remove","lines":[" "],"id":534},{"start":{"row":133,"column":5},"end":{"row":133,"column":6},"action":"remove","lines":[" "]},{"start":{"row":133,"column":4},"end":{"row":133,"column":5},"action":"remove","lines":[" "]},{"start":{"row":133,"column":0},"end":{"row":133,"column":4},"action":"remove","lines":["    "]},{"start":{"row":132,"column":29},"end":{"row":133,"column":1},"action":"remove","lines":[""," "]}],[{"start":{"row":135,"column":3},"end":{"row":135,"column":4},"action":"insert","lines":[" "],"id":535}],[{"start":{"row":135,"column":4},"end":{"row":135,"column":8},"action":"insert","lines":["    "],"id":536}],[{"start":{"row":135,"column":8},"end":{"row":135,"column":9},"action":"remove","lines":[" "],"id":537}],[{"start":{"row":132,"column":0},"end":{"row":132,"column":29},"action":"remove","lines":["    for recipe in the_recipe:"],"id":538},{"start":{"row":131,"column":68},"end":{"row":132,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":132,"column":7},"end":{"row":135,"column":46},"action":"remove","lines":[" count = mongo.db.recipe.find_one(","        {'_id': ObjectId(recipe_id)}, {\"views\"})","        mongo.db.recipe.update_one({'_id': ObjectId(recipe_id)}, {","                \"$set\": {\"views\": count + 1}})"],"id":539},{"start":{"row":132,"column":6},"end":{"row":132,"column":7},"action":"remove","lines":[" "]},{"start":{"row":132,"column":5},"end":{"row":132,"column":6},"action":"remove","lines":[" "]},{"start":{"row":132,"column":4},"end":{"row":132,"column":5},"action":"remove","lines":[" "]}],[{"start":{"row":132,"column":4},"end":{"row":132,"column":5},"action":"insert","lines":["v"],"id":540},{"start":{"row":132,"column":5},"end":{"row":132,"column":6},"action":"insert","lines":["i"]},{"start":{"row":132,"column":6},"end":{"row":132,"column":7},"action":"insert","lines":["o"]}],[{"start":{"row":132,"column":6},"end":{"row":132,"column":7},"action":"remove","lines":["o"],"id":541},{"start":{"row":132,"column":5},"end":{"row":132,"column":6},"action":"remove","lines":["i"]},{"start":{"row":132,"column":4},"end":{"row":132,"column":5},"action":"remove","lines":["v"]}],[{"start":{"row":132,"column":4},"end":{"row":135,"column":1},"action":"insert","lines":["db.products.update(","   { sku: \"abc123\" },","   { $inc: { quantity: -2, \"metrics.orders\": 1 } }",")"],"id":542}],[{"start":{"row":132,"column":4},"end":{"row":132,"column":5},"action":"insert","lines":["m"],"id":543},{"start":{"row":132,"column":5},"end":{"row":132,"column":6},"action":"insert","lines":["o"]},{"start":{"row":132,"column":6},"end":{"row":132,"column":7},"action":"insert","lines":["n"]},{"start":{"row":132,"column":7},"end":{"row":132,"column":8},"action":"insert","lines":["g"]},{"start":{"row":132,"column":8},"end":{"row":132,"column":9},"action":"insert","lines":["o"]},{"start":{"row":132,"column":9},"end":{"row":132,"column":10},"action":"insert","lines":["."]}],[{"start":{"row":133,"column":3},"end":{"row":133,"column":20},"action":"remove","lines":["{ sku: \"abc123\" }"],"id":544},{"start":{"row":133,"column":3},"end":{"row":133,"column":31},"action":"insert","lines":["{'_id': ObjectId(recipe_id)}"]}],[{"start":{"row":134,"column":46},"end":{"row":134,"column":47},"action":"remove","lines":[" "],"id":545},{"start":{"row":134,"column":45},"end":{"row":134,"column":46},"action":"remove","lines":["1"]},{"start":{"row":134,"column":44},"end":{"row":134,"column":45},"action":"remove","lines":[" "]},{"start":{"row":134,"column":43},"end":{"row":134,"column":44},"action":"remove","lines":[":"]},{"start":{"row":134,"column":42},"end":{"row":134,"column":43},"action":"remove","lines":["\""]},{"start":{"row":134,"column":41},"end":{"row":134,"column":42},"action":"remove","lines":["s"]},{"start":{"row":134,"column":40},"end":{"row":134,"column":41},"action":"remove","lines":["r"]},{"start":{"row":134,"column":39},"end":{"row":134,"column":40},"action":"remove","lines":["e"]},{"start":{"row":134,"column":38},"end":{"row":134,"column":39},"action":"remove","lines":["d"]},{"start":{"row":134,"column":37},"end":{"row":134,"column":38},"action":"remove","lines":["r"]},{"start":{"row":134,"column":36},"end":{"row":134,"column":37},"action":"remove","lines":["o"]},{"start":{"row":134,"column":35},"end":{"row":134,"column":36},"action":"remove","lines":["."]},{"start":{"row":134,"column":34},"end":{"row":134,"column":35},"action":"remove","lines":["s"]},{"start":{"row":134,"column":33},"end":{"row":134,"column":34},"action":"remove","lines":["c"]},{"start":{"row":134,"column":32},"end":{"row":134,"column":33},"action":"remove","lines":["i"]},{"start":{"row":134,"column":31},"end":{"row":134,"column":32},"action":"remove","lines":["r"]},{"start":{"row":134,"column":30},"end":{"row":134,"column":31},"action":"remove","lines":["t"]},{"start":{"row":134,"column":29},"end":{"row":134,"column":30},"action":"remove","lines":["e"]},{"start":{"row":134,"column":28},"end":{"row":134,"column":29},"action":"remove","lines":["m"]},{"start":{"row":134,"column":27},"end":{"row":134,"column":28},"action":"remove","lines":["\""]},{"start":{"row":134,"column":26},"end":{"row":134,"column":27},"action":"remove","lines":[" "]},{"start":{"row":134,"column":25},"end":{"row":134,"column":26},"action":"remove","lines":[","]},{"start":{"row":134,"column":24},"end":{"row":134,"column":25},"action":"remove","lines":["2"]},{"start":{"row":134,"column":23},"end":{"row":134,"column":24},"action":"remove","lines":["-"]},{"start":{"row":134,"column":22},"end":{"row":134,"column":23},"action":"remove","lines":[" "]},{"start":{"row":134,"column":21},"end":{"row":134,"column":22},"action":"remove","lines":[":"]},{"start":{"row":134,"column":20},"end":{"row":134,"column":21},"action":"remove","lines":["y"]},{"start":{"row":134,"column":19},"end":{"row":134,"column":20},"action":"remove","lines":["t"]},{"start":{"row":134,"column":18},"end":{"row":134,"column":19},"action":"remove","lines":["i"]},{"start":{"row":134,"column":17},"end":{"row":134,"column":18},"action":"remove","lines":["t"]},{"start":{"row":134,"column":16},"end":{"row":134,"column":17},"action":"remove","lines":["n"]},{"start":{"row":134,"column":15},"end":{"row":134,"column":16},"action":"remove","lines":["a"]}],[{"start":{"row":134,"column":14},"end":{"row":134,"column":15},"action":"remove","lines":["u"],"id":546},{"start":{"row":134,"column":13},"end":{"row":134,"column":14},"action":"remove","lines":["q"]},{"start":{"row":134,"column":12},"end":{"row":134,"column":13},"action":"remove","lines":[" "]}],[{"start":{"row":134,"column":12},"end":{"row":134,"column":13},"action":"insert","lines":["v"],"id":547},{"start":{"row":134,"column":13},"end":{"row":134,"column":14},"action":"insert","lines":["i"]},{"start":{"row":134,"column":14},"end":{"row":134,"column":15},"action":"insert","lines":["e"]},{"start":{"row":134,"column":15},"end":{"row":134,"column":16},"action":"insert","lines":["w"]},{"start":{"row":134,"column":16},"end":{"row":134,"column":17},"action":"insert","lines":["s"]},{"start":{"row":134,"column":17},"end":{"row":134,"column":18},"action":"insert","lines":[":"]}],[{"start":{"row":134,"column":18},"end":{"row":134,"column":19},"action":"insert","lines":[" "],"id":548},{"start":{"row":134,"column":19},"end":{"row":134,"column":20},"action":"insert","lines":["1"]}],[{"start":{"row":135,"column":0},"end":{"row":135,"column":4},"action":"insert","lines":["    "],"id":549}],[{"start":{"row":134,"column":12},"end":{"row":134,"column":13},"action":"insert","lines":["\""],"id":550}],[{"start":{"row":134,"column":18},"end":{"row":134,"column":19},"action":"insert","lines":["\""],"id":551}],[{"start":{"row":134,"column":12},"end":{"row":134,"column":13},"action":"remove","lines":["\""],"id":552}],[{"start":{"row":134,"column":17},"end":{"row":134,"column":18},"action":"remove","lines":["\""],"id":553}],[{"start":{"row":132,"column":4},"end":{"row":132,"column":5},"action":"insert","lines":["v"],"id":554},{"start":{"row":132,"column":5},"end":{"row":132,"column":6},"action":"insert","lines":["i"]},{"start":{"row":132,"column":6},"end":{"row":132,"column":7},"action":"insert","lines":["e"]},{"start":{"row":132,"column":7},"end":{"row":132,"column":8},"action":"insert","lines":["w"]},{"start":{"row":132,"column":8},"end":{"row":132,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":132,"column":8},"end":{"row":132,"column":9},"action":"remove","lines":["s"],"id":555},{"start":{"row":132,"column":7},"end":{"row":132,"column":8},"action":"remove","lines":["w"]},{"start":{"row":132,"column":6},"end":{"row":132,"column":7},"action":"remove","lines":["e"]},{"start":{"row":132,"column":5},"end":{"row":132,"column":6},"action":"remove","lines":["i"]},{"start":{"row":132,"column":4},"end":{"row":132,"column":5},"action":"remove","lines":["v"]}],[{"start":{"row":132,"column":4},"end":{"row":132,"column":5},"action":"insert","lines":["n"],"id":556},{"start":{"row":132,"column":5},"end":{"row":132,"column":6},"action":"insert","lines":["e"]},{"start":{"row":132,"column":6},"end":{"row":132,"column":7},"action":"insert","lines":["w"]},{"start":{"row":132,"column":7},"end":{"row":132,"column":8},"action":"insert","lines":["_"]},{"start":{"row":132,"column":8},"end":{"row":132,"column":9},"action":"insert","lines":["v"]},{"start":{"row":132,"column":9},"end":{"row":132,"column":10},"action":"insert","lines":["i"]},{"start":{"row":132,"column":10},"end":{"row":132,"column":11},"action":"insert","lines":["e"]}],[{"start":{"row":132,"column":11},"end":{"row":132,"column":12},"action":"insert","lines":["w"],"id":557},{"start":{"row":132,"column":12},"end":{"row":132,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":132,"column":13},"end":{"row":132,"column":14},"action":"insert","lines":[" "],"id":558},{"start":{"row":132,"column":14},"end":{"row":132,"column":15},"action":"insert","lines":["="]}],[{"start":{"row":132,"column":15},"end":{"row":132,"column":16},"action":"insert","lines":[" "],"id":559}],[{"start":{"row":133,"column":2},"end":{"row":133,"column":4},"action":"insert","lines":["  "],"id":560}],[{"start":{"row":133,"column":4},"end":{"row":133,"column":8},"action":"insert","lines":["    "],"id":561}],[{"start":{"row":133,"column":8},"end":{"row":133,"column":12},"action":"insert","lines":["    "],"id":562}],[{"start":{"row":133,"column":12},"end":{"row":133,"column":16},"action":"insert","lines":["    "],"id":563}],[{"start":{"row":133,"column":16},"end":{"row":133,"column":20},"action":"insert","lines":["    "],"id":564}],[{"start":{"row":133,"column":20},"end":{"row":133,"column":24},"action":"insert","lines":["    "],"id":565}],[{"start":{"row":133,"column":24},"end":{"row":133,"column":28},"action":"insert","lines":["    "],"id":566}],[{"start":{"row":133,"column":28},"end":{"row":133,"column":32},"action":"insert","lines":["    "],"id":567}],[{"start":{"row":134,"column":3},"end":{"row":134,"column":4},"action":"insert","lines":[" "],"id":568}],[{"start":{"row":134,"column":4},"end":{"row":134,"column":8},"action":"insert","lines":["    "],"id":569}],[{"start":{"row":134,"column":8},"end":{"row":134,"column":12},"action":"insert","lines":["    "],"id":570}],[{"start":{"row":134,"column":12},"end":{"row":134,"column":16},"action":"insert","lines":["    "],"id":571}],[{"start":{"row":134,"column":16},"end":{"row":134,"column":20},"action":"insert","lines":["    "],"id":572}],[{"start":{"row":134,"column":20},"end":{"row":134,"column":24},"action":"insert","lines":["    "],"id":573}],[{"start":{"row":134,"column":24},"end":{"row":134,"column":28},"action":"insert","lines":["    "],"id":574}],[{"start":{"row":134,"column":28},"end":{"row":134,"column":32},"action":"insert","lines":["    "],"id":575}],[{"start":{"row":134,"column":32},"end":{"row":134,"column":36},"action":"insert","lines":["    "],"id":576}],[{"start":{"row":134,"column":36},"end":{"row":134,"column":40},"action":"insert","lines":["    "],"id":577},{"start":{"row":134,"column":40},"end":{"row":134,"column":44},"action":"insert","lines":["    "]},{"start":{"row":134,"column":44},"end":{"row":134,"column":48},"action":"insert","lines":["    "]}],[{"start":{"row":134,"column":44},"end":{"row":134,"column":48},"action":"remove","lines":["    "],"id":578},{"start":{"row":134,"column":40},"end":{"row":134,"column":44},"action":"remove","lines":["    "]},{"start":{"row":134,"column":36},"end":{"row":134,"column":40},"action":"remove","lines":["    "]},{"start":{"row":134,"column":32},"end":{"row":134,"column":36},"action":"remove","lines":["    "]}],[{"start":{"row":134,"column":32},"end":{"row":134,"column":36},"action":"insert","lines":["    "],"id":579}],[{"start":{"row":134,"column":32},"end":{"row":134,"column":36},"action":"remove","lines":["    "],"id":580}],[{"start":{"row":135,"column":0},"end":{"row":135,"column":4},"action":"remove","lines":["    "],"id":581},{"start":{"row":134,"column":52},"end":{"row":135,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":134,"column":41},"end":{"row":134,"column":42},"action":"insert","lines":["'"],"id":582}],[{"start":{"row":134,"column":47},"end":{"row":134,"column":48},"action":"insert","lines":["'"],"id":583}],[{"start":{"row":134,"column":34},"end":{"row":134,"column":35},"action":"remove","lines":["$"],"id":584}],[{"start":{"row":134,"column":33},"end":{"row":134,"column":34},"action":"remove","lines":[" "],"id":585}],[{"start":{"row":134,"column":33},"end":{"row":134,"column":34},"action":"insert","lines":[" "],"id":586}],[{"start":{"row":132,"column":15},"end":{"row":132,"column":16},"action":"remove","lines":[" "],"id":587},{"start":{"row":132,"column":14},"end":{"row":132,"column":15},"action":"remove","lines":["="]},{"start":{"row":132,"column":13},"end":{"row":132,"column":14},"action":"remove","lines":[" "]},{"start":{"row":132,"column":12},"end":{"row":132,"column":13},"action":"remove","lines":["s"]},{"start":{"row":132,"column":11},"end":{"row":132,"column":12},"action":"remove","lines":["w"]},{"start":{"row":132,"column":10},"end":{"row":132,"column":11},"action":"remove","lines":["e"]},{"start":{"row":132,"column":9},"end":{"row":132,"column":10},"action":"remove","lines":["i"]},{"start":{"row":132,"column":8},"end":{"row":132,"column":9},"action":"remove","lines":["v"]},{"start":{"row":132,"column":7},"end":{"row":132,"column":8},"action":"remove","lines":["_"]},{"start":{"row":132,"column":6},"end":{"row":132,"column":7},"action":"remove","lines":["w"]},{"start":{"row":132,"column":5},"end":{"row":132,"column":6},"action":"remove","lines":["e"]},{"start":{"row":132,"column":4},"end":{"row":132,"column":5},"action":"remove","lines":["n"]}],[{"start":{"row":132,"column":13},"end":{"row":132,"column":21},"action":"remove","lines":["products"],"id":588},{"start":{"row":132,"column":13},"end":{"row":132,"column":14},"action":"insert","lines":["r"]},{"start":{"row":132,"column":14},"end":{"row":132,"column":15},"action":"insert","lines":["e"]},{"start":{"row":132,"column":15},"end":{"row":132,"column":16},"action":"insert","lines":["c"]},{"start":{"row":132,"column":16},"end":{"row":132,"column":17},"action":"insert","lines":["i"]},{"start":{"row":132,"column":17},"end":{"row":132,"column":18},"action":"insert","lines":["p"]},{"start":{"row":132,"column":18},"end":{"row":132,"column":19},"action":"insert","lines":["e"]},{"start":{"row":132,"column":19},"end":{"row":132,"column":20},"action":"insert","lines":["s"]}],[{"start":{"row":134,"column":34},"end":{"row":134,"column":35},"action":"insert","lines":["$"],"id":589}],[{"start":{"row":134,"column":32},"end":{"row":134,"column":54},"action":"remove","lines":["{ $inc: {'views': 1} }"],"id":590},{"start":{"row":134,"column":32},"end":{"row":134,"column":79},"action":"insert","lines":["{ $inc: { quantity: -2, \"metrics.orders\": 1 } }"]}],[{"start":{"row":134,"column":28},"end":{"row":134,"column":32},"action":"remove","lines":["    "],"id":591},{"start":{"row":134,"column":24},"end":{"row":134,"column":28},"action":"remove","lines":["    "]},{"start":{"row":134,"column":20},"end":{"row":134,"column":24},"action":"remove","lines":["    "]},{"start":{"row":134,"column":16},"end":{"row":134,"column":20},"action":"remove","lines":["    "]},{"start":{"row":134,"column":12},"end":{"row":134,"column":16},"action":"remove","lines":["    "]},{"start":{"row":134,"column":8},"end":{"row":134,"column":12},"action":"remove","lines":["    "]},{"start":{"row":134,"column":4},"end":{"row":134,"column":8},"action":"remove","lines":["    "]},{"start":{"row":134,"column":0},"end":{"row":134,"column":4},"action":"remove","lines":["    "]},{"start":{"row":133,"column":62},"end":{"row":134,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":133,"column":62},"end":{"row":133,"column":63},"action":"insert","lines":[" "],"id":592}],[{"start":{"row":133,"column":65},"end":{"row":133,"column":66},"action":"remove","lines":["$"],"id":593}],[{"start":{"row":133,"column":72},"end":{"row":133,"column":80},"action":"remove","lines":["quantity"],"id":594},{"start":{"row":133,"column":72},"end":{"row":133,"column":73},"action":"insert","lines":["'"]},{"start":{"row":133,"column":73},"end":{"row":133,"column":74},"action":"insert","lines":["v"]},{"start":{"row":133,"column":74},"end":{"row":133,"column":75},"action":"insert","lines":["i"]},{"start":{"row":133,"column":75},"end":{"row":133,"column":76},"action":"insert","lines":["e"]},{"start":{"row":133,"column":76},"end":{"row":133,"column":77},"action":"insert","lines":["w"]},{"start":{"row":133,"column":77},"end":{"row":133,"column":78},"action":"insert","lines":["s"]}],[{"start":{"row":133,"column":78},"end":{"row":133,"column":79},"action":"insert","lines":[";"],"id":595}],[{"start":{"row":133,"column":78},"end":{"row":133,"column":79},"action":"remove","lines":[";"],"id":596}],[{"start":{"row":133,"column":78},"end":{"row":133,"column":79},"action":"insert","lines":["'"],"id":597}],[{"start":{"row":133,"column":83},"end":{"row":133,"column":104},"action":"remove","lines":[", \"metrics.orders\": 1"],"id":598}],[{"start":{"row":133,"column":65},"end":{"row":133,"column":66},"action":"insert","lines":["$"],"id":599}],[{"start":{"row":133,"column":86},"end":{"row":133,"column":87},"action":"insert","lines":[","],"id":600}],[{"start":{"row":133,"column":87},"end":{"row":133,"column":88},"action":"insert","lines":[" "],"id":601}],[{"start":{"row":133,"column":87},"end":{"row":133,"column":88},"action":"remove","lines":[" "],"id":603}],[{"start":{"row":133,"column":86},"end":{"row":133,"column":87},"action":"remove","lines":[","],"id":604}],[{"start":{"row":133,"column":65},"end":{"row":133,"column":66},"action":"insert","lines":["'"],"id":605}],[{"start":{"row":133,"column":70},"end":{"row":133,"column":71},"action":"insert","lines":["'"],"id":606}],[{"start":{"row":133,"column":85},"end":{"row":133,"column":86},"action":"remove","lines":["2"],"id":607},{"start":{"row":133,"column":84},"end":{"row":133,"column":85},"action":"remove","lines":["-"]}],[{"start":{"row":133,"column":84},"end":{"row":133,"column":85},"action":"insert","lines":["1"],"id":608}],[{"start":{"row":133,"column":32},"end":{"row":133,"column":33},"action":"remove","lines":[" "],"id":609},{"start":{"row":133,"column":28},"end":{"row":133,"column":32},"action":"remove","lines":["    "]},{"start":{"row":133,"column":24},"end":{"row":133,"column":28},"action":"remove","lines":["    "]},{"start":{"row":133,"column":20},"end":{"row":133,"column":24},"action":"remove","lines":["    "]},{"start":{"row":133,"column":16},"end":{"row":133,"column":20},"action":"remove","lines":["    "]},{"start":{"row":133,"column":12},"end":{"row":133,"column":16},"action":"remove","lines":["    "]},{"start":{"row":133,"column":8},"end":{"row":133,"column":12},"action":"remove","lines":["    "]},{"start":{"row":133,"column":4},"end":{"row":133,"column":8},"action":"remove","lines":["    "]},{"start":{"row":133,"column":0},"end":{"row":133,"column":4},"action":"remove","lines":["    "]},{"start":{"row":132,"column":28},"end":{"row":133,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":135,"column":0},"end":{"row":135,"column":2},"action":"insert","lines":["# "],"id":610},{"start":{"row":136,"column":0},"end":{"row":136,"column":2},"action":"insert","lines":["# "]},{"start":{"row":137,"column":0},"end":{"row":137,"column":2},"action":"insert","lines":["# "]},{"start":{"row":138,"column":0},"end":{"row":138,"column":2},"action":"insert","lines":["# "]}],[{"start":{"row":134,"column":0},"end":{"row":135,"column":0},"action":"insert","lines":["",""],"id":611},{"start":{"row":135,"column":0},"end":{"row":136,"column":0},"action":"insert","lines":["",""]},{"start":{"row":136,"column":0},"end":{"row":137,"column":0},"action":"insert","lines":["",""]},{"start":{"row":137,"column":0},"end":{"row":138,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":129,"column":18},"end":{"row":129,"column":19},"action":"remove","lines":["p"],"id":612},{"start":{"row":129,"column":17},"end":{"row":129,"column":18},"action":"remove","lines":["u"]},{"start":{"row":129,"column":16},"end":{"row":129,"column":17},"action":"remove","lines":["w"]},{"start":{"row":129,"column":15},"end":{"row":129,"column":16},"action":"remove","lines":["e"]},{"start":{"row":129,"column":14},"end":{"row":129,"column":15},"action":"remove","lines":["i"]},{"start":{"row":129,"column":13},"end":{"row":129,"column":14},"action":"remove","lines":["v"]}],[{"start":{"row":129,"column":13},"end":{"row":129,"column":14},"action":"insert","lines":["t"],"id":613},{"start":{"row":129,"column":14},"end":{"row":129,"column":15},"action":"insert","lines":["h"]},{"start":{"row":129,"column":15},"end":{"row":129,"column":16},"action":"insert","lines":["e"]},{"start":{"row":129,"column":16},"end":{"row":129,"column":17},"action":"insert","lines":["_"]},{"start":{"row":129,"column":17},"end":{"row":129,"column":18},"action":"insert","lines":["r"]},{"start":{"row":129,"column":18},"end":{"row":129,"column":19},"action":"insert","lines":["e"]},{"start":{"row":129,"column":19},"end":{"row":129,"column":20},"action":"insert","lines":["c"]},{"start":{"row":129,"column":20},"end":{"row":129,"column":21},"action":"insert","lines":["i"]},{"start":{"row":129,"column":21},"end":{"row":129,"column":22},"action":"insert","lines":["p"]},{"start":{"row":129,"column":22},"end":{"row":129,"column":23},"action":"insert","lines":["e"]}],[{"start":{"row":130,"column":4},"end":{"row":130,"column":10},"action":"remove","lines":["viewup"],"id":614},{"start":{"row":130,"column":4},"end":{"row":130,"column":5},"action":"insert","lines":["t"]},{"start":{"row":130,"column":5},"end":{"row":130,"column":6},"action":"insert","lines":["h"]},{"start":{"row":130,"column":6},"end":{"row":130,"column":7},"action":"insert","lines":["e"]},{"start":{"row":130,"column":7},"end":{"row":130,"column":8},"action":"insert","lines":["_"]},{"start":{"row":130,"column":8},"end":{"row":130,"column":9},"action":"insert","lines":["r"]},{"start":{"row":130,"column":9},"end":{"row":130,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":130,"column":4},"end":{"row":130,"column":10},"action":"remove","lines":["the_re"],"id":615},{"start":{"row":130,"column":4},"end":{"row":130,"column":14},"action":"insert","lines":["the_recipe"]}]]},"ace":{"folds":[],"scrolltop":1677.0703125,"scrollleft":0,"selection":{"start":{"row":130,"column":14},"end":{"row":130,"column":14},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":115,"state":"start","mode":"ace/mode/python"}},"timestamp":1562350579097,"hash":"9934f2d4d458c23114a56299767e929dab2bfe9f"}