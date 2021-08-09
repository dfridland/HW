import json
with open('text7js.json', 'w', encoding='ascii') as f_j:
    with open("text7.txt", 'r', encoding='ascii') as f:

           profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}

           avr_profit = {"Average profit": sum(int(i) for i in profit.values())/
                                           len([int(i) for i in profit.values() if int(i) > 0])}

           result =[profit, avr_profit]
           print(result)
           json.dump(result, f_j)
