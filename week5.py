class Book:
    def __init__(self,author,book_name,num_pages,year_published):
        self.author=author
        self.book_name=book_name
        self.num_pages=num_pages
        self.year_published=year_published
    def get_book_info(self):
        return(f'I am currently reading {self.book_name} written by {self.author} in the year {self.year_published} with {self.num_pages} pages.😎😎\n'
                "Study")
class Genre(Book):
    def __init__(self,author,book_name,num_pages,year_published,genre):
        super().__init__(author, book_name,num_pages,year_published)
        self.genre=genre
    def get_book_info(self):
        book_info=super().get_book_info()
        return f"{book_info} well,the genre is {self.genre}"

#assign to an instance
book1=Book("Shakespeare","Hamlet",121,1606)
book2=Genre("Voltaire","Candide",98,1768,"Philosophy")
print(book2.get_book_info())

print()
print("Heading to Question 2")
print()
# Create a program that includes animals or vehicles with the same action (like move()). 
# However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Cow(Animal):
    def move(self):
        print("Walking 🐄🐄")


class Snake(Animal):
    def move(self):
        print("slithers 🐍🐍")

animals = [Cow(), Snake()]
for animal in animals:
    animal.move()
