#Code for filter strings in dataframe paaaaassssaaaaaa

is_30 =  df_training_dataset['Telefono']=='Iphone'
print('--------------')
gapminder_2002 = df_training_dataset[is_30]
print(gapminder_2002.shape)
print('--------------')
gapminder_2002.head(20)

#___________________________________________________
#contar valores de una columna en el df
print(df_training_dataset['Genero'].value_counts(),'\n')
print("Nulos: ",df_training_dataset['Genero'].isna().sum())
#________________________________________________

#Imputaciones a nulos

#Imputacion constante a -1
si_constant_minusone = SimpleImputer(
    missing_values=np.nan,
    strategy='constant',
    fill_value=-1,
    copy=True
)
#Imputacion constante a 0
si_constant_zero = SimpleImputer(
    missing_values=np.nan,
    strategy='constant',
    fill_value=0,
    copy=True
)
#Imputacion mean (sin uso en este caso)
si_mean = SimpleImputer(
    missing_values=np.nan,
    strategy='mean'
)
#Imputacion median
si_median = SimpleImputer(
    missing_values=np.nan,
    strategy='median'
)
#Imputacion most_frequent (sin uso en este caso)
si_most_frequent = SimpleImputer(
    missing_values=np.nan,
    strategy='most_frequent'
)
#____________________________________________________
#hallar medianas de un df
df_training_dataset.median(axis = 0) 
#_____________________________________________

#aumentar tamaño de muestreo en el notebook
pd.options.display.max_rows = 4000
#______________________________________________


#derivada parcial python

<from math import *
import sympy as sp


def derivada(expr, variables):
    for der_respect in variables:
        var = sp.Symbol(f'{der_respect}')
        funcion = sp.Derivative(expr, var, evaluate=True)
        print(f'La derivada parcial df/d{der_respect} =  {funcion}')


if __name__ == '__main__':
    variables = ['x', 'y', 'z']
    expr = input("\nFuncion a evaluar:    f(x,y,z)=")
    derivada(expr, variables)>
   
#_____________________________________________________
#
#melt para unir multiples columnas en una columna con valores
#
df1 = pd.melt(df0, id_vars=["Z_MARCA", "Z_GAMA", "Z_MODELO", "Z_DEPARTAMENTO", "Z_PUNTO_VENTA"], 
                  var_name="Semana", value_name="Demanda")

#____________________________________________________________
#CAtegoricas a numericas simples
#llevando de tipo object a tipo category
df1['Z_MARCA'] = df1['Z_MARCA'].astype('category')
df1['Z_GAMA'] = df1['Z_GAMA'].astype('category')
#revisando columnas tipo category
cat_columns = df1.select_dtypes(['category']).columns
cat_columns
#Llevandolas a numericas
df1[cat_columns] = df1[cat_columns].apply(lambda x: x.cat.codes)
#_____________________________________________________________
