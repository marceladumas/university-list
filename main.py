import pandas as pd
from sqlalchemy import create_engine

lista_universidades = pd.read_csv('lista_universidades_2021.csv')
lista_universidades = lista_universidades.rename(columns={'Sigla': 'sigla', 'Instituição(IES)': 'instituicao'})
lista_universidades = lista_universidades.drop(columns=['Código Mantenedora', 'Situação da IES', 'Razão Social', 'Telefone', 'e-Mail', 'Município', 'UF',
                                                        'CNPJ', 'Sinalizações Vigentes', 'Representante Legal', 'Natureza Jurídica', 'Código IES',
                                                        'Reitor/Dirigente Principal', 'IGC', 'Ano IGC', 'Ano CI-EaD', 'Ano CI', 'CI-EaD', 'CI',
                                                        'Data do Ato de Criação da IES', 'Categoria Administrativa', 'Categoria', 'Tipo de Credenciamento',
                                                        'Organização Acadêmica', 'Endereço Sede', 'Sitio'])


dataFrame = pd.DataFrame(data=lista_universidades)
tableName = "university"
sqlEngine = create_engine('mysql+pymysql://root:@172.17.0.2/campaign', pool_recycle=3306)
dbConnection = sqlEngine.connect()

try:
    frame = dataFrame.to_sql(tableName, dbConnection, if_exists='replace')
    sqlEngine.execute('ALTER TABLE `university` ADD id int NOT NULL AUTO_INCREMENT primary key')

except ValueError as vx:
    print(vx)

except Exception as ex:
    print(ex)

else:
    print("Table %s created successfully." % tableName)

finally:
    dbConnection.close()