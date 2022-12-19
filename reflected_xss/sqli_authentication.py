import pymysql as sql

db_username = 'root'
db_password = 'password'
db_name = 'mydb'

# Connect to MySQL database
def authenticate_broken(username, password):
    connection = sql.connect(host='localhost',
                             user=db_username,
                             password=db_password,
                             database=db_name,
                             )

    with connection:
        with connection.cursor() as cursor:
            query = f'SELECT * FROM users where username = "{username}" and password = "{password}";'
    #        SELECT * FROM users where username = 'admin' or 1=1; --{username}' and password = '{password}'
            cursor.execute(query)
            result = cursor.fetchall()
            if len(result) == 1:
                return(f'Welcome {result[0][1]}')
            else:
                return('Failed to login, no user exists with those credentials')
        
def authenticate(username, password):
    connection = sql.connect(host='localhost',
                             user=db_username,
                             password=db_password,
                             database=db_name,
                             )

    with connection:
        with connection.cursor() as cursor:
            query = f'SELECT * FROM users where username = %s and password = %s;'
    #        SELECT * FROM users where username = 'admin' or 1=1; --{username}' and password = '{password}'
            cursor.execute(query, (username, password))
            result = cursor.fetchall()
            if len(result) == 1:
                return(f'Welcome {result[0][1]}')
            else:
                return('Failed to login, no user exists with those credentials')
 
# Ask for credentials
r = authenticate_broken(username = 'admin',
                    password = 'admin')
print(f'regular: {r}')

r = authenticate_broken(username = '" or 1=1 LIMIT 1;#',
                    password = '')
print(f'sqli: {r}')

r = authenticate_broken(username = 'admin',
                    password = 'password')
print(f'failed: {r}')

