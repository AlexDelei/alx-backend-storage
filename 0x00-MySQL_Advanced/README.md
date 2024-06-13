## General Objectives
1. #### How to create tables with constraints
SQL constraints are used to specify rules for the data in a table.

Constraints are used to limit the type of data that can go into a table. This ensures the accuracy and reliability of the data in the table. If there is any violation between the constraint and the data action, the action is aborted.

**NOT NULL** - Ensures that a column cannot have a NULL value
**UNIQUE** - Ensures that all values in a column are different
**PRIMARY KEY** - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
**FOREIGN KEY** - Prevents actions that would destroy links between tables
**CHECK** - Ensures that the values in a column satisfies a specific condition
**DEFAULT** - Sets a default value for a column if no value is specified
**CREATE INDEX** - Used to create and retrieve data from the database very quickly


2. #### How to optimize queries by adding indexes
syntax -->
```
CREATE TABLE person(
	id INT NOT NULL,  
  	first_name VARCHAR(15) NOT NULL,
  	last_name VARCHAR(15) NOT NULL,
  	age INT NOT NULL,
  	PRIMARY KEY(id)
);
/* Index on First Name */
CREATE INDEX person_fname ON person (first_name);
/* Will tell us whether our query uses the intended index */
explain SELECT * FROM person WHERE first_name = "Donald" \G
```

3. #### What is and how to implement stored procedures and functions in MySQL
 A stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again.

##### Stored Procedure syntax
```
 CREATE PROCEDURE procedure_name
AS
sql_statement
GO;
```

##### Executing a stored Procedure
```
EXEC procedure_name;
```

**Example 1**
```
CREATE PROCEDURE SelectAllCustomers
AS
SELECT * FROM Customers
GO;
```

Execution:
```
EXEC SelectAllCustomers;
```

**Example 2**
Stored Procedures with one parameter
```
CREATE PROCEDURE SelectAllCustomers @City nvarchar(30)
AS
SELECT * FROM Customers WHERE City = @City
GO;
```

Execution:
```
EXEC SelectAllCustomers @City = 'London';
```

**Example 3**
Stored Procedures with multiple parameters

```
CREATE PROCEDURE SelectAllCustomers @City nvarchar(30), @PostalCode nvarchar(10)
AS
SELECT * FROM Customers WHERE City = @City AND PostalCode = @PostalCode
GO;
```

Execution:
```
EXEC SelectAllCustomers @City = 'London', @PostalCode = 'WA1 1DP';
```
4. #### What is and how to implement views in MySQL
A view contains rows and columns, just like a real table. The fields in a view are fields from one or more real tables in the database.

A view is created with a ```CREATE VIEW``` statement.

**Create View syntax**
```
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```


**Example 1**
```
mysql> CREATE TABLE t (qty INT, price INT);
mysql> INSERT INTO t VALUES(3, 50);
mysql> CREATE VIEW v AS SELECT qty, price, qty*price AS value FROM t;
mysql> SELECT * FROM v;
+------+-------+-------+
| qty  | price | value |
+------+-------+-------+
|    3 |    50 |   150 |
+------+-------+-------+
```


#### A view definition is subject to the following restrictions
- The SELECT statement cannot refer to system variables or user-defined variables.

- Within a stored program, the SELECT statement cannot refer to program parameters or local variables.

- The SELECT statement cannot refer to prepared statement parameters.

- Any table or view referred to in the definition must exist. If, after the view has been created, a table or view that the definition refers to is dropped, use of the view results in an error. To check a view definition for problems of this kind, use the CHECK TABLE statement.

- The definition cannot refer to a TEMPORARY table, and you cannot create a TEMPORARY view.

- You cannot associate a trigger with a view.

- Aliases for column names in the SELECT statement are checked against the maximum column length of 64 characters (not the maximum alias length of 256 characters).

5. #### What is and how to implement triggers in MySQL