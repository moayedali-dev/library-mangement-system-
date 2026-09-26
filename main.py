from books import books
print ("welcome to libarary mange system ")
print()
print("books")
print("-------------")
for book in books:
    print ("title:",book ["title"])
    print ("author:", book ["author"])
    print ("available:", book ["available"])
    print ()
