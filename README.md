# Programa de Análisis Financiero 💼💰

Este programa de análisis financiero te permite evaluar la liquidez, solvencia y eficiencia de una empresa a partir de sus informes financieros trimestrales. La modularización del código se ha realizado dividiéndolo en varios archivos para mejorar la organización y facilitar su mantenimiento.

[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)

## Créditos 🙏

Este programa de análisis financiero está basado en el video educativo proporcionado por Ariel Mamani de InverArg en el canal de "Joven Inversor". Puedes encontrar el video original en el siguiente enlace:

### [QUE ES Y COMO HACER Analisis Fundamental || Con InverArg](https://www.youtube.com/watch?v=ehLyujzFzt4)

Agradecemos sinceramente a Ariel Mamani por compartir su conocimiento en materia de análisis financiero y valoración de empresas. Este programa ha sido desarrollado con la intención de aplicar las enseñanzas brindadas en el video mencionado y facilitar a los usuarios un análisis financiero elemental de acciones.

## Requerimientos 🛠️

- pandas
- yahooquery

Puedes instalar las dependencias ejecutando el siguiente comando:

```bash
pip install pandas yahooquery
```

## Carpetas y Archivos de Lógica 📂

### `logic/clase_analisisfinanciero.py`

Este archivo define la clase `AnalisisFinanciero`, responsable de realizar el análisis financiero de la empresa. Contiene métodos para validar el ticker, calcular la liquidez, solvencia y eficiencia, y mostrar los resultados.

### `logic/clasificacion.py`

En `clasificacion.py`, se encuentran funciones para clasificar los resultados en diferentes categorías y asignarles colores. La función `clasificacion_color` asigna colores a las clasificaciones, mientras que las funciones `clasificar_liquidez`, `clasificar_solvencia` y `clasificar_eficiencia` clasifican y devuelven resultados junto con su respectivo color.

### `logic/clase_color.py`

El archivo `clase_color.py` contiene la definición de la clase `ColorResultado`. Esta clase se encarga de dar formato de color al resultado para su presentación en la consola.

## Uso 🚀

1. Ejecuta `main.py`.
2. Ingresa el ticker de la acción que deseas analizar.
3. Observa los resultados clasificados y presentados con colores en la consola.

## Limitaciones ⚠️

- El programa asume que los datos financieros están disponibles a través de Yahoo Finance y que el ticker ingresado es válido.
- La precisión del análisis depende de la calidad y disponibilidad de los datos financieros de la empresa.
- La clasificación y colores pueden variar según los criterios específicos establecidos en las funciones de clasificación.

## Contribuir 🤝

Aquí hay algunas formas en las que puedes contribuir:

1. **Informar Problemas (Bugs):** Si encuentras algún problema o error, por favor, crea un informe detallado en la sección de problemas (issues) del repositorio. Incluye información sobre el problema y cómo reproducirlo.

2. **Solicitar Nuevas Funcionalidades:** Si tienes ideas para nuevas características o mejoras, no dudes en sugerirlas creando una solicitud de mejora en la sección de problemas (issues).

3. **Envío de Parches:** Si deseas contribuir directamente al código, puedes enviar un "pull request". Asegúrate de seguir las mejores prácticas y de probar adecuadamente tu código antes de enviar la solicitud.

4. **Mejora de Documentación:** Mejorar la documentación es siempre bienvenido. Si encuentras áreas en la documentación que pueden ser más claras o si deseas agregar ejemplos adicionales, ¡adelante!

## Cómo Contribuir 🛠️

1. Clona el repositorio:

   ```bash
   git clone https://github.com/AgusLov/Analisis-fundamental-programa.git
   ```

2. Crea una rama para tu contribución:

   ```bash
   git checkout -b nombre-de-tu-rama
   ```

3. Realiza tus cambios y pruebas.

4. Haz commit de tus cambios:

   ```bash
   git commit -m "Descripción de tus cambios"
   ```

5. Envía tu rama:

   ```bash
   git push origin nombre-de-tu-rama
   ```

6. Crea un pull request en el repositorio.


