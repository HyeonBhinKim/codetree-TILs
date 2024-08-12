class Product:
    def __init__(self, name='codetree', code='50'):
        self.name = name
        self.code = code

name, code = tuple(input().split())
merchant = Product()
print(f"product {merchant.code} is {merchant.name}")
merchant = Product(name, code)
print(f"product {merchant.code} is {merchant.name}")