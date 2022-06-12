from pyparsing import empty
from api.scrapers.scraper_nacion import scraping_nacion_deportes,scraping_nacion_mundo,scraping_nacion_pais,scraping_nacion_tecnologia,scraping_nacion_deportes_for_index
def test_scraper_return_nacion_deportes():
    response = scraping_nacion_deportes()
    assert "Deportes" in response
def test_scraper_return_nacion_pais():
    response = scraping_nacion_pais()
    assert "El Pais" in response
def test_scraper_return_nacion_mundo():
    response = scraping_nacion_mundo()
    assert "El Mundo" in response
def test_scraper_return_nacion_tecnologia():
    response = scraping_nacion_tecnologia()
    assert "Tecnologia" in response
def test_scraper_return_nacion_for_index():
    returned_data = scraping_nacion_deportes_for_index()
    assert returned_data.values() is not empty