import csv
from pathlib import Path

INPUT_CSV = Path(r"C:\\Users\\FrancoZanetti\\OneDrive - LIESA\\LIESA\\13. quoter_AI\\quoter_AI\\data\\productos.csv")
OUTPUT_HTML = Path(r"C:\\Users\\FrancoZanetti\\OneDrive - LIESA\\LIESA\\13. quoter_AI\\quoter_AI\\catalogo.html")

# Abrir CSV de productos
with INPUT_CSV.open(newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    # Crear archivo HTML de salida
    with OUTPUT_HTML.open("w", encoding="utf-8") as f:
        f.write("<!DOCTYPE html>\n<html>\n<head>\n")
        f.write("<meta charset='UTF-8'>\n")
        f.write("<title>Catálogo Copilot</title>\n")
        f.write("<meta name='robots' content='noindex'>\n")
        f.write("</head>\n<body>\n")
        f.write("<h1>Catálogo LIESA – Formato tabla estructurada</h1>\n")

        # Crear tabla
        f.write("<table border='1' cellspacing='0' cellpadding='5'>\n")
        f.write("<thead><tr>")
        f.write("<th>Nombre</th><th>SKU</th><th>MPN</th><th>Precio</th><th>Stock</th>")
        f.write("</tr></thead>\n<tbody>\n")

        # Agregar productos como filas
        for row in reader:
            f.write("<tr>")
            f.write(f"<td>{row.get('productName', 'Sin nombre')}</td>")
            f.write(f"<td>{row.get('sku', 'N/A')}</td>")
            f.write(f"<td>{row.get('mpn', 'N/A')}</td>")
            f.write(f"<td>${row.get('price', 'N/D')}</td>")
            f.write(f"<td>{row.get('stock', 'Sin datos')} unidades</td>")
            f.write("</tr>\n")

        f.write("</tbody></table>\n</body>\n</html>")