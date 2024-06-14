-- Creating a View that will have an ordered
-- number of non-unique fans by their country

CREATE VIEW v AS
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

SELECT * FROM v;
