# this script basically reads a txt document with a list of all the
# articles and then turns them into html files so i don't really need
# to rewrite everything every time i change the source code
#
# PATH: py/articles.txt 

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


listcomplete = [x.split("69TITLE69") for x in listfinish]

print(listcomplete)

for x in listcomplete:

    
    print("length:", len(x))

    if len(x) <= 2:
        title = x[0]
        article = x[1]
        html = open("py/articlehtml.txt", "r", encoding="utf8").read().format(title, title, article)
        print(html)

        with open(("./articles/" + title.replace(" - ", "-").replace(",", "").replace("""'""", "").replace("?", "").replace(" ", "-") + ".html"), "w", encoding="utf8") as file:
            file.write(html)
    else:
        print(x + "\n \n \n ^^^^^^^^^^^ \n TOO SHORT!!!!")


input()