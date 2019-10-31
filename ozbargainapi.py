#!/usr/bin/python3
import feedparser, argparse
from termcolor import colored

parser = argparse.ArgumentParser(description="A tool to search the latest ozbargain posts")
parser.add_argument('searchstring')
parser.add_argument('-n', '--number', type=int, default=5, help='Number of pages to search')
args = parser.parse_args()
#print(args.searchstring)
#if args.number:
#    print(args.number)

print("OZBARGAIN Search Results")
matches = []
for x in range(1,args.number):
    if x == 1:
        d = feedparser.parse('https://www.ozbargain.com.au/feed')
    else:
        d = feedparser.parse('https://www.ozbargain.com.au/feed/' + str(x))
    for entry in d['entries']:
        if args.searchstring.lower() in entry.title.lower():
            matches.append(entry.title + " | " + entry.link)
matches = list(dict.fromkeys(matches))
for result in matches:
    print(result)
