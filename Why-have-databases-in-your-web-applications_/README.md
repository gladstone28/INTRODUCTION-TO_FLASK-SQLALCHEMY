link to lesson
https://www.codecademy.com/courses/learn-flask-databases/lessons/flask-intro-sql-alchemy/exercises/databases-motivation-intro


INTRODUCTION TO FLASK-SQLALCHEMY
Why have databases in your web applications?
1 min
Web applications are often built around a lot of data that change frequently. The data is usually organized in entities related in some way. For example, entities such as users are related to products by the act of purchasing, music albums are related to a specific artist by authoring, users are related to other users by befriending, etc.

Relational databases offer robust and efficient data management. A usual relational database consists of tables that represent entities and/or relationships amongst entities. The attributes of entities are constrained (for example, NAME attribute is a string, and a user’s PASSWORD should not be empty). The way a database is organized in entities, attributes and relationships, without data being present, is called the database schema.

Database schema design: A simple book club scenario

You want to create a personal book club application. Each month you pick a book your friends can review and rate. Your web app manages registered readers, the list of books you choose each month, and the ratings the readers write for those books. Moreover, you can show the annotations your friends made while reading the suggested books.

The schema for this problem is shown on the right. Inspect the schema by following the instructions below.


### Instructions
Entities in our database are Reader, Book, Review and Annotation. Those represent tables in the schema.

Attributes are properties of an entity and are represented as columns in a database table. For example, Reader’s attributes are NAME, SURNAME and EMAIL, and Review’s attributes are TEXT and STARS (representing ratings from 1 to 5).

Relationships are represented as arrows between tables. Readers are in a relationship with books by reviewing them and by making annotations. A reader can review and annotate multiple books. A book can have multiple reviews and annotations. Each review or annotation is associated with one book and one reader. We say that Reader is in a one-to-many relationship with Review, and Annotation. Similarly, Book is in a one-to-many relationship with Review and Annotation.

Columns with the yellow key represent the primary key columns that uniquely identify entries in the table.

Columns with the silver key symbols represent the foreign key columns that represent references to the primary keys of other tables.

Note: often when modeling application databases, nouns represent entities (readers and books) and verbs represent relationships (to review).

![](./books-schema.webp)
