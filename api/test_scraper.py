import scraper_nacion
def test_scraper_return():
    response = scraper_nacion.scraping_nacion_deportes()
    string_with_title = response[0] 
    assert "https://www.nacion.com" in string_with_title