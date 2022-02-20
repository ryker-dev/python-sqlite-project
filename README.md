# SQLite database with Python3 3.9.x
This project was made for a university course.

# Project requirements

## Theoretical, design documentation

### Structure of the document
- [ ]   Introduction
- [ ]   ER model and transformation to relational model
- [ ]   Database implementation.
- [ ]   Discussion, reflection and conclusion. 

### Design requirements
- [ ]   ER model and database should have at least 6 entities
- [ ]   ER-model should have at least one M:N relationship
- [ ]   Needs to have an ER model as well as a relational model
- [ ]   Define minimum and maximum cardinalities and integrity constraints
- [ ]   At least five different queries or views need to be developed
- [ ]   Two JOIN-clauses need to be used in at least one query
- [ ]   The use of indices with justification

### Practical part
- [ ]   Python program has at least 5 queries, 1 insert, 1 update and 1 bokeh-visualization
- [ ]   Database can be tested and used through SQLite and Python user interface
- [ ]   Python program demonstrates how to read data, update existing or insert new data
- [ ]   Database implements integrity constraints with CASCADE and similar commands
- [ ]   Database has indices that are reasonable

#### Returnables
- [ ]   Report document (PDF)
- [ ]   Python program
- [ ]   SQLite database
- [ ]   Separate text file that includes the necessary SQL commands to create tables for the database (can be run with .read)
- [ ]   HTML file created by bokeh (if generated)
- [ ]   Video demonstration

#### Format
One ZIP or TAR file that includes:
- Report.pdf
- SQL queries.sql
- PythonDBProgram
    - Bokeh HTML
    - Premade SQLite database

## Possible problem areas in the project
- Problems in the modeling and using wrong models in the wrong phases
- Not having cardinalities in the model
- Not using integrity constraints (CASCADE, CHECK, etc.)
- Not using M:N relationship (or missing the query demonstrating it)
- Python program crashes during runtime
- Missing the SQL commands for creating the tables or they do not work when using .read-command