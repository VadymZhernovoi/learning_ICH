import logging
from contextlib import contextmanager
from typing import Any

import pymysql

# Включим журнал (логирование)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MySQLConnector:
    """Менеджер для работы с базой данных MySQL"""

    # def __init__(self, host='localhost', port=3306, user='root', password='', database='it_school'):
    def __init__(self, host="ich-db.edu.itcareerhub.de", port=3306, user="ich1", password="password",
                 database="sakila"):
        self.config = {
            'host': host,
            'port': port,
            'user': user,
            'password': password,
            'database': database,
            'charset': 'utf8mb4',
            'autocommit': False
        }
        self._test_connection()

    def _set_connection(self):
        """Checking the connection to the DB"""
        try:
            with self.get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT 1")
                    result = cursor.fetchone()
                    if result[0] == 1:
                        logger.info(f"Подключение к БД {self.database} прошло успешно.")
        except Exception as e:
            logger.error(f"Ошибка подключения к БД: {e}")
            raise

    @contextmanager
    def get_connection(self):
        """Сontext manager for working with connection"""
        connection = None
        try:
            connection = pymysql.connect(**self.config)
            yield connection
        except Exception as e:
            if connection:
                connection.rollback()
            logger.error(f"Ошибка БД: {e}")
            raise
        finally:
            if connection:
                connection.close()

    def query_execute(self, query: str, params: tuple = None, fetch: str = None) -> Any:
        """
        SQL query execution

        :param query: SQL query
        :param params: Parameters for the request
        :param fetch: fetch: 'one', 'all', None
        :return: Query result / number of rows
        """
        with self.get_connection() as connection:
            try:
                with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                    cursor.execute(query, params)

                    if fetch == 'one':
                        result = cursor.fetchone()
                    elif fetch == 'all':
                        result = cursor.fetchall()
                    else:
                        result = cursor.rowcount

                    connection.commit()
                    return result

            except Exception as e:
                connection.rollback()
                logger.error(f"Ошибка выполнения SQL запроса: {e}")
                logger.error(f"SQL запрос: {query}")
                logger.error(f"Параметры запроса: {params}")
                raise


mysql_connector = MySQLConnector()
