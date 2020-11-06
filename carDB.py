import pandas as pd
import pyodbc

# Import CSV
data = pd.read_csv (r'car.csv')   
df = pd.DataFrame(data, columns= ['CarModleId','CarModleName','SalesName','SoldMonth','NumberSold'])

# Connect to SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RON\SQLEXPRESS;'
                      'Database=TestDB;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

# Create Table
cursor.execute('CREATE TABLE car (
    CarModleId int,
    CarModleName varchar(50),
    SalesName varchar(50),
    SoldMonth varchar(10)
    NumberSold int)')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO Car (CarModleId,CarModleName,SalesName,SoldMonth,NumberSold)
                VALUES (?,?,?)
                ''',
                row.CarModleId, 
                row.CarModleName,
                row.SalesName,
                row.SoldMonth,
                row.NumberSold
                )
conn.commit()
