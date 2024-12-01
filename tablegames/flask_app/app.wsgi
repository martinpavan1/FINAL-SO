import sys
import os

# Agregar el directorio del proyecto al sys.path
sys.path.insert(0, '/var/www/flask_app')


# Importar la aplicación Flask como "application"
from app import app as application
