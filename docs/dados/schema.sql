CREATE TABLE exercicio (
	id INTEGER NOT NULL, 
	nome VARCHAR(80) NOT NULL, 
	grupo_muscular VARCHAR(40), 
	PRIMARY KEY (id)
);

CREATE TABLE refeicao (
	id INTEGER NOT NULL, 
	usuario_id INTEGER NOT NULL, 
	data_hora DATETIME NOT NULL, 
	descricao VARCHAR(255), 
	proteina_g FLOAT, 
	carbo_g FLOAT, 
	gordura_g FLOAT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(usuario_id) REFERENCES usuario (id)
);

CREATE TABLE serie (
	id INTEGER NOT NULL, 
	treino_exercicio_id INTEGER NOT NULL, 
	repeticoes INTEGER NOT NULL, 
	carga FLOAT, 
	duracao_seg INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(treino_exercicio_id) REFERENCES treino_exercicio (id)
);

CREATE TABLE treino (
	id INTEGER NOT NULL, 
	usuario_id INTEGER NOT NULL, 
	data_hora DATETIME NOT NULL, 
	observacoes VARCHAR(255), 
	percepcao_esforco INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(usuario_id) REFERENCES usuario (id)
);

CREATE TABLE treino_exercicio (
	id INTEGER NOT NULL, 
	treino_id INTEGER NOT NULL, 
	exercicio_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(treino_id) REFERENCES treino (id), 
	FOREIGN KEY(exercicio_id) REFERENCES exercicio (id)
);

CREATE TABLE usuario (
	id INTEGER NOT NULL, 
	nome VARCHAR(100) NOT NULL, 
	email VARCHAR(120) NOT NULL, 
	senha_hash VARCHAR(255) NOT NULL, 
	criado_em DATETIME, 
	PRIMARY KEY (id), 
	UNIQUE (email)
);
