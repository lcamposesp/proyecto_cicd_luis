import scraper_nacion
def test_scraper_return_deportes():
    response = scraper_nacion.scraping_nacion_deportes()
    assert "Deportes" in response
def test_scraper_return_pais():
    response = scraper_nacion.scraping_nacion_pais()
    assert "El Pais" in response