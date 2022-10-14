
#IMPORTAR
from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash #Encargado de mostrar mensajes o errores
#IMPORTAR RE
import re #Importando las expresiones regulares
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #Expresion regular de email


class Recipe:

    def __init__(self, data):

        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructioms = data['instructioms']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        # JOIN(
        self.first_name = data['first_name']


    @staticmethod
    def valida_receta(formulario):

        es_valido = True

        if formulario['name'] =='':
            flash ('Debe ingresar un nombre','recipe')
            es_valido = False

        es_valido = True
        
        if formulario['description'] =='':
            flash ('Debe ingresar una descripcion','recipe')
            es_valido = False

        es_valido = True
        
        if formulario['instructioms'] =='':
            flash ('Debe ingresar instrucciones','recipe')
            es_valido = False

        es_valido = True
        
        return es_valido
        
        


    @classmethod

    def save(cls, formulario):

        query = "INSERT INTO recipes (name, description, instructioms, date_made, under_30, user_id) VALUES (%(name)s,  %(description)s,  %(instructioms)s,  %(date_made)s,  %(under_30)s,  %(user_id)s)"


        results = connectToMySQL('recetas_practica_examen').query_db(query, formulario)

        return results


    @classmethod
    def get_all(cls):
        query = "SELECT recipes.*, first_name FROM recipes LEFT JOIN users ON users.id = recipes.user_id;"

        results = connectToMySQL('recetas_practica_examen').query_db(query)
        recipes =[]

        for recipe in results:
            recipes.append(cls(recipe))

        return recipes
    
    @classmethod
    def update_recipe(cls, formulario):
        query = "UPDATE recipes SET name=%()s, description=%(description)s, instructioms=%(instructioms)s, date_made=%(date_made)s, under_30=%(under_30)s "

        results = connectToMySQL('recetas_practica_examen').query_db(query, formulario)

        return results


    @classmethod
    def get_by_id(cls, formulario):

        query = "SELECT recipes.*, first_name FROM recipes LEFT JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s ;"
        results = connectToMySQL('recetas_practica_examen').query_db(query, formulario)

        recipeId = cls(results[0]) #result[0] = diccionario con todos los datos de la receta; cls() creamos la instancia en base a ese diccionario
        return recipeId
        
    
    @classmethod
    def update_recipe(cls, formulario):

        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructioms=%(instructioms)s, date_made=%(date_made)s, under_30=%(under_30)s WHERE id=%(recipe_id)s "
        result = connectToMySQL('recetas_practica_examen').query_db(query, formulario)
        return result


    @classmethod
    def delete_recipe(cls, formulario):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        result = connectToMySQL('recetas_practica_examen').query_db(query, formulario)
        return result




        


