# dictionary of our whole menu
menu = {
    'appetizers': (
        'wings',
        'cookies',
        'spring rolls',
    ),
    'entrees': (
        'salmon',
        'steak',
        'meat tornado',
        'a literal garden',
    ),
    'desserts': (
        'ice cream',
        'cake',
        'pie',
    ),
    'drinks': (
        'coffee',
        'tea',
        'unicorn tears',
    ),
}

total_order = {}


# capitalize each word in a series of words
def cap(stuff):
    words = stuff.split(' ')
    capped = []
    for word in words:
        word = word[0].upper() + word[1:].lower()
        capped.append(word)
    return ' '.join(capped)


def printLine(line, width):
    space = (width-len(line))
    # we have to pad the indent more than the extradent when space is odd
    indent = round(space/2+.1)
    extradent = int(space/2)
    print('** ' + (' ' * indent) + line + (' ' * extradent) + ' **')


def printBlock(lines):

    # first, lets get the longest line, so we know
    # how wide to make everything
    width = 0
    for line in lines:
        if(width < len(line)):
            width = len(line)

    # now, lets print out those lines!
    print('*' * (width+6))
    for line in lines:
        printLine(line, width)
    print('*' * (width+6))


def printMenu(menu, items):
    print("\n"+cap(menu))
    print('-' * len(menu))

    for item in items:
        print(cap(item))


def validItem(item):
    for category in menu:
        if item in menu[category]:
            return True
    return False


# how many orders of this particular menu item have we ordered?
def numItem(item):
    if(total_order.get(item)):
        return total_order[item]


# print the welcome block
printBlock((
    'Welcome to the Snakes Cafe!',
    'Please see our menu below.',
    '',
    'To quit at any time, type "quit"',
))

# print the menus
for category in menu:
    printMenu(category, menu[category])

# print the end of the menu block
print('')
printBlock((
    'What would you like to order?',
))


# loop to allow user to oder items
order = ''
while order == '':
    order = input('> ')
    order = order.lower()
    if(order == 'quit'):
        quit = ''
        break
    elif validItem(order):
        if(total_order.get(order) is None):
            total_order[order] = 1
        else:
            total_order[order] += 1
        num = numItem(order)
        orders = 'order' if num == 1 else 'orders'
        have = 'has' if num == 1 else 'have'
        printLine(f'{str(num)} {orders} of {cap(order)} {have} been added to your meal', 0)
        order = ''
        continue
    else:
        printLine(f"Sorry, we don't sell {cap(order)} here.", 0)
        order = ''
        continue


# we had to input quit to get to this stage
for item in total_order:
    num = numItem(item)
    orders = 'order' if num == 1 else 'orders'
    printLine(f'{str(num)} {orders} of {cap(item)}', 0)
