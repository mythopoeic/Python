from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start :", tag
        for each in attrs:
            if type(each[1]) != 'NoneType':
                print "-> %s > %s" % (each[0],each[1])
            else:
                print "-> %s > None" % each[0]
    def handle_endtag(self, tag):
        print "End   :", tag
    def handle_startendtag(self, tag, attrs):
        print "Empty :", tag
        for each in attrs:
            if type(each[1]) != 'NoneType':
                print "-> %s > %s" % (each[0],each[1])
            else:
                print "-> %s > None" % each[0]

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

N = input()
for _ in range(N):
    parser.feed(raw_input())