#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import HTMLParser
import re

# Original tweet
original_tweet = "I luv my &lt;3 iphone &amp; you're awsm apple. DisplayIsAwesome, sooo happppppy 🙂 http://www.apple.com"

print original_tweet

# Decode data
tweet = original_tweet.decode("utf8").encode('ascii','ignore')

# Escape HTML characters
html_parser = HTMLParser.HTMLParser()

tweet = html_parser.unescape(tweet)

# Apostrophe lookup
APOSTROPHES = {"'s" : " is", "'re" : " are"} ## Need a huge dictionary

words = tweet.split()
print words

reformed = [APOSTROPHES[word] if word in APOSTROPHES else word for word in words]

reformed = ' '.join(reformed)

# Split attached words
cleaned = ' '.join(re.findall('[A-Z][^A-Z]*', reformed))

#tweet = _slang_lookup(cleaned)

print cleaned