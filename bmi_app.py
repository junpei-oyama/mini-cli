def main():
    height_cm = float(input("身長(cm)："))
    weight_kg = float(input("体重(kg)："))

    height_m = height_cm / 100
    bmi = round(weight_kg / (height_m ** 2), 2)

    print(bmi)




if __name__ == '__main__':
    main()