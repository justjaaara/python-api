# Se indica la versión de python que correrá cuando se ejecute el contenedor 
FROM python:3.7.11-slim

# Se establece la carpeta mencionada como espacio de trabajo 
WORKDIR  /python-api

# Se copia las dependencias de local al contenedor
COPY requirements.txt requirements.txt

# Se instalan las dependencias anteriormente copiadas para ejecutar el proyecto
RUN pip install -r requirements.txt

# Se copia la carpeta raíz a el directiorio razi del contenedor
COPY . .

# Al iniciar el contenedor se ejecutará los siguientes comandos

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
