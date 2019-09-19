def main():

    payment = int(input("合計金額："))
    number_of_people = int(input("人数："))

    payment_1 = payment // number_of_people
    remainder = payment % number_of_people

    print(f"{payment}円 {number_of_people}人 １人あたり{payment_1}円です。端数は{remainder}円です。")


if __name__ == '__main__':
    main()