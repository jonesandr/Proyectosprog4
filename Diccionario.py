import sqlite3

dictionary_db = "dictionary.db"


def get_connection():
    return sqlite3.connect(dictionary_db)


def create_tables():
    tables = [
        """
        CREATE TABLE IF NOT EXISTS dictionary(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL,
            meaning TEXT NOT NULL
        );
        """
    ]
    connection = get_connection()
    cursor = connection.cursor()
    for table in tables:
        cursor.execute(table)


def main():
    create_tables()
    menu = """
a) Add a new word
b) Edit existing word
c) Delete existing word
d) View word list
e) Search for word meaning
f) Quit
Choose: """
    choice = ""
    while choice != "f":
        choice = input(menu)
        if choice == "a":
            word = input("Enter the word: ")
            possible_meaning = search_word_meaning(word)
            if possible_meaning:
                print(f"The word '{word}' already exists")
            else:
                meaning = input("Enter the meaning: ")
                add_word(word, meaning)
                print("Word added")
        if choice == "b":
            word = input("Enter the word to edit: ")
            new_meaning = input("Enter the new meaning: ")
            edit_word(word, new_meaning)
            print("Word updated")
        if choice == "c":
            word = input("Enter the word to delete: ")
            delete_word(word)
        if choice == "d":
            words = get_words()
            print("=== Word list ===")
            for word in words:
                print(word[0])
        if choice == "e":
            word = input("Enter the word to search meaning for: ")
            meaning = search_word_meaning(word)
            if meaning:
                print(f"The meaning of '{word}' is:\n{meaning[0]}")
            else:
                print(f"Word '{word}' not found")


def add_word(word, meaning):
    connection = get_connection()
    cursor = connection.cursor()
    statement = "INSERT INTO dictionary(word, meaning) VALUES (?, ?)"
    cursor.execute(statement, [word, meaning])
    connection.commit()


def edit_word(word, new_meaning):
    connection = get_connection()
    cursor = connection.cursor()
    statement = "UPDATE dictionary SET meaning = ? WHERE word = ?"
    cursor.execute(statement, [new_meaning, word])
    connection.commit()


def delete_word(word):
    connection = get_connection()
    cursor = connection.cursor()
    statement = "DELETE FROM dictionary WHERE word = ?"
    cursor.execute(statement, [word])
    connection.commit()


def get_words():
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT word FROM dictionary"
    cursor.execute(query)
    return cursor.fetchall()


def search_word_meaning(word):
    connection = get_connection()
    cursor = connection.cursor()
    query = "SELECT meaning FROM dictionary WHERE word = ?"
    cursor.execute(query, [word])
    return cursor.fetchone()


if __name__ == '__main__':
    main()