-- imprting a table into the database hbtn_0c_0
USE hbtn_0c_0;
SELECT city, AVG(value) AS A_temp
FROM temperatures
GROUP BY city
ORDER BY A_temp DESC;
