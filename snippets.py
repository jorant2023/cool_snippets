#Code for filter strings in dataframe

is_30 =  df_training_dataset['Telefono']=='Iphone'
print('--------------')
gapminder_2002 = df_training_dataset[is_30]
print(gapminder_2002.shape)
print('--------------')
gapminder_2002.head(20)

#___________________________________________________
#testing
