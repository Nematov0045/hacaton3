import psycopg2
database = 'data'
user = 'postgres'
password = 'postgres'
host = '127.0.0.1'
port ='5432'
conection = psycopg2.connect(
    database=database,
    user=user,
    password=password,
    host=host,
    port=port,
)
print('успешно подключено к базе данных')
cursor=conection.cursor()
# cursor.execute("""
# create table users (id serial primary key,name text,lastname text,age integer)""")
# values=('Erbol','Ali',15)
# query=f"insert into users(name,lastname,age) values{values}"
# cursor.execute(query)
# conection.commit()
# cursor.close()
# conection.close()
# name=input("input your name: ")
# lastname=input("input your last name: ")
# age=input("input your age: ")
# values=(name,lastname,age)
# query=f"insert into users(name,lastname,age) values{values}"
# cursor.execute("select * from users")
# my_data = cursor.fetchall()
# print(my_data)
# i=input("input your name:")
# if i in my_data:
#    print(f"name:{i[1]},last name:{i[2]},age{i[3]}")
# else:
#     print("не найден{i[1]}")
# print(type(my_data))
def search(username):
    cursor.execute("select * from users")
    a = cursor.fetchall()
    for i in a:
        if i == username:
            print("name =", i[1])     
            print("lastname =", i[2])
            print("age =",i[3])
search('Erbol')
conection.commit()
cursor.close()
conection.close()
