🧾 ## Generador de PDF con Factura y Popup Educativo
Este script en Python genera un archivo PDF que simula una factura comercial legítima y, al abrirse, ejecuta automáticamente un mensaje emergente (popup) mediante JavaScript. Está diseñado exclusivamente para fines educativos y de concientización sobre los riesgos de seguridad asociados a la ejecución automática de código en documentos PDF.

🎯 Características
Genera un PDF con una factura ficticia (con productos, cantidades, precios y totales).

Incluye un JavaScript que muestra un cuadro de diálogo con un mensaje personalizado al abrir el archivo.

Utiliza operadores PDF estándar (texto, fuentes, posicionamiento relativo).

No requiere dependencias externas (solo Python 3).

Compatible con cualquier lector PDF que soporte JavaScript (Adobe Reader, Foxit, etc.).

📋 Requisitos
Python 3.6 o superior.

Ninguna librería adicional.

🚀 Uso
Guarda el script como popup_factura.py.

Ejecuta desde la terminal:

bash
python popup_factura.py "Tu mensaje aquí" nombre_archivo.pdf
Argumentos
"mensaje" (obligatorio): texto que aparecerá en el popup. Debe ir entre comillas.

nombre_archivo.pdf (obligatorio): nombre del archivo de salida (si no tiene extensión .pdf, se agrega automáticamente).

📌 Ejemplos
bash
# Mensaje simple
python popup_factura.py "¡Cuidado! Esto es una simulación" factura_aviso.pdf

# Mensaje con comillas escapadas automáticamente
python popup_factura.py "Alerta: \"No abras archivos sospechosos\"" ejemplo.pdf
Al abrir factura_aviso.pdf con Adobe Reader, verás la factura y un popup como este:

https://i.imgur.com/placeholder.png (reemplazar con imagen real)

🔍 Explicación del código
El PDF se construye manualmente mediante una cadena de texto que sigue la especificación PDF. Los objetos principales son:

Objeto 1 (Catalog): raíz del documento, define la acción de apertura (/OpenAction) que apunta al objeto 5.

Objeto 5 (Action): contiene el JavaScript (app.alert).

Objeto 7 (Stream): incluye los comandos de dibujo de la factura (fuentes, texto, posiciones).

Tabla xref y trailer: permiten la navegación interna del archivo.

Los desplazamientos de texto se realizan con operadores Td relativos, lo que garantiza que todo el contenido se visualice correctamente.

🛡️ Análisis de seguridad
Puedes inspeccionar el PDF generado con herramientas como las de Didier Stevens:

bash
# Ver estadísticas rápidas
pdfid factura_aviso.pdf

# Extraer el objeto JavaScript
pdf-parser -o 5 -f dump factura_aviso.pdf

# Ver el contenido de la página (stream)
pdf-parser -o 7 -f dump factura_aviso.pdf
Esto revelará la presencia de /OpenAction, /JavaScript y el código del popup, demostrando cómo un documento aparentemente inofensivo puede ejecutar acciones automáticas.

⚠️ Advertencia
Este script es únicamente para fines educativos y no debe utilizarse para actividades maliciosas. La ejecución automática de JavaScript en PDF puede ser explotada por atacantes para distribuir malware. Utilízalo en entornos controlados para concienciar sobre:

Los peligros de abrir archivos adjuntos de fuentes no confiables.

La necesidad de mantener actualizados los lectores PDF.

La opción de deshabilitar JavaScript en programas como Adobe Reader (Edición → Preferencias → JavaScript).

🤝 Contribuciones
Las sugerencias y mejoras son bienvenidas. Si encuentras algún error o deseas ampliar la funcionalidad (por ejemplo, incluir imágenes o tablas más complejas), no dudes en abrir un issue o enviar un pull request.

📄 Licencia
Este proyecto se distribuye bajo la licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente, siempre que se mantenga el aviso de copyright y la limitación de responsabilidad.
