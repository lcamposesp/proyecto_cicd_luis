# RapinoticiasCR

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=rapinoticiascr2022os&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=rapinoticiascr2022os)

Pagina web que provee a los usuarios con resumenes rapidos ademas del link a las noticias de diversos medios en Costa Rica. Las rapinoticias como se ven en la pagina web, tienen tres partes:
  - Titulo
  - Link a la noticias
  - Resumen corto de la misma (WIP)

El proyecto trabaja bajo un marco donde las noticias no contienen ningun tipo de elemento que no este disponible de manera publica. Cualquier persona puede ver esta misma informacion en las paginas de cada uno de los medios, la pagina lo unico que hace es facilitar el verlas. 

De momento la pagina no muestra resultados de otros medios mas que La Nacion, asi que cualquier ayuda es bien recibida. 


Para los colaboradores del repositorio

Para correr el proyecto, se necesita de:
 - Python 3.8 al menos
 - Crear un Python virtualenv. Para mas pasos sobre como crearlo aqui esta la [documentacion]('https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/)
 - Correr dentro de la carpeta root del directorio correr desde la terminal `pip install -r requirements.txt`
 - Para ejecutar los test en la aplicacion correr desde la terminal `pytest` y si se quiere con coverage `coverage run -m pytest` y despues `coverage html` para crear la carpeta htmlcov en la cual se encuentra `index.html` que contiene el reporte
 - Para correr la aplicacion local correr desde la terminal `flask run`

