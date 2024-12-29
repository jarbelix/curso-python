from flask import Flask, render_template

app = Flask(__name__)

# rotas
@app.route('/')
def homepage():
    #return "Meu site no Flask"
    return render_template('homepage.html')

@app.route('/blog')
def blog():
    return "Meu Blog no Flask"

if __name__ == '__main__':
    app.run()



