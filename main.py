import pandas as pd
from sqlalchemy import create_engine
# import pymsql

lista_universidades = pd.read_csv('lista_universidades_2021.csv')
lista_universidades = lista_universidades.rename(columns={'Sigla': 'initials', 'Instituição(IES)': 'institution'})

dataFrame = pd.DataFrame(data=lista_universidades['subchannel'])
tableName = "university"
sqlEngine = create_engine('mysql+pymysql://root:@172.17.0.2/campaign', pool_recycle=3306)
dbConnection = sqlEngine.connect()

try:
    frame = dataFrame.to_sql(tableName, dbConnection, if_exists='replace', index=False)
    sqlEngine.execute('ALTER TABLE `university` ADD id bigint NOT NULL AUTO_INCREMENT primary key')

except ValueError as vx:
    print(vx)

except Exception as ex:
    print(ex)

else:
    print("Table %s created successfully." % tableName)

finally:
    dbConnection.close()