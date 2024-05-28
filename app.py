from flask import Flask, render_template, jsonify ,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import redirect
app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/', methods=['GET', 'POST'])
def homeproject():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
        
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)


# Create Endpoint
@app.route('/create', methods=['POST'])
def create_todo():
    if request.method == 'POST':
        data = request.get_json()
        title = data.get('title')
        desc = data.get('desc')
        if title and desc:
            todo = Todo(title=title, desc=desc)
            db.session.add(todo)
            db.session.commit()
            return jsonify({"message": "Todo created successfully"}), 201
        else:
            return jsonify({"error": "Title and description are required"}), 400

# Read Endpoint
@app.route('/read', methods=['GET'])
def read_todo():
    allTodo = Todo.query.all()
    todos = []
    for todo in allTodo:
        todos.append({
            "sno": todo.sno,
            "title": todo.title,
            "desc": todo.desc,
            "date_created": todo.date_created
        })
        return jsonify(todos)

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    if request.method == 'POST':
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        db.session.commit()
        return redirect('/')
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")


@app.route('/show')
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'This is products page'

if __name__ == "__main__":
    app.run(debug=True, port=5001)