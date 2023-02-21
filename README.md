![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)

El siguiente contenido es una guía para poder seguir el trabajo realizado por **Marcos Larran** para el **Proyecto Individual - 01** de SoyHenry.

## Contenido

El contenido va a ser listado en el orden dicatado por las consignas del proyecto.

* **MLOpsReviews**
    En esta carpeta se encuentra toda la data necesaria para realizar el proyecto. Toda esta en formato csv. Se listan los archivos a continuación:
    - amazon_prime_titles.csv
    - disney_plus_titles.csv
    - hulu_titles.csv
    - netflix_titles.csv
    - ratings: carpeta que cuenta con 8 archivos csv (numerados del 1 al 8) con las puntuaciones de los programas de las 4 plataformas.
    
    Todo esto fue entregado por Henry.

* **Data Engineering y funciones.ipynb**
    En este notebook se encuentran todas las transformaciones solicitadas para los datasets de las plataformas de streaming asi también como una primera inspección de los ratings de los usuarios. Se crearon y probaron las funciones con las que cuenta la API.

* **plataformas_API.csv**
    Este archivo csv fue creado en el notebook Data Engineering y funciones en el que se encuentra solamente el contenido necesario para que la API pueda realizar las funciones requeridas. Esto tiene el fin de que el dataset sea lo mas liviano posible y la aplicación funcione lo mejor posible. Fue cargado en un Google Drive público de donde la API toma los datos.

* **rankings.csv**
    Archivo creado en el notebook Data Engineering y funciones que une los 8 csv con los puntajes de los usuarios y donde se encuentra transformada la columna timestamp a la fecha en la que se valoró el programa. El único fin que persigue es el de simplificar la carga de los datos durante el análisis exploratorio de los mismos.

* **API**
    Carpeta donde se encuentran solamente los archivos necesarios para el funcionamiento de la API de consultas. Estos son:
    - main.py: Código de la API.
    - requirements.txt: Listado de módulos necesarios para el funcionamiento de la API.
    - .space: Carpeta creada por Deta Space. Necesaria para el deploy de la API.
    - Spacefile: Archivo creado por Deta Space. Necesario para el deploy de la API.

    No hay ningún archivo que no sea necesario para la creación/deploy de la API.

* **Analisis exploratorio de datos.ipynb**
    Notebook donde se realiza un pequeño análisis de los csv con las valoraciones de los usuarios acerca de los programas de las plataformas de streaming.

* **ratings.parquet**
    Archivo en formato parquet creado en el notebook del EDA para alivianar la llamada desde el notebook Sistema de recomendación.

* **Sistema de recomendación.ipynb**
    Notebook donde se realiza la optimización de hiperparámetros, el entrenamiento y se crea la función para realizar la recomendación.

* **sistema_recomendacion.joblib**
    Modelo ya entrenado para importarlo y realizar las predicciones. Se creó en el notebook Sistema de recomendación.ipynb.

* **Usuarios posibles.csv**
    Archivo creado en Sistema de recomendacion que contiene un listado de los usuarios con los que se pudo entrenar el modelo.

* **predicciones.ipynb**
    Archivo donde se probó el modelo con algunas predicciones.

* **API 2**
    Carpeta que contiene:
    - main.py: Código de la API.