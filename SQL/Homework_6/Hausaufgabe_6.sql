# 1. Выведите одним запросом с использованием UNION столбцы id, employee_id из таблицы orders
# 	 и соответствующие им столбцы из таблицы purchase_orders 
# 	 В таблице purchase_orders  created_by соответствует employee_id
SELECT 
    id, employee_id
FROM
    orders 
UNION ALL # или просто UNION - в задании ничего несказано про дубликаты
SELECT 
    id, created_by
FROM
    purchase_orders;

# 2. Из предыдущего запроса удалите записи там где employee_id не имеет значения 
#    Добавьте дополнительный столбец со сведениями из какой таблицы была взята запись
SELECT 
    id, employee_id, 'orders' as 'from table'
FROM
    orders 
WHERE employee_id IS NOT NULL
UNION 
SELECT 
    id, created_by, 'purchase_orders' as 'from table'
FROM
    purchase_orders;

# 3. Выведите все столбцы таблицы order_details а также дополнительный столбец payment_method из таблицы purchase_orders 
#	 Оставьте только заказы для которых известен payment_method
SELECT 
    od.*, p.payment_method
FROM
    order_details AS od
JOIN 
	orders AS o ON od.order_id = o.id
JOIN
    employees AS e ON o.employee_id = e.id
JOIN
    purchase_orders AS p ON e.id = p.created_by AND p.payment_method IS NOT NULL;
    
# 4. Выведите заказы orders и фамилии клиентов customers для тех заказов по которым были инвойсы таблица invoices
SELECT 
    o.*, c.last_name
FROM
    orders AS o
JOIN
    invoices AS i ON o.id = i.order_id
LEFT JOIN
    customers AS c ON o.customer_id = c.id;

# 5. Подсчитайте количество инвойсов для каждого клиента из предыдущего запроса
SELECT 
    c.last_name, count(i.order_id)
FROM
    orders AS o
JOIN
    invoices AS i ON o.id = i.order_id
LEFT JOIN
    customers AS c ON o.customer_id = c.id
GROUP BY c.last_name;