# Importações
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portifolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando o banco
db = SQLAlchemy(app)

# Criando a classe para o banco de dados
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

# Conteúdo da página
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades Dinâmicas
@app.route('/', methods=['GET','POST'])
def process_form():
    if request.method == 'POST':

        if request.form.get('button_python'):
            return render_template(
                'acess_py.html',
                button_python=True
            )
        
        if request.form.get('button_html'):
            return render_template(
                'acess_html.html',
                button_html=True
            )
        
        if request.form.get('button_db'):
            return render_template(
                'acess_db.html',
                button_db=True
            )
        
        if request.form.get('button_f1'):
            return render_template(
                'acess_f1.html',
                button_f1=True
            )

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        mail = request.form.get('email')
        content = request.form.get('text')

        # Salvar usuário no banco de dados
        user = User(email=mail, text=content)
        db.session.add(user)
        db.session.commit()

        return redirect('/')

    return render_template('index.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)