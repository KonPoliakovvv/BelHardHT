class Phone:
    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(self, caller_name):
        print(f"Звонит {caller_name}")

    def get_info(self):
        return (self.brand, self.model, self.issue_year)

    def __str__(self):
        return f"Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}"

# Создание объекта класса Phone
phone = Phone(brand="Apple", model="iPhone 14", issue_year=2023)

# Вызов метода receive_call
phone.receive_call("ПётрРЦ")

# Вывод информации об устройстве с помощью метода __str__
print(phone)
