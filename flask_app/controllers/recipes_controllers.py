from flask import render_template, redirect, request, session, flash
from flask_app import app

from flask_app.models.users import User
from flask_app.models.recipes import Recipe

#Importación de Bcrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/add/recipe')
def add_recipe():

    if 'user_id' not in session:
        return redirect('/')

    #Yo sé que en sesión tengo el id de mi usuario (session['user_id'])
    #Queremos una función que en base a ese id me regrese una instancia del usuario
    formulario = {"id": session['user_id']}

    user = User.get_by_id(formulario) #Recibo la instancia de usuario en base a su ID

    return render_template('add_recipe.html', user=user)



@app.route('/save/recipes', methods=['POST'])
def save_recipes():

    if 'user_id' not in session:
        return redirect('/')

    #Yo sé que en sesión tengo el id de mi usuario (session['user_id'])
    #Queremos una función que en base a ese id me regrese una instancia del usuario
    formulario = {"id": session['user_id']}

    user = User.get_by_id(formulario) #Recibo la instancia de usuario en base a su ID

    if not Recipe.valida_receta(request.form):
        return redirect('/add/recipe')


    Recipe.save(request.form)
    return redirect ('/dashboard')

@app.route('/edit/recipes/<int:id>')
def edit_recipe(id):
    
    if 'user_id' not in session:
        return redirect('/')

    #Yo sé que en sesión tengo el id de mi usuario (session['user_id'])
    #Queremos una función que en base a ese id me regrese una instancia del usuario
    formulario = {"id": session['user_id']}

    user = User.get_by_id(formulario) #Recibo la instancia de usuario en base a su ID

    formulario_recetas = {"id": id}
    recipeId = Recipe.get_by_id(formulario_recetas)

    return render_template('edit.html', user=user, recipeId=recipeId)


@app.route('/update/recipes', methods=['POST'])
def update():
    if 'user_id' not in session:
        return redirect('/')

    #Yo sé que en sesión tengo el id de mi usuario (session['user_id'])
    #Queremos una función que en base a ese id me regrese una instancia del usuario
    formulario = {"id": session['user_id']}

    user = User.get_by_id(formulario) #Recibo la instancia de usuario en base a su ID


    if not Recipe.valida_receta(request.form):
        return redirect('/edit/recipes/'+request.form['recipe_id']) 

    Recipe.update_recipe(request.form) 

    return redirect ('/dashboard')

@app.route('/delete/recipes/<int:id>')

def delete(id):
    if 'user_id' not in session:
        return redirect('/')



    formulario = {"id": id}    #ID DE LA RECETA PARA PODER, EDITAR BORRAR ECT *estenombre debe ser igual
    Recipe.delete_recipe(formulario) #<- a este nombre

    return redirect ('/dashboard')

@app.route('/view/recipes/<int:id>')
def view_recipe(id):

    if 'user_id' not in session:
        return redirect('/')

    #Yo sé que en sesión tengo el id de mi usuario (session['user_id'])
    #Queremos una función que en base a ese id me regrese una instancia del usuario
    formulario = {"id": session['user_id']}

    user = User.get_by_id(formulario) #Recibo la instancia de usuario en base a su ID

    formulario_recetas = {"id": id}
    recipeId = Recipe.get_by_id(formulario_recetas)

    return render_template('view.html', user=user, recipeId=recipeId)




