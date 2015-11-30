import ibm_db

# This example assumes you have already run db2sampl. We are querying a table
# from the sample database as an example.

# replace <host> with your hostname
# replace <user> with your username
# replace <pass> with your password
ibm_db_conn = ibm_db.connect('DATABASE=sample;HOSTNAME=<host>;PROTOCOL=TCPIP;PORT=50000;UID=<user>;PWD=<pass>', '', '')

# This example queries the emp table from the sample database
result = ibm_db.exec_immediate(ibm_db_conn, 'select * from emp')

# the fetch_assoc returns a dictionary, with the key's being the result columns
# and the values being the values of each row
row = ibm_db.fetch_assoc(result)
while row:
    print row
    row = ibm_db.fetch_assoc(result)

# finally, always close the connection.
ibm_db.close(ibm_db_conn)
