# 1. Выведите Ваш возраст на текущий день в секундах

SELECT DATEDIFF(CURDATE(), CAST(19660429 AS DATE)) * 86400 AS " Мой возраст на текущий день в секундах";
# точнее не могу, т.к. не знаю время своего рождения

# 2. Выведите какая дата будет через 51 день

SELECT DATE_FORMAT(DATE_ADD(CURDATE(), INTERVAL 51 DAY), '%d.%m.%Y') AS "CURDATE + 51 day";

# 3. Отформатируйте предыдущей запрос - выведите день недели для этой даты Используйте документацию My SQL

SELECT CONCAT(DATE_ADD(CURDATE(), INTERVAL 51 DAY), 
			  ' - это ', DATE_FORMAT(DATE_ADD(CURDATE(), INTERVAL 51 DAY), '%w'), 
			  '-й день недели') AS "Новая дата";

# 4.  Подключитесь к базе данных northwind Выведите столбец с исходной датой создания транзакции transaction_created_date из таблицы inventory_transactions, 
# а также столбец полученный прибавлением 3 часов к этой дате

USE northwind;
SELECT 
    transaction_created_date,
    DATE_ADD(transaction_created_date, INTERVAL 3 HOUR) AS "transaction_created_date + 3 hour"
FROM
    inventory_transactions;
    
# 5. Выведите столбец с текстом  'Клиент с id <customer_id> сделал заказ <order_date>' из таблицы orders
#    Запрос написать двумя способами - с использованием неявных преобразований а также с указанием изменения типа данных для столбца customer_id
#    Внимание В MySQL функция CAST не принимает VARCHAR в качестве параметра для длины. Вместо этого, нужно использовать CHAR для указания длины.

#  1-й способ
SELECT CONCAT('Клиент с id ', customer_id, ' сделал заказ ', order_date) AS Commentar
FROM orders;

#  2-й способ
SELECT CONCAT('Клиент с id ', cast(customer_id as char), ' сделал заказ ', order_date) AS "Комментарий"
FROM orders;

