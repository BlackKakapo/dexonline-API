from bs4 import BeautifulSoup
import requests
import html5lib



"""
	Function getWordOfThe
	Required @link
	Return @list

	Universal function that receives a link and returns a list of definition (word and definition)
"""
def getWordOfThe(link=None):
	# Call function to get spans by link
	spans = getSpans(link)

	definition = []
	for span in spans:
		try:
			word = span.find('b').text
			definition.append(str(word).strip())

			span.find("b").extract()
			definition.append(span.text.strip())

		except:
			error = 'Error that will not be displayed :D'
	return definition

"""
	Function getWordOfThe
	Required @link
	Return @list

	Universal function that receives a link and returns the span tags
"""
def getSpans(link=None):
	response = requests.get(link)
	soup = BeautifulSoup(response.content, features="html5lib")
	spans = soup.find_all('span','def')

	return spans

"""
	Function toString
	Required @list or @listOfLists
	Return nothing
	Print word and definition
	Ex:
		WORD: Default word
		DEFINITION: Default definition

	Work for function: getWordDefinition, getWordOfTheDay, getWordOfTheMonth
"""
def toString(listOfDefinition=['Default word', 'Default definition']):
	if str(type(listOfDefinition[0])) == "<class 'list'>" and str(type(listOfDefinition[1])) == "<class 'list'>":
		for definition in listOfDefinition:
			print('WORD: ' + str(definition[0]))
			print('DEFINITIN: ' + str(definition[1]) + '\n')

	elif str(type(listOfDefinition[0])) == "<class 'str'>":
		print('WORD: ' + str(listOfDefinition[0]))
		print('DEFINITIN: ' + str(listOfDefinition[1]) + '\n')

"""
	Function getWordDefinition
	Required @word
	Return @listOfLists

	In every list is present: word and definition
"""
def getWordDefinition(word=None):
	link = 'https://dexonline.ro/definitie/' + str(word) + '/expandat'

	# Call function to get spans by link
	spans = getSpans(link)

	definition = []
	for span in spans:
		wordDef = []
		try:
			word = span.find("b").text
			wordDef.append(str(word).strip())
			span.find("b").extract()

			for word in span:
				wordDef.append(span.text.strip())

			if wordDef[1] != '' or wordDef[1] != '':
				definition.append(wordDef)
		except:
			error = 'Error that will not be displayed :D'
	return definition

"""
	Function getWordOfTheDay
	Required nothing
	Return @list
	
	In list is present: word and definition
"""
def getWordOfTheDay():
	link = 'https://dexonline.ro/cuvantul-zilei'
	return getWordOfThe(link)

"""
	Function getWordOfTheMonth
	Required nothing
	Return @list
	
	In list is present: word and definition
"""
def getWordOfTheMonth():
	link = 'https://dexonline.ro/cuvantul-lunii'
	return getWordOfThe(link)