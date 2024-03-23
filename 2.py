class PurchaseCounter:
    def __init__(self):
        self.purchases = {}  # Словарь для хранения покупок и их количества
    def add_purchase(self, item):
        """Метод для добавления покупки"""
        self.purchases[item] = self.purchases.get(item, 0) + 1
    def remove_purchase(self, item):
        """Метод для удаления покупки"""
        if item in self.purchases:
            if self.purchases[item] == 1:
                del self.purchases[item]
            else:
                self.purchases[item] -= 1
        else:
            print("Такой покупки нет в списке")
    def display_purchases(self):
        """Метод для вывода покупок и их количества"""
        print("Список покупок:")
        for item, count in self.purchases.items():
            print(f"{item}: {count}")
# Использования класса счетчика покупок
counter = PurchaseCounter()

# Добавление покупок
counter.add_purchase("Яблоко")
counter.add_purchase("Груша")
# Вывод покупок и их количества
counter.display_purchases()

# Удаление покупок
counter.remove_purchase("Яблоко")
counter.remove_purchase("Груша")

# Вывод обновленного списка покупок и их количества
counter.display_purchases()
