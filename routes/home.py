from flask import Blueprint, render_template
home_route = Blueprint('home', __name__)
from routes.clientes import cliente_route

@home_route.route('/')
def home():
    return render_template('index.html')