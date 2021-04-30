from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/")
def tela_inicial():
    return render_template('tela_inicial.html')

@app.route("/")
def perfil_usuario():
    return render_template('perfil_usuario.html')

if __name__ == '__main__':
    app.run(debug=True)