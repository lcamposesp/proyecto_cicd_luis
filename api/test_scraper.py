import scraper_nacion
def test_scraper_return_nacion_deportes():
    response = scraper_nacion.scraping_nacion_deportes()
    assert "Deportes" in response
def test_scraper_return_nacion_pais():
    response = scraper_nacion.scraping_nacion_pais()
    assert "El Pais" in response
def test_scraper_return_nacion_mundo():
    response = scraper_nacion.scraping_nacion_mundo()
    assert "El Mundo" in response
def test_scraper_return_nacion_tecnologia():
    response = scraper_nacion.scraping_nacion_tecnologia()
    assert "Tecnologia" in response