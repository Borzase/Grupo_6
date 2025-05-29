## Se necesitan importar las siguientes librerias

import pandas as pd
import numpy as np
import scipy.stats as pearsonr
import matplotlib.pyplot as plt
import seaborn as sns

def describe_df(dataframe):
    """ 
    La función trabaja sobre un dataframe y clasifica los datos de las variables según el tipo de datos que contiene cada variable, 
    el porcentaje de nulos, los valores unicos de la variable y en función de esta última la cardinalidad que presenta.

    Argumentos:
    dataframe (pandas dataframe) = es el dataframe sobre el que se quiere aplicar la función

    Retorna:
    Devuelve un nuevo dataframe organizado cuyo índice son los cuatro descriptores
    
    """
    dic_columnas = {}
    for columna in dataframe.columns:
        a = dataframe[columna].dtype
        b = round((len(dataframe.loc[dataframe[columna].isna()])/len(dataframe)*100),2)
        c = dataframe[columna].nunique()
        d = round(dataframe[columna].nunique()/len(dataframe)*100, 2)
        dic_columnas[columna] = [a, b, c, d]

    indice = ["DATA_TYPE", "MISSINGS (%)", "UNIQUE_VALUES", "CARDIN (%)"]
    df = pd.DataFrame(dic_columnas, index = indice)
    return df



def tipifica_variables (df_in, umbral_categoria = 10, umbral_continua=20.0):
    """ 
    La función se utiliza para categorizar las columnas de un dataframe en binaria, categorica, 
    numérica discontinua y numerico continua. Para clasificar las numericas se utilizan los umbrales.
    
    Argumentos:
    df_in (pandas dataframe) = El dataframe a categorizar
    umbral_categoria (int) = Por defecto el umbral de categoria son 10.
    umbral_continua (float) = Por defecto el umbral de continua son 20
    
    Retorna:
    Devuelve un dataframe con el nombre de la columna y su tipo de categoria"""
    
    diccion = {}
    for columna in df_in.columns:
      if df_in[columna].nunique() == 2:
        diccion[columna] = "Binaria"
      if df_in[columna].nunique() > 2 and df_in[columna].nunique() < umbral_categoria:
        diccion[columna] = "Categórica"
      if df_in[columna].nunique() >= umbral_categoria:
        diccion[columna] = "Numérica discreta"
      if (df_in[columna].nunique()/len(df_in[columna]) * 100) >= umbral_continua:
          diccion[columna] = "Numérica continua"
        
    categoria = pd.Series(diccion)
    df = pd.DataFrame(categoria)
    
    return df.rename(columns={0:"Categoria"})


def get_features_num_regression(dataframe, target_col,umbral_corr, pvalue = None):
    """ 
    La función se utiliza sobre una columna numérica continua para saber la correlación frente a
    otras columnas numéricas. Se utiliza un umbral de correlación para seleccionar las correlaciones
    que superen dicho valor y un pvalor que por defecto es None y que sirve para confirmar significación
    estadística.
    
    Argumentos:
    dataframe (pandas dataframe) = dataframe que se quiere analizar
    target_col (string) = la columna objetivo del dataframe
    umbral_corr (float)= nivel límite de correlación entre las variables
    pvalue (None) = por defecto None pero espera un float 
    
    Retorna
    Devuelve una lista con las variables numéricas que han superado el umbral de correlación, 
    y en caso de introducir el pvalue, de las varibales cuyo p-valor está por debajo del pvalue indicado.
    Se ofrece además de manera visual una matriz de correlación entre la columna target y las variables seleccionadas
    """
    try: 
        if dataframe[target_col].nunique()/len(dataframe) * 100 >= 20:  # Condición de que la columna target sea numerica continua
            lista_columnas = []
            tabla = dataframe.drop(target_col, axis=1)
            for col in tabla.columns:
                if dataframe[col].dtype != 'object' or dataframe[col].dtype != 'bool':
                    corrs = pearsonr(dataframe[target_col], dataframe[col])
                    if pvalue != None:
                        if np.abs(corrs[0]) > umbral_corr and corrs[1] <= pvalue:
                            lista_columnas.append(col)
                    else:
                        if np.abs(corrs[0]) > umbral_corr:
                            lista_columnas.append(col)
    
            lista_columnas.insert(0, target_col)
            corr_matrix = dataframe[lista_columnas].corr()
            figura = plt.figure(figsize=(10,10))
            sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True, square=True, linewidths=.5) # el cmap es el rango de colores usado para representar "el calor"
            plt.title('Matriz de Correlación')
            plt.xticks(rotation=45)  # Rota las etiquetas de las x si es necesario
            plt.yticks(rotation=45)  # Rota las etiquetas de las y si es necesario
            lista_columnas.remove(target_col)

            return lista_columnas, figura
        else: 
            return print(f"La variable {target_col} no cumple con el umbral de variable numérica continua")
    except KeyError: 
        print(f"¡Lo siento, la columna '{target_col}' no existe! Revisa que esté bien escrita")


def plot_features_num_regression(dataframe, target_col, lista = [], umbral_corr = 0.0, pvalue = None):
    """ 
    La función tiene por objeto analizar las funciones numéricas de un dataframe o las variables
    introducidas por lista y conocer la correlación frente a la columna target.
    
    Argumentos:
    dataframe (pandas dataframe) = el dataframe sobre el que se va a trabajar
    target_col ('string') = el nombre de la columna target
    lista (list) = es una lista que por defecto va vacia
    umbral_corr (float) = por defecto tiene valor 0 
    pvalue (None) = por defecto None, se espera que sea un valor float
    
    Retorna:
    La función devuelve un pairplot con las columnas que han superado los umbrales de correlación
    y, en caso de incluir el pvalue, cuyo p-valor sea inferior al pvalue."""
    try:
        if dataframe[target_col].nunique()/len(dataframe) * 100 >= 20:
            lista_columnas = []
            if len(lista) == 0:
                tabla = dataframe.drop(target_col, axis=1)
                for col in tabla.columns:
                    if dataframe[col].dtype != 'object' or dataframe[col].dtype != "bool":
                        corrs = pearsonr(dataframe[target_col], dataframe[col])
                        if pvalue != None:
                            if np.abs(corrs[0]) > umbral_corr and corrs[1] <= pvalue:
                                lista_columnas.append(col)
                        else:
                            if np.abs(corrs[0]) > umbral_corr:
                                lista_columnas.append(col)
                lista_columnas.insert(0, target_col)
                return sns.pairplot(dataframe[lista_columnas])

            else:
                lista
                for col in lista:
                    corrs = pearsonr(dataframe[target_col], dataframe[col])
                    if pvalue != None:
                        if np.abs(corrs[0]) < umbral_corr or corrs[1] > pvalue:
                            lista.remove(col)
                    else:
                        if np.abs(corrs[0]) < umbral_corr:
                            lista_columnas.remove(col)
                lista.insert(0, target_col)
                return sns.pairplot(dataframe[lista])
                
        else: 
            return print(f"La variable {target_col} no cumple con el umbral de variable numérica continua")
        
    except KeyError: 
        print(f"¡Lo siento, la columna '{target_col}' no existe! Revisa que esté bien escrita")
        