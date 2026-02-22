#!/usr/bin/env python3
"""
Genera un PDF con apariencia de factura y un mensaje emergente (popup) al abrirlo.
Corregido: uso correcto de operadores de texto (desplazamientos relativos).
Uso: python popup_factura_corregido.py "Mensaje de alerta" archivo_salida.pdf
"""

import sys

def generar_pdf_factura(mensaje, archivo_salida):
    mensaje_js = mensaje.replace('"', '\\"')

    # Estructura del PDF con offsets fijos (calculados para este contenido)
    pdf = f"""%PDF-1.4
%âãÏÓ

# Catálogo
1 0 obj
<< /Type /Catalog
   /Pages 3 0 R
   /OpenAction 5 0 R
>>
endobj

# Outlines vacío
2 0 obj
<< /Type /Outlines /Count 0 >>
endobj

# Páginas
3 0 obj
<< /Type /Pages
   /Kids [4 0 R]
   /Count 1
>>
endobj

# Página
4 0 obj
<< /Type /Page
   /Parent 3 0 R
   /MediaBox [0 0 612 792]
   /Resources << /Font << /F1 6 0 R >> >>
   /Contents 7 0 R
>>
endobj

# Acción JavaScript
5 0 obj
<< /Type /Action
   /S /JavaScript
   /JS (app.alert("{mensaje_js}");)
>>
endobj

# Fuente Helvetica
6 0 obj
<< /Type /Font
   /Subtype /Type1
   /BaseFont /Helvetica
   /Encoding /WinAnsiEncoding
>>
endobj

# Stream de contenido (factura)
7 0 obj
<< /Length 1200 >>
stream
BT
  /F1 24 Tf
  50 750 Td
  (EMPRESA DE EJEMPLO S.A.) Tj

  /F1 14 Tf
  0 -30 Td          # Baja 30 unidades
  (FACTURA N°: 2025-001) Tj

  /F1 12 Tf
  0 -25 Td
  (FECHA: 22/02/2025) Tj
  0 -20 Td
  (CLIENTE: Juan Perez) Tj
  0 -20 Td
  (RUT: 12.345.678-9) Tj

  # Cabecera de tabla
  /F1 14 Tf
  0 -30 Td
  (DESCRIPCION) Tj
  200 0 Td          # Desplazamiento horizontal de 200 puntos
  (CANT.) Tj
  100 0 Td
  (P.UNIT.) Tj
  100 0 Td
  (TOTAL) Tj

  /F1 12 Tf
  # Producto 1
  -400 -30 Td       # Volver a la izquierda y bajar
  (Laptop HP Pavilion) Tj
  200 0 Td
  (2) Tj
  100 0 Td
  ($450.00) Tj
  100 0 Td
  ($900.00) Tj

  # Producto 2
  -400 -20 Td
  (Mouse Inalambrico) Tj
  200 0 Td
  (5) Tj
  100 0 Td
  ($12.50) Tj
  100 0 Td
  ($62.50) Tj

  # Producto 3
  -400 -20 Td
  (Teclado Mecanico) Tj
  200 0 Td
  (1) Tj
  100 0 Td
  ($85.00) Tj
  100 0 Td
  ($85.00) Tj

  # Línea separadora
  -400 -30 Td
  0 0 Td
  (__________________________________________________) Tj

  # Totales
  /F1 14 Tf
  -200 -25 Td       # Mover a la derecha y bajar
  (SUBTOTAL:) Tj
  100 0 Td
  ($1047.50) Tj

  -200 -20 Td
  (IVA 19%:) Tj
  100 0 Td
  ($199.03) Tj

  -200 -20 Td
  (TOTAL:) Tj
  100 0 Td
  ($1246.53) Tj

  # Pie de página
  /F1 10 Tf
  -300 -50 Td
  (Gracias por su compra. Este documento es una simulacion con fines educativos.) Tj
ET
endstream
endobj

xref
0 8
0000000000 65535 f
0000000020 00000 n
0000000135 00000 n
0000000200 00000 n
0000000280 00000 n
0000000455 00000 n
0000000580 00000 n
0000000685 00000 n

trailer
<< /Size 8
   /Root 1 0 R
>>
startxref
1740
%%EOF
"""
    with open(archivo_salida, "wb") as f:
        f.write(pdf.encode("latin-1"))
    print(f"[+] PDF generado: {archivo_salida}")

def main():
    if len(sys.argv) != 3:
        print("Uso: python popup_factura_corregido.py \"<mensaje>\" <archivo_salida.pdf>")
        sys.exit(1)
    mensaje = sys.argv[1]
    archivo = sys.argv[2] if sys.argv[2].endswith(".pdf") else sys.argv[2] + ".pdf"
    generar_pdf_factura(mensaje, archivo)

if __name__ == "__main__":
    main()
