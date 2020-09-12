CREATE TABLE notas(
    id int(25) auto_increment not null,
    usuario_id int(25) not null,
    titulo varchar(255) not null,
    descripcion MEDIUMTEXT,
    fecha date not null,
    PRIMARY KEY(id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDB;

CREATE TABLE notas(
    id int(255 auto_increment not null,
    nombre varchar(100),
    apellidos varchar(200),
    email varchar(60) not null,
    password varchar(255) not null,
    fecha date not null,
    CONSTRAINT uq_email UNIQUE(email),
    PRIMARY KEY(id)
)ENGINE=InnoDB;