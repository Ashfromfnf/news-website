# this script basically reads a txt document with a list of all the
# articles and then turns them into html files so i don't really need
# to rewrite everything every time i change the source code
#
# PATH: py/articles.txt

txtPath = "C:/Users/andre/Documents/GitHub/website-but-boring/py/articles.txt"

txt = open(txtPath, "r").read()

txtlist = txt.split("YOU'REBEAUTIFUL")

print(txt)

input("")