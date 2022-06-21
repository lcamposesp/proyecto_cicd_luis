from pyparsing import empty
from api.scrapers.scraper_elfinanciero import *
from api.scrapers.scraper_nacion import *



# Test for titles and url crawlers #
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

def test_scraper_return_nacion_deportes_for_index():
    returned_data = scraping_nacion_deportes_for_index()
    assert returned_data.values() is not empty

def test_scraper_return_nacion_elpais_for_index():
    returned_data = scraping_nacion_elpais_for_index()
    assert returned_data.values() is not empty

def test_scraper_return_nacion_mundo_for_index():
    returned_data = scraping_nacion_mundo_for_index()
    assert returned_data.values() is not empty

def test_scraper_return_nacion_tecnologia_for_index():
    returned_data = scraping_nacion_tecnologia_for_index()
    assert returned_data.values() is not empty

def test_scraper_return_nacion_economia_for_index():
    returned_data = scraping_nacion_economia_for_index()
    assert returned_data.values() is not empty

def test_scraper_return_economia_ef_for_index():
    returned_data = scraping_elfinanciero_economia_for_index()
    assert returned_data.values() is not empty

def test_scraper_return_opinion_ef_for_index():
    returned_data = scraping_elfinanciero_opinion_for_index()
    assert returned_data.values() is not empty

def test_scraper_return_pymes_ef_for_index():
    returned_data = scraping_elfinanciero_pymes_for_index()
    assert returned_data.values() is not empty

def test_scraper_return_tecnologia_ef_for_index():
    returned_data = scraping_elfinanciero_tecnologia_for_index()
    assert returned_data.values() is not empty

# Tests for extra content # 
def test_scraper_return_nacion_deportes_extra_content():
    response = more_content_deportes()
    assert response is not empty
