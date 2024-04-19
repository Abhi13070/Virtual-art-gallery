from flask import Flask
from .models import db
from flask_migrate import Migrate

app = Flask(__name__)

app.secret_key = 'mnbvcxz92+iobugvy554576*()%~`5rsaxfi8716jhajh$^*'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:yHRICSDnZtQwYvFMSADAviCLkjTxuXQo@monorail.proxy.rlwy.net:21845/railway'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Set to False for better performance

# Initialize SQLAlchemy with the app
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Import views
import art_web.views

# This block should be executed after creating the app instance
with app.app_context():
    # Create or upgrade the database schema
    db.create_all()
