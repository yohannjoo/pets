from flask import Flask, render_template, redirect, request
from mysqlconn import connectToMySQL
app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL("chiaPets")
    pets = mysql.query_db('SELECT * FROM pets')
    print(pets)
    return render_template('index.html', all_pets = pets)

@app.route("/create_pet", methods=["POST"])
def add_pet():
    mysql = connectToMySQL("chiaPets")
    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(nm)s, %(tp)s, NOW(), NOW());"
    data = {
        'nm': request.form['name'],
        'tp': request.form['type']
    }
    new_pet_id = mysql.query_db(query, data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)