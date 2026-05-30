# PulseFlow 🚀

**Sistema Automatizado de Alertas e Integración de Datos.**

## Descripción
PulseFlow es una solución de monitoreo automatizada diseñada para procesar orígenes de datos y enviar notificaciones instantáneas.

## Problema que resuelve
En entornos críticos y de alta disponibilidad, es fácil perder de vista alertas importantes ocultas en grandes volúmenes de datos. PulseFlow automatiza la filtración, previene duplicados y notifica instantáneamente, asegurando respuestas rápidas.

## Caso de Uso en El Salvador
Ideal para instituciones financieras, clínicas u ONGs locales que manejan grandes bases de datos (ej: registros hospitalarios, caídas de cajeros automáticos) y necesitan escalar operaciones de TI sin presupuestos masivos para sistemas complejos. 

## Tecnologías Utilizadas
- Python 3.10+
- Pandas (Procesamiento de datos eficiente)
- Requests (Llamadas a API)
- Python-dotenv (Seguridad y configuración)

## Arquitectura del Flujo
1. **Configuración**: Carga de credenciales y rutas desde `.env`.
2. **Extracción**: Lectura de origen de datos (CSV) validando estructura mediante Pandas.
3. **Procesamiento**: Filtrado por severidad (`critical`) y chequeo contra `processed_alerts.json` para evitar duplicados.
4. **Notificación**: Envío mediante API a Telegram.
5. **Registro (Logs)**: Trazabilidad local en archivo físico y consola.
6. **Despliegue Cloud (Nuevo)**: Contenedor Docker configurado para ejecución aislada y persistencia mediante volúmenes.

## Estructura del Proyecto
```txt
PulseFlow/
├── data/
│   └── sample_alerts.csv     
├── logs/
│   └── app.log
├── src/
│   ├── config.py             
│   ├── main.py               
│   ├── services/
│   │   ├── alert_processor.py 
│   │   ├── data_loader.py    
│   │   └── notifier.py       
│   └── utils/
│       └── logger.py         
├── .env.example              
├── requirements.txt          
└── README.md                 
```

## Instalación

1. Clona el repositorio
```bash
git clone https://github.com/tu-usuario/PulseFlow.git
cd PulseFlow
```

2. Creación de entorno virtual
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instalar dependencias
```bash
pip install -r requirements.txt
```

## Configuración del `.env`
Copia `.env.example` a un archivo `.env`:
```bash
cp .env.example .env
```
Edita `.env` con tus datos.

### Cómo crear un Bot de Telegram
1. Abre Telegram y busca a `@BotFather`.
2. Envía `/newbot` y sigue los pasos.
3. Recibirás un `TELEGRAM_BOT_TOKEN`. Pégalo en tu `.env`.

### Cómo obtener el `TELEGRAM_CHAT_ID`
1. Busca `@userinfobot` o similar en Telegram.
2. Inicia un chat y te dirá tu ID (un número). Pégalo en tu `.env`.

## Ejecución

### Ejecución Local
```bash
python -m src.main
```

### Ejecución con Docker (Cloud/VPS)
```bash
# Construir la imagen
docker build -t pulseflow .

# Ejecutar montando volúmenes para persistir datos y logs
docker run -d --name pulseflow-bot \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/logs:/app/logs \
  -v $(pwd)/processed_alerts.json:/app/processed_alerts.json \
  --env-file .env \
  pulseflow
```

## Ejemplos

### Ejemplo de datos de entrada (CSV)
```csv
id,title,description,status,priority,date
1,Fallo de conexión,No hay conexión en área admtva,critical,high,2026-05-26
```

### Ejemplo de alerta enviada
```txt
🚨 *ALERTA CRÍTICA* 🚨

🔹 *ID:* 1
🔹 *Título:* Fallo de conexión
🔹 *Fecha:* 2026-05-26
🔹 *Prioridad:* high

📝 *Descripción:* No hay conexión en área admtva
```

## Mejoras Futuras
- Integración con **Google Sheets API**.
- CI/CD automatizado vía **GitHub Actions**.
- Despliegue serverless usando **Google Cloud Run**.
- Programación periódica (ejecución automática) usando **cron jobs**.
- Desarrollo de un **dashboard web** visual para el histórico de alertas.

## Habilidades Demostradas (Portafolio)
- Python intermedio/avanzado.
- Arquitectura Modular.
- Procesamiento de datos (Pandas).
- Integración de APIs de terceros (Requests).
- DevOps culture (12-factor apps con .env, versionado, logs).
