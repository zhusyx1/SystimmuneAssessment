# SystimmuneAssessment
Part I

Please see network diagram in diagram.png. 
Explaination: Web client send HTTP request to web server through firewall for safety whereas web server would reply web client with HTML/JavaScript. In web server, there could be anything like apache. Web server offers web app like C/ C#/C++. And web app will be connect with SQL database.

 

Part II 

Below is the SQL database create statement, table name is Car, with columns of CarModleId, CarModleName, SalesName, SoldMonth, NumberSold. CarModelId and NumberSold are type of integer whereas the rest of columns are char.
CREATE TABLE Car (
	    CarModleId int,
	    CarModleName varchar(50),
	    SalesName varchar(50),
	    SoldMonth varchar(10)
	    NumberSold int
)


Part III

I have chosen CSV as the encoding format for my data, because CSV files are plain-text files, it’s easier for developers to import into/from spreadsheet and database. And CSV can easily organize large amounts of data.

Instructions of run the program:
-	Python 3.8 was used in the program.
-	Anaconda was used (pandas)
-	In terminal, run python carDealer.py --input_csv_name car.csv
-	Expected outcome: top.html and sales.html will be created in the same directory with one table in each file. 
