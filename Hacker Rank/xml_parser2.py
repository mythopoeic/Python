import xml.etree.ElementTree as etree
N = input()
myString = ""
count = 0
for _ in range(N):
    myString += raw_input()
    
 


def goDeeper(depth, node):
    if len(node)>0:   
        depth = max(goDeeper(depth + 1, x) for x in node)
    return depth


tree = etree.ElementTree(etree.fromstring(myString))
root = tree.getroot()

print(goDeeper(0, root))