-- Write your query for task 3 in this cell
SELECT
	product_type,
	MIN(price) AS min_price,
	MAX(price) AS max_price
FROM products
GROUP BY product_type;