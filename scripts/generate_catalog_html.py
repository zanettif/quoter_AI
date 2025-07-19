import csv
from pathlib import Path

INPUT_CSV = Path(r"C:\\Users\\FrancoZanetti\\OneDrive - LIESA\\LIESA\\13. quoter_AI\\quoter_AI\\data\\productos.csv")
OUTPUT_HTML = Path(r"C:\\Users\\FrancoZanetti\\OneDrive - LIESA\\LIESA\\13. quoter_AI\\quoter_AI\\catalogo.html")

with INPUT_CSV.open(newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    with OUTPUT_HTML.open("w", encoding="utf-8") as f:
        f.write("<!DOCTYPE html><html><head><meta charset='UTF-8'>\n")
        f.write("<title>Catálogo Copilot</title>\n")
        f.write("<meta name='robots' content='noindex'>\n")
        f.write("</head><body>\n")
        f.write("<h1>Catálogo LIESA – Generado para Copilot</h1>\n")

        for row in reader:
            nombre = row.get("productName", "Producto sin nombre")
            sku = row.get("SKU", "N/A")
            mpn = row.get("MPN", "N/A")
            precio = row.get("price", "N/D")
            stock = row.get("stock", "Sin datos")

            f.write(f"<h2>{nombre}</h2>\n")
            f.write("<ul>\n")
            f.write(f"<li>SKU: {sku}</li>\n")
            f.write(f"<li>MPN: {mpn}</li>\n")
            f.write(f"<li>Precio: ${precio}</li>\n")
            f.write(f"<li>Stock: {stock} unidades</li>\n")
            f.write("</ul>\n")

        f.write("</body></html>")
