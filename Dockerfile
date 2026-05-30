# Utilizar una imagen base oficial y ligera de Python
FROM python:3.10-slim

# Establecer variables de entorno para evitar que Python genere archivos .pyc 
# y para que el log se muestre en tiempo real (unbuffered)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Crear un directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias primero para aprovechar el caché de Docker
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código fuente al contenedor
COPY . .

# Crear el volumen de datos para preservar los logs y procesados
VOLUME ["/app/data", "/app/logs"]

# Comando por defecto para ejecutar la aplicación
CMD ["python", "-m", "src.main"]
