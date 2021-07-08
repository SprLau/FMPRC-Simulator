from vocab import *
import random
print("\n----------------------------------------------")
country = input("国家：")
event = input("事件：")
print("------------------------------------ *纯属娱乐\n")


def print_with_comma(sentence):
    print(sentence, end="，")

def print_with_period(sentence):
    print(sentence, end="。")

def print_with_no_jump(sentence):
    print(sentence, end="")

def print_with_punctuation(sentence):
    print(sentence, end="、")

print_with_comma(random.choice(heading))

select_denouncement = random.randint(0, 1)
print_with_comma(
    denouncement[0] + country + event if select_denouncement == 0 
    else denouncement[1] + event + denouncement[2] + country + denouncement[3])

print_with_no_jump(threats[0] + country)
print_with_punctuation(threats[random.randint(1, 3)])
print_with_period(threats[random.randint(4, 8)])

print_with_comma(country + event + blame[random.randint(0, 1)] + '，' + blame[2])

print_with_period(threat_again[0] + country + threat_again[1])

print_with_no_jump(country + threat_over_and_over_again[random.randint(0, 1)])

print_with_period(urge[0] + country + urge[1] + event + urge[2])

print_with_comma(will_do[0] + country + event + will_do[1])
print_with_period(will_do[random.randint(2, 3)])

print_with_comma(threats_threats_threats[0] + country + threats_threats_threats[1])
print_with_period(threats_threats_threats[random.randint(2, 4)])

selected = random.choice(cliche)
print_with_comma(selected)
another = random.choice(cliche)
while another == selected:
    another = random.choice(cliche)
print_with_period(another)

selected = random.randint(1, 3)
another = random.randint(1, 3)
while another == selected:
    another = random.randint(1, 3)

print_with_comma(greatness[0] + greatness[selected] + greatness[another])

print_with_period(country + random.choice(blame_again))

selected = random.choice(blame_over_and_over_again)
another = random.choice(blame_over_and_over_again)
while another == selected:
    another = random.choice(blame_over_and_over_again)

print_with_comma(country + selected + '、' + another)

print_with_period(ending[0] + country + ending[1] + country +ending[2])

print('\n')