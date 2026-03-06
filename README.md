:chart_with_downwards_trend: Proyecto Final

:ledger: Descripción del Proyecto\
Este proyecto consiste en el análisis exploratorio de una base de datos transaccional de ventas de comestibles en Estados Unidos. El objetivo principal es comprender la estructura del negocio, identificar los principales impulsores de ingresos y analizar el comportamiento de ventas desde una perspectiva comercial y temporal. A través de la integración de múltiples tablas relacionales, se construyó un dataset único que permite evaluar productos, categorías, clientes, ciudades y desempeño de vendedores. El análisis busca generar insights estratégicos que puedan apoyar la toma de decisiones comerciales.

:pushpin: Objetivos del Proyecto\
El objetivo principal de este proyecto es realizar un Análisis Exploratorio de Datos (EDA) para comprender en profundidad el comportamiento de las ventas y la dinámica del negocio.

De manera específica, el análisis busca:
1. Evaluar cómo se distribuyen los ingresos y el ticket promedio.
2. Identificar los productos y categorías que generan mayor ingreso.
3. Analizar el impacto de los descuentos en el volumen y el ingreso.
4. Detectar patrones temporales en las ventas (mensuales y semanales).
5. Examinar la concentración geográfica y el desempeño de los vendedores.

El propósito final es transformar datos transaccionales en insights accionables que permitan entender los principales motores del negocio y posibles áreas de optimización.

:books: Estructura del Proyecto\
:file_folder: Proyecto_final\
├── data/\
│   ├── raw/\
│   │       ├── categiries.csv\
│   │       ├── cities.csv\
│   │       ├── countries.csv\
│   │       ├── customers.csv\
│   │       ├── products.csv\
│   │       └── sales.csv\
│   └── processed/\
│   │       └── sales_final.csv\
├── notebooks/\
│   ├── 01.eda_preliminar_bank.ipynb\
│   ├── 02.transformacion_limpieza.ipynb\
│   └── 03.eda.ipynb\
├── src/\
│   └── sp_eda.py\
├── .gitignore\
├── Dashboard_Proyecto_final.pbix\
└── README.md

:nut_and_bolt: Herramientas Utilizadas
- Visual Studio Code
- Python
- Librerias:
    * Pandas
    * Numpy
    * Seaborn
    * Matplotlib
- Power BI

**Conjuntos de datos**

El conjunto de datos completo utilizado en este proyecto es extenso y no se puede almacenar directamente en GitHub.

Puede descargarlo aquí:

Conjunto de datos completo:
https://drive.google.com/file/d/1EEeNo8H8ijg0XVMVv3pHEnunW2ZzbkKO/view?usp=drive_link

Archivos incluidos:
- sales.csv
- sales_final.csv

Para una exploración rápida, se incluye los conjuntos de datos de muestra en este repositorio:
- sales_sample.csv
- sales_final_sample.csv

:page_with_curl: Plan de ejecución del Proyecto
1. *Comprensión inicial de los datos.*
Se revisó la estructura de las tablas, sus relaciones y los tipos de variables disponibles.
2. *Limpieza y preparación de datos.*
Se validaron claves, se gestionaron nulos, se recalculó 'TotalPrice', se crearon columnas nuevas 'RevenueBruto', 'DiscountAmount', 'MonthNum', 'Month' y 'DayOfWeek'  y se integraron todas las tablas en un dataset único.
3. *Análisis descriptivo de datos.*
Se calcularon métricas descriptivas (media, mediana, desviación estándar, cuartiles) para entender la distribución y variabilidad de las ventas.
4. *Análisis estadístico de los datos.*
Se evaluaron patrones de ingresos, comportamiento de descuentos, concentración por productos y tendencias temporales.
5. *Análisis de correlación.*
Se identificaron los principales impulsores del revenue y posibles anomalías estructurales en el dataset.
6. *Desarrollo de un Dashboard Operativo.*
Se creó un dashboard interactivo que permite monitorear ingresos, categorías, desempeño comercial y tendencias en tiempo real.
7. *Informe explicativo del análisis.*
Se documentaron los principales hallazgos e insights estratégicos para facilitar la interpretación del negocio.

:white_check_mark: Informe explicativo del análisis\
El análisis exploratorio realizado sobre más de 6,6 millones de transacciones permitió comprender en profundidad la estructura del negocio y los principales factores que impulsan el revenue. A nivel general, se observó que los ingresos están principalmente determinados por el precio del producto y la cantidad vendida, lo que indica que el crecimiento depende tanto del volumen como del valor unitario de los artículos comercializados.

La distribución de ingresos presenta una asimetría positiva, con presencia de transacciones de alto valor que elevan la media, aunque la mayoría de las ventas corresponden a tickets de valor medio. No se identificó una concentración extrema en productos, categorías, ciudades o vendedores, lo que refleja una estructura comercial diversificada y con bajo riesgo de dependencia en un único segmento.

En cuanto a los descuentos, el análisis mostró que no generan un aumento significativo en la cantidad vendida y reducen el ticket promedio por transacción, lo que sugiere que la estrategia promocional actual no es un motor relevante de crecimiento.

Desde la perspectiva temporal, el comportamiento de las ventas es estable durante el período analizado, con variaciones moderadas entre meses y días de la semana, pero sin tendencias estructurales marcadas.

Finalmente, se detectó una anomalía importante en la correlación entre CustomerID y Quantity, lo que evidenció una posible generación estructural de dicha variable. Por esta razón, fue excluida del análisis para garantizar la consistencia y validez de los resultados.

En conjunto, el estudio proporciona una visión integral del desempeño comercial y establece una base sólida para la optimización estratégica del negocio.

*Recomendaciones para el negocio*
1. **Revisar la estrategia de descuentos**
Los descuentos reducen el ticket promedio sin aumentar el volumen, por lo que se recomienda aplicarlos de forma más estratégica y segmentada.
2. **Potenciar categorías y productos con mayor contribución**
Aunque el ingreso está diversificado, se pueden reforzar las categorías líderes para maximizar rentabilidad.
3. **Enfocar el crecimiento en volumen y precio**
Dado que el ingreso depende principalmente del precio y la cantidad vendida, estrategias como bundles o ajustes de precios pueden ser más efectivas que descuentos generales.
4. **Utilizar el dashboard para monitoreo continuo**
El seguimiento periódico de métricas clave permitirá detectar oportunidades y riesgos de forma temprana.

:black_nib: Autoría\
Liudmyla Rudenkova\
Marzo 2026\
[@LiudmylaR](https://github.com/LiudmylaR)