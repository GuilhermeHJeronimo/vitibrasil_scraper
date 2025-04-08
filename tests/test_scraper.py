
from app.services.scraper.scraper import scrape_table

def test_scrape():
    url = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02"
    result = scrape_table(url)
    assert result["status"] == "success"
    assert result["rows_collected"] > 0

