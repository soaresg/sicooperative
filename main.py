
import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import col


def initialize_spark(path, appName, master):
    spark = SparkSession \
        .builder \
        .master(master) \
        .appName(appName) \
        .config("spark.jars", path) \
        .getOrCreate()
    
    return spark

def getData(spark, db, table):
    return spark.read \
    .jdbc(
        url="jdbc:postgresql://localhost:5433/" + db,
        table=table,
        properties= {
            "user": "sicooperative",
            "password": "SiCooperative2022",
            "driver": "org.postgresql.Driver"
        }
    )
    
def ajustColumns(df, prefix):
    df = df.select(*(col(x).alias(prefix + x) for x in df.columns))
    
    return df

def joinDataFrames():
    columns = [ 
        "ass_nome",
        "ass_sobrenome",
        "ass_idade", 
        "mov_vlr_transacao",
        "mov_des_transacao",
        "mov_data_movimento",
        "car_num_cartao",
        "car_nom_impresso",
        "car_data_criacao",
        "con_tipo",
        "con_data_criacao"
    ]
    
    df = df_movimento.join(df_cartao, df_movimento["mov_id_cartao"] == df_cartao["car_id"], "inner")
    df = df.join(df_conta, df.car_id_conta == df_conta.con_id, "inner")
    df = df.join(df_associado, df.con_id_associado == df_associado.ass_id, "inner")
    
    df = df.select(columns).toDF(*(
        "nome_associado",
        "sobrenome_associado",
        "idade_associado",
        "vlr_transacao_movimento",
        "des_transacao_movimento",
        "data_movimento",
        "numero_cartao",
        "nome_impresso_cartao",
        "data_criacao_cartao",
        "tipo_conta",
        "data_criacao_conta"
    ))
    
    return df

csvPath = input("Digite o caminho em que o arquivo csv será salvo: ") + "/sicoop"
postgresDriverPath = os.path.dirname(os.path.abspath(__file__)) + "/workspace/postgresql-42.5.0.jar"
appName = "Desafio SiCooperative - Pyspark Postgres via psycopg2"
master = "local"

spark = initialize_spark(postgresDriverPath, appName, master)

df_associado = getData(spark, "sicooperative", "associado")
df_cartao = getData(spark, "sicooperative", "cartao")
df_conta = getData(spark, "sicooperative", "conta")
df_movimento = getData(spark, "sicooperative", "movimento")

df_movimento = ajustColumns(df_movimento, 'mov_')
df_cartao = ajustColumns(df_cartao, 'car_')
df_conta = ajustColumns(df_conta, 'con_')
df_associado = ajustColumns(df_associado, 'ass_')

df = joinDataFrames()

df.write.option("header", "true").csv(csvPath, mode='overwrite')

print('Data exportada para: ' + csvPath)
