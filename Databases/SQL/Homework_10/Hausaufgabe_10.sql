# Таблица order_details

# 1 Для каждого product_id выведите inventory_id а также предыдущий и последующей inventory_id по убыванию quantity
SELECT 
	product_id,
    inventory_id,
    LAG(inventory_id) OVER (PARTITION BY product_id ORDER BY quantity DESC) AS prev_inventory,
    LEAD(inventory_id) OVER (PARTITION BY product_id ORDER BY quantity DESC) AS next_inventory,
	quantity
FROM order_details;

# 2 Выведите максимальный и минимальный unit_price для каждого order_id с помощью функции FIRST VALUE  
#   Вывести order_id и полученные значения
SELECT 
	order_id,
    FIRST_VALUE(unit_price) OVER (PARTITION BY order_id ORDER BY unit_price) AS min_price,
    FIRST_VALUE(unit_price) OVER (PARTITION BY order_id ORDER BY unit_price DESC) AS max_price,
	unit_price
FROM order_details;

# 3 Выведите order_id и столбец с разнице между  unit_price для каждой заказа и минимальным unit_price в рамках одного заказа 
#   Задачу решить двумя способами - с помощью First VAlue и MIN

# with First_VAlue
SELECT
	order_id,
    unit_price,
    FIRST_VALUE(unit_price) OVER (PARTITION BY order_id ORDER BY unit_price) AS min_price,
    unit_price - FIRST_VALUE(unit_price) OVER (PARTITION BY order_id ORDER BY unit_price) AS diff_price
FROM order_details;
# или
WITH cte_F_V AS
	(SELECT
		order_id,
		unit_price,
		FIRST_VALUE(unit_price) OVER (PARTITION BY order_id ORDER BY unit_price) AS min_price
	FROM order_details)
SELECT
	*,
    unit_price - min_price AS diff_price
FROM cte_F_V;

# with MIN
WITH cte_MIN AS
	(SELECT
		order_id,
        unit_price,
		MIN(unit_price) OVER (PARTITION BY order_id) AS min_price
	FROM order_details)
SELECT
	*,
    unit_price - min_price AS diff_price
FROM cte_MIN
ORDER BY order_id, unit_price;
# или
SELECT
	order_id,
    unit_price,
    MIN(unit_price) OVER (PARTITION BY order_id) AS min_price,
    unit_price - MIN(unit_price) OVER (PARTITION BY order_id) AS diff_price
FROM order_details
ORDER BY order_id, unit_price;

# 4 Присвойте ранг каждой строке используя RANK по убыванию quantity
SELECT 
	*,
    RANK() OVER (ORDER BY quantity DESC) AS rank_quantity
FROM order_details;

# в чём подвох? Как-то подозрительно просто...

# 5  Из предыдущего запроса выберите только строки с рангом до 10 включительно
SELECT *
FROM (SELECT *, RANK() OVER (ORDER BY quantity DESC) AS rank_quantity FROM order_details) AS sel_rank
WHERE sel_rank.rank_quantity <= 10;
# или
WITH cte_rank AS 
	(SELECT 
		*, 
		RANK() OVER (ORDER BY quantity DESC) AS rank_quantity 
    FROM order_details) 
SELECT *
FROM cte_rank
WHERE cte_rank.rank_quantity <= 10;

