# База данных northwind
# Работаем с таблицей purchase_order_details
USE northwind;

# 1 Посчитайте основные статистики - среднее, сумму, минимум, максимум столбца unit_cost.
SELECT 
    AVG(unit_cost) AS avg_unit_cost,
    SUM(unit_cost) AS sum_unit_cost,
    MIN(unit_cost) AS min_unit_cost,
    MAX(unit_cost) AS max_unit_cost
FROM
    purchase_order_details;

# 2 Посчитайте количество уникальных заказов purchase_order_id
SELECT 
    COUNT(DISTINCT purchase_order_id) as count_dist_purchase_order_id
FROM
    purchase_order_details;

# 3 Посчитайте количество продуктов product_id в каждом заказе purchase_order_id 
#   Отсортируйте полученные данные по убыванию количества
SELECT 
    purchase_order_id, 
    COUNT(product_id) AS count_product_id
FROM
    purchase_order_details
GROUP BY 1
ORDER BY COUNT(product_id) DESC;

# 4 Посчитайте заказы по дате доставки date_received Считаем только те продукты, количество quantity которых больше 30
SELECT 
	coalesce(date_received, 'date unknow') AS date_received_,
    COUNT(purchase_order_id) AS count_purchase_order_id
FROM
    purchase_order_details
WHERE
    quantity > 30
GROUP BY 1
ORDER BY 1; # сортировку добавил от себя

SELECT 
date_received,
#    date_format(date_received, '%d-%m-%Y') AS date_received_,
    COUNT(purchase_order_id) AS count_purchase_order_id
FROM
    purchase_order_details;
SELECT 
date_received,
coalesce(date_format(date_received, 'date unknow'), '%d-%m-%Y') AS date_received_
FROM
    purchase_order_details;