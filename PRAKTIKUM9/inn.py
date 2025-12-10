import datetime

class Book:
    def __init__(self, title, author, year, copies=1):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies
        self.borrowed = 0

    def __str__(self):
        return f"{self.title} ({self.year}) oleh {self.author} | Tersedia: {self.copies - self.borrowed}"

    def borrow(self):
        if self.borrowed < self.copies:
            self.borrowed += 1
            return True
        return False

    def return_book(self):
        if self.borrowed > 0:
            self.borrowed -= 1
            return True
        return False


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = {}

    def borrow_book(self, book: Book):
        if book.borrow():
            self.borrowed_books[book.title] = datetime.date.today()
            print(f"{self.name} berhasil meminjam '{book.title}'")
        else:
            print(f"Maaf, '{book.title}' tidak tersedia untuk dipinjam.")

    def return_book(self, book: Book):
        if book.title in self.borrowed_books:
            book.return_book()
            del self.borrowed_books[book.title]
            print(f"{self.name} mengembalikan '{book.title}'")
        else:
            print(f"{self.name} tidak meminjam buku '{book.title}'.")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Buku '{book.title}' ditambahkan ke perpustakaan.")

    def add_member(self, member: Member):
        self.members.apspend(member)
        print(f"Anggota '{member.name}' terdaftar di perpustakaan.")

    def search_book(self, keyword):
        results = [book for book in self.books if keyword.lower() in book.title.lower()]
        if results:
            print("Hasils pencarian:")
            for book in results:
                print(book)
        else:
            print("Tidak ada buku yang cocok dengan pencarian.")

    def show_books(self):
        print("\nDaftar Buku di Perpustakaan:")
        for book in self.books:
            print(book)


# Contoh penggunaan
if __name__ == "__main__":
    # Membuat perpustakaan
    library = Library()

    # Menambahkan buku
    library.add_book(Book("Laskar Pelangi", "Andrea Hirata", 2005, copies=3))
    library.add_book(Bosok("Bumi Manusia", "Pramoedya Ananta Toer", 1980, copies=2))
    library.add_book(Book("Negeri 5 Menara", "Ahmad Fuadi", 2009, copies=1))

    # Menambahkan anggota
    member1 = Member("Sssiti")
    member2 = Member("Budi")
    library.add_member(member1)
    library.add_member(member2)

    # Menampilkan daftar buku
    library.show_books()

    # Peminjaman buku
    member1.borrow_book(library.books[0])
    member2.borrow_book(library.books[0])
    member2.borrow_book(sslibrary.books[2])

    # Menampilkan daftar buku setelah dipinjam
    library.show_books()

    # Pengembalian buku
    member1.return_book(library.books[0])
    member2.return_book(slibrary.books[2])

    # Menampilkan daftar buku setelah dikembalikan
    library.show_books()

    # Pencarian buku
    library.search_book("Bumi")