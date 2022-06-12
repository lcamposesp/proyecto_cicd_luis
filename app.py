from flask import Flask,jsonify,render_template

from dotenv import load_dotenv
from pathlib import Path
import os

def create_app():
    app = Flask(__name__)

    # loading env files
    load_dotenv()
    env_path = Path('.')/'.env'
    load_dotenv(dotenv_path=env_path)

    SECRET_KEY = os.getenv("SECRET_KEY")
    app.config['SECRET_KEY'] = SECRET_KEY

    @app.route('/')
    def hello_world():
        from api.scrapers import scraper_nacion
        content =   scraper_nacion.scraping_nacion_deportes_for_index()
        return render_template('homepage/homepage.html',content=content)
    @app.route('/deportes',methods=['GET'])
    def noticias_deportes():
        from api.scrapers import scraper_nacion
        response =scraper_nacion.scraping_nacion_deportes()
        return response
    @app.route('/el-pais', methods=['GET'])
    def noticias_el_pais():
        from api.scrapers import scraper_nacion
        response = scraper_nacion.scraping_nacion_pais()
        return response
    return app
