# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Statement for enabling the development environment
DEBUG = True

PORT = "5000"
DATABASE = "Test_Database"
LOG = "URL_Shortener_Test.log"


# Define the database - we are working with SQLite
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, DATABASE + '.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Enable protection against *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True
