# API Simple que sirve un modelo para la prevención del Churn

API Simple que sirve un modelo para la prevención del Churn. Este proyecto utiliza Python y Flask para proveer una API que permite predecir la probabilidad de que un cliente abandone una compañía o servicio (Churn).

## Tecnologías usadas
- **Python**: Lenguaje de programación utilizado.
- **Flask**: Librería minimalista para el provisionamiento de APIs.
- **scikit-learn**: Librería de aprendizaje automático.
- **pickle**: Librería para cargar y guardar variables en memoria.

## Instalación Local

Esta API requiere Python y las librerías señaladas en el `requirements.txt`.

1. Clonar el repositorio.
2. Instalar las dependencias necesarias:

pip install -r requirements.txt

3. Ejecutar la API:
python app.py


### Verificar que la API está corriendo exitosamente

Para confirmar que la API funciona correctamente, puedes enviar una solicitud de prueba:

curl --location --request GET 'http://localhost:3001/query?feats=465,France,Female,51,8,122522.32,1,0,0,181297.65'


Si todo está bien, deberías obtener una respuesta como la siguiente:

{"response": [1]}


## Organización del Proyecto

El proyecto sigue la siguiente estructura:

- **data**: Directorio para los datos utilizados y generados.
- **models**: Contiene los modelos entrenados y serializados.
- **notebooks**: Jupyter notebooks para exploración y análisis.
- **src**: Código fuente para el proyecto.
- **requirements.txt**: Dependencias del proyecto.

(Descripción detallada de la estructura de directorios...)

## Equipo

- Juan Perez Nombrefalso
- Ricardo Alanís Tamez

## Contribuir

Para contribuir al proyecto, por favor haz un fork del repositorio y envía un pull request con tus cambios propuestos.

---

Project based on the [cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science/). #cookiecutterdatascience