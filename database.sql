-- AeroBrasil Linhas Aereas | Banco de dados relacional
-- MySQL 8.0.16+ | Execucao integral em banco vazio
-- Modelo conforme DER do README: PASSAGEIRO, AERONAVE, AEROPORTO, VOO, RESERVA
-- Massa de dados: 350 + 25 + 25 + 200 + 400 = 1000 registros.

CREATE DATABASE IF NOT EXISTS aerobrasil_reservas
    CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE aerobrasil_reservas;

-- Tabelas dependentes removidas primeiro para permitir reexecucao completa.
DROP TABLE IF EXISTS reserva;
DROP TABLE IF EXISTS voo;
DROP TABLE IF EXISTS aeroporto;
DROP TABLE IF EXISTS aeronave;
DROP TABLE IF EXISTS passageiro;

CREATE TABLE passageiro (
    id_passageiro INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(120) NOT NULL,
    documento_identificacao VARCHAR(30) NOT NULL UNIQUE,
    data_nascimento DATE NOT NULL,
    contato VARCHAR(150) NULL,
    CONSTRAINT chk_passageiro_nome CHECK (CHAR_LENGTH(TRIM(nome)) > 0)
) ENGINE=InnoDB;

CREATE TABLE aeronave (
    id_aeronave INT PRIMARY KEY AUTO_INCREMENT,
    modelo VARCHAR(80) NOT NULL,
    capacidade INT NOT NULL,
    CONSTRAINT chk_aeronave_capacidade CHECK (capacidade > 0)
) ENGINE=InnoDB;

CREATE TABLE aeroporto (
    id_aeroporto INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(160) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    estado_pais VARCHAR(100) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE voo (
    num_voo INT PRIMARY KEY,
    data DATE NOT NULL,
    hora_partida TIME NOT NULL,
    hora_chegada TIME NOT NULL,
    id_aeronave INT NOT NULL,
    id_aeroporto_origem INT NOT NULL,
    id_aeroporto_destino INT NOT NULL,
    CONSTRAINT fk_voo_aeronave FOREIGN KEY (id_aeronave)
        REFERENCES aeronave(id_aeronave) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_voo_origem FOREIGN KEY (id_aeroporto_origem)
        REFERENCES aeroporto(id_aeroporto) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_voo_destino FOREIGN KEY (id_aeroporto_destino)
        REFERENCES aeroporto(id_aeroporto) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT chk_voo_aeroportos CHECK (id_aeroporto_origem <> id_aeroporto_destino)
) ENGINE=InnoDB;

CREATE TABLE reserva (
    num_reserva INT PRIMARY KEY AUTO_INCREMENT,
    data_reserva DATE NOT NULL,
    num_assento VARCHAR(5) NOT NULL,
    classe VARCHAR(20) NOT NULL DEFAULT 'Economica',
    valor_total DECIMAL(10,2) NOT NULL,
    id_passageiro INT NOT NULL,
    num_voo INT NOT NULL,
    CONSTRAINT fk_reserva_passageiro FOREIGN KEY (id_passageiro)
        REFERENCES passageiro(id_passageiro) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT fk_reserva_voo FOREIGN KEY (num_voo)
        REFERENCES voo(num_voo) ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT uq_reserva_assento_voo UNIQUE (num_voo, num_assento),
    CONSTRAINT chk_reserva_valor CHECK (valor_total >= 0),
    CONSTRAINT chk_reserva_classe CHECK (classe IN ('Economica','Executiva')),
    CONSTRAINT chk_reserva_assento CHECK (CHAR_LENGTH(TRIM(num_assento)) > 0)
) ENGINE=InnoDB;

-- Insercao de dados de teste; tabelas independentes antes das dependentes.

-- PASSAGEIRO: 50 registros
INSERT INTO passageiro (id_passageiro, nome, documento_identificacao, data_nascimento, contato) VALUES
  (1, 'Henrique Oliveira Vieira', 'BR000000001', '1999-02-15', 'contato001@exemplo.com'),
  (2, 'Paula Barbosa Santos', 'BR000000002', '1986-02-04', 'contato002@exemplo.com'),
  (3, 'Beatriz Pereira Pereira', 'BR000000003', '1999-06-23', 'contato003@exemplo.com'),
  (4, 'Igor Carvalho Martins', 'BR000000004', '1985-04-28', 'contato004@exemplo.com'),
  (5, 'Renata Ribeiro Dias', 'BR000000005', '1980-01-10', 'contato005@exemplo.com'),
  (6, 'Camila Costa Almeida', 'BR000000006', '1959-12-03', 'contato006@exemplo.com'),
  (7, 'João Rocha Silva', 'BR000000007', '1958-08-03', 'contato007@exemplo.com'),
  (8, 'Sofia Dias Ribeiro', 'BR000000008', '1987-02-17', 'contato008@exemplo.com'),
  (9, 'Davi Rodrigues Mendes', 'BR000000009', '1998-01-21', 'contato009@exemplo.com'),
  (10, 'Kevin Ferreira Ferreira', 'BR000000010', '1958-05-03', 'contato010@exemplo.com'),
  (11, 'Talita Santos Barbosa', 'BR000000011', '1956-04-24', 'contato011@exemplo.com'),
  (12, 'Eduarda Gomes Souza', 'BR000000012', '1985-12-23', 'contato012@exemplo.com'),
  (13, 'Marcos Silva Rocha', 'BR000000013', '1974-06-26', 'contato013@exemplo.com'),
  (14, 'Vitória Lima Nascimento', 'BR000000014', '2002-08-10', 'contato014@exemplo.com'),
  (15, 'Fernanda Souza Gomes', 'BR000000015', '1966-07-02', 'contato015@exemplo.com'),
  (16, 'Miguel Martins Carvalho', 'BR000000016', '1997-05-08', 'contato016@exemplo.com'),
  (17, 'Yasmin Teixeira Teixeira', 'BR000000017', '1957-05-12', 'contato017@exemplo.com'),
  (18, 'Gabriela Mendes Rodrigues', 'BR000000018', '1955-04-30', 'contato018@exemplo.com'),
  (19, 'Otávio Vieira Oliveira', 'BR000000019', '1975-08-27', 'contato019@exemplo.com'),
  (20, 'Alice Nascimento Lima', 'BR000000020', '1976-09-18', 'contato020@exemplo.com'),
  (21, 'Helena Almeida Costa', 'BR000000021', '1968-06-30', 'contato021@exemplo.com'),
  (22, 'Pedro Oliveira Vieira', 'BR000000022', '1972-06-28', 'contato022@exemplo.com'),
  (23, 'Bruno Barbosa Santos', 'BR000000023', '1988-04-06', 'contato023@exemplo.com'),
  (24, 'Isabela Pereira Pereira', 'BR000000024', '1995-10-16', 'contato024@exemplo.com'),
  (25, 'Rafael Carvalho Martins', 'BR000000025', '1981-04-03', 'contato025@exemplo.com'),
  (26, 'Caio Ribeiro Dias', 'BR000000026', '1956-06-13', 'contato026@exemplo.com'),
  (27, 'Júlia Costa Almeida', 'BR000000027', '1967-08-11', 'contato027@exemplo.com'),
  (28, 'Samuel Rocha Silva', 'BR000000028', '1978-02-05', 'contato028@exemplo.com'),
  (29, 'Daniel Dias Ribeiro', 'BR000000029', '1992-06-28', 'contato029@exemplo.com'),
  (30, 'Larissa Rodrigues Mendes', 'BR000000030', '1986-06-09', 'contato030@exemplo.com'),
  (31, 'Thiago Ferreira Ferreira', 'BR000000031', '1973-02-07', 'contato031@exemplo.com'),
  (32, 'Elisa Santos Barbosa', 'BR000000032', '1982-04-24', 'contato032@exemplo.com'),
  (33, 'Lívia Gomes Souza', 'BR000000033', '1974-11-22', 'contato033@exemplo.com'),
  (34, 'Vinícius Silva Rocha', 'BR000000034', '1986-12-18', 'contato034@exemplo.com'),
  (35, 'Felipe Lima Nascimento', 'BR000000035', '2000-08-30', 'contato035@exemplo.com'),
  (36, 'Natália Souza Gomes', 'BR000000036', '1964-08-23', 'contato036@exemplo.com'),
  (37, 'William Martins Carvalho', 'BR000000037', '1969-08-02', 'contato037@exemplo.com'),
  (38, 'Gustavo Teixeira Teixeira', 'BR000000038', '1995-06-09', 'contato038@exemplo.com'),
  (39, 'Nicole Mendes Rodrigues', 'BR000000039', '1961-02-25', 'contato039@exemplo.com'),
  (40, 'Ana Vieira Oliveira', 'BR000000040', '1997-06-17', 'contato040@exemplo.com'),
  (41, 'Henrique Nascimento Lima', 'BR000000041', '1985-09-06', 'contato041@exemplo.com'),
  (42, 'Paula Almeida Costa', 'BR000000042', '1985-08-07', 'contato042@exemplo.com'),
  (43, 'Beatriz Oliveira Vieira', 'BR000000043', '1987-10-04', 'contato043@exemplo.com'),
  (44, 'Igor Barbosa Santos', 'BR000000044', '1980-11-18', 'contato044@exemplo.com'),
  (45, 'Renata Pereira Pereira', 'BR000000045', '1983-09-25', 'contato045@exemplo.com'),
  (46, 'Camila Carvalho Martins', 'BR000000046', '1996-07-24', 'contato046@exemplo.com'),
  (47, 'João Ribeiro Dias', 'BR000000047', '1974-11-01', 'contato047@exemplo.com'),
  (48, 'Sofia Costa Almeida', 'BR000000048', '1974-08-19', 'contato048@exemplo.com'),
  (49, 'Davi Rocha Silva', 'BR000000049', '1959-04-11', 'contato049@exemplo.com'),
  (50, 'Kevin Dias Ribeiro', 'BR000000050', '1965-07-14', 'contato050@exemplo.com'),

-- AERONAVE: 25 registros
INSERT INTO aeronave (id_aeronave, modelo, capacidade) VALUES
  (1, 'Airbus A320', 180),
  (2, 'Airbus A320neo', 186),
  (3, 'Airbus A321', 220),
  (4, 'Boeing 737-800', 189),
  (5, 'Boeing 737 MAX 8', 186),
  (6, 'Embraer E195', 118),
  (7, 'Embraer E195-E2', 136),
  (8, 'Embraer E190', 100),
  (9, 'Airbus A319', 144),
  (10, 'Airbus A220-300', 145),
  (11, 'Airbus A320', 180),
  (12, 'Airbus A320neo', 186),
  (13, 'Airbus A321', 220),
  (14, 'Boeing 737-800', 189),
  (15, 'Boeing 737 MAX 8', 186),
  (16, 'Embraer E195', 118),
  (17, 'Embraer E195-E2', 136),
  (18, 'Embraer E190', 100),
  (19, 'Airbus A319', 144),
  (20, 'Airbus A220-300', 145),
  (21, 'Airbus A320', 180),
  (22, 'Airbus A320neo', 186),
  (23, 'Airbus A321', 220),
  (24, 'Boeing 737-800', 189),
  (25, 'Boeing 737 MAX 8', 186);

-- AEROPORTO: 25 registros
INSERT INTO aeroporto (id_aeroporto, nome, cidade, estado_pais) VALUES
  (1, 'Aeroporto Internacional de Guarulhos', 'Guarulhos', 'São Paulo'),
  (2, 'Aeroporto de Congonhas', 'São Paulo', 'São Paulo'),
  (3, 'Aeroporto Internacional de Viracopos', 'Campinas', 'São Paulo'),
  (4, 'Aeroporto Internacional do Galeão', 'Rio de Janeiro', 'Rio de Janeiro'),
  (5, 'Aeroporto Santos Dumont', 'Rio de Janeiro', 'Rio de Janeiro'),
  (6, 'Aeroporto Internacional de Brasília', 'Brasília', 'Distrito Federal'),
  (7, 'Aeroporto Internacional de Confins', 'Confins', 'Minas Gerais'),
  (8, 'Aeroporto Internacional de Salvador', 'Salvador', 'Bahia'),
  (9, 'Aeroporto Internacional do Recife', 'Recife', 'Pernambuco'),
  (10, 'Aeroporto Internacional de Fortaleza', 'Fortaleza', 'Ceará'),
  (11, 'Aeroporto Internacional de Natal', 'São Gonçalo do Amarante', 'Rio Grande do Norte'),
  (12, 'Aeroporto Internacional de João Pessoa', 'Bayeux', 'Paraíba'),
  (13, 'Aeroporto Internacional de Maceió', 'Rio Largo', 'Alagoas'),
  (14, 'Aeroporto Internacional de Aracaju', 'Aracaju', 'Sergipe'),
  (15, 'Aeroporto Internacional de Porto Alegre', 'Porto Alegre', 'Rio Grande do Sul'),
  (16, 'Aeroporto Internacional de Florianópolis', 'Florianópolis', 'Santa Catarina'),
  (17, 'Aeroporto Internacional de Curitiba', 'São José dos Pinhais', 'Paraná'),
  (18, 'Aeroporto Internacional de Manaus', 'Manaus', 'Amazonas'),
  (19, 'Aeroporto Internacional de Belém', 'Belém', 'Pará'),
  (20, 'Aeroporto Internacional de São Luís', 'São Luís', 'Maranhão'),
  (21, 'Aeroporto Internacional de Cuiabá', 'Várzea Grande', 'Mato Grosso'),
  (22, 'Aeroporto Internacional de Campo Grande', 'Campo Grande', 'Mato Grosso do Sul'),
  (23, 'Aeroporto de Goiânia', 'Goiânia', 'Goiás'),
  (24, 'Aeroporto de Vitória', 'Vitória', 'Espírito Santo'),
  (25, 'Aeroporto Internacional de Foz do Iguaçu', 'Foz do Iguaçu', 'Paraná');

-- VOO: 50 registros
INSERT INTO voo (num_voo, data, hora_partida, hora_chegada, id_aeronave, id_aeroporto_origem, id_aeroporto_destino) VALUES
  (1001, '2026-11-01', '06:00:00', '08:15:00', 1, 4, 10),
  (1002, '2026-11-01', '09:10:00', '12:25:00', 4, 11, 21),
  (1003, '2026-11-01', '13:20:00', '17:35:00', 7, 18, 7),
  (1004, '2026-11-01', '17:30:00', '19:45:00', 10, 25, 18),
  (1005, '2026-11-02', '06:40:00', '09:55:00', 13, 7, 4),
  (1006, '2026-11-02', '09:50:00', '13:05:00', 16, 14, 15),
  (1007, '2026-11-02', '13:00:00', '15:15:00', 19, 21, 1),
  (1008, '2026-11-02', '17:10:00', '20:25:00', 22, 3, 12),
  (1009, '2026-11-03', '06:20:00', '10:35:00', 25, 10, 23),
  (1010, '2026-11-03', '09:30:00', '11:45:00', 3, 17, 9),
  (1011, '2026-11-03', '13:40:00', '16:55:00', 6, 24, 20),
  (1012, '2026-11-03', '17:50:00', '21:05:00', 9, 6, 7),
  (1013, '2026-11-04', '06:00:00', '08:15:00', 12, 13, 17),
  (1014, '2026-11-04', '09:10:00', '12:25:00', 15, 20, 3),
  (1015, '2026-11-04', '13:20:00', '17:35:00', 18, 2, 14),
  (1016, '2026-11-04', '17:30:00', '19:45:00', 21, 9, 25),
  (1017, '2026-11-05', '06:40:00', '09:55:00', 24, 16, 11),
  (1018, '2026-11-05', '09:50:00', '13:05:00', 2, 23, 22),
  (1019, '2026-11-05', '13:00:00', '15:15:00', 5, 5, 8),
  (1020, '2026-11-05', '17:10:00', '20:25:00', 8, 12, 19),
  (1021, '2026-11-06', '06:20:00', '10:35:00', 11, 19, 5),
  (1022, '2026-11-06', '09:30:00', '11:45:00', 14, 1, 16),
  (1023, '2026-11-06', '13:40:00', '16:55:00', 17, 8, 2),
  (1024, '2026-11-06', '17:50:00', '21:05:00', 20, 15, 13),
  (1025, '2026-11-07', '06:00:00', '08:15:00', 23, 22, 24),
  (1026, '2026-11-07', '09:10:00', '12:25:00', 1, 4, 10),
  (1027, '2026-11-07', '13:20:00', '17:35:00', 4, 11, 21),
  (1028, '2026-11-07', '17:30:00', '19:45:00', 7, 18, 7),
  (1029, '2026-11-08', '06:40:00', '09:55:00', 10, 25, 18),
  (1030, '2026-11-08', '09:50:00', '13:05:00', 13, 7, 4),
  (1031, '2026-11-08', '13:00:00', '15:15:00', 16, 14, 15),
  (1032, '2026-11-08', '17:10:00', '20:25:00', 19, 21, 1),
  (1033, '2026-11-09', '06:20:00', '10:35:00', 22, 3, 12),
  (1034, '2026-11-09', '09:30:00', '11:45:00', 25, 10, 23),
  (1035, '2026-11-09', '13:40:00', '16:55:00', 3, 17, 9),
  (1036, '2026-11-09', '17:50:00', '21:05:00', 6, 24, 20),
  (1037, '2026-11-10', '06:00:00', '08:15:00', 9, 6, 7),
  (1038, '2026-11-10', '09:10:00', '12:25:00', 12, 13, 17),
  (1039, '2026-11-10', '13:20:00', '17:35:00', 15, 20, 3),
  (1040, '2026-11-10', '17:30:00', '19:45:00', 18, 2, 14),
  (1041, '2026-11-11', '06:40:00', '09:55:00', 21, 9, 25),
  (1042, '2026-11-11', '09:50:00', '13:05:00', 24, 16, 11),
  (1043, '2026-11-11', '13:00:00', '15:15:00', 2, 23, 22),
  (1044, '2026-11-11', '17:10:00', '20:25:00', 5, 5, 8),
  (1045, '2026-11-12', '06:20:00', '10:35:00', 8, 12, 19),
  (1046, '2026-11-12', '09:30:00', '11:45:00', 11, 19, 5),
  (1047, '2026-11-12', '13:40:00', '16:55:00', 14, 1, 16),
  (1048, '2026-11-12', '17:50:00', '21:05:00', 17, 8, 2),
  (1049, '2026-11-13', '06:00:00', '08:15:00', 20, 15, 13),

-- RESERVA: 50 registros
INSERT INTO reserva (num_reserva, data_reserva, num_assento, classe, valor_total, id_passageiro, num_voo) VALUES
  (1, '2026-10-31', '01A', 'Economica', '280.00', 1, 1001),
  (2, '2026-10-27', '01A', 'Economica', '333.00', 44, 1038),
  (3, '2026-10-23', '01A', 'Economica', '386.00', 87, 1075),
  (4, '2026-10-19', '01A', 'Executiva', '921.90', 130, 1112),
  (5, '2026-10-16', '01A', 'Economica', '492.00', 173, 1149),
  (6, '2026-10-12', '01A', 'Economica', '545.00', 216, 1186),
  (7, '2026-11-02', '01A', 'Economica', '598.00', 259, 1023),
  (8, '2026-10-29', '01A', 'Executiva', '1367.10', 302, 1060),
  (9, '2026-10-26', '01A', 'Economica', '704.00', 345, 1097),
  (10, '2026-10-22', '01A', 'Economica', '757.00', 38, 1134),
  (11, '2026-10-18', '01A', 'Economica', '810.00', 81, 1171),
  (12, '2026-08-25', '01A', 'Executiva', '1812.30', 124, 1008),
  (13, '2026-11-05', '01A', 'Economica', '916.00', 167, 1045),
  (14, '2026-11-01', '01A', 'Economica', '969.00', 210, 1082),
  (15, '2026-10-28', '01A', 'Economica', '1022.00', 253, 1119),
  (16, '2026-10-24', '01A', 'Executiva', '2257.50', 296, 1156),
  (17, '2026-10-21', '01A', 'Economica', '1128.00', 339, 1193),
  (18, '2026-08-28', '01A', 'Economica', '1181.00', 32, 1030),
  (19, '2026-11-07', '01A', 'Economica', '1234.00', 75, 1067),
  (20, '2026-11-03', '01A', 'Executiva', '2702.70', 118, 1104),
  (21, '2026-10-31', '01A', 'Economica', '290.00', 161, 1141),
  (22, '2026-10-27', '01A', 'Economica', '343.00', 204, 1178),
  (23, '2026-09-03', '01A', 'Economica', '396.00', 247, 1015),
  (24, '2026-08-30', '01A', 'Executiva', '942.90', 290, 1052),
  (25, '2026-11-10', '01A', 'Economica', '502.00', 333, 1089),
  (26, '2026-11-06', '01A', 'Economica', '555.00', 26, 1126),
  (27, '2026-11-02', '01A', 'Economica', '608.00', 69, 1163),
  (28, '2026-10-29', '01A', 'Executiva', '1388.10', 112, 1200),
  (29, '2026-09-06', '01A', 'Economica', '714.00', 155, 1037),
  (30, '2026-11-16', '01A', 'Economica', '767.00', 198, 1074),
  (31, '2026-11-12', '01A', 'Economica', '820.00', 241, 1111),
  (32, '2026-11-08', '01A', 'Executiva', '1833.30', 284, 1148),
  (33, '2026-11-05', '01A', 'Economica', '926.00', 327, 1185),
  (34, '2026-09-12', '01A', 'Economica', '979.00', 20, 1022),
  (35, '2026-09-08', '01A', 'Economica', '1032.00', 63, 1059),
  (36, '2026-11-18', '01A', 'Executiva', '2278.50', 106, 1096),
  (37, '2026-11-15', '01A', 'Economica', '1138.00', 149, 1133),
  (38, '2026-11-11', '01A', 'Economica', '1191.00', 192, 1170),
  (39, '2026-09-18', '01A', 'Economica', '1244.00', 235, 1007),
  (40, '2026-09-14', '01A', 'Executiva', '2723.70', 278, 1044),
  (41, '2026-09-11', '01A', 'Economica', '300.00', 321, 1081),
  (42, '2026-11-21', '01A', 'Economica', '353.00', 14, 1118),
  (43, '2026-11-17', '01A', 'Economica', '406.00', 57, 1155),
  (44, '2026-11-13', '01A', 'Executiva', '963.90', 100, 1192),
  (45, '2026-09-21', '01A', 'Economica', '512.00', 143, 1029),
  (46, '2026-09-17', '01A', 'Economica', '565.00', 186, 1066),
  (47, '2026-09-13', '01A', 'Economica', '618.00', 229, 1103),
  (48, '2026-11-23', '01A', 'Executiva', '1409.10', 272, 1140),
  (49, '2026-11-20', '01A', 'Economica', '724.00', 315, 1177),
  (50, '2026-09-27', '01A', 'Economica', '777.00', 8, 1014),