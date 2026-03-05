import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def analisis_rapido(df):
    """
    Realiza un análisis exploratorio básico de un DataFrame.
    Esta función muestra:
    - Las primeras 5 filas del DataFrame.
    - Información general de la estructura (tipos de datos y valores no nulos).
    - Número total de filas duplicadas.
    - Cantidad de valores nulos por columna.

    Args:
        df (pandas.DataFrame): DataFrame que se desea analizar.

    Retorna: 
        NONE. La función imprime resultados en pantalla.

    """
    print("Las 5 primeras columnas de Dataframe son:")
    display(df.head())
    print("Información básica de Dataframe:")
    display(df.info())
    print(f"El número de duplicados es: {df.duplicated().sum()}")
    print("El número de valores nulos es:")
    display(df.isna().sum())


def descriptivo_num(df):
    """
    Muestra un análisis descriptivo básico de las variables numéricas y tipo fechade un DataFrame.

    La función:
    - Identifica las columnas de tipo numérico y fecha.
    - Imprime sus nombres.
    - Presenta las estadísticas descriptivas principales
      (count, mean, std, min, percentiles y max) redondeadas a 2 decimales.

    Args:
        df (pandas.DataFrame): DataFrame que se desea analizar.

    Retorna: 
        NONE. La función muestra resultados en pantalla.
    """
    columnas_num = df.select_dtypes(include=['number','datetime']).columns
    print("Variables numéricas son:\n", columnas_num)

    print("\nLas estadísticas básicas:")
    display(df.describe().round(2).T)   
    

def descriptivo_cat(df):
    """
    Realiza un análisis descriptivo de las variables categóricas de un DataFrame.

    La función:
    - Identifica las columnas categóricas (tipo 'category', 'object' o 'string').
    - Muestra las estadísticas descriptivas básicas (count, unique, top, freq).
    - Indica el número de valores únicos por variable.
    - Presenta los 10 valores más frecuentes de cada columna, incluyendo valores nulos.

    Args:
        df (pandas.DataFrame): DataFrame que se desea analizar.

    Retorna: 
        NONE. La función muestra resultados en pantalla.
    """
    columnas_cat = df.select_dtypes(include=['category','object','string']).columns
    print("Variables categoricas son:\n", columnas_cat)

    print("\nLas estadísticas básicas:")
    display(df.describe(include=['category','object','string']).round(2).T)

    for col in columnas_cat:
        print(f"La columna *{col}* tiene {df[col].nunique()} valores unicos:")
        print("Los 10 valores con más frequencia son:")
        display(df[col].value_counts(dropna = False).head(10))


def porcent_nulos(df):
    
    nulos_porc = df.isnull().mean() * 100
    nulos_tabla = pd.DataFrame(nulos_porc, columns=['nulos%'])

    return (
        nulos_tabla[nulos_tabla['nulos%'] > 0]
        .sort_values(by='nulos%', ascending=False)
        .round(2)
    )


def claves_merge(df_izq, df_der, clave):
    """
    Verifica la integridad de una clave antes de realizar un merge entre dos DataFrames.

    Args:
        df_izq (pd.DataFrame): DataFrame principal (tabla izquierda).
        df_der (pd.DataFrame): DataFrame secundario (tabla derecha).
        clave (str): Nombre de la columna clave para la unión.

    Validaciones realizadas:
    - Coincidencia de tipos de datos.
    - Detección de valores nulos.
    - Verificación de unicidad en la tabla derecha.
    - Identificación de claves faltantes en la tabla derecha.

    Esta función ayuda a prevenir problemas de integridad referencial
    y posibles duplicaciones tras realizar un merge.
    """
    print(f" Clave: {clave}")
    
    # 1. Comprobamos tipos de datos de las claves
    print("1. Tipos de datos:")
    print(f"Dtype izquierda  : {df_izq[clave].dtype}")
    print(f"Dtype derecha: {df_der[clave].dtype}")
    
    if df_izq[clave].dtype != df_der[clave].dtype:
        print("Diferentes tipos de datos!")
    else:
        print("Tipos de datos coinciden!")
    
    # 2. Valores nulos
    print("2. Valores nulos:")
    print(f"Valores nulos en la izquierda: {df_izq[clave].isnull().sum()}")
    print(f"Valores nulos en la derecha: {df_der[clave].isnull().sum()}")
    
    # 3. Unicidad en la tabla derecha
    print("3. Unicidad en la tabla derecha:")
    unique_count = df_der[clave].nunique()
    total_rows = df_der.shape[0]
    
    print(f"Valores únicos: {unique_count}")
    print(f"Total filas   : {total_rows}")
    
    if unique_count == total_rows:
        print("La clave es única (1:1 o N:1 relación)")
    else:
        print("La clave NO es única (1:N relationship possible)")
    
    # 4. Claves faltantes en la tabla derecha
    print("4. Las claves de la izquierda que faltan en la derecha:")
    faltan_claves = df_izq[~df_izq[clave].isin(df_der[clave])][clave].nunique()
    print(f"Faltan claves únicas: {faltan_claves}")
    
    if faltan_claves == 0:
        print("Todas las claves coinciden")
    else:
        print("Faltan algunas claves de la tabla izquierda en la tabla derecha")


def histplot_num(df):
    """
    Genera histogramas con curva KDE para las variables numéricas y de tipo fecha
    de un DataFrame, excluyendo dentro del bucle las columnas 'SalesID', 'SalesPersonID', 'CustomerID', 'SalesDate', 'MonthNum'.

    Args:
        df (pandas.DataFrame): DataFrame que contiene los datos a analizar.

    Retorna: 
        NONE. Muestra en pantalla las gráficas de distribución de cada variable válida.
    """
    columnas_num = df.select_dtypes(include=['number', 'datetime']).columns
    for col in columnas_num:
        # Excluir columnas no deseadas dentro del bucle
        if col in ['SalesID', 'SalesPersonID', 'CustomerID', 'SalesDate', 'MonthNum']:
            continue
        print(f"Distribución de la columna *{col}*")
        plt.figure(figsize=(10, 3))
        sns.histplot(df[col], kde=True)
        plt.xlabel(col)
        plt.ylabel('Frecuencia')
        plt.show()


def boxplots_num(df):
    """
    Genera diagramas de caja (boxplots) para detectar valores atípicos en las
    variables numéricas y de tipo fecha de un DataFrame.
    Se excluyen automáticamente las columnas 'SalesID', 'SalesDate', 'MonthNum'
    dentro del bucle de iteración.

    Args:
        df (pandas.DataFrame): DataFrame que contiene los datos a analizar.

    Retorna: 
        NONE. Muestra en pantalla los boxplots de cada variable válida.
    """

    columnas_num = df.select_dtypes(include=['number', 'datetime']).columns
    for col in columnas_num:

        # Excluir columnas no deseadas
        if col in ['SalesID', 'SalesDate', 'MonthNum']:
            continue
        plt.figure(figsize=(10, 2))
        sns.boxplot(x=df[col])
        plt.title(f'Análisis de Outliers: {col}')
        plt.xlabel(col)
        plt.ylabel('Frecuencia')
        plt.show()


def countplot_cat(df, max_categories = 100):
    """
    Muestra gráficos de distribución para columnas categóricas de un DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame de entrada.
        max_categories (int), opcional (default = 100)
            Número máximo de categorías permitido para mostrar el gráfico.
            Si una columna tiene más, se omite la visualización.
    """
    columnas_cat = df.select_dtypes(include=['category','object','string']).columns
    for col in columnas_cat:
        if df[col].nunique() > max_categories:
            print(f"La columna *{col}* tiene demasiadas categorias para visualización")
            continue
        print(f"Distribución de la columna *{col}*")
        plt.figure(figsize = [12,3])
        sns.countplot(x = df[col], order = df[col].value_counts().index)
        plt.tight_layout()
        plt.show()


def correlaciones(df):
    """
    Calcula y muestra la matriz de correlación para variables numéricas.

    Args:
        df (pandas.DataFrame): DataFrame de entrada.
    """
    corr = df.select_dtypes(include="number").corr()
    # Creamos una máscara para el triángulo superior
    mask = np.triu(np.ones_like(corr, dtype=bool))

    plt.figure(figsize=(12, 8))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap="coolwarm", center=0)
    plt.title("Matriz de correlación")
    plt.show()
