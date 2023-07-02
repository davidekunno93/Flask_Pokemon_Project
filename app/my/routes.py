from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user



my = Blueprint('my', __name__, template_folder='my_templates')

@my.route('/mybattles')
@login_required
def mybattles():
    wins = current_user.wins
    losses = current_user.losses
    if not wins:
        wins = 0
    if not losses:
        losses = 0
    if wins == 0:
        ratio = "None"
    elif losses == 0 and wins != 0:
        ratio = "Infinite"
    else:
        ratio = "{:.2f}".format(wins / losses)
    return render_template('mybattles.html', wins=wins, losses=losses, ratio=ratio)

@my.route('/myfriends')
@login_required
def myfriends():
    return render_template("myfriends.html")