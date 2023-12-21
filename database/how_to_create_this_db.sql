CREATE TABLE users(
    user_id bigint PRIMARY KEY NOT NULL,
    balance decimal(10,2) DEFAULT 0.0 NOT NULL,
    seller boolean DEFAULT false NOT NULL,
    admin boolean DEFAULT false NOT NULL
);

