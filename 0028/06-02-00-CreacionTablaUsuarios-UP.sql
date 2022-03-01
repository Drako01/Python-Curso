CREATE TABLE public.usuario
(
    id_usuario serial NOT NULL,
    username character varying,
    password character varying,
    PRIMARY KEY (id_usuario)
);

ALTER TABLE public.usuario
    OWNER to postgres;