CREATE TABLE IF NOT EXISTS associado (
    id SERIAL,
    nome VARCHAR(100) NOT NULL,
    sobrenome VARCHAR(255) NOT NULL,
    idade INT NOT NULL,
    email VARCHAR(255) NOT NULL,
    CONSTRAINT "PK_associado" PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS conta (
    id SERIAL,
    tipo VARCHAR(50) NOT NULL,
    data_criacao TIMESTAMP NOT NULL,
    id_associado INT,
    CONSTRAINT "PK_conta" PRIMARY KEY (id),
    CONSTRAINT "FK_conta_associado" FOREIGN KEY (id_associado)
        REFERENCES associado (id)
);

CREATE TABLE IF NOT EXISTS cartao (
    id SERIAL,
    num_cartao VARCHAR(50) NOT NULL,
    nom_impresso VARCHAR(100) NOT NULL,
    data_criacao TIMESTAMP NOT NULL,
    id_conta INT NOT NULL,
    id_associado INT,
    CONSTRAINT "PK_cartao" PRIMARY KEY (id),
    CONSTRAINT "FK_cartao_conta" FOREIGN KEY (id_conta)
        REFERENCES conta (id),
    CONSTRAINT "FK_cartao_associado" FOREIGN KEY (id_associado)
        REFERENCES associado (id)
);

CREATE TABLE IF NOT EXISTS movimento (
    id SERIAL,
    vlr_transacao FLOAT NOT NULL,
    des_transacao VARCHAR(255),
    data_movimento TIMESTAMP NOT NULL,
    id_cartao INT,
    CONSTRAINT "PK_movimento" PRIMARY KEY (id),
    CONSTRAINT "FK_movimento_cartao" FOREIGN KEY (id_cartao)
        REFERENCES cartao (id)
);