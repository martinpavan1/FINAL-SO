#Imagen base
FROM python:3.8-slim

# Instalacion apache y wsgi
RUN apt-get update && apt-get install -y \
    apache2 \
    libapache2-mod-wsgi-py3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

#Directorio de trabajo
WORKDIR /var/www/flask_app

# Copia los archivos al contenedor 
COPY . /var/www/flask_app

RUN pip install --no-cache-dir -r requirements.txt


# Creacion del .conf de Apache
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf

#Expone puerto 80'
EXPOSE 80

CMD ["apache2ctl", "-D", "FOREGROUND"]