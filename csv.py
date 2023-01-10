import psycopg2
conn = psyvopg2.connect("host=localhost dbname=postgres user=postgres")

db_table_name = "sample_db"
csv_file_name = "sample_file_pass"

def insert_data(self, conn, csv_file_name, db_table_name):
    #insert data from the csv file into db table
    # Using BULK INSERT query. Skip the csv Headers
    
    qry = "BULK INSERT" + db_table_name + "FROM" + csv_file_name+ " WITH(FORMAT = 'CSV', FIRSTROW = 2)"

    # Execute query
    cursor = conn.cursor()
    success = cursor.execute(qry)
    conn.commit()
    cursor.close
    
# calling function
insert_data(conn,csv_file_name,db_table_name)
    
