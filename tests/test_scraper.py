from api.scrapers.scraper_nacion import scraping_nacion_deportes,scraping_nacion_mundo,scraping_nacion_pais,scraping_nacion_tecnologia
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