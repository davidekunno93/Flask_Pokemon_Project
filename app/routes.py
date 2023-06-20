# importing app to route different web directories
from app import app
from flask import render_template, request, redirect, url_for
from .auth.forms import PokeForm, CatchForm
from .models import Pokemon, pokemon_pull, Team, User
from flask_login import current_user, login_user, logout_user, login_required

# if url = localhost:5000/ call this function and return this
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=["GET", "POST"])
@login_required
def search():
    form = PokeForm()
    if request.method == "POST":
        if form.validate():
            name = form.pokemon.data
            pokemon = Pokemon(name)
            pokedex = pokemon.pokedex()
            return render_template("pokedex.html", pokemon=pokedex)
    return render_template("search.html", form=form)

@app.route('/pokedex')
@login_required
def pokedex():
    return render_template("pokedex.html")

rotation = []
@app.route('/dashboard', methods=["GET", "POST"])
@login_required
def dashboard():
    name = pokemon_pull()
    rotation.append(name)
    pokemon = Pokemon(name)
    pokedex = pokemon.pokedex()
    if len(rotation) > 2:
        rotation.pop(0)
    if request.method == "POST":
        if "catch" in request.form:
            print('Catch that pokemon!')
            print(current_user.get_id())
            print(rotation[0], current_user.get_id())
            team_member = Team(rotation[0], current_user.get_id())
            team_member.catch_pokemon()
            return redirect(url_for('caught'))
    return render_template("dashboard.html", pokemon=pokedex)

@app.route('/caught')
@login_required
def caught():
    pokemon = Pokemon(rotation[0])
    info = pokemon.pokedex()
    return render_template('caught.html', pokemon=info)