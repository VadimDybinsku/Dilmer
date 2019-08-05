class animals(object):
    __char_1_1 = 'wild'
    char_1_2 = 'pets'
    char_1_3 = 'daily activity'
    char_1_4 = 'night activity'
    def __init__(self, say):
        self.say = say
    def voice(self):
        print(self.say)
class dog(animals):
    char_2_1 = 'say: woof woof!!!'
class cat(animals):
    char_3_1 = 'say: meow'
pappy = dog('woof woof!!!')
kitti = cat('meow')
pappy.voice()
kitti.voice()
print('Dog:', (dog.char_1_2),',', (dog.char_1_3),',', (dog.char_2_1))
print('Cat:', (cat.char_1_2),',', (cat.char_1_4),',', (cat.char_3_1))
