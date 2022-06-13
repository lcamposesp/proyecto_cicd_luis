from flask import Flask,jsonify,render_template,url_for
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
from pathlib import Path
import os

def create_app():
    app = Flask(__name__,template_folder='templates')
    Bootstrap(app)
    # loading env files
    load_dotenv()
    env_path = Path('.')/'.env'
    load_dotenv(dotenv_path=env_path)

    SECRET_KEY = os.getenv("SECRET_KEY")
    app.config['SECRET_KEY'] = SECRET_KEY

    @app.route('/')
    def hello_world():
        return render_template('homepage/homepage.html')
    @app.route('/deportes',methods=['GET'])
    def noticias_deportes():
        from api.scrapers import scraper_nacion
        content =scraper_nacion.scraping_nacion_deportes_for_index()
        return render_template('homepage/deportes.html',content=content)
    @app.route('/elpais', methods=['GET'])
    def noticias_el_pais():
        from api.scrapers import scraper_nacion
        content = scraper_nacion.scraping_nacion_elpais_for_index()
        return render_template('homepage/deportes.html',content=content)
    @app.route('/mundo')
    def noticias_mundo():
        from api.scrapers import scraper_nacion
        content = scraper_nacion.scraping_nacion_mundo_for_index()
        return render_template('homepage/mundo.html',content=content)
    @app.route('/tecnologia')
    def noticias_tecnologia():
        from api.scrapers import scraper_nacion
        content = scraper_nacion.scraping_nacion_tecnologia_for_index()
        return render_template('homepage/tecnologia.html',content=content)
        
    return app
app = create_app()
if __name__ == '__main__':
    app.run(debug=False)