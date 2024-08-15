from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store
items = []

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to display all items
@app.route('/items')
def display_items():
    return render_template('items.html', items=items)

# Route for creating a new item
@app.route('/create', methods=['GET', 'POST'])
def create_item():
    if request.method == 'POST':
        item_name = request.form['name']
        items.append(item_name)
        return redirect(url_for('display_items'))
    return render_template('create.html')

# Route for updating an item
@app.route('/update/<int:item_id>', methods=['GET', 'POST'])
def update_item(item_id):
    if request.method == 'POST':
        new_name = request.form['name']
        items[item_id] = new_name
        return redirect(url_for('display_items'))
    return render_template('update.html', item=items[item_id], item_id=item_id)

# Route for deleting an item
@app.route('/delete/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    items.pop(item_id)
    return redirect(url_for('display_items'))

if __name__ == "__main__":
    app.run(debug=True)

