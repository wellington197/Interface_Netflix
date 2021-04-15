from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
    return render_template('login.html')
    return render_template('perfil_usuario.html')
    return render_template('tela_inicial.html')


if __name__ == '__main__':
    app.run(debug=True)