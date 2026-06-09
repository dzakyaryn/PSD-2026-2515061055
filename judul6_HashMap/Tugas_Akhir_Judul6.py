class Node:
    def __init__(self, sku, name):
        self.sku = sku
        self.name = name
        self.next = None

class HashMap:
    def __init__(self, size=5):
        self.size = size
        self.table = [None] * size

    def hash_func(self, sku):
        return sum(ord(c) for c in str(sku)) % self.size

    def insert(self, sku, name):
        index = self.hash_func(sku)
        current = self.table[index]
        
        while current:
            if current.sku == sku:
                current.name = name
                return
            current = current.next
            
        new_node = Node(sku, name)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, sku):
        index = self.hash_func(sku)
        current = self.table[index]
        
        while current:
            if current.sku == sku:
                return current.name
            current = current.next
        return None

    def display(self):
        for i in range(self.size):
            print(f"Rak [{i}]", end="")
            curr = self.table[i]
            while curr:
                print(f" -> [{curr.sku}: {curr.name}]", end="")
                curr = curr.next
            print(" -> NULL")

if __name__ == "__main__":
    hm = HashMap(size=5)
    
    hm.insert("TV-55", "Smart TV Samsung")
    hm.insert("IP-10", "Iphone 17 pro max")
    hm.insert("SH-42", "Sepatu Nike")
    hm.insert("TS-M", "Kaos Hitam M")
    hm.insert("TS-L", "Kaos Hitam L")
    
    hm.display()
    
    print("\nCari 'TV-55':", hm.search("TV-55"))
    print("Cari 'HP-01':", hm.search("HP-01"))