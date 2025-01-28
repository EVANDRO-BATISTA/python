from flask import Flask
from app.routes import init_routes  # Importa a função de inicialização das rotas

app = Flask(__name__)
app.debug = True
# Inicializa as rotas
init_routes(app)

#if __name__ == '__main__':
#    app.run(debug=True)