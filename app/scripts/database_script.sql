CREATE TABLE city (
    ibge TEXT NOT NULL,
    name TEXT NOT NULL,
    federative_unit TEXT NOT NULL,
    flag TEXT,
    blazon TEXT,
    motto TEXT,
    anthem TEXT,
    total_area INTEGER,
    zip_range TEXT,
    CONSTRAINT ibge_key UNIQUE (ibge)
);