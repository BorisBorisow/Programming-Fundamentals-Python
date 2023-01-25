class Inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []
        self.left_capacity = capacity

    def __repr__(self):
        return f'Items: {", ".join(self.items)}.\nCapacity left: {self.left_capacity}'

    def add_item(self, item: str):
        if len(self.items) < self.__capacity:
            self.items.append(item)
            self.left_capacity = self.__capacity - len(self.items)
        else:
            return 'not enough room in the inventory'

    def get_capacity(self):
        return self.__capacity


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)

# class Inventory:
#     def __init__(self, __capacity: int):
#         self.__capacity = __capacity
#         self.items = []
#
#     def add_item(self, item: str):
#         if self.__capacity > len(self.items):
#             self.items.append(item)
#         else:
#             return f"Not enough room in the inventory"
#
#     def get_capacity(self):
#         return self.__capacity
#
#     def __repr__(self):
#         current_capacity = len(self.items) - self.__capacity
#         return f"Items: {', '.join(self.items)}.\nCapacity left: {current_capacity}"
#
#
# inventory = Inventory(2)
# inventory.add_item("potion")
# inventory.add_item("sword")
# print(inventory.add_item("bottle"))
# print(inventory.get_capacity())
# print(inventory)
