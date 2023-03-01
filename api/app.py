from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Publicacion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(50))
    contenido = db.Column(db.String(250))

class Publicacion_Schema(ma.Schema):
    class Meta:
        fields = ("id","titulo","contenido")
    
post_schema = Publicacion_Schema()
posts_schema = Publicacion_Schema(many = True)



if __name__ == '__main__':
    app.run(debug=True)