from typing import List


class BankAccount:
    """"
    bank account management
    """
    all_account_number: List[int] = []
    last_account_number = 999

    def __int__(self, name: str) -> None:
        BankAccount.last_account_number += 1
        an = BankAccount.last_account_number
        self.account_number: int = an
        BankAccount.all_account_number.append(an)
        self.name = name
        self.balance: float = 0

    def display(self) -> None:
        """
        show account balance.
        :return:
        """
        print(40 * '_')
        print(f'Hi,{self.name}\nYour curent balance: {self.balance}')
        print(40 * '_')

    def deposit(self) -> None:
        """"
        Increase account
        :return:
        """
        amount = eval(input('please enter amount to deposit: '))
        self.balance += amount
        self.display()

    def withdraw(self) -> None:
        """"
        withdraw from bank account.
        :return:
        """
        amount = eval(input('Please Enter amount to withdraw: '))
        if amount > self.balance:
            print('Insufficient Balance! ')
        else:
            self.balance -= amount
        self.display()


def main():
    acc1 = BankAccount()
    print(40 * '*')
    print(f'account_number: {acc1.account_number}')
    print(40 * '*')
    acc1.display()

    while True:
        choice = int(input('Enter:\n1 to see your balance,\n2 to deposit,\n3 to withdraw,'
                           '\n4 to exit.\n\t your choice: '))
        if choice == 1:
            acc1.display()
        elif choice == 2:
            acc1.deposit()
        elif choice == 3:
            acc1.withdraw()
        elif choice == 4:
            break
        else:
            print('Please enter a valid number.')


if __name__ == '__main__':
    main()
