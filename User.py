class User(object):

	    def __init__(self):
		self.recipes = {}

	    def create_recipe(self, name, item):
		if name in self.recipes.keys():
         	 	return 'recipe already exists!'
		self.recipes[name] = item

        	return self.recipes

	    def read_recipes(self, recipe_name, new_name):
		pass

	    def update_recipes(self, recipe_name, new_name):
		pass

            def delete_recipes(self, recipe_name, new_name):
		pass

