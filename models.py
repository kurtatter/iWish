import sqlite3


class Wish:
    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor()

    def __repr__(self):
        return f'Wish<{self.title}'

    def __str__(self):
        return f'Wish<{self.title}'

    def get_all(self):
        sql_code = '''SELECT * FROM wish'''
        try:
            print(self.cursor.execute(sql_code))
            wishes = self.cursor.fetchall()
            print('wishes: ', wishes)
            if wishes: return wishes
        except sqlite3.Error as e:
            print('Ошибка чтения из БД', e)
        return []

    def add_wish(self, title, price, url, description):
        self.title = title
        try:
            self.cursor.execute('INSERT INTO wish VALUES(NULL, ?, ?, ?, ?)',
                                (title, price, url, description))
            self.db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавление в БД', e)
            return False
        return True

    def edit_wish(self, wish_id, title, price, url, description):
        try:
            self.cursor.execute('UPDATE wish SET title=?, price=?, url=?, description=? WHERE id=?',
                                (title, price, url, description, str(wish_id)))
            self.db.commit()
        except sqlite3.Error as e:
            print('Ошибка обновления записи в БД', e)
            return False
        return True

    def delete_wish(self, wish_id):
        try:
            self.cursor.execute('DELETE FROM wish WHERE id=' + str(wish_id))
            self.db.commit()
        except sqlite3.Error as e:
            print('Ошибка удаления записи', e)
            return False
        return True

    def get_wish(self, wish_id):
        try:
            self.cursor.execute(f"SELECT * FROM wish WHERE id = {wish_id} LIMIT 1")
            res = self.cursor.fetchone()
            if res:
                print(*res)
                return res
        except sqlite3.Error as e:
            print("Ошибка получения статьи из БД " + str(e))

        return (False, False)
