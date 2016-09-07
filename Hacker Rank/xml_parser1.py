import xml.etree.ElementTree as etree
N = input()
myString = ""
count = 0
for _ in range(N):
    myString += raw_input()
    
 

tree = etree.ElementTree(etree.fromstring(myString))



def traverse(node):
  return len(node.attrib) + sum(traverse(child) for child in node)

print traverse(tree.getroot())
'''
11
<feed xml:lang='en'>
  <title>HackerRank</title>
  <subtitle lang='en'>Programming challenges</subtitle>
  <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
  <updated>2013-12-25T12:00:00</updated>
  <entry>
  	<author gender='male'>Harsh</author>
    <question type='hard'>XML 1</question>
    <description type='text'>This is related to XML parsing</description>
  </entry>
</feed>
'''