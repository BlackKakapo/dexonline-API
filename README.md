# Dexonline.ro API

A simple API that queries dexonline.ro, it returns the definitions of the words.
>This is not an official API
#
What is dexonline - [info](https://wiki.dexonline.ro/wiki/Informații)
#

How to install, using pip install?

>pip install dexonlineBK

#

### Functionality
The first thing we need to do is import the library
```python
from dexonlineBK import dexonlineBK as DO
```
The first, and most important, function is getWordDefinition()
This function returns the list of lists
```python
definitions = DO.getWordDefinition("neexplicabil")

for defs in definitions:
	print(defs[0])
	print(defs[1] + "\n")
```
Output:
```
NEEXPLICÁBIL
adj. v. inexplicabil.

NEEXPLICABIL
adj. inexplicabil, neînțeles. (Un fapt ~.)

Neexplicabil
≠ explicabil
```
For more printing comfort I have the toString() function
```python
DO.toString(definitions)
```
Output:
```
WORD: NEEXPLICÁBIL
DEFINITION: adj. v. inexplicabil.

WORD: NEEXPLICABIL
DEFINITION: adj. inexplicabil, neînțeles. (Un fapt ~.)

WORD: Neexplicabil
DEFINITION: ≠ explicabil
```
getWordOfTheDay() function, returns the list with the word and its definition
toString() also works with this function
```python
DO.toString(DO.getWordOfTheDay())
```
Output:
```python
WORD: ARÉIC, -Ă,
DEFINITION: areici, -ce, adj. (Geol.; despre regiuni, soluri) Lipsit de apă, uscat, arid. [Pr.: -re-ic] – Din fr. aréique.
```
getWordOfTheMonth() function, returns the list with the word and its definition
toString() also works with this function
```python
DO.toString(DO.getWordOfTheMonth())
```
Output:
```python
WORD: ntur
DEFINITION: i [At: ALR II, 5752/791 / E: fo] (Reg) Onomatopee care imită trilurile turturicii.
```
reallyExist() function, returns boolean.
dexonline.ro have list of words in romanina.
And here you check if this word exists in Romanian.
```python
print(DO.reallyExist('mama'))
```
Output:
```python
True
```
randomWord() function, returns random word.
dexonline.ro have a page with 100 random words.
```python
print(DO.randomWord())
```
Output:
```python
desfălura
```
```python
DO.toString(DO.getWordDefinition(DO.randomWord()))
```
Output:
```python
WORD: desfălura
DEFINITION: vr [At: DUMITRAȘCU, STR. 13 / V: ~lău~, ~fău~ / Pzi: ~rez / E: nct] (Olt) 1 A se descheia la haină. 2 (Pex) A se dezbrăca de haină, rămânând doar în cămașă.

WORD: desfălăura
DEFINITION: v vz desfălura

WORD: desfăura
DEFINITION: v vz desfălura
```
#
>The API is still being tested
