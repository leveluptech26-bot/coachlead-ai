-- Database Schema
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT
);

CREATE TABLE leads (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    problem TEXT
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    lead_id INT,
    message TEXT
);
