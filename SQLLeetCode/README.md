30 Day Challenge of practicing sql by solving sql leetcode problems without the help of AI.

# 0-day_one.sql
#### Question 1. _Recyclable and Low Fat Products_
##### Write a solution to find the ids of products that are both low fat and recyclable.

Table: ```Products```
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
```
**product_id** : is the primary key (column with unique values) for this table.<br>
**low_fats** : is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.<br>
**recyclable** : is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.


##### Solution
```
-- Using AND operator in sql
SELECT product_id FROM Products WHERE low_fats='Y' AND recyclable='Y';
```
