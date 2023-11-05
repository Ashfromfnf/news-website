# this script basically reads a txt document with a list of all the
# articles and then turns them into html files so i don't really need
# to rewrite everything every time i change the source code
#
# PATH: py/articles.txt

txtPath = r"py/articles.txt"

txt = open("py\input.txt", "r", encoding="utf8").read()

txtlist = txt.split("YOU'REBEAUTIFUL")

print(txt)
print(txtlist)

finish = txt.replace(r"\n", "")
listfinish = finish.split("YOU'REBEAUTIFUL")

print("list finish:")
print(listfinish)


html = open("py/articlehtml.txt", "r", encoding="utf8").read()
print(html)

for i, val in listfinish:
    obj = listfinish[val]
    objli = obj.split("69TITILE69")


    title = objli[0]
    article = objli[1]

    html = open("py/articlehtml.txt", "r", encoding="utf8").read()

    print(html)

input("heyy")