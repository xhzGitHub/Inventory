# Set shanghai timezone 
timezone "Asia/shanghai"

# MySQL “incorrect string value” error when save unicode string in Django
If it's a new project, I'd just drop the database, and create a new one with a proper charset:

    CREATE DATABASE <dbname> CHARACTER SET utf8;

<https://stackoverflow.com/questions/2108824/mysql-incorrect-string-value-error-when-save-unicode-string-in-django>
