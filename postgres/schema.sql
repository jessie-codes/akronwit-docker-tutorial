
CREATE TABLE IF NOT EXISTS users (
    user_id serial UNIQUE,
    username text NOT NULL,
    password text NOT NULL
);

INSERT INTO users(username, password)
VALUES ('aanderson', 'password1'),
('mmasters', 'password2');