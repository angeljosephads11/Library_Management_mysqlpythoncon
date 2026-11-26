import mysql.connector
class Book:
    def __init__(self):
        try:
            self.con=mysql.connector.connect(user='root',password='root',host='localhost',database='library_management')
            print(self.con)
            print('connnection established')
        except:
            print('Failed to establish connection')
    def create(self,title,author,category,total_copies,available_copies):
        try:
            cursor=self.con.cursor()
            if  total_copies!=0:
                print('enter a non negative number')
                if available_copies>total_copies:
                    query='insert into Books(title,author,category,total_copies,available_copies)values(%s,%s,%s,%s,%s)'
                    data=(title,author,category,total_copies,available_copies)
                    cursor.execute(query,data)
                    self.con.commit()
                    print('added books to the table succsesfully')
                else:
                    print('the available copies are greater than total copies')
                    print('not inserted successfully')
        except:
            print('failed to add books to the table')

    def read(self):
        try:
            cursor=self.con.cursor()
            query='select * from Books where available_copies>=1 order by title limit 20'
            cursor.execute(query,)
            records=cursor.fetchall()
            if records:
                for row in records:
                    print(row)
            else:
                print('no record found')
        except:
            print('failed to View Available books')

    def search(self,id,title,author):
        try:
            cursor=self.con.cursor()
            query='select * from Books where book_id=%s or title=%s or author=%s '
            data=(id,title,author)
            cursor.execute(query,data)
            records=cursor.fetchall()
            if records:
                for row in records:
                    print(row)
            else:
                print('no record found')
        except:
            print('Failed to search')
    def update(self,available_copies,book_id):
        try:
            cursor=self.con.cursor()
            query='update Books set available_copies=%s where book_id=%s'
            data=(available_copies,book_id)
            cursor.execute(query,data)
            self.con.commit()
            if cursor.rowcount>0:
                print('updated succesfully')
            else:
                print('not updated')
        except:
             print('Failed to update')
    def delete(self,book_id):
        try:
            cursor=self.con.cursor()
            query='delete from Books where book_id=%s'
            data=(book_id,)
            cursor.execute(query,data)
            self.con.commit()
            if cursor.rowcount>0:
                print('deleted successfully')
            else:
                print('not deleted')
        except:
            print('Failed to delete')
    def summary(self):
        try:
            cursor=self.con.cursor()
            query='select count(*),avg(total_copies),count(available_copies),category from Books group by category'
            cursor.execute(query)
            records=cursor.fetchone()
            if records:
                print(records)
            else:
                print('no record found')
        except:
            print('failed to View Available books')

b=Book()
while(1):
    print('1.AddBook')
    print('2.View Available Books')
    print('3.Search Book')
    print('4.UpdateAvailable Copies')
    print('5.Delete Book')
    print('6.Library Summary')
    print('7.Exit')
    ch=int(input('enter your choice'))
    if ch==1:
        title=input('enter the book title')
        author=input('enter the book author')
        category=input('enter the category')
        total_copies=input('enter the total_copies')
        available_copies=input('enter the available copies')
        b.create(title,author,category,total_copies,available_copies)
    elif ch==2:
        b.read()
    elif ch==3:
        id=int(input('enter the id'))
        title=input('enter the title')
        author=input('enter the author')
        b.search(id,title,author)
    elif ch==4:
        available_copies=int(input('enter the available copies'))
        id=int(input('enter the id'))
        b.update(available_copies, id)
    elif  ch==5:
        id=int(input('enter the id'))
        b.delete(id)
    elif ch==6:
       b.summary()
    elif ch==7:
        exit()
    else:
        print('invalid  input')