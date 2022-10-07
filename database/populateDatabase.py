import random
from datetime import datetime, timedelta
from random import randint

from database.functionsDatabase import executeInsertQuery, executeSelectQuery


def populateAssociado(fake, quantity):    
    for x in range(quantity):
        firstName = fake.first_name()
        lastName = fake.last_name()
        age = str(randint(18, 90))
        email = "{0}.{1}{2}@{3}".format(firstName, lastName, age, fake.free_email_domain())        
        query = "INSERT INTO associado (nome, sobrenome, idade, email) VALUES ('{0}','{1}',{2},'{3}')".format(firstName, lastName, age, email)
        
        executeInsertQuery(query)
        
    return True

def populateConta():
    results = executeSelectQuery('SELECT DISTINCT id FROM associado ORDER BY 1')
    
    for x in results:
        tipoContaInt = randint(1,3)
    
        if tipoContaInt == 1:
            tipoConta = "Conta Corrente"
        elif tipoContaInt == 2:
            tipoConta = "Conta Salário"
        else:
            tipoConta = "Conta Poupança"
            
        query = "INSERT INTO conta (tipo, data_criacao, id_associado) VALUES ('{0}', '{1}', {2})".format(tipoConta, datetime.now() - timedelta(randint(0, 1000)), x[0])
        
        executeInsertQuery(query)
        
    return True
            
def populateCartao(fake, quantity):
    selectQuery = "SELECT CONCAT(nome, ' ', sobrenome) AS nom_impresso, co.id AS id_conta, a.id AS id_associado FROM conta AS co LEFT JOIN associado AS a ON a.id = co.id_associado ORDER BY co.id"
    
    results = executeSelectQuery(selectQuery)
    
    for result in results:
        for x in range(quantity):
            cardNumber = fake.credit_card_number()
        
            query = "INSERT INTO cartao (num_cartao, nom_impresso, data_criacao, id_conta, id_associado) VALUES ('{0}', '{1}', '{2}', {3}, {4})".format(cardNumber, result[0], datetime.now() - timedelta(randint(0, 1000)),result[1], result[2])
        
            executeInsertQuery(query)
            
    return True

def populateMovimento(fake, quantity):
    selectQuery = "SELECT DISTINCT id FROM cartao ORDER BY 1"
    results = executeSelectQuery(selectQuery)
    
    for result in results:
        for x in range(quantity):
            vlrTransaction = round(random.uniform(1, 1000), 2)
        
            query = "INSERT INTO movimento (vlr_transacao, des_transacao, data_movimento, id_cartao) VALUES ({0}, '{1}', '{2}', {3})".format(vlrTransaction, fake.pystr(), datetime.now() - timedelta(randint(0, 1000)), result[0])
        
            executeInsertQuery(query)
            
    return True
