from flask import Flask
from config import Config
from flask_login import LoginManager
from .models import User

# instanciating app in Flask class
app = Flask(__name__)

app.config.from_object(Config)

# enabling login perisitance 
login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

login.init_app(app)

login.login_view = 'auth.login'

# this line of code - directs the flask app to routes for web routes
from . import routes



# new directory for organization
from .auth.routes import auth
app.register_blueprint(auth)

#database stuff
from .models import db
from flask_migrate import Migrate
from . import models

db.init_app(app)
migrate = Migrate(app, db)