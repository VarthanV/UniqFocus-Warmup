class Node(object):
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        self.parent = None
        self.wallet = 0
        self.power = 0
        self.count = 0
        self.transaction_count = 0

    def __str__(self):
        return self.name

    def add_left(self, node):
        if self.left == None:
            self.left = node
        while self.left.left != None:
            self.left = self.left.left
        self.left = node
        self.increase_power()
        self.watch_match()

    def add_right(self, node):
        if self.right == None:
            self.right = node
        else:
            while self.right.right != None:
                self.right = self.right.right
            self.right = node
            self.increase_power()
            self.watch_match()

    def watch_transaction_count(self):
        if self.transaction_count >= 10:
            raise Exception("More than 10 transactions not allowed")

    def insert_as_my_referral(self, node):
        while(self.left.left != None):
            self.left = self.left.left
        self.left = node
        print(f"My leaf node is {self.left.name}")

    def calculate_leaf(self):
        while(self.left.left != None):
            self.left = self.left.left
        print(f"My leaf node is {self.left.name}")

    def watch_match(self):
        self.watch_transaction_count()
        if(self.left and self.right):
            self.wallet += 3
            self.transaction_count = 1
            self.count -= 2
            print(
                f'{self.name.upper()} \n WALLET :{self.wallet} \nPOWER:{self.power} \nCOUNT :{self.count}')
        else:
            print(
                f"{self.name.upper()}\n WALLET: {self.wallet} \nPOWER:{self.power}\nCOUNT:{self.count}")

    def increase_power(self):
        self.power += 1
        self.count += 1


def find_ancestors(val, root):
    if root == None:
        return True
    elif root.name == val:
        return True
    elif find_ancestors(val, root.left):
        print(root.name)
    elif find_ancestors(val, root.right):
        print(root.name)


# Initializing Nodes
vichu = Node("Vichu")
mowli = Node("Mowli")
mowli.parent = vichu
arun = Node("Arun")
hari = Node("Hari")
priya = Node('priya')
diya = Node('Diya')
yamini = Node('yamini')
shalini = Node("Shalini")
haritha = Node('haritha')
mohana = Node("mohana")
nisha = Node('nisha')
yazhini = Node('yazhini')
srinithi = Node('srinithi')
kaviya = Node('kaviya')
boomika = Node('boomika')
poornima = Node('poornima')
# Adding Nodes
# vichu.add_left(mowli)
# vichu.add_right(arun)
# mowli.add_left(hari)
# mowli.add_right(priya)
# priya.add_left(yamini)
# priya.add_right(shalini)
# shalini.add_right(yazhini)

# Inserting as my referral
# vichu.add_left(mowli)
# vichu.add_left(arun)
# vichu.add_left(hari)
# vichu.add_left(yamini)
# vichu.add_left(shalini)
# vichu.calculate_leaf()
# vichu.insert_as_my_referral(priya)
# vichu.add_right(boomika)
# boomika.add_left(nisha)
# boomika.add_right(mohana)

# print(vichu.parent)
# print(boomika.parent)

vichu.add_left(mowli)
mowli.add_left(boomika)

# print(mowli.parent)
# print(vichu.left)
# find_ancestors('boomika',vichu)

print(mowli.parent)
