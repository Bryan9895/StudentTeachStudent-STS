CREATE DATABASE IF NOT EXISTS aula;

USE aula;

CREATE TABLE IF NOT EXISTS alunos (
    nome VARCHAR(255),
    curso VARCHAR(255),
    matricula VARCHAR(20) UNIQUE,
    constraint matricula_unique primary key (matricula)
);

INSERT INTO alunos (nome, curso, matricula) VALUES
 ("Lilia Carla", "Python, Informatica Basica, Manutenção de Computadores", "20261321000040"),
    ("Yasmin Erbenes", "Python, Informatica Basica", "20261321000073"),
    ("Suellen Quinteta", "Python, Informatica Basica", "20261321000056"),
    ("Nicolas Mateus", "Python, Informatica Basica, Manutenção de Computadores", "20261321000064"),
    ("Esther Tiburcio", "Python, Manutenção de Computadores, Front-end", "20261321000019");
    