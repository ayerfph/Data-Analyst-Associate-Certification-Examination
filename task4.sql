-- Write your query for task 4 in this cell
SELECT product_id, price, average_units_sold
FROM products 
WHERE product_type IN ('Meat', 'Dairy')
	  AND average_units_sold > 10;