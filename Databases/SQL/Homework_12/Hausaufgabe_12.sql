SELECT * FROM employees;

# 1 Вывести id департамента, в котором работает сотрудник, в зависимости от Id сотрудника

DELIMITER //
CREATE PROCEDURE p_show_depatment(IN employee_id INT)
BEGIN
	SELECT department_id AS 'ID департамента' FROM employees WHERE id = employee_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE p_get_depatment(IN employee_id INT, OUT dep_id INT)
BEGIN
	SELECT department_id INTO dep_id FROM employees WHERE id = employee_id;
END //
DELIMITER ;

CALL p_show_depatment(16);

CALL p_get_depatment(16, @depID);
SELECT @depID AS 'ID департамента';

# 2 Создайте хранимую процедуру get_employee_age, которая принимает id сотрудника (IN-параметр) и возвращает его возраст через OUT-параметр.

DELIMITER //
CREATE PROCEDURE get_employee_age(IN employee_id INT, OUT employee_ INT)
BEGIN	
	SELECT age INTO employee_ FROM employees WHERE id = employee_id;
END //
DELIMITER ;

CALL get_employee_age(22, @age);
SELECT @age AS 'Возраст';

# 3 Создайте хранимую процедуру increase_salary, которая принимает зарплату сотрудника (INOUT-параметр) и уменьшает ее на 10%.

DROP PROCEDURE increase_salary;
DELIMITER //
CREATE PROCEDURE increase_salary(INOUT salary DOUBLE) 	# всё перепробовал, NUMERIC(10.2) и DECIMAL(10.2) не подходят! Отбрасывают дробную часть!!!
														# c FLOAT проблема с округлением
														# Нормально работает DOUBLE, но результат, естественно, надо округлять до 2-х после запятой!
BEGIN
    SET salary = ROUND(salary * 0.1, 2); 				# округляем результат
END //
DELIMITER ;

SET @salary = 1023.45;
CALL increase_salary(@salary);
SELECT @salary AS 'New salary';


