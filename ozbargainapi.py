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
			d = feedparser.parse('https://www.ozbargain.com.au/feed')
		else:
			d = feedparser.parse('https://www.ozbargain.com.au/feed/' + str(x))
		for entry in d['entries']:
			finalarray.append(entry.title + " | " + entry.link)
#	print(finalarray)
	return(finalarray)
#print(args.searchstring)
#if args.number:
#    print(args.number)

def searcher(searcharg):
	print("OZBARGAIN Search Results")
	matches = []
	searchArray = feedDownloader(args.number)
	for entry in searchArray:
#		print(entry)
		if searcharg.lower() in entry.lower():
			matches.append(entry)
	matches = list(dict.fromkeys(matches))
	for result in matches:
		print(result)

if args.searchstring == "all":
	usedArray = []
	searchArray = feedDownloader(args.number)
	for entry in searchArray:
		if entry not in usedArray:
			print(entry)
			usedArray.append(entry)
		else:
			continue
else:
	searcher(args.searchstring)
