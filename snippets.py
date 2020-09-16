#Code for filter strings in dataframe

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
