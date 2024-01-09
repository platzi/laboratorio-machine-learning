# Utilizar una imagen base oficial de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Instalar git, gcc y python3-dev
RUN apt-get update && \
    apt-get install -y git gcc python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copiar el archivo de dependencias y luego instalarlas
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 3001

# Comando para ejecutar la aplicación
CMD ["python", "/app/src/app.py"]
