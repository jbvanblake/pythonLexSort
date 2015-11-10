

# print(sorted([[1,2,3],[3,2,1],[2,1,3]]))
def convert(order, word):
    array = []
    for c in word:
        array.append(order.index(c))
    return array
# print(convert("acb", "abc"))

def lexSort(strings, order):
    sortedList = sorted(strings, key=lambda word: [convert(order,word)])
    print(sortedList)

lexSort(["acb", "abc", "bca"], "abc")
lexSort(["acb", "abc", "bca"], "cba")
lexSort(["aaa","aa",""], "a")

