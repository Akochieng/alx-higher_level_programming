-- list records of the second table of the database
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND TRIM(name) <> ''
ORDER BY score DESC;
