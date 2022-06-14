from flask import Flask,jsonify,render_template,url_for
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from pathlib import Path
from apscheduler.scheduler import Scheduler
import os
import atexit



def create_app():
    cron = Scheduler(daemon=True)
    # Explicitly kick off the background thread
    cron.start()
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

    # In order for more content to be passed, different methods had to be created in scraper_nacion.py to get that as a list. The list is whaty we are passing down to these variables
    
    # =================================== Jobs that run every 2 hours to update content ===================================== #
    #@cron.interval_schedule(hours=2)
    def get_content_deportes_titles_url():
        from api.scrapers import scraper_nacion
        content_deportes = scraper_nacion.scraping_nacion_deportes_for_index()
        return content_deportes

    #@cron.interval_schedule(hours=2)
    def get_extra_content_deportes():
        from api.scrapers import scraper_nacion
        extra_content_deportes = scraper_nacion.more_content_deportes()
        return extra_content_deportes
    
    #@cron.interval_schedule(hours=2)
    def get_content_elpais_titles_url():
        from api.scrapers import scraper_nacion
        content_elpais = scraper_nacion.scraping_nacion_elpais_for_index()
        return content_elpais

    #@cron.interval_schedule(hours=2)
    def get_content_mundo_titles_url():
        from api.scrapers import scraper_nacion
        content_mundo = scraper_nacion.scraping_nacion_mundo_for_index()
        return content_mundo

    #@cron.interval_schedule(hours=2)
    def get_content_tecnologia_titles_url():
        from api.scrapers import scraper_nacion
        content_tecnologia = scraper_nacion.scraping_nacion_tecnologia_for_index()
        return content_tecnologia
    #@cron.interval_schedule(hours=2)
    def get_content_economia_titles_url():
        from api.scrapers import scraper_nacion
        content_economia = scraper_nacion.scraping_nacion_economia_for_index()
        return content_economia
    # =================================== Jobs that run every 2 hours to update content ====================================== #
    @app.route('/')
    def hello_world():
        return render_template('homepage/homepage.html')

    @app.route('/deportes',methods=['GET'])
    def noticias_deportes():
        return render_template('homepage/deportes.html',content=get_content_deportes_titles_url(),extra_content_deportes=get_extra_content_deportes())

    @app.route('/elpais', methods=['GET'])
    def noticias_el_pais():
        return render_template('homepage/elpais.html',content=get_content_elpais_titles_url())

    @app.route('/mundo')
    def noticias_mundo():
        return render_template('homepage/mundo.html',content=get_content_mundo_titles_url())

    @app.route('/tecnologia')
    def noticias_tecnologia():
        return render_template('homepage/tecnologia.html',content=get_content_tecnologia_titles_url())

    @app.route('/economia')
    def noticias_economia():
        return render_template('homepage/economia.html',content=get_content_economia_titles_url())

    atexit.register(lambda: cron.shutdown(wait=False))
    return app

app = create_app()
crsf = CSRFProtect()
crsf.init_app(app)
if __name__ == '__main__':
    app.run(debug=False)