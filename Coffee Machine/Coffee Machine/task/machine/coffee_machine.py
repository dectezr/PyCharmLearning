# Write your code here
class CoffeeMachine:
    status = [400, 540, 120, 9, 550]
    name = ['water', 'milk', 'coffee beans', 'disposable cups', 'money']
    espresso = [-250, 0, -16, -1, 4]
    latte = [-350, -75, -20, -1, 7]
    cappuccino = [-200, -100, -12, -1, 6]
    flag = True

    def state_check(self):
        print('The coffee machine has:')
        for i in range(len(self.status) - 1):
            print(f'{self.status[i]} of {self.name[i]}')
        print(f'${self.status[4]} of {self.name[4]}')
        return None

    def sell_coffee(self):
        coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        if coffee == 'back':
            return None
        else:
            coffee = int(coffee)
            if coffee == 1:
                coffee = self.espresso
            elif coffee == 2:
                coffee = self.latte
            elif coffee == 3:
                coffee = self.cappuccino
        for i in range(len(self.status) - 1):
            if self.status[i] + coffee[i] < 0:
                print(f'Sorry,not enough {self.name[i]}!')
                return None
        for i in range(len(self.status)):
            self.status[i] += coffee[i]
        print('I have enough resources, making you a coffee!')
        return True

    def add_ingredients(self):
        for i in range(len(self.status) - 1):
            if i in [0, 1]:
                response = 'ml of ' + self.name[i]
            elif i == 2:
                response = 'grams of ' + self.name[i]
            else:
                response = self.name[i] + ' of coffee'
            self.status[i] += int(input(f'Write how many {response} do you want to add:'))
        return True

    def output_money(self):
        print('I gave you $' + str(self.status[-1]))
        self.status[-1] = 0
        return True

    def action(self, action_take):
        if action_take == 'buy':
            self.sell_coffee()
        elif action_take == 'fill':
            self.add_ingredients()
        elif action_take == 'take':
            self.output_money()
        elif action_take == 'remaining':
            self.state_check()
        elif action_take == 'exit':
            self.flag = False
        return True


coffee_machine = CoffeeMachine()
while coffee_machine.flag:
    coffee_machine.action(input('Write action (buy, fill, take, remaining, exit):'))

# print("""Starting to make a coffee
# Grinding coffee beans
# Boiling water
# Mixing boiled water with crushed coffee beans
# Pouring coffee into the cup
# Pouring some milk into the cup
# Coffee is ready!""")

# print('For', coffee, 'cups of coffee you will need:')
# print(coffee * 200, 'ml of water')
# print(coffee * 50, 'ml of milk')
# print(coffee * 15, 'g of coffee beans')

# possible = min([water // 200, milk // 50, beans // 15])
# if coffee == possible:
#     print('Yes, I can make that amount of coffee')
# elif coffee < possible:
#     print('Yes, I can make that amount of coffee (and even', possible - coffee, 'more than that)')
# else:
#     print('No, I can make only', possible, 'cups of coffee')
