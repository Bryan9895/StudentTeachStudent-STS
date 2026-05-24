CREATE DATABASE IF NOT EXISTS aula;

USE aula;

CREATE TABLE IF NOT EXISTS alunos (
    nome VARCHAR(255) not null,
    curso VARCHAR(255) not null,
    matricula VARCHAR(20) not null,
    email VARCHAR(255) unique not null,
    GitHub VARCHAR(50) unique not null,
    constraint pk_alunos primary key (matricula)
);


insert into alunos (nome, curso, matricula, email, GitHub) values 
    ("Esther Tiburcio", "Python, Front-end", "20261321000019", "esther.tiburcio10@aluno.ifce.edu.br", "tiburcio67"),
    ("Nicolas Mateus", "Python, Informatica Basica", "20261321000064", "silva.nicolas62@aluno.ifce.edu.br", "xxx"),
    ("Miguel Rogisson", "Python, Informatica Basica", "20261321000060", "miguel.rogisson10@aluno.ifce.edu.br", "rogisson"),
    ("Yasmin Erbenes", "Python, STS", "20261321000073", "yasmin.erbenes90@aluno.ifce.edu.br", "yasminerbenes"),
    ("Suellen Quinteta", "Python, Informatica Basica", "20261321000056", "maria.quintela09@aluno.ifce.edu.br", "xxxx"),
    ("Miguel Angelo", "Python", "20261321000058", "miguel.angelo09@aluno.ifce.edu.br", "angellsxxz"),
    ("Lilia Carla", "Python, Informatica Basica", "20261321000040", "pinheiro.lilia11@aluno.ifce.edu.br", "xxxxx"),
    ("Wesley Ryan", "Python, Informatica Basica", "20261321000072", "ryan.vidal62@aluno.ifce.edu.br", "ryanzito-ops")
;

create table if not exists presenca (
    id int auto_increment primary key,
    matricula varchar(20) not null,
    data date not null,
    nome varchar(255) not null,
    num_faltas int default 0,
    constraint fk_presenca foreign key (matricula) references alunos(matricula)
);

insert into presenca (matricula, data, nome, num_faltas) values 
    ("20261321000019", "2026-05-22", "Esther Tiburcio", 0),
    ("20261321000064", "2026-05-22", "Nicolas Mateus", 0),
    ("20261321000060", "2026-05-22", "Miguel Rogisson", 0),
    ("20261321000073", "2026-05-22", "Yasmin Erbenes", 0),
    ("20261321000056", "2026-05-22", "Suellen Quinteta", 0),
    ("20261321000058", "2026-05-22", "Miguel Angelo", 0),
    ("20261321000040", "2026-05-22", "Lilia Carla", 0),
    ("20261321000072", "2026-05-22", "Wesley Ryan", 0);


