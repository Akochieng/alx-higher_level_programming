-- group by score and the label number for number of records of scores
SELECT score, COUNT(score) as number FROM second_table GROUP BY score ORDER BY score DESC;
