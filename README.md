# Scraper de Casas y Departamentos en Mercado Libre

Este es un scraper creado en Python que permite buscar y recopilar información sobre casas y departamentos en venta o alquiler en Mercado Libre.

## Instalación

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/Ashranka/Scraper_MercadoLibre.git
    ```

2. Instala las dependencias necesarias utilizando pip:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta el script `scraper.py`:

    ```bash
    python scraper.py
    ```

2. El scraper solicitará la ubicación y los filtros de búsqueda, como el tipo de propiedad (casa o departamento), precio, cantidad de habitaciones, etc.

3. Una vez proporcionados los filtros, el scraper buscará en Mercado Libre y recopilará los datos de las propiedades encontradas.

4. Los datos se guardarán en un archivo CSV en el directorio de salida especificado.

## Ejemplo de Uso

```bash
python scraper.py
```
## Ejemplo de Resultado

El scraper generará un archivo CSV con los siguientes campos:

- ID
- Título
- Precio
- Dirección
- Descripción
- URL
