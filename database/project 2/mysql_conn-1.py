import mysql.connector

myquery = "SELECT r.ramName, mb.motherboardName, cpu.cpuName FROM ram r JOIN ram_motherboard_junction rmj ON r.TypeId = rmj.TypeId JOIN motherboard mb ON mb.motherboardId = rmj.motherboardId JOIN cpu_socket_type_junction cstj ON mb.motherboardId = cstj.motherboardId JOIN central_Processing_Unit cpu ON cpu.cpuId = cstj.TypeId JOIN ram_speed_junction rsj ON r.TypeId = rsj.TypeId WHERE r.TypeId = (SELECT TypeId FROM ram_Speed_Type WHERE TypeName = 'DDR4-3200') AND cpu.cpuId = rsj.cpuId;"

try:
    cnx = mysql.connector.connect(user='<yourusername>', password='<yourpassword>',
    host='127.0.0.1',database='project1')

    # Prepare a cursor object using cursor() method
    cursor = cnx.cursor ()

    # Execute the SQL query using execute() method.
    cursor.execute (myquery)

    # Fetch all rows
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
except mysql.connector.Error as e:
    print (e)

finally:

    # Close the cursor object
    cursor.close ()

    # Close the connection
    cnx.close ()
