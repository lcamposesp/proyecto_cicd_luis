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
    

    # =================================== Methods that actually do the scraping ====================================== #

    @app.route('/')
    def hello_world():
        return render_template('homepage/homepage.html')

    @app.route('/deportes',methods=['GET'])
    def noticias_deportes():
        from api.scrapers import scraper_nacion
        content_deportes = scraper_nacion.scraping_nacion_deportes_for_index()
        extra_content = scraper_nacion.more_content_deportes()
        return render_template('homepage/deportes.html',content=content_deportes,extra_content=extra_content)

    @app.route('/elpais', methods=['GET'])
    def noticias_el_pais():
        from api.scrapers import scraper_nacion
        content_elpais = scraper_nacion.scraping_nacion_elpais_for_index()
        extra_content = scraper_nacion.more_content_el_pais()
        return render_template('homepage/elpais.html',content=content_elpais,extra_content=extra_content)

    @app.route('/mundo')
    def noticias_mundo():
        from api.scrapers import scraper_nacion
        content_mundo = scraper_nacion.scraping_nacion_mundo_for_index()
        extra_content = scraper_nacion.more_content_el_mundo()
        return render_template('homepage/mundo.html',content=content_mundo,extra_content=extra_content)

    @app.route('/tecnologia')
    def noticias_tecnologia():
        from api.scrapers import scraper_nacion
        content_tecnologia = scraper_nacion.scraping_nacion_tecnologia_for_index()
        extra_content = scraper_nacion.more_content_tecnologia()
        return render_template('homepage/tecnologia.html',content=content_tecnologia,extra_content=extra_content)

    @app.route('/economia')
    def noticias_economia():
        from api.scrapers import scraper_nacion
        content_economia = scraper_nacion.scraping_nacion_economia_for_index()
        extra_content = scraper_nacion.more_content_economia()
        return render_template('homepage/economia.html',content=content_economia,extra_content=extra_content)
    
    @app.route('/cultura')
    def noticias_cultura():
        from api.scrapers import scraper_nacion
        content = scraper_nacion.scraping_nacion_cultura_for_index()
        extra_content = scraper_nacion.more_content_cultura()
        return render_template('homepage/cultura.html',content=content,extra_content=extra_content)

    @app.route('/entretenimiento')
    def noticias_entretenimiento():
        from api.scrapers import scraper_nacion
        content = scraper_nacion.scraping_nacion_entretenimiento_for_index()
        extra_content = scraper_nacion.more_content_entretenimiento()
        return render_template('homepage/entretenimiento.html',content=content,extra_content=extra_content)

    @app.route('/economia_ef')
    def noticias_economiaef():
        from api.scrapers import scraper_elfinanciero
        content_economia = scraper_elfinanciero.scraping_elfinanciero_economia_for_index()
        extra_content = scraper_elfinanciero.more_content_economiaef()
        return render_template('homepage/economia_ef.html',content=content_economia, extra_content = extra_content)

    @app.route('/opinion_ef')
    def noticias_opinionef():
        from api.scrapers import scraper_elfinanciero
        content_opinion = scraper_elfinanciero.scraping_elfinanciero_opinion_for_index()
        extra_content = scraper_elfinanciero.more_content_opinionef()
        return render_template('homepage/opinion_ef.html',content=content_opinion, extra_content = extra_content)

    @app.route('/pymes_ef')
    def noticias_pymesef():
        from api.scrapers import scraper_elfinanciero
        content_pymes = scraper_elfinanciero.scraping_elfinanciero_pymes_for_index()
        extra_content = scraper_elfinanciero.more_content_pymesef()
        return render_template('homepage/pymes_ef.html',content=content_pymes, extra_content = extra_content)

    @app.route('/tecnologia_ef')
    def noticias_tecnologiaef():
        from api.scrapers import scraper_elfinanciero
        content_tecnologia = scraper_elfinanciero.scraping_elfinanciero_tecnologia_for_index()
        extra_content = scraper_elfinanciero.more_content_tecnologiaef()
        return render_template('homepage/tecnologia_ef.html',content=content_tecnologia, extra_content = extra_content)
    
    @app.route('/gerencia_ef')
    def noticias_gerenciaef():
        from api.scrapers import scraper_elfinanciero
        content = scraper_elfinanciero.scraping_elfinanciero_gerencia_for_index()
        extra_content = scraper_elfinanciero.more_content_gerenciaef()
        return render_template('homepage/gerencia.html',content=content, extra_content = extra_content)
    
    @app.route('/negocios_ef')
    def noticias_negociosef():
        from api.scrapers import scraper_elfinanciero
        content = scraper_elfinanciero.scraping_elfinanciero_negocios_for_index()
        extra_content = scraper_elfinanciero.more_content_negociosef()
        return render_template('homepage/negocios.html',content=content, extra_content = extra_content)
    
    @app.route('/finanzas_ef')
    def noticias_finanzasef():
        from api.scrapers import scraper_elfinanciero
        content= scraper_elfinanciero.scraping_elfinanciero_finanzas_for_index()
        extra_content = scraper_elfinanciero.more_content_finanzasef()
        return render_template('homepage/finanzas.html',content=content, extra_content = extra_content)

    return app

app = create_app()
if __name__ == '__main__':
    # CRSF is used in order to protect the page against vulnerabilities #
    crsf = CSRFProtect()
    crsf.init_app(app)
    app.run(debug=False)