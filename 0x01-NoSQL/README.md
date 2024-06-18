### General Objectives
What NoSQL means

What is difference between SQL and NoSQL

What is ACID

What is a document storage

What are NoSQL types

What are benefits of a NoSQL database

How to query information from a NoSQL database

How to insert/update/delete information from a NoSQL database

How to use MongoDB

MongoDB is a document database. It stores data in a type of JSON format called BSON.


# Getting started with MongoDB


### SQL vs Document Databases
SQL databases are considered relational databases. They store related data in separate tables. When data is needed, it is queried from multiple tables to join the data back together.

MongoDB is a document database which is often referred to as a non-relational database. This does not mean that relational data cannot be stored in document databases. It means that relational data is stored differently. A better way to refer to it is as a non-tabular database.

MongoDB stores data in flexible documents. Instead of having multiple tables you can simply keep all of your related data together. This makes reading your data very fast.

### Local vs Cloud Database
MongoDB can be installed locally, which will allow you to host your own MongoDB server on your hardware. This requires you to manage your server, upgrades, and any other maintenance.

You can download and use the MongoDB open source Community Server on your hardware for free.

However, for this course we are going to use MongoDB Atlas, a cloud database platform. This is much easier than hosting your own local database.

To be able to experiment with the code examples, you will need access to a MongoDB database.

