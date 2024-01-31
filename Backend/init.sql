-- init.sql

-- Create the users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Insert some sample data
INSERT INTO users (name) VALUES
    ('John Doe'),
    ('Jane Smith'),
    ('Bob Johnson');
