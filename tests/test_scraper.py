from pyparsing import empty
from api.scrapers.scraper_nacion import *
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
def test_scraper_return_nacion_for_index():
    returned_data = scraping_nacion_elpais_for_index()
    assert returned_data.values() is not empty
def test_scraper_return_nacion_for_index():
    returned_data = scraping_nacion_mundo_for_index()
    assert returned_data.values() is not empty

# More tests need to be added to validate the extra content that is being added. An example test case could be
# def test_scraper_return_extra_content_deportes():
#   returned_Data = more_content_deportes()
#   assert returned_data is not empty 