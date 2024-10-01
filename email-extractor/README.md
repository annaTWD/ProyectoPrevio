# Email Extractor

## Cómo ejecutar el proyecto

1. Clona el repositorio.
2. Construye la imagen de Docker.
3. Ejecuta el contenedor Docker.

### Comandos:

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/email-extractor.git
cd email-extractor

# Construir la imagen de Docker
docker build -t email-extractor .

# Ejecutar el contenedor Docker
docker run -it email-extractor
