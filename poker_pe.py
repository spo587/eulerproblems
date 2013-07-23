from collections import defaultdict

def get_hands(filename):
    with open('poker.txt') as f:
        lines = f.readlines()
        return lines


def get_a_hand(lines):
    index = 0
    while index < len(lines):
        split = lines[index].split()
        hand1 = split[0:5]
        hand2 = split[5:10]
        yield hand1, hand2
        index += 1

def is_flush(suits, values):
    if len(set(suits))==1:
        return True
    else:
        return False

def is_straight(suits, values):
    values.sort()
      
    for i in range(4):
        if not values[i+1] == values[i] + 1:
            break
    else:
        print values
        return True

    if values == [2, 3, 4, 5, 14]:
        return True
    else:
        return False


def multi_dict_generator(values):
    d = defaultdict(int)

    for card in values:
        d[card] += 1
    
    occurance_dict = defaultdict(tuple)

    for card in d:
        occurance_dict[d[card]] += card,

    return occurance_dict

def basic_ranker(suits, values):

    ans = 0
    occ_d = multi_dict_generator(values)
    keys = occ_d.keys()
    
    if is_flush(suits, values):
        ans += 12
    if is_straight(suits, values):
        #print 'hand is straight'
        ans += 11

    if 4 in occ_d: #Four of a kind
        ans = 16 + occ_d[4][0]*.1

    if 3 in occ_d: #Three of a kind
        ans += 10 + occ_d[3][0]*.1
        if 2 in occ_d: #Full house
            ans += 4 

    if 2 in occ_d: #pairs
        if len(occ_d[2]) == 2: #two pair
            higher = max(occ_d[2])
            lower = min(occ_d[2])
            ans += 8 + higher*.1 + lower * .01
        else:
            ans += 4 + occ_d[2][0]*.1

    if ans == 0: #High card
        ans += max(occ_d[1])*.1

    return ans

def break_tie(vals1, vals2):
    vals1.sort()
    vals2.sort()

    for i in range(4, -1, -1):
        if vals1 > vals2:
            return 1
        elif vals1 < vals2:
            return 2


def compare_hands(hand1, hand2):
    card_dict = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,\
                 '8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}

    suits1 = [card[1] for card in hand1]
    values1 = [card_dict[card[0]] for card in hand1]
    
    suits2 = [card[1] for card in hand2]
    values2 = [card_dict[card[0]] for card in hand2]


    #print 'rank of hand1 ', basic_ranker(suits1,values1)
    #print 'rank of hand2 ', basic_ranker(suits2,values2)
    if basic_ranker(suits1, values1) > basic_ranker(suits2, values2):
        return 1
    elif basic_ranker(suits1, values1) < basic_ranker(suits2, values2):
        return 2
    else:
        return break_tie(values1, values2)


if __name__ == '__main__':
    hands = get_hands('poker.txt')
    player1 = 0
    player2 = 0

    for hand1, hand2 in get_a_hand(hands):
        #print 'hand1 ', hand1
        #print 'hand2 ', hand2
        compare = compare_hands(hand1,hand2)
        #print compare
        if compare == 1:
            player1 +=1
        elif compare == 2:
            player2 += 1
    print player1, player2




        
        
        






            
