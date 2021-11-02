# put your python code here
days = int(input())
food_cost = int(input())
flight = int(input())
hotel = int(input())
print(days*food_cost + flight*2 + hotel *(days-1))