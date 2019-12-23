#!/usr/bin/python3
import feedparser, argparse
#from termcolor import colored

parser = argparse.ArgumentParser(description="A tool to search the latest ozbargain posts")
parser.add_argument('searchstring', help='The string to search for (use string \"all\" to print all entries)')
parser.add_argument('-n', '--number', type=int, default=5, help='Number of pages to search')
args = parser.parse_args()

def feedDownloader(number):
	finalarray = []
	for x in range(1,number):
		if x ==1:
			d = feedparser.parse('https://www.ozbargain.com.au/deals/feed')
		else:
			d = feedparser.parse('https://www.ozbargain.com.au/deals/feed/' + str(x))
		for entry in d['entries']:
			finalarray.append(entry.title + " | " + entry.link)
	return(list(dict.fromkeys(finalarray)))

def searcher(searcharg):
	print("OZBARGAIN Search Results")
	matches = []
	searchArray = feedDownloader(args.number)
	for entry in searchArray:
		if searcharg.lower() in entry.lower():
			matches.append(entry)
	for result in matches:
		print(result)

if args.searchstring == "all":
	searchArray = feedDownloader(args.number)
	for entry in searchArray:
		print(entry)
else:
	searcher(args.searchstring)
