#PANDAS COMMANDS
#Imports
import pandas as pd
import numpy  as np

#Leitura de Aqrquivos
df=pd.read_csv('Nome_do_Arquivo.csv',sep=',')


#Corte de Dataset
df = df[['NAME_SYSTEM','EMAIL']].copy()

#Valores Unicos
df.drop_duplicates()

#Dropar Colunas
df=df.drop(columns=['OID_SYSTEM','CONTACT_NAME','PHONE','ID_LEITURA','TYPE_CONSTANT','STATUS','ID_SYSTEM_TYPE','DESCRIPTION_SYSTEM_TYPE']).drop_duplicates()

#Filtros
filter_email=df['EMAIL_VALIDACAO']=='Valid'
df=df[filter_email]

#Mais Filtros
df=df[df.ENVIA_EMAIL==1]

#Transformar uma coluna em index
df=df.set_index('NAME_SYSTEM')

#Exibição
df.head()


#Loops
#For
#Valores unicos de um campo especifico
for data in df.DATA.unique():

#Filtro de dois campos
aux=df[df.DATA==data]['CONSUMO_MADRUGADA']
	
	
#Strings		
data='Consumo Madrugada em '+data
string_result=string1+string2
assunto = "CAS - Condomino {} - Suspeita de vazamento".format(name)
mensagem ='''
Prezado, <br> Durante a semana do dia {} a {}, foi constatado que o condomínio {} <br> possui suspeita
de vazamento em suas unidades consumidoras conforme tabela abaixo. <br><br>'''.format(dt_fim,dt_ini,name)
	
html=mensagem+dt[dt.index== name].to_html(index=False)
  
#List
list=[]
para=dt_vaz[dt_vaz.index==name]['EMAIL'].to_list()
resp=dt_vaz[dt_vaz.index==name]['EMAIL_RESPONSAVEL'].drop_duplicates().to_list()


#Add Columns to a Dataset
DataFrameName.insert(loc, column, value, allow_duplicates = False)
#loc: loc is an integer which is the location of column where we want to insert new column.
#column: column is a string which is name of column to be inserted.
#value: value is simply the value to be inserted. It can be int, string, float or anything or even series / List of values. Providing only one value will set the same value for all rows.
#allow_duplicates : allow_duplicates is a boolean value which checks if column with same name already exists or not.
#Ex
df.insert(loc=len(df.columns), value=aux.values,column=data)

#Datas
from datetime import datetime, timedelta
dt_ini=datetime.today().strftime('%d/%m/%Y')
dt_fim= datetime.today() - timedelta(days=7)
dt_fim= dt_fim.strftime('%d/%m/%Y')



# Single selections using iloc and DataFrame
# Rows:
data.iloc[0] # first row of data frame (Aleshia Tomkiewicz) - Note a Series data type output.
data.iloc[1] # second row of data frame (Evan Zigomalas)
data.iloc[-1] # last row of data frame (Mi Richan)
# Columns:
data.iloc[:,0] # first column of data frame (first_name)
data.iloc[:,1] # second column of data frame (last_name)
data.iloc[:,-1] # last column of data frame (id)

# Multiple row and column selections using iloc and DataFrame
data.iloc[0:5] # first five rows of dataframe
data.iloc[:, 0:2] # first two columns of data frame with all rows
data.iloc[[0,3,6,24], [0,5,6]] # 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
data.iloc[0:5, 5:8] # first 5 rows and 5th, 6th, 7th columns of data frame (county -> phone1).

# Select rows with index values 'Andrade' and 'Veness', with all columns between 'city' and 'email'
data.loc[['Andrade', 'Veness'], 'city':'email']
# Select same rows, with just 'first_name', 'address' and 'city' columns
data.loc['Andrade':'Veness', ['first_name', 'address', 'city']]
 
# Change the index to be based on the 'id' column
data.set_index('id', inplace=True)
# select the row with 'id' = 487
data.loc[487]

# Select rows with first name Antonio, # and all columns between 'city' and 'email'
data.loc[data['first_name'] == 'Antonio', 'city':'email']
 
# Select rows where the email column ends with 'hotmail.com', include all columns
data.loc[data['email'].str.endswith("hotmail.com")]   
 
# Select rows with last_name equal to some values, all columns
data.loc[data['first_name'].isin(['France', 'Tyisha', 'Eric'])]   
       
# Select rows with first name Antonio AND hotmail email addresses
data.loc[data['email'].str.endswith("gmail.com") & (data['first_name'] == 'Antonio')] 
 
# select rows with id column between 100 and 200, and just return 'postal' and 'web' columns
data.loc[(data['id'] > 100) & (data['id'] <= 200), ['postal', 'web']] 
 
# A lambda function that yields True/False values can also be used.
# Select rows where the company name has 4 words in it.
data.loc[data['company_name'].apply(lambda x: len(x.split(' ')) == 4)] 
 
# Selections can be achieved outside of the main .loc for clarity:
# Form a separate variable with your selections:
idx = data['company_name'].apply(lambda x: len(x.split(' ')) == 4)
# Select only the True values in 'idx' and only the 3 columns specified:
data.loc[idx, ['email', 'first_name', 'company']]

# ix indexing works just the same as .loc when passed strings
data.ix[['Andrade']] == data.loc[['Andrade']]
# ix indexing works the same as .iloc when passed integers.
data.ix[[33]] == data.iloc[[33]]
 
# ix only works in both modes when the index of the DataFrame is NOT an integer itself.




























