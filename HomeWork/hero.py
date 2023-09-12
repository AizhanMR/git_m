class SuperHero:
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase


    def gname(self):
        return f'name: {self.name}'
    def health(self):
        return f'multiplied health: {self.health_points * 2}'

    def __str__(self):
       return f'nickname: {self.nickname}\n' \
              f'superpower: {self.superpower}\n' \
              f'health: {self.health_points}\n'

    def __len__(self):
       return f'length of catchphrase: {len(self.catchphrase)}'

name = SuperHero('Luffy', 'Strawhat', 'rubber limbs', 9, 'GumGum')


print(name.gname())
print(name)
print(name.health())
print(name.__len__())