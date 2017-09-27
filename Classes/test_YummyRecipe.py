import unittest


class RecipeTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_recipe_initialy_empty(self):
        self.assertEqual(self.user.recipes, {})

    def test_create_recipe_successfully(self):
        initial_recipe_count = len(self.user.recipes)
        self.user.create_recipe('Rolex', 'eggs')

        new_recipe_count = len(self.user.recipes)
        self.assertEqual(new_recipe_count - initial_recipe_count, 1)

    def test_create_recipe_when_recipe_already_exists(self):
        self.user.recipes = {'Peppers': ['black']}
        self.assertEqual(self.user.create_recipe('Peppers', 'black'),
                         'recipe already exists!', msg='recipe already exists!')

    def test_update_recipes(self):
        self.user.recipes = {'Peppers': ['black']}
        self.assertEqual(self.user.update_recipes(
            'Peppers', 'black_pepper'), {'black_pepper': ['black']})

    def test_updating_non_existing_recipe(self):
        self.user.recipes = {'Peppers': ['black']}
        self.assertEqual(self.user.update_recipes('Pepper', 'black'),
                         'recipe name does not exist here', msg='recipe name does not exist here')

    def test_update_recipe_item(self):
        self.user.recipes = {'Peppers': ['black']}
        self.assertEqual(self.user.update_recipe_item(
            'Peppers', 'black', 'blac'), {'Peppers': ['blac']})

    def test_updating_non_existing_recipe_item(self):
        self.user.recipes = {'Peppers': ['black']}
        self.assertEqual(self.user.update_recipe_item('Peppers', 'blac', 'bla'),
                         'Item not in list', msg='Item not in list')

    def test_read_recipe_items(self):
        self.user.recipes = {'Peppers': ['black', 'red']}
        self.assertEqual(self.user.read_list('shoes'), ['flats', 'highs'])

    def test_delete_recipe(self):
        self.user.recipes = {'Peppers': ['black', 'red'], 'Onions': ['diced', 'ground']}
        self.assertEqual(self.user.delete_recipes(
            'Peppers'), {'Onions': ['diced', 'ground']})

    def test_delete_recipe_item(self):
        self.user.recipes = {'Peppers': ['black', 'red'], 'Onions': ['diced', 'ground']}
        self.assertEqual(self.user.delete_recipe_item('Peppers', 'black'), {
            'Peppers': ['red'], 'Onions': ['diced', 'ground']})
