from flask import Flask,jsonify
from api import scraper_nacion


application = Flask(__name__)
SECRET_KEY = '1393459340023492'
application.config['SECRET_KEY'] = SECRET_KEY

@application.route('/')
def hello_world():  
        return('<h1>API Sencilla de Flask que hace un crawl de noticias de Costa Rica </h1>')
@application.route('/deportes',methods=['GET'])
def noticias_deportes():
    response =scraper_nacion.scraping_nacion_deportes()
    return response
@application.route('/el-pais', methods=['GET'])
def noticias_el_pais():
    response = scraper_nacion.scraping_nacion_pais()
    return response 
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()