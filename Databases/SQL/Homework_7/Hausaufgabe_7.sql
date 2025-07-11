# 1. Вывести названия продуктов таблица products, включая количество заказанных единиц quantity для
# каждого продукта таблица order_details. Решить задачу с помощью cte и подзапроса.
WITH 
	cte_o AS (SELECT product_id, sum(quantity) AS quantity_sum 
			  FROM order_details 
			  GROUP BY product_id)
SELECT 
    product_name, 
    coalesce(o.quantity_sum,0),
    o.product_id, id # вывожу что бы себя проверить
FROM
    products AS p
LEFT JOIN
    cte_o AS o ON p.id = o.product_id;

# подзапрос
SELECT 
    product_name, 
    coalesce(o.quantity_sum,0), 
    o.product_id, id # вывожу что бы себя проверить
FROM 
    (SELECT product_id, sum(quantity) AS quantity_sum 
	 FROM order_details 
	 GROUP BY product_id) AS o
RIGHT JOIN
    products AS p ON o.product_id = p.id;
    
# 2. Найти все заказы таблица orders, сделанные после даты самого первого заказа клиента Lee таблица customers.

#  т. к. в таблице customs два разных клиента по фамилии 'Lee' (разные имена), то берём первого попавшегося
WITH 
	cte_c AS (SELECT order_date
			  FROM orders
			  JOIN customers AS c ON customer_id = c.id AND last_name = 'Lee'
			  ORDER BY order_date
			  LIMIT 1)
SELECT 
    *
FROM
    orders
WHERE order_date > (SELECT order_date FROM cte_c);

# подзапрос
SELECT 
    *
FROM
    orders
WHERE order_date > (SELECT order_date
					FROM orders
					JOIN customers AS c ON customer_id = c.id AND last_name = 'Lee'
					ORDER BY order_date 
                    LIMIT 1);

# 3. Найти все продукты таблицы products c максимальным target_level
WITH 
	cte_p AS (SELECT max(target_level) AS max_target 
			  FROM products)
SELECT * 
FROM products
WHERE target_level = (SELECT max_target FROM cte_p);

# подзапрос
SELECT * 
FROM products
WHERE target_level = (SELECT max(target_level) AS max_target FROM products);





