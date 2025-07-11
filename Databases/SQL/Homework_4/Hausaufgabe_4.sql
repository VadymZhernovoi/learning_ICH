# 1 Подключитесь к своей базе данных созданной на уроке
USE 210225_Zhernovoi;
# 2. Создайте таблицу, которая отражает погоду в Вашем городе за последние 5 дней и включает следующее столбцы
#	Id - первичный ключ, заполняется автоматически
#	Дата - не может быть пропуском
#	Дневная температура - целое число, принимает значения от -30 до 30
#	Ночная температура - целое число, принимает значения от -30 до 30
#	Скорость ветра - подумайте какой тип данных и ограничения необходимы для этого столбца
CREATE TABLE Wheather (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    LastData DATE NOT NULL CHECK(LastData < getdate()), # AND (LastData - CURRENT_DATE()) <= 5),
    DayTemperature INT CHECK (DayTemperature >= - 3 AND DayTemperature <= 30),
    NightTemperature INT CHECK (NightTemperature >= - 30 AND NightTemperature <= 30),
    WindSpeed INT CHECK (WindSpeed > 0)
);
select cast (1 as decimal);
# 3 Заполните таблицу 5 строками - за последние 5 дней 
INSERT INTO  Wheather 
	(LastData, 
    DayTemperature, 
    NightTemperature, 
    WindSpeed) 
VALUES 
	(subdate(curdate(), INTERVAL 5 DAY),
	3,
	-3,
	4),
    (subdate(curdate(), INTERVAL 4 DAY),
	5,
	-1,
	6),
    (subdate(curdate(), INTERVAL 3 DAY),
	8,
	0,
	1),
    (subdate(curdate(), INTERVAL 2 DAY),
	6,
	3,
	2),
    (subdate(curdate(), INTERVAL 1 DAY),
	9,
	3,
	3);

# 4 Увеличьте значения ночной температуры на градус если скорость ветра не превышала 3 м/с
UPDATE Wheather 
SET 
    NightTemperature = NightTemperature + 1
WHERE
    WindSpeed <= 3;
    
# 5 На основе полученной таблицы создайте представление в своей базе данных - включите все строки Вашей таблицы 
#	и дополнительно рассчитанные столбцы
#	Средняя суточная температура - среднее арифметическое между ночной и дневной температурами
#	Столбец на основе скорости ветра - если скорость ветра не превышала 2 м/с то значение ‘штиль’, 
#	от 2 включительно до 5 - ‘умеренный ветер’, в остальных случаях - ‘сильный ветер’
CREATE VIEW v_Wheather AS
    SELECT 
        *,
        (DayTemperature + NightTemperature) / 2 AS AverageTermperature,
        CASE
			WHEN WindSpeed < 2 THEN 'штиль'
            WHEN WindSpeed >= 2 AND WindSpeed < 5 THEN 'умеренный ветер'
            ELSE 'сильный ветер'
		END AS WindStark
    FROM
        Wheather;