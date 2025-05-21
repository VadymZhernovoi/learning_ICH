# 1. Подключаюсь к базе данных northwind. Выбераю все записи из таблицы suppliers. 
USE northwind;
SELECT 
    *
FROM
    suppliers;

# 2. Из таблицы suppliers выбираю только те записи, где поле company имеет значение "Supplier A"
SELECT 
    *
FROM
    suppliers
WHERE
    company = 'Supplier A';

# 3. Выбираю все строки из таблицы purchase_orders
SELECT 
    *
FROM
    purchase_orders;
    
# 4. Из таблицы purchase_orders выбираю только те записи, где supplier_id = 2
SELECT 
    *
FROM
    purchase_orders
WHERE
    supplier_id = 2;
    
# 5. Выбираю из таблицы purchase_orders поля supplier_id и shipping_fee там, где created_by равно 1 и supplier_id равен 5.
SELECT 
    supplier_id, shipping_fee
FROM
    purchase_orders
WHERE
    created_by = 1 AND supplier_id = 5;
# Результат - нет ни одной записи, удовлетворяющей условию: created_by равно 1 и supplier_id равен 5 

/* 6. Из таблицы employees вывожу поля last_name и first_name для тех записей,
где поле address имеет значение 123 2nd Avenue или 123 8th Avenue */
# способ 1 - с применением оператора OR:
SELECT 
    last_name, first_name
FROM
    employees
WHERE
    address = '123 2nd Avenue'
        OR address = '123 8th Avenue';
# способ 2 - с применением оператора IN:
SELECT 
    last_name, first_name
FROM
    employees
WHERE 
    address IN ('123 2nd Avenue','123 8th Avenue');
    
# 7. Из таблицы suppliers вывожу все имена сотрудников, которые содержат английскую букву p в середине фамилии
# Задача поставлена не совсем однозначно!
# Если имелось ввиду, что в середине фамилии - это не в начале и в конце, то это так:
SELECT 
    first_name
FROM
    employees
WHERE
	last_name like '_%p%_';
# А если в середине фамилии - это просто в фамилии, то это так:
SELECT 
    first_name
FROM
    employees
WHERE
	last_name like '%p%';
# Но в нашей конкретной базе данных результат совпадает
# А если быть уж совсем дотошным, то надо вычислять середину каждой фамилии и искать там символ 'p' :)

# 8. Выбераю все записи из таблицы orders там, где поле shipper_id не заполнено
SELECT 
    *
FROM
    orders
WHERE
    shipper_id IS NULL;