# Работаем с базой данных sakila.

# 1. Вывести названия фильмов с расшифровкой рейтинга для каждого. Рейтинги описаны здесь. 
#	 В таблице film хранятся годы рейтингов. Нужно воспользоваться оператором case чтобы определить для каждого кода условие, 
#    по которому будет выводится его развернутое описание (1 предложение). 
SELECT
    title AS Film,
    CASE rating
        WHEN 'G'     THEN 'G — General Audiences'
        WHEN 'PG'    THEN 'PG — Parental Guidance Suggested'
        WHEN 'PG-13' THEN 'PG‑13 — Parents Strongly Cautioned'
        WHEN 'R'     THEN 'R — Restricted'
        WHEN 'NC-17' THEN 'NC‑17 — Adults Only'
        ELSE              'Ошибочный рейтинг'
    END AS rating_description
FROM film
ORDER BY title;

# 2. Выведите количество фильмов в каждой категории рейтинга. Используем group by. 

SELECT
    CASE rating
        WHEN 'G'     THEN 'G — General Audiences'
        WHEN 'PG'    THEN 'PG — Parental Guidance Suggested'
        WHEN 'PG-13' THEN 'PG‑13 — Parents Strongly Cautioned'
        WHEN 'R'     THEN 'R — Restricted'
        WHEN 'NC-17' THEN 'NC‑17 — Adults Only'
        ELSE              'Ошибочный рейтинг'
    END AS rating_description,
    COUNT(*) AS "Count of films"
FROM film AS f
GROUP BY f.rating 
ORDER BY rating_description;

# 3. Используя оконные функции и partition by, выведите:
#    - список названий фильмов, 
# 	 - рейтинг и количество фильмов в каждом рейтинге. 
# 	 Объясните, чем отличаются результаты предыдущего запроса и запроса в этой задаче. 
SELECT
    f.title AS Film,
	CASE rating
        WHEN 'G'     THEN 'G — General Audiences'
        WHEN 'PG'    THEN 'PG — Parental Guidance Suggested'
        WHEN 'PG-13' THEN 'PG‑13 — Parents Strongly Cautioned'
        WHEN 'R'     THEN 'R — Restricted'
        WHEN 'NC-17' THEN 'NC‑17 — Adults Only'
        ELSE              'Ошибочный рейтинг'
    END AS rating_description,
    COUNT(*) OVER (PARTITION BY f.rating) AS "Count of films"
FROM film AS f 
ORDER BY rating_description, Film;

# В предыдущем задании группируем строкам по реутингу, 
# а в этом выводим все строки и добавляем колонку, в которой показываем кол/во фильмов и т.д. и т.п. ...

# 4. Изучите таблицы payment и customer. 
#    Выведите список всех платежей с указанием имени и фамилии каждого заказчика, датой платежа и суммой.

SELECT 
	c.first_name AS "Имя",
	c.last_name AS "Фамилия",
	p.payment_date AS "Дата платежа",
	p.amount AS "Платёж"
FROM payment AS p 
JOIN customer AS c
ON p.customer_id = c.customer_id 
ORDER BY c.last_name, c.first_name, p.payment_date

# 5. Поменяйте предыдущий запрос так, чтобы дата выводилась в формате “число, название месяца, год” (без времени).

SELECT 
	c.first_name AS "Имя",
	c.last_name AS "Фамилия",
	DATE_FORMAT(p.payment_date, '%d %M %Y') AS "Дата платежа",
	p.amount AS "Платёж"
FROM payment AS p 
JOIN customer AS c
ON p.customer_id = c.customer_id 
ORDER BY c.last_name, c.first_name, p.payment_date
