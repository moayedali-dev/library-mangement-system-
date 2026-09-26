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
search_title = input ("Enter book title to search:")
for book in books:
    if book ["title"] .lower() == search_title .lower() :
          print("The book title is found")
          break
    else:
         print("book not found")
         