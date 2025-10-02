from flask import Flask, request , jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db =SQLAlchemy(app)
with app.app_context():
    db.create_all()

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))
    
    def __repr__(self):
        return f'{self.name} - {self.description}'

@app.route('/')
def index():
    return 'Hello!'

@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    
    output = []
    for drink in drinks:
        drink_data = {'id':drink.id,
                      'name': drink.name, 
                      'description':drink.description}
        
        output.append(drink_data)
      
    return {"drinks":output}

@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return jsonify({'name': drink.name, 'description':drink.description})


@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'],description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return jsonify({'id':drink.id})

@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return jsonify({'Error': "not found"})
    db.session.delete(drink)
    db.session.commit()
    return jsonify({'message':'Sucessful'})

@app.route('/drinks/<id>', methods=['PATCH'])
def patch_drink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return jsonify({'Error': "not found"})
    
    data = request.get_json()
    
    if 'name' in data:
        drink.name = data['name']
        
    if 'description' in data:
        drink.description = data['description']

    db.session.commit()
    
    return jsonify({'id':drink.id,
                    'name':drink.name,
                   'description':drink.description
                   })