from flask import Flask
from flask import render_template, url_for

def init_routes(app: Flask):
    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('index.html')

    @app.route('/eventos')
    def eventos():
        return render_template('eventos.html')