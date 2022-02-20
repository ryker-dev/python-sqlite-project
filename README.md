# SQLite database with Python3 3.9.x
This project was made for a university course.
## Usage
Download the source files and run _main.py_
```
git clone https://github.com/ryker-dev/python-sqlite-project.git
python .\PythonDBProgram\main.py
```

### Database
If no database exists, the Python application will initialise it for you.  
The database can also be created through the SQLite3 commandline tool using _.read_
```
.read "SQL queries.sql"
```

Database management can be done through the commandline tool or through the program.
# Project requirements

## Theoretical, design documentation

### Structure of the document
- [X]   Introduction
- [X]   ER model and transformation to relational model
- [X]   Database implementation.
- [X]   Discussion, reflection and conclusion. 

### Design requirements
- [X]   ER model and database should have at least 6 entities
- [X]   ER-model should have at least one M:N relationship
- [X]   Needs to have an ER model as well as a relational model
- [X]   Define minimum and maximum cardinalities and integrity constraints
- [X]   At least five different queries or views need to be developed
- [X]   Two JOIN-clauses need to be used in at least one query
- [X]   Justification and planning for the use of indices

### Practical part
- [X]   Python program has at least 5 queries, 1 insert, 1 update and 1 bokeh-visualization
- [X]   Database can be tested and used through SQLite and Python user interface
- [X]   Python program demonstrates how to read data, update existing or insert new data
- [X]   Database implements integrity constraints with CASCADE and similar commands
- [ ]   Database has indices **implemented** that are reasonable (Optional)

#### Returnables
- [X]   Report document (PDF)
- [X]   Python program
- [X]   SQLite database
- [X]   Separate text file that includes the necessary SQL commands to create tables for the database (can be run with .read)
- [X]   HTML file created by bokeh (if generated)
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