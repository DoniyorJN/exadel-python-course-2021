def collect_leaves(tree, result=None):
    if result is None: 
        result = []
    if(isinstance(tree, list)):
        for i in tree:
            if(isinstance(i, int)):
                result.append(i)
            elif(isinstance(i, list) or isinstance(i, dict)):
                collect_leaves(i, result)
    elif(isinstance(tree, dict)):
        for i in tree:
            if(isinstance(tree[i], int)):
                result.append(i)
            elif(isinstance(tree[i], list) or isinstance(tree[i], dict)):
                collect_leaves(tree[i], result)
    return result

# print time
tree = {
   "node1": {
       "node11": {
           "node111": [1, 2, 3],
           "node112": [4, 5]
       },
       "node12": [6]
   },
   "node2": [7, 8, 9]
}
treelist=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(collect_leaves(tree))
print(collect_leaves(treelist))

# assert time
assert collect_leaves(tree) == treelist
assert collect_leaves(treelist) == treelist
assert collect_leaves(1) == []
