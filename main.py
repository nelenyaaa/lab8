import datetime
from sqlalchemy import create_engine, Column, Integer, String, DATETIME
from sqlalchemy.orm import declarative_base, Session

# Підключення до бази даних
engine = create_engine('sqlite:///db.db', echo=False)
Base = declarative_base()


# Оголошення класів моделей

class Incomes(Base):
    __tablename__ = 'incomes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    income = Column(Integer)
    date = Column(DATETIME)


# Створення таблиць
Base.metadata.create_all(engine)


# Створення сесії
def create_session():
    return Session(engine)


# Функція для створення нового запису
def create_record(session, name, income, date):
    new_record = Incomes(name=name, income=income, date=date)
    session.add(new_record)
    session.commit()


# Функція видалення запису
def delete_record(session, id):
    record_to_delete = session.query(Incomes).filter_by(id=id).first()
    if record_to_delete:
        session.delete(record_to_delete)
        session.commit()


# Функція для отримання всіх записів
def get_all_records(session):
    records = session.query(Incomes).all()
    if records:
        for record in records:
            print(f"{record.id}\t{record.name}\t{record.income}\t{record.date}")
    else:
        print("Записів не існує.")


def search_record(session, id):
    records = session.query(Incomes).filter_by(id=id).all()
    if records:
        for record in records:
            print(f"{record.id}\t{record.name}\t{record.income}\t{record.date}")
    else:
        print("Таких записів не знайдено.")


# Функція для отримання записів з сумою більше...
def get_records_greater_than(session, income):
    records = session.query(Incomes).filter(Incomes.income > income).all()
    if records:
        for record in records:
            print(f"{record.id}\t{record.name}\t{record.income}\t{record.date}")
    else:
        print("Таких записів не знайдено.")


# Закриття сесії
def close_session(session):
    session.close()


# Приклад використання:
session = create_session()

# Створення записів
create_record(session, "Роялті з треків", 5000, datetime.datetime.now())
create_record(session, "Гроші які дала мама", 200, datetime.datetime.now())

# Отримання всіх повідомлень
print("Всі записи:")
get_all_records(session)

#Пошук записів
print("\nЗапис який ви хотіли знайти:")
search_record(session, 2,)

# Отримання записів де income більше за вказане значення
print("\nЗаписи більші за вказане значення:")
get_records_greater_than(session, 500)


print("\nВидалення повідомлення та виведення всіх повідомлень")
delete_record(session, 4)
get_all_records(session)

# Закриття сесії
close_session(session)
