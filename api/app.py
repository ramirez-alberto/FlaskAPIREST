from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

class Publicacion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(50))
    contenido = db.Column(db.String(250))

class Publicacion_Schema(ma.Schema):
    class Meta:
        fields = ("id","titulo","contenido")
    
post_schema = Publicacion_Schema()
posts_schema = Publicacion_Schema(many = True)

class RecursoListarPublicaciones(Resource):
    def get(self):
        publicaciones = Publicacion.query.all()
        return posts_schema.dump(publicaciones)
    def post(self):
        nueva_publicacion = Publicacion(
            titulo = request.json['titulo'],
            contenido = request.json['contenido']
        )

        db.session.add(nueva_publicacion)
        db.session.commit()
        return post_schema.dump(nueva_publicacion)
    
api.add_resource(RecursoListarPublicaciones, '/publicaciones')

if __name__ == '__main__':
    app.run(debug=True)