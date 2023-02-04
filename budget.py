class Category:
    
    def __init__(self, category):
        self.category = category
        self.ledger = []

    
    def deposit(self, *args):

        amount = args[0]
        description = ''

        if len(args) > 1:
            description = args[1]
        
        if(description == ""):
            self.ledger.append({"amount": float(amount), "description": ""})
        else:
            self.ledger.append({"amount": float(amount), "description": description})
        return

    def withdraw(self, *args):

        if(self.check_funds(args[0])):
            amount = args[0]
            description = ''

            if len(args) > 1:
                description = args[1]
                
            if(description == ""):
                self.ledger.append({"amount": float(amount) * -1, "description": ""})
            else:
                self.ledger.append({"amount": float(amount) * -1, "description": description})
            
            return True
        else:
            return False

    def get_balance(self):

        current_bal = 0

        for x in self.ledger:
            current_bal += x['amount']

        return current_bal

    def transfer(self, amount, new_category):
        if(self.check_funds(amount)):

            
            transfer_to = "Transfer to {}".format(new_category.category)
            self.withdraw(amount, transfer_to)
            
            old_category = "Transfer from {}".format(self.category)
            #self.category = new_category
            new_category.deposit(amount, old_category)
            return True
        else:
            return False
            
        return 

    def check_funds(self, amount):

        ledger_bal = 0

        for x in self.ledger:
            ledger_bal += x['amount']

        if ledger_bal >= float(amount):
            return True
        else:
            return False

    def get_withdrawls(self):
        total = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total+= item["amount"]
        return total

    def __str__(self):
        category = str(self.category)
        full_ledger = category.center(30,'*')
        full_amount = 0

        for x in self.ledger:
            full_amount += x['amount']
            item_amount = "{:.2f}".format(x['amount'])
            next_line = "\n" + x['description'][:23] + item_amount.rjust(30 - len(x['description'][:23]))
            full_ledger += next_line

        full_ledger += "\n" + "Total: " + str(full_amount)
        return full_ledger

def truncate(n):
    multiplier = 10
    return int(n * multiplier) / multiplier

def getTotals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawls()
        breakdown.append(category.get_withdrawls())
    
    #Breakdown of spending rounded down to nearest 10th
    rounded = list(map(lambda x: truncate(x/total), breakdown))
    return rounded

    

def create_spend_chart(categories):

    res = "Percentage spent by category\n"
    i = 100
    totals = getTotals(categories)

    # print totals and bars
    while i >= 0:
        cat_spaces = " "
        for total in totals:
            if total * 100 >= i:
                cat_spaces += "o  "
            else:
                cat_spaces += "   "
        res+= str(i).rjust(3) + "|" + cat_spaces + ("\n")
        i-=10

    # print bottom line
    dashes = "-" + "---"*len(categories)
    names = []
    x_axis = ""
    for category in categories:
        names.append(category.category)

    maxi = max(names, key=len)

    # print category names
    for x in range(len(maxi)):
        nameStr = '     '
        for name in names:
            if x >= len(name):
                nameStr += "   "
            else:
                nameStr += name[x] + "  "

        if x != len(maxi) - 1:
            nameStr += '\n' 
                 
        x_axis += nameStr

    res+= dashes.rjust(len(dashes)+4) + "\n" + x_axis
    return res

'''
         
        rjustnum = 0

        if horizontal_line == '100|':
            rjustnum = 0
        elif horizontal_line == '0|':
            rjustnum = 4
        else:
            rjustnum = 4

        y_axis = str(i) + "|"

        horizontal_line += y_axis.rjust(rjustnum)

        for x in spend_chart_list:
            keys = list(x.keys())
            title = keys[0]
            percent = x[title][0]

            horizontal_line += ' o '

                
    
        print(horizontal_line)

        

    print("    ---------")

    title_line = ''
    for x in spend_chart_list:
        title_line += " "
        keys = list(x.keys())
        title = keys[0]
        for y in title:
            title_line += y

    text = ''


    for x in zip_longest(*title_line.split(), fillvalue=' '):
        print("     "  + '  '.join(x))

  

    spend_chart_list = []
    total = 0
    cat_total = 0
    print('='*50)

    horizontal_line = ''

    for x in categories:
        for y in x.ledger:
            if float(y['amount']) < 0:
                total += float(y['amount'] * -1)

    for x in categories:
        cat_title = x.category
        cat_with = { cat_title : [] }
        cat_total = 0
        for y in x.ledger:
            if float(y['amount']) < 0:
                cat_total += float(y['amount'] * -1)
                
        cat_with[cat_title].append( int((cat_total / total) * 100) )
        spend_chart_list.append(cat_with)


    for i in range(100, -1, -10):
        
    

    #print(title_line)
    #print(spend_chart_list)
    #print("Total : " + str(int(total) ))

'''



