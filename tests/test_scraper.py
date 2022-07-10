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

def test_scraper_return_nacion_cultura_for_index():
    returned_data = scraping_nacion_cultura_for_index()
    assert returned_data.values() is not empty

def test_scraper_return_nacion_entretenimiento_for_index():
    returned_data = scraping_nacion_entretenimiento_for_index()
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

def test_scraper_return_gerencia_ef_for_index():
    returned_data = scraping_elfinanciero_gerencia_for_index()
    assert returned_data.values() is not empty

def test_scraper_return_negocios_ef_for_index():
    returned_data = scraping_elfinanciero_negocios_for_index()
    assert returned_data.values() is not empty

def test_scraper_return_finanzas_ef_for_index():
    returned_data = scraping_elfinanciero_finanzas_for_index()
    assert returned_data.values() is not empty

# Tests for extra content # 
def test_scraper_return_nacion_deportes_extra_content():
    response = more_content_deportes()
    assert response is not empty

def test_scraper_return_nacion_pais_extra_content():
    response =  more_content_el_pais()
    assert response is not empty

def test_scraper_return_nacion_tecnologia_extra_content():
    response =  more_content_tecnologia()
    assert response is not empty

def test_scraper_return_nacion_economia_extra_content():
    response =  more_content_economia()
    assert response is not empty

def test_scraper_return_nacion_mundo_extra_content():
    response = more_content_el_mundo()
    assert response is not empty

def test_scraper_return_nacion_cultura_extra_content():
    response = more_content_cultura()
    assert response is not empty

def test_scraper_return_nacion_entretenimiento_extra_content():
    response = more_content_entretenimiento()
    assert response is not empty

def test_scraper_return_ef_economia_extra_content():
    response = more_content_economiaef()
    assert response is not empty

def test_scraper_return_ef_pymes_extra_content():
    response = more_content_pymesef()
    assert response is not empty

def test_scraper_return_ef_tecnologia_extra_content():
    response = more_content_tecnologiaef()
    assert response is not empty

def test_scraper_return_ef_opinion_extra_content():
    response = more_content_opinionef()
    assert response is not empty

def test_scraper_return_ef_gerencia_extra_content():
    response = more_content_gerenciaef()
    assert response is not empty

def test_scraper_return_ef_negocios_extra_content():
    response = more_content_negociosef()
    assert response is not empty

def test_scraper_return_ef_finanzas_extra_content():
    response = more_content_finanzasef()
    assert response is not empty