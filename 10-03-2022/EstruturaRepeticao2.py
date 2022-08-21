class createItem:
    def __init__(self, name, value, type):
        self.name = name
        self.value = value
        self.type = type

    def returnItem(self):
        print("")
        print("-" * 50)
        print(f"| nome: {self.name}")
        print(f"| valor: {self.value}")
        print(f"| tipo: {self.type}")
        print("-" * 50)
        print("")  


item1 = createItem("Camisa com Estampa", "U$ 15,00", "Camisa")

item1.returnItem()