# 自定义异常类
class InventoryError(Exception):
    pass

class InsufficientInventoryError(InventoryError):
    def __init__(self,isbn,request,available):
        self.isbn = isbn
        self.request = request
        self.available = available
        super.__init__(f"ISBN {isbn}库存不足！请求{request}本，库存{available}本")

class MinusquantityError(InventoryError):
    def __init__(self,quantity):
        self.quantity = quantity
        super.__init__(f"操作数量不能为负数！{quantity}")

class IdenticalISBNError(InventoryError):
    def __init__(self,isbn):
        self.isbn = isbn
        super.__init__(f"已存在相同{isbn}的书籍！")

# 基础图书类
class Book:
    total_type = 0
    total_inventory = 0

    def __init__(self,title,author,isbn,stock):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__stock = max(0,stock)

        Book.total_type += 1
        Book.total_inventory += self.__stock

# 封装
    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def isbn(self):
        return self.__isbn

    @property
    def stock(self):
        return self.__stock

    def add_stock(self,quantity):
        if quantity <0:
            raise MinusquantityError(quantity)
        self.__stock += quantity
        Book.total_inventory += quantity
        print(f"成功入库{quantity}本<<{self.__title}>>,当前库存{self.__stock}本!")

    def move_stock(self,quantity):
        if quantity < 0:
            raise MinusquantityError(quantity)
        elif self.__stock < quantity:
            raise InsufficientInventoryError(quantity,self.__isbn,self.__stock)
        self.__stock -= quantity
        Book.total_inventory -= quantity
        print(f"成功出库{quantity}本<<{self.title}>>,当前库存{self.__stock}本!")

    def display_book(self):
        return (
            f"图书信息:\n"
            f"书名:<<{self.__title}>>\n"
            f"作者:{self.__author}\n"
            f"ISBN编号:{self.__isbn}\n"
            f"库存:{self.__stock}本\n"
        )

# 继承与多态
class Audiobook(Book):
    def __init__(self,title,author,isbn,stock=0,duration=0,narrator='未知'):
        super().__init__(title,author,isbn,stock)
        self.__duration = duration
        self.__narrator = narrator

    def display_book(self):
        base_info = super().display_book()
        return (
            f"{base_info}"
            f"类型：有声书\n"
            f"时长：{self.__duration}\n"
            f"朗诵者：{self.__narrator}\n"
        )

class Ebook(Book):
    def __init__(self, title, author, isbn, stock=0,format="NULL",file_mb=0 ):
        super().__init__(title, author, isbn, stock)
        self.__format = format
        self.__file_mb = file_mb

    def display_book(self):
        base_info = super().display_book()
        return(
            f"{base_info}"
            f"类型：电子书\n"
            f"格式：{self.__format}\n"
            f"大小：{self.__file_mb}\n"
        )

class Managesystem:
    def __init__(self):
        self.__books = {}

    def add_book(self,book):
        if book.isbn in self.__books:
            raise IdenticalISBNError(book.isbn)
        self.__books[book.isbn] = book
        print(f"图书<<{book.title}>>已成功添加到库存系统中！")

    def get_book(self,book):
        if book.isbn not in self.__books:
            raise InsufficientInventoryError(f"你所查找的ISBN号为{book.isbn}的书籍不存在！")
        return self.__books[book.isbn]

    def display_all_books(self):
        if not self.__books:
            print("库存暂无图书！")
            return
        print("\n=== 所有图书 ===")
        for book in self.__books.values():
            print("\n"+book.display_book())
            print("-" * 40)

    def display_info(self):
        print(f"当前图书种类：{Book.total_type}种")
        print(f"当前图书总库存：{Book.total_inventory}本")

# 测试
if __name__ == "__main__":
    inventory = Managesystem()
# 添加图书
    try:
        book1 = Book("Python编程：从入门到实践", "埃里克·马瑟斯", "9787115428028", 50)
        inventory.add_book(book1)

        ebook1 = Ebook("流畅的Python", "卢西亚诺·拉马略", "9787115454157", 30, "PDF", 25)
        inventory.add_book(ebook1)

        audiobook1 = Audiobook("人类简史", "尤瓦尔·赫拉利", "9787508647357", 20, 12, "李雷")
        inventory.add_book(audiobook1)
    except IdenticalISBNError as e:
        print(e)

# 图书入库
    try:
        book1.add_stock(20)
        ebook1.add_stock(15)

    except MinusquantityError as e:
        print(e)

# 图书出库
    try:
        book1.move_stock(5)
    except InsufficientInventoryError as e:
        print(e)

# 查看所有图书
    inventory.display_all_books()
    inventory.display_info()