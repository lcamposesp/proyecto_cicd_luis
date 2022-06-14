from flask import Flask,jsonify,render_template,url_for
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from pathlib import Path
import os

def create_app():
    # Setup of the application, passing down the location of the templates file that contains the HTML code
    app = Flask(__name__,template_folder='templates')
    Bootstrap(app)
    # loading env files
    load_dotenv()
    env_path = Path('.')/'.env'
    load_dotenv(dotenv_path=env_path)
    # Key loading for project to run
    SECRET_KEY = os.getenv("SECRET_KEY")

    app.config['SECRET_KEY'] = SECRET_KEY    
    # Import of API methhods that will be used and variable initialization to avoid calls each time the route changes
    # The content being initialized below contains titles and their respective URLs which are a dictionary that will get passed to each HTML template
    from api.scrapers import scraper_nacion
    content_deportes = scraper_nacion.scraping_nacion_deportes_for_index()
    content_elpais = scraper_nacion.scraping_nacion_elpais_for_index()
    content_mundo = scraper_nacion.scraping_nacion_mundo_for_index()
    content_tecnologia = scraper_nacion.scraping_nacion_tecnologia_for_index()
    content_economia = scraper_nacion.scraping_nacion_economia_for_index()

    # In order for more content to be passed, different methods had to be created in scraper_nacion.py to get that as a list. The list is whaty we are passing down to these variables

    extra_content_deportes = scraper_nacion.more_content_deportes()

    @app.route('/')
    def hello_world():
        return render_template('homepage/homepage.html')
    @app.route('/deportes',methods=['GET'])
    def noticias_deportes():
        return render_template('homepage/deportes.html',content=content_deportes,extra_content_deportes=extra_content_deportes)
    @app.route('/elpais', methods=['GET'])
    def noticias_el_pais():
        return render_template('homepage/elpais.html',content=content_elpais)
    @app.route('/mundo')
    def noticias_mundo():
        return render_template('homepage/mundo.html',content=content_mundo)
    @app.route('/tecnologia')
    def noticias_tecnologia():
        return render_template('homepage/tecnologia.html',content=content_tecnologia)
    @app.route('/economia')
    def noticias_economia():
        return render_template('homepage/economia.html',content=content_economia)
    return app

app = create_app()
crsf = CSRFProtect()
crsf.init_app(app)
if __name__ == '__main__':
    app.run(debug=False)