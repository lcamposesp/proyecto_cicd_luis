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

    # =================================== Methods that actually fo the scraping ===================================== #
    # FYI at the moment each time a user changes a route the method for each view gets called and is then passed to the template
    # Due to the nature of the project and the low scale right now its not really a priority. If we are approached by a web letting us know that we are killing their servers then we can start working on this. 
    
    def get_content_deportes_titles_url():
        from api.scrapers import scraper_nacion
        content_deportes = scraper_nacion.scraping_nacion_deportes_for_index()
        return content_deportes

    def get_extra_content_deportes():
        from api.scrapers import scraper_nacion
        extra_content_deportes = scraper_nacion.more_content_deportes()
        return extra_content_deportes
    
    def get_content_elpais_titles_url():
        from api.scrapers import scraper_nacion
        content_elpais = scraper_nacion.scraping_nacion_elpais_for_index()
        return content_elpais

    def get_content_mundo_titles_url():
        from api.scrapers import scraper_nacion
        content_mundo = scraper_nacion.scraping_nacion_mundo_for_index()
        return content_mundo

    def get_content_tecnologia_titles_url():
        from api.scrapers import scraper_nacion
        content_tecnologia = scraper_nacion.scraping_nacion_tecnologia_for_index()
        return content_tecnologia


    def get_content_economia_titles_url():
        from api.scrapers import scraper_nacion
        content_economia = scraper_nacion.scraping_nacion_economia_for_index()
        return content_economia
    
    # Methods pertaining El Financiero #
    # This is what will get the content and pass it to each HTML # 
    def get_content_economiaef_titles_url():
        from api.scrapers import scraper_elfinanciero
        content_economia = scraper_elfinanciero.scraping_elfinanciero_economia_for_index()
        return content_economia
    def get_extra_content_economiaef():
        from api.scrapers import scraper_elfinanciero
        extra_content = scraper_elfinanciero.more_content_economiaef()
        return extra_content
    def get_content_opinionaef_titles_url():
        from api.scrapers import scraper_elfinanciero
        content_opinion = scraper_elfinanciero.scraping_elfinanciero_opinion_for_index()
        return content_opinion
    def get_extra_content_opinionaef():
        from api.scrapers import scraper_elfinanciero
        extra_content = scraper_elfinanciero.more_content_opinionef()
        return extra_content
    
    # =================================== Methods that actually do the scraping ====================================== #

    @app.route('/')
    def hello_world():
        return render_template('homepage/homepage.html')

    @app.route('/deportes',methods=['GET'])
    def noticias_deportes():
        content_deportes = get_content_deportes_titles_url()
        extra_content_deportes = get_extra_content_deportes()
        return render_template('homepage/deportes.html',content=content_deportes,extra_content_deportes=extra_content_deportes)

    @app.route('/elpais', methods=['GET'])
    def noticias_el_pais():
        content_elpais = get_content_elpais_titles_url()
        return render_template('homepage/elpais.html',content=content_elpais)

    @app.route('/mundo')
    def noticias_mundo():
        content_mundo = get_content_mundo_titles_url()
        return render_template('homepage/mundo.html',content=content_mundo)

    @app.route('/tecnologia')
    def noticias_tecnologia():
        content_tecnologia = get_content_tecnologia_titles_url()
        return render_template('homepage/tecnologia.html',content=content_tecnologia)

    @app.route('/economia')
    def noticias_economia():
        content_economia = get_content_economia_titles_url()
        return render_template('homepage/economia.html',content=content_economia)

    @app.route('/economia_ef')
    def noticias_economiaef():
        content_economia = get_content_economiaef_titles_url()
        extra_content = get_extra_content_economiaef()
        return render_template('homepage/economia_ef.html',content=content_economia, extra_content = extra_content)

    @app.route('/opinion_ef')
    def noticias_opinionef():
        content_opinion = get_content_opinionaef_titles_url()
        extra_content = get_extra_content_opinionaef()
        return render_template('homepage/economia_ef.html',content=content_opinion, extra_content = extra_content)

    return app

app = create_app()
if __name__ == '__main__':
    crsf = CSRFProtect()
    crsf.init_app(app)
    app.run(debug=False)