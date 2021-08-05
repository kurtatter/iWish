CREATE TABLE IF NOT EXISTS wish (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL,
price text not null,
url text NOT NULL,
description text NOT NULL
);