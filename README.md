<br />

<p align="center">


  <h3 align="center">Machine learning model lab</h3>

  <p align="center">
    Reto escuela de ciencia de datos Platzi.
    <br />
    <br />
</p>

## Introducción

El reto consiste en realizar mejoras a un modelo de machine learning de aprendizaje supervisado de clasificación, el cual busca predecir la variable "Churn" (Renuncia voluntaria de los servicios contratados) de un dataset de clientes perteneciente a una empresa de telecomunicaciones.

Y por ende también se hace necesario modificar el script de la API (Flask) con la que se realiza las predicciones del modelo.

A continuacion se encuentra el README original del repositorio del laboratorio/reto.

---
---
# laboratorio-machine-learning
API Simple que sirve un modelo para la prevención del Churn

## Tecnologías usadas
This API uses a number of open source projects to work properly:

* [Python] - Lenguaje de programación
* [Flask] - Libreria minimalista para el provisionamiento de APIs
* [scikit-learn] - Libreria de aprendizaje automatico
* [pickle] - Libreria para cargar y guardar variables en memoria

## Instalación Local
Esta API requiere Python y las librerias señaladas en el requirements.txt

1. Clonar repositorio
2. Correr la api, ejecutando desde la carpeta de proyecto

```
python app.py
```

#### Verificar que la app esta corriendo exitosamente

La api se verifica mandando un ejemplo para confirmar que esta funcionando correctamente

```
curl --location --request GET 'http://localhost:3001/query?feats=465,France,Female,51,8,122522.32,1,0,0,181297.65'
```

Si todo esta bien, deberías de obtener una respuesta así
```
{"response": [1]}
```

#### Equipo

* Juan Perez Nombrefalso
* Ricardo Alanís Tamez


