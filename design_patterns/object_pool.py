
'''
Used primarily for database connections
'''

class DBConnection:
    def __init__(self):
        print("does lots of initialization work")

class ObjectPool:
    def __init__(self):
        self.pool = [DBConnection(), DBConnection()]
    
    def get_connection(self):
        if self.pool:
            print('getting connection...')
            return self.pool.pop()
        else: print('pool is empty. someone must return connection first.')
    
    def return_connection(self, connection):
        if len(self.pool) < 2:
            print('returning connection...')
            self.pool.append(connection)
        else: print('pool is full.')

pool = ObjectPool()
bob = pool.get_connection()
lisa = pool.get_connection()
john = pool.get_connection()

pool.return_connection(lisa)
john = pool.get_connection()


# conn1 = DBConnection() # bob created
# conn2 = DBConnection() # jo created
# conn3 = DBConnection() # ellen created

# object_pool = list()

# object_pool.append(DBConnection())
# object_pool.append(DBConnection())

# print(object_pool)

# print('my guy bob needs a connection')
# bob = object_pool.pop()
# print(bob)

# print('our girl johanna needs a connection')
# johanna = object_pool.pop()
# print(johanna)

# print('joanna is returning her connection to the pool')
# object_pool.append(johanna)

# print('now ellen needs a connection')
# ellen = object_pool.pop()
# print(ellen)