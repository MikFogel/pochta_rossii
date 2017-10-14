import time

actions = {
    1: "Получить посылку",
    2: "Отправить посылку",
    3: "Не заходить на почту"
}

class client:
    def __init__(self, action=0):
        self.action = actions[action]

    def set_action(new_action):
        self.action = new_action


class baba:
    def __init__(self):
        self.response = "Вас много, а я одна, мужчина встаньте в очередь, ходють тут..."

    def talk(self):
        print (self.response)
        for i in range(1, 10):
            print ("прошло %d минут" %i)
            time.sleep(1)
        print (self.response)


    def __add__(self, other):
        print ("Вы выбрали: " + other.action)
        self.talk()
        self.act("Получить посылку")
        self.talk()
        print ("все мужчина, у меня обед, не стойте тут. вас много, а я одна")

    def act(self, str):
        if str == "Получить посылку":
            self.response = "Нет вашей посылки, потерялась, заполняйте бланк"
        if str ==  "Отправить посылку":
            self.response = "В такой упаковке от отправляем, вот Вам наша коробочка, переписывайте адрес"


while True:
    print ("_" * 100)
    for k,v in actions.items():
        print ("%s - [%s]" %(v, k) )

    print ("_" * 100)
    client_choose = input("Добро пожаловать!!! Вы подошли к филиалу ада на земле - ПОЧТА РОССИИ, Ваш выбор: ")

    if client_choose == '3':
        print ("_" * 100)
        print ("ПОБЕДА!!! И правильно сделали, пользуйтесь нормальными службами доставки и экономьте время :) ")
        break
    else:
        new_client = client(int(client_choose))
        new_baba = baba()
        new_baba + new_client
        print ("Вы проиграли")
        print ("_" * 100)
        break
