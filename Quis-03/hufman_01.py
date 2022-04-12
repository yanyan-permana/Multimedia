
def Total_Gain(data, coding):
    # total bit space to stor the data before compression
    before_compression = len(data) * 8
    after_compression = 0
    symbols = coding.keys()
    for symbol in symbols:
        count = data.count(symbol)
        # calculate how many bit is required for that symbol in total
        after_compression += count * len(coding[symbol])
    print("Space usage before compression (in bits):", before_compression)
    print("Space usage after compression (in bits):",  after_compression)


def Calculate_Probability(data):
    symbols = dict()
    for element in data:
        # print(element)
        if symbols.get(element) == None:
            symbols[element] = 1
        else:
            symbols[element] += 1
        # print(symbols)
    return symbols


data = " yyyyyaaaaaaannnnnnn"
# print(data)
symbol_with_probs = Calculate_Probability(data)
# print('symbol_with_probs :',symbol_with_probs)
symbols = symbol_with_probs.keys()
probabilities = symbol_with_probs.values()
# print("symbols: ", symbols)
# print("probabilities: ", probabilities)


class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        # probability of symbol
        self.prob = prob

        # symbol
        self.symbol = symbol

        # left node
        self.left = left

# right node
        self.right = right

        # tree direction (0/1)
        self.code = ''

        # tree parent
        self.parent = ''


# converts into object
nodes = []
for symbol in symbols:
    nodes.append(Node(symbol_with_probs.get(symbol), symbol))

# print the entire object
# for i in nodes:
    # print(i.__dict__)

# looping to create huffman tree
i = 1
while len(nodes) > 1:
    # sort all the nodes in ascending order based on their probability

    nodes = sorted(nodes, key=lambda x: x.prob)

    # print('\niteration number : ',i)

    # to visualize the making of huffman tree
    # for node in nodes:
    # print(node.symbol, node.prob)
    # try:
    # print('left',node.left.__dict__)
    # print('right',node.right.__dict__)
    # except:
    # pass

    # pick 2 smallest nodes
    right = nodes[0]
    left = nodes[1]

    left.code = 0
    right.code = 1

    left.parent = left.symbol+right.symbol
    right.parent = left.symbol+right.symbol

    # combine the 2 smallest nodes to create new node

newNode = Node(left.prob+right.prob, left.symbol+right.symbol, left, right)

nodes.remove(left)
nodes.remove(right)
nodes.append(newNode)
# i+=1
# loop ended
# print('\ncreated huffman tree : ')
# print(nodes[0].__dict__)

codes = dict()


def Calculate_Codes(node, val=''):
    # huffman code for current node
    # print('node code: ',node.code)
    newVal = val + str(node.code)
    # print(node.symbol,newVal)
    # print(node.__dict__)
    if(node.left):
        # print("left True", node.left.__dict__)
        Calculate_Codes(node.left, newVal)
    if(node.right):
        # print('right True', node.right.__dict__)
        Calculate_Codes(node.right, newVal)

    if(not node.left and not node.right):
        # print(codes)
        codes[node.symbol] = newVal

    # print(codes)
    return codes


huffman_encoding = Calculate_Codes(nodes[0])
print("symbols with codes : ", huffman_encoding)

""" A helper function to calculate the space difference between compressed and non compressed data"""


def Total_Gain(data, coding):
    # total bit space to stor the data before compression
    before_compression = len(data) * 8
    after_compression = 0
    symbols = coding.keys()

    print('symbols: ', symbols)
    print('coding: ', coding)
    for symbol in symbols:
        count = data.count(symbol)


# calculate how many bit is required for that symbol in total
# after_compression += count * len(coding[symbol])
        print('after_compression: ', after_compression)
    print("Space usage before compression (in bits):", before_compression)
    print("Space usage after compression (in bits):",  after_compression)
