# Таблица purchase_order_details
# 1. Для каждого заказа order_id выведите минимальный, максмальный и средний unit_cost
SELECT 
    purchase_order_id, unit_cost,
    min(unit_cost) OVER (PARTITION BY purchase_order_id) AS min_, 
    max(unit_cost) OVER (PARTITION BY purchase_order_id) AS min_,
    avg(unit_cost) OVER (PARTITION BY purchase_order_id) AS min_
FROM
    purchase_order_details;

# 2. Оставьте только уникальные строки из предыдущего запроса
SELECT DISTINCT
    purchase_order_id, unit_cost,
    min(unit_cost) OVER (PARTITION BY purchase_order_id) AS min_, 
    max(unit_cost) OVER (PARTITION BY purchase_order_id) AS min_,
    avg(unit_cost) OVER (PARTITION BY purchase_order_id) AS min_
FROM
    purchase_order_details;
#
WITH cte_ AS (
	SELECT 
		purchase_order_id, unit_cost,
		min(unit_cost) OVER (PARTITION BY purchase_order_id) AS min_, 
		max(unit_cost) OVER (PARTITION BY purchase_order_id) AS max_,
		avg(unit_cost) OVER (PARTITION BY purchase_order_id) AS avg_
	FROM
		purchase_order_details)
select * FROM cte_
UNION
select * FROM cte_;
#
with cte_ AS (
	SELECT 
		purchase_order_id, unit_cost,
		min(unit_cost) OVER (PARTITION BY purchase_order_id) AS min_, 
		max(unit_cost) OVER (PARTITION BY purchase_order_id) AS max_,
		avg(unit_cost) OVER (PARTITION BY purchase_order_id) AS avg_
	FROM
		purchase_order_details)
SELECT * FROM cte_
GROUP BY 1,2;
    
# 3. Посчитайте стоимость продукта в заказе как quantity*unit_cost Выведите суммарную стоимость продуктов с помощью оконной функции 
SELECT DISTINCT
	purchase_order_id,  
    round(sum(quantity * unit_cost) OVER (PARTITION BY purchase_order_id), 2) AS order_price
FROM purchase_order_details
ORDER BY purchase_order_id;
#    Сделайте то же самое с помощью GROUP BY
SELECT 
	purchase_order_id, 
	ROUND(sum(quantity * unit_cost), 2) AS order_price
FROM purchase_order_details 
GROUP BY purchase_order_id;

# 4. Посчитайте количество заказов по дате получения и posted_to_inventory Если оно превышает 1 то выведите '>1' в противном случае '=1'
#    Выведите purchase_order_id, date_received и вычисленный столбец
SELECT 
	purchase_order_id,
    coalesce(cast(date_received AS DATE),'unknow') AS date_received_,
	CASE 
		WHEN COUNT(purchase_order_id) OVER (PARTITION BY CAST(date_received AS DATE), posted_to_inventory) > 1 THEN '>1'
		ELSE '=1'
    END AS count_
FROM purchase_order_details
ORDER BY date_received;
