#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 19:34:32 2021

@author: sbarcenas
"""

import pandas as pd

url = "Casos_positivos_de_COVID-19_en_Colombia.csv"
df = pd.read_csv(url)


df.drop(['Código ISO del país','Nombre del grupo étnico','Pertenencia étnica',
         'Tipo de recuperación', 'Nombre del país' ],
axis =1, inplace = True)

df.loc[df['Ubicación del caso'] == 
       'CASA', 'Ubicación del caso'] = 'Casa'
df.loc[df['Ubicación del caso'] == 
       'casa', 'Ubicación del caso'] = 'Casa'
df.loc[df['Estado'] == 
       'leve', 'Estado'] = 'Leve'
df.loc[df['Estado'] == 
       'LEVE', 'Estado'] = 'Leve'
df.loc[df['Recuperado'] == 
       'fallecido', 'Recuperado'] = 'Fallecido'
df.loc[df['Nombre departamento'] == 
       'BARRANQUILLA', 'Nombre departamento'] = 'ATLANTICO'
df.loc[df['Nombre departamento'] == 
       'CARTAGENA', 'Nombre departamento'] = 'BOLIVAR'
df.loc[df['Nombre departamento'] == 
       'STA MARTA D.E ', 'Nombre departamento'] = 'MAGDALENA'


#1 Número de casos de Contagiados en el País.
TT = df.shape[0]
print(f'El número de contagiados en colombia es: {TT}') 

#2 Número de Municipios Afectados
CT = df.groupby('Nombre municipio').size()
print(f'Numero de municipios afectados afectados: {len(CT)}' )

#3 Liste los municipios afectados 

AF = df['Nombre municipio'].value_counts()
MAF = df.groupby('Nombre municipio').size()
print(f'Municipios afectados: {MAF}')

#4 Número de personas que se encuentran en atención en casa
CAS = df[df['Ubicación del caso']=='Casa'].shape[0]
print(f'Atención en casa: {CAS}' )

#5: Número de personas que se encuentran recuperados
RE =  df[df['Recuperado'] == 'Recuperado'].shape[0]
print(f'Recuperados: {RE}' )

#6 Número de personas que ha fallecido
F = df[df['Recuperado'] == 'Fallecido'].shape[0]
print(f'Fallecidos: {F}')

#7 Ordenar de Mayor a menor por tipo de caso (Importado, en estudio, Relacionado)
TC = df.groupby('Tipo de contagio').size().sort_values(ascending = False)
print(f'Tipos de caso {TC}')

#8 Número de departamentos afectados
DAF_N = df.groupby('Nombre departamento').size()
print(f'Número Departamentos afectados: {len(DAF_N)}')

#9 Liste los departamentos afectados(sin repetirlos)
DAF = df.groupby('Nombre departamento').size()
print(f'Departamentos afectados: {len(DAF)}')

#10 Ordene de mayor a menor por tipo de atención
UBC = df.groupby('Ubicación del caso').size().sort_values(ascending = False)
print(f'Ubicaciones de casos: {UBC}')

#11 Liste de mayor a menor los 10 departamentos con mas casos de contagiados
MD = df.groupby('Nombre departamento').size().sort_values(ascending = False).head(10)
print(f'Departamentos mas afectados: {MD}')

#12 Liste de mayor a menor los 10 departamentos con mas casos de fallecidos
MFD = df[df['Estado'] =='Fallecido']['Nombre departamento'].value_counts().head(10)
print(f'Departamentos mas fallecidos: {MD}')


#13 Liste de mayor a menor los 10 departamentos con mas casos de recuperados
MRD = df[df['Recuperado'] =='Recuperado']['Nombre departamento'].value_counts().head(10)
print(f'Departamentos mas recuperados {MRD}')

#14 Liste de mayor a menor los 10 municipios con mas casos de contagiados
MCM = df.groupby('Nombre municipio').size().sort_values(ascending = False).head(10)
print(f'Municipios mas contagiados {MCM}')

#15 Liste de mayor a menor los 10 municipios con mas casos de fallecidos
MFM = df[df['Estado'] =='Fallecido']['Nombre municipio'].value_counts(ascending = False).head(10)
print(f'Mas casos fallecidos {MFM}')