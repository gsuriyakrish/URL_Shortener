# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Statement for enabling the Production environment
DEBUG = False

PORT = "5001"
DATABASE = "Production_Database"
LOG = "URL_Shortener_Production.log"


# Define the database - we are working with SQLite
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, DATABASE + '.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Enable protection against *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True


