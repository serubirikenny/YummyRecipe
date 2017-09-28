from flask import *
from functools import wraps
from Classes.User import User

app = Flask(__name__)

app.secret_key = 'elgordo123456789'
users = {'admin': 'admin', 'art': 'art'}
user = User()




@app.route('/index')
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
def add_list():
    error = None
    if request.method == 'POST':
        recipe_name = request.form['recipe_name']
        items = request.form['items']
        flash("You have succesfully added registered {} {}".format(recipe_name, items))

        if recipe_name and items:
            user.create_recipe(recipe_name, items)
            return redirect(url_for('index'))
    return render_template('add_list.html', error=error)


@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    error = None
    if request.method == 'POST':
        recipe_name = request.form['recipe_name']
        items = request.form['items']
        flash("You have succesfully added registered {} {}".format(recipe_name, items))

        if recipe_name and items:
            user.add_recipe_item(recipe_name, items)
            return redirect(url_for('item', recipe_name=recipe_name))
    return render_template('add_list.html', error=error)


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash("You need to login first.")
            return redirect(url_for('log'))
    return wrap

@app.route('/editlist', methods=['GET', 'POST'])
def editlist():
    error = None
    if request.method == 'POST':
        p_name = request.form['previous_name']
        n_name = request.form['new_name']


        if p_name and n_name:
            user.update_recipe(p_name, n_name)
            return redirect(url_for('index'))
    return render_template('editlist.html', error=error)

@app.route('/editlistitem', methods=['GET', 'POST'])
def editlistitem():
    error = None
    l_name = ''
    if request.method == 'POST':
        l_name = request.form['list_name']
        o_name = request.form['item_name']
        ni_name = request.form['new_item_name']

    if l_name and o_name and ni_name:
        user.edit_recipe_item(l_name, o_name, ni_name)
    return redirect(url_for('index'))
    return render_template('editlist_item.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You Were Logged Out !')
    return redirect(url_for('login'))


@app.route('/item/<list_name>')
@login_required
def item(list_name):
    items = user.read_recipes(list_name)
    return render_template('item.html', items=items, list_name=list_name)


@app.route('/delete/<list_name>/<item_name>')
def delete(list_name, item_name):
    user.delete_recipe_item(list_name, item_name)
    return redirect(url_for('item', list_name=list_name))
    return render_template('item.html')


@app.route('/delete_list/<list_name>')
def delete_list(list_name):
    user.delete_recipes(list_name)
    return redirect(url_for('index'))
    return render_template('index.html')

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
