from flask import Flask,jsonify
from api import scraper_nacion
from dotenv import load_dotenv
from pathlib import Path
import os

app = Flask(__name__)

# loading env files
load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

SECRET_KEY = os.getenv("SECRET_KEY")
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def hello_world():  
        return('<h1>API Sencilla de Flask que hace un crawl de noticias de Costa Rica </h1>')
@app.route('/deportes',methods=['GET'])
def noticias_deportes():
    response =scraper_nacion.scraping_nacion_deportes()
    return response
@app.route('/el-pais', methods=['GET'])
def noticias_el_pais():
    response = scraper_nacion.scraping_nacion_pais()
    return response 
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()