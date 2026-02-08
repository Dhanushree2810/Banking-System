from db_config import cursor, conn
from banking_logic import SavingsAccount


def create_account(name, acc_no, balance):

    acc = SavingsAccount(name, acc_no, balance)

    cursor.execute(
        "INSERT INTO accounts (id,name,balance) VALUES (%s,%s,%s)",
        (acc.account_no, acc.name, acc.balance)
    )

    conn.commit()


def deposit(acc_no, amount):

    cursor.execute(
        "SELECT name,balance FROM accounts WHERE id=%s",
        (acc_no,)
    )

    data = cursor.fetchone()

    if data:
        acc = SavingsAccount(data[0], acc_no, data[1])
        new_balance = acc.deposit(amount)

        cursor.execute(
            "UPDATE accounts SET balance=%s WHERE id=%s",
            (new_balance, acc_no)
        )

        conn.commit()
        return new_balance


def withdraw(acc_no, amount):

    cursor.execute(
        "SELECT name,balance FROM accounts WHERE id=%s",
        (acc_no,)
    )

    data = cursor.fetchone()

    if data:
        acc = SavingsAccount(data[0], acc_no, data[1])
        result = acc.withdraw(amount)

        if isinstance(result, int):
            cursor.execute(
                "UPDATE accounts SET balance=%s WHERE id=%s",
                (result, acc_no)
            )
            conn.commit()

        return result
