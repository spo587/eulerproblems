
f = open('poker.txt')

lines = f.readlines()







def split_lines(lines):
    for i in range(len(lines)):
        split = lines[i].split()
        hand1 = split[0:4]
        hand2 = split[5:9]
        lines[i] = hand1 + hand2
    return lines



new_lines = split_lines(lines)

card_dict = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}

def calculate_rank(hand):
    suits = [card_dict[card[1]] for card in hand]
    values = [card_dict[card[0]] for card in hand]
    if len(set(suits))==1:
        sorted_values = values.sort()
        if sorted_values[4] == sorted_values[0]+4:
            return 'straight flush mothafuckahs'
        elif sorted_values[4] == 13 and sorted_values[0:4] == [2,3,4,5]:
            return 'straight flush'
        else:
            return 'just a flush'


            
