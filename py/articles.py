# this script basically reads a txt document with a list of all the
# articles and then turns them into html files so i don't really need
# to rewrite everything every time i change the source code
#
# PATH: py/articles.txt 

txt = open("py\input.txt", "r", encoding="utf8").read()


print(txt)

txt = txt.replace(r"\n", "<br>")
finish = txt.replace(r"\'", "'")
finish = finish.replace("69AUTHOR69", "YOU'REBEAUTIFUL")
listfinish = finish.split("YOU'REBEAUTIFUL")

print("list finish:")
print(listfinish)


html = open("py/articlehtml.html", "r", encoding="utf8").read()
print("html")


listcomplete = [x.split("69TITLE69") for x in listfinish]


print("\n\n\n\n\n\n\n\n\n\n\n listcomplete: \n\n\n\n\\n\n\n\n\n\\n\n\n\n\n\n\n\n" + str(listcomplete))

for x in listcomplete:


    if len(x) == 1:
        prevtitle = str(x[0])
        

    
    print("length:", len(x))

    if len(x) == 2:
        x.insert(0, prevtitle)
        title = x[0]
        article = x[1]

        print("the title should be inserted, quality check for further information: " + str(x))

    if len(x) == 3:
        title = x[0]
        article = x[2]
        author = x[1]
        html = open("py/articlehtml.html", "r", encoding="utf8").read().format(title, title, article, author)
        print(html)

        print(str(x))
        with open(("./articles/" + title.replace(" - ", "-").replace(",", "").replace("""'""", "").replace("?", "").replace(" ", "-").replace(":", "") + ".html"), "w", encoding="utf8") as file:
            file.write(html)

    elif len(x) > 3:
        print(str(x) + "\n \n \n ^^^^^^^^^^^ \n HEAVY FUCKING FORMATTING ISSUE!!!!" + "LENGTH: " + str(len(x)))


input()