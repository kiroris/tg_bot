CREATE TABLE users (
    user_id bigint PRIMARY KEY NOT NULL,
    balance decimal(10,2) DEFAULT 0.0 NOT NULL,
    admin boolean DEFAULT false NOT NULL,
    fk_country_id SERIAL,
    FOREIGN KEY (fk_country_id) REFERENCES countries (country_id)
);
