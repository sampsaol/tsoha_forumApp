CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username TEXT UNIQUE,
  password TEXT
);

CREATE TABLE chains (
  id SERIAL PRIMARY KEY,
  content TEXT,
  category TEXT,
  user_id INTEGER REFERENCES users,
  sent_at TIMESTAMP
);

CREATE TABLE messages (
  id SERIAL PRIMARY KEY,
  content TEXT,
  chain_id INTEGER REFERENCES chains,
  user_id INTEGER REFERENCES users
);

CREATE TABLE likes (
  id SERIAL PRIMARY KEY,
  message_id INTEGER REFERENCES messages,
  user_id INTEGER REFERENCES users
);