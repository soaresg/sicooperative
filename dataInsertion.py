from faker import Faker

from database.populateDatabase import (populateAssociado, populateCartao,
                                       populateConta, populateMovimento)

fake = Faker()

populateAssociado(fake, 1)
populateConta()
populateCartao(fake, 1)
populateMovimento(fake, 1)
