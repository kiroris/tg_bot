CREATE TABLE IF NOT EXISTS countries (
    country_id SERIAL PRIMARY KEY,
    country_eng VARCHAR(150) NOT NULL,
    country_rus VARCHAR(150) NOT NULL
);

