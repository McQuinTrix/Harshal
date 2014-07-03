#Name: Harshal Carpenter

#Importing Regex Package Of Python
import re

#Some identifiers
keyword = 0
identifier = 0
integer = 0
real = 0
special = 0
error = 0

#Opening files to write on it
out = open("out.txt","w")
sym = open("sym.txt","w")

with open("new.txt", "r") as f:
	for line in f:
		for word in line.split():
			if (word == "if") or (word == "then") or (word == "else") or (word == "begin") or (word == "end"):
				out.write("\n Keyword: "+ word)
				keyword += 1
			elif (word == """(""" ) or (word == """)""" ) or (word == """[""" ) or (word == """]""" ) or (word == """+""" ) or (word == """-""" ) or (word == """=""" ) or (word == """,""" ) or (word == """;""" ):
				#This is generally not a good way of doing it but I was not able to implement a better way of doing it(with Regex)
				out.write("\n Special Keyword: "+ word)
				special += 1
			else:
				try:
					word = int(word)
					word = str(word)
					out.write("\n Integer Keyword: "+ word)
					integer += 1
					continue
				except ValueError:
					try:
						word = float(word)
						word = str(word)
						out.write("\n Real Keyword: "+ word)
						real += 1
						continue
					except ValueError:
						try:
							if re.match("^[A-Za-z]*$",word):
								out.write("\n Identifier Keyword: "+ word)#hex(id(word))
								sym.write("\n Identifier"+ str(identifier) +": "+ word + "\t Memory:" + str(hex(id(word))))
								identifier += 1
							else:
								out.write("Error Word: "+ word)
								error += 1
						except ValueError:
							error += 1

out.write("\n\nKeywords: " + str(keyword))
out.write("\nSpecial Keywords: "+ str(special))
out.write("\nIntegers: " + str(integer))
out.write("\nReal: " + str(real))
out.write("\nIdentifier: " + str(identifier))
out.close()
sym.close()

########################################################################
