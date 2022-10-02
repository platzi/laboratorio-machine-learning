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

#### Contribuir

Hacer fork del repositorio y mandar pull request con los cambios propuestos

