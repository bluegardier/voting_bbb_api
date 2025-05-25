CREATE TABLE IF NOT EXISTS voting_bbb_table (
    id SERIAL PRIMARY KEY,
    request_id TEXT NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    arthur_aguiar INTEGER NOT NULL,
    davi_brito INTEGER NOT NULL,
    yagami_light INTEGER NOT NULL
);
