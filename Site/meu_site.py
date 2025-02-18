from flask import Flask, render_template

app = Flask(__name__)

#Criar a primeira pagina do site
#route -> seria o link das paginas
#função -> o que você quer exibir nquela pagina

@app.route("/")
def homepage():
    return render_template("homepage.html")


#Criar o site no ar
if __name__ == "__main__":
    app.run(debug=True)