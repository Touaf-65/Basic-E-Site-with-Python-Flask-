from models import db
from auth import auth
import secrets
from flask import Flask, render_template


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
secret_key = secrets.token_hex(16)
app.secret_key = secret_key

db.init_app(app)
app.register_blueprint(auth)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":

    with app.app_context():
        db.create_all()
    app.run(debug=True)