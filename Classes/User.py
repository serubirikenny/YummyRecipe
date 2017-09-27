class User(object):

    def __init__(self):
        self.recipes = {}

    def create_recipe(self, name, items):
        items = list(items)
        if name not in self.recipes.keys():
            self.recipes[name] = [item for item in items]
        elif name in self.recipes.keys():
            return 'recipe already exists!'
        return self.recipes

    def read_recipes(self, name):
        '''
        Returns items from specified list
        '''
        items = []
        if name in self.recipes.keys():
            items = [item for item in self.recipes[name]]
        return items


    def update_recipes(self, recipe_name, new_name):
        '''
        creates recipe name
        '''
        if recipe_name in self.recipes.keys():
           
            self.recipes[new_name] = self.recipes.pop(recipe_name)
        else:
            return "recipe name does not exist here"
        return self.recipes

    def delete_recipes(self, recipe_name):
        '''
        deletes recipes
        '''
        if recipe_name in self.recipes.keys():
            del self.recipes[recipe_name]
        else:
            return 'recipe name does not exist in the system'
        return self.recipes

    def update_recipe_item(self, recipe_name, item_name, new_name):
        '''
        creates recipe name
        '''
        if recipe_name in self.recipes.keys():
            for item in self.recipes[recipe_name]:
                if item == item_name:
                    self.recipes[recipe_name].remove(item)
                    self.recipes[recipe_name].append(new_name)
                else:
                    return 'Item not in recipe'
            else:
                return "recipe doesn't exist"
        return self.recipes

    def add_recipe_item(self, recipe_name, *items):
        '''
        method adds recipe items
        '''
        items = list(items)
        if recipe_name in self.recipes.keys():
            for item in items:
                if item not in self.recipes[recipe_name]:
                    self.recipes[recipe_name].append(item)
                else:
                    return 'Item already exists!'
                return self.recipes

    def delete_recipe_item(self, recipe_name, item):
        '''
        method deletes item in a recipe
        '''
        if item in self.recipes[recipe_name]:
            self.recipes[recipe_name].remove(item)
        else:
            return 'item not in recipe'
        return self.recipes

    def edit_recipe_item(self, recipe_name, item_name, new_name):
        '''
        creates recipe name
        '''
        if recipe_name in self.recipes.keys():
            for item in self.recipes[recipe_name]:
                if item == item_name:
                    self.recipes[recipe_name].remove(item)
                    self.recipes[recipe_name].append(new_name)
                else:
                    return 'Item not in recipe'
        else:
            return "list name doesn't exist"
        return self.recipes
