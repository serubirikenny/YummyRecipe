from flask import *
from functools import wraps
from Classes.User import User

app = Flask(__name__)

app.secret_key = 'elgordo123456789'
users = {'admin': 'admin', 'art': 'art'}
user = User()

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash("You need to login first.")
            return redirect(url_for('login'))
    return wrap




@app.route('/index')
@login_required
def index():
    lists = user.recipes
    return render_template('index.html', lists=lists)


@app.route('/signup', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        flash("You have succesfully been registered {} {}".format(name, password))

        if name and password:
            users[email] = password
            return redirect(url_for('login'))
    return render_template('signup.html', error=error)


@app.route('/add_list', methods=['GET', 'POST'])
@login_required
def add_list():
    error = None
    if request.method == 'POST':
        recipe_name = request.form['recipe_name']
        item1 = request.form['item1']
        item2 = request.form['item2']
        item3 = request.form['item3']
        items = [item1,item2,item3]

        flash("You have succesfully added  {} {}".format(recipe_name, items))

        if recipe_name and items:
            user.create_recipe(recipe_name, items)
            return redirect(url_for('index'))
    return render_template('add_list.html', error=error)


@app.route('/add_item/<recipe_name>', methods=['GET', 'POST'])
@login_required
def add_item(recipe_name):
    error = None
    if request.method == 'POST':
        recipe_name = request.form['recipe_name']
        items = request.form['items']
        flash("You have succesfully added registered {} {}".format(recipe_name, items))

        if recipe_name and items:
            user.add_recipe_item(recipe_name, [items])
            return redirect(url_for('item', recipe_name=recipe_name))
    return render_template('add_item.html',recipe_name= recipe_name, error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You Were Logged Out !')
    return redirect(url_for('login'))

@app.route('/item/<recipe_name>')
@login_required
def item(recipe_name):
    items = user.read_recipes(recipe_name)
    print(items)
    return render_template('item.html', items=items, recipe_name=recipe_name)

@app.route('/delete/<recipe_name>/<item_name>')
@login_required
def delete(recipe_name, item_name):
    user.delete_recipe_item(recipe_name, item_name)
    return redirect(url_for('item', recipe_name=recipe_name))
    return render_template('item.html',recipe_name=recipe_name,items=items)

@app.route('/delete_recipes/<recipe_name>')
@login_required
def delete_recipes(recipe_name):
    """"
    Route enables user to delete recipe category
    """
    user.delete_recipes(recipe_name)
    return redirect(url_for('index'))
    return render_template('index.html')





@app.route('/updatelist/<recipe_name>', methods=['GET', 'POST'])
@login_required
def updatelist(recipe_name):
    """"
    Route enables user to edit recipe category
    """
    error = None    
    if request.method == 'POST':
        recipe_name = request.form['recipe_name']
        new_name = request.form['new_name']
        flash("You have succesfully added registered {} {}".format(recipe_name, new_name))

        if recipe_name and new_name:
            user.update_recipes(recipe_name, new_name)
            return redirect(url_for('index',recipe_name=recipe_name))
    return render_template('updaterecipe.html',recipe_name=recipe_name)

@app.route('/updatelistitem/<recipe_name>/<item_name>', methods=['GET', 'POST'])
@login_required
def updatelistitem(recipe_name, item_name):
    """"
    Route enables user to edit recipe category item
    """
    error = None
    if request.method == 'POST':
        recipe_name = request.form['recipe_name']
        item_name = request.form['item_name']
        new_name = request.form['new_item_name']
        flash("You have succesfully added registered {} {} {}".format(recipe_name, item_name, new_name))

        if recipe_name and item_name:
            user.update_recipe_item(recipe_name, item_name, new_name)
            return redirect(url_for('item', recipe_name=recipe_name, item_name=item_name))
    return render_template('updaterecipeitem.html', recipe_name=recipe_name, item_name=item_name)





@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] not in users.keys() or request.form['password'] not in users.values():
            error = 'Invalid Credentials'
        else:
            session['logged_in'] = True
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
