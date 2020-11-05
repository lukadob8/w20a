import dbcreds
import mariadb

username = input("Username: ")
password = input("Password: ")

def login():
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", [username, password])
    user = cursor.fetchall()
    cursor.close()
    conn.close()
    if len(user) == 1:
        print("Login successful")
        return True
    else:
        print("login invalid")
        return False

while login() == False:
    username = input("Username: ")
    password = input("Password: ")
    

    

print("To make a blog post press B")
print("To see all posts press R")
user_choice = input("Your selection: ")

def makePost():
    blog_post = input("Write your blog post here: ")
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO blog_post(username, content, id) VALUES(?, ?, NULL)", [username, blog_post])
    conn.commit()
    cursor.close()
    conn.close()

def showBlogs():
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM blog_post")
    posts = cursor.fetchall()
    print(posts)
    cursor.close()
    conn.close()

if user_choice == "B":
    makePost()

elif user_choice == "R":
    showBlogs()

