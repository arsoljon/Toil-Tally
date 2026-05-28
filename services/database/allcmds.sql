---Before each connection---
PRAGMA foreign_keys = ON;
---setup---
CREATE TABLE IF NOT EXISTS jobs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(255) UNIQUE,
  duration TEXT
);
CREATE TABLE IF NOT EXISTS sessions (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   job_id INTEGER,
   session_seconds INTEGER,
   pause_seconds INTEGER,
   date TEXT,
   FOREIGN KEY(job_id) references jobs(id) ON DELETE CASCADE
 );
---insert---
INSERT INTO jobs (name, duration) VALUES ('devops', '03:04:05') on CONFLICT(name) DO UPDATE SET duration = excluded.duration;
INSERT INTO jobs (name, duration) VALUES ('stonks', '02:03:04') on CONFLICT(name) DO UPDATE SET duration = excluded.duration;
INSERT INTO sessions(job_id, session_seconds, pause_seconds, date) VALUES ( (SELECT id FROM jobs WHERE name='devops') ,123,456,'1/2/2026');
INSERT INTO sessions(job_id, session_seconds, pause_seconds, date) VALUES ((SELECT id FROM jobs WHERE name='devops'),123,456,'1/2/2026');
INSERT INTO sessions(job_id, session_seconds, pause_seconds, date) VALUES ((SELECT id FROM jobs WHERE name='stonks'),135,479,'1/2/2026');
INSERT INTO sessions(job_id, session_seconds, pause_seconds, date) VALUES ((SELECT id FROM jobs WHERE name='stonks'),531,965,'1/2/2026');
 ---requests---
 SELECT * FROM sessions;
 ---delete---
 DELETE FROM jobs where id = (SELECT id from jobs where name='devops');
 ---update---
UPDATE jobs SET duration = '04:05:06' WHERE id = 1;