import sqlite3

import sqlite3

sqlite_file = 'site.db'    # name of the sqlite database file
table_name = 'Tests'   # name of the table to be created
id_column = 'id' # name of the PRIMARY KEY column
new_column1 = 'hint'  # name of the new column
column_type = 'TEXT' # E.g., INTEGER, TEXT, NULL, REAL, BLOB
default_val = 'Hello World' # a default value for the new column rows

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# A) Adding a new column without a row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column1, ct=column_type))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()