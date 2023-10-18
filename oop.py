class Airaport:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.list = []
        self.list_plain = []
    def __str__(self):
        return f'Airaport nomi "{self.name}", Ochilgan sanasi "{self.age} - yil"'
class Bilet:
    def __init__(self, uchish, davlat, narxi):
        self.uchish = uchish
        self.davlat = davlat
        self.narxi = narxi
    def __str__(self):
        return f'Uchish voqti {self.uchish}:00, Uchadigan davlati {self.davlat} , Chipta narxi {self.narxi}$'
class User:
    def __init__(self, name, lastname, age, money):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.money = money
    def get_money(self):
        return self.money
class Samolyot:
    def __init__(self, Nomi, turi):
        self.name = Nomi
        self.turi = turi
    def __str__(self):
        return f'Samoliot nomi "{self.name}", Samoliot turi "{self.turi}"'
u1 = Airaport(input('Airaport nomini kiriting: '), int(input('Airaport ochilgan yilni kiriting: ')))
for i in range(int(input('Nechta bilet kiritasiz: '))):
    a = Bilet(int(input('Samolyot uchish vaqtini kiriting: ')), input('Davlatini kiriting: '), int(input('Chiptani narxini kiriting: ')))
    i = Samolyot(input('Samoliyot nomini kiriting: '), input('Samoliot turini kiriting: '))
    u1.list_plain.append(i)
    u1.list.append(a)
print(u1)
u2 = User(input('Ismingizni kiriting: '), input('Familyangizni kiriting: '), int(input('Yoshingizni kiriting: ')), int(input('Pulingizni kiriting: ')))
print('Chiptalar royxati!')
lst = []
for n, i in enumerate(u1.list):
    print(n + 1, '>>>', str(i))
    lst.append(str(i))
choise = input('Qaysi davlatni tanlaysiz: ')
for n, i in enumerate(lst):
    if choise in str(i).split(' ')[5]:
        u2.money -= a.narxi
        print(f'Marhamat samolyotga chiqishingiz mumkin\nsizning samolyotingiz {u1.list_plain[n]}')
        break
print(f'sizda {u2.get_money()} mana shuncha pul qoldi')