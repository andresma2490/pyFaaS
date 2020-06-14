import numpy as np
import pandas as pd
import requests
import io

def handle(req):
	url = 'https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD'
	
	try:
	  print("Descargando los datos")
	  urlData = requests.get(url).content
	
	except:
	  print("Hubo un error, intentelo de nuevo")
	  return
	
	df = pd.read_csv(io.StringIO(urlData.decode('utf-8')), usecols=['Departamento o Distrito ', 'Ciudad de ubicación', 'atención', 'Edad', 'Tipo'])
	df = df.rename(columns = {'Departamento o Distrito ':'Departamento', 'Ciudad de ubicación':'Ciudad'})
	df = df.loc[ df.Departamento == 'Valle del Cauca' ]
	
	print("\nCasos de COVID-19 en el Valle del Cauca")
	print(df.groupby('Ciudad').Ciudad.count())
	
	print("\nDe los cuales en Cali son del tipo...")
	df = df.loc[ df.Ciudad == 'Cali' ]
	print(df.groupby('Tipo').Tipo.count())
	
	return 
