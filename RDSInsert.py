import os
import psycopg2
import json

def lambda_handler(event, context):
    # Get environment variables for the database connection
    db_host = os.environ['DbHost']
    db_name = os.environ['DbName']
    db_user = os.environ['DbUser']
    db_password = str(os.environ['DbPassword'])
    db_port = os.environ['DbPort']

    # Extract data from the API Gateway event
    request_body = event['body']
    Jmeno = request_body['Jmeno']
    Prijmeni = request_body['Prijmeni']
    Email = request_body['Email']
    Telefon = request_body['Telefon']
    Intolerance = request_body['Intolerance']
    Vegetarian = request_body['Vegetarian']
    Alkohol = request_body['Alkohol']
    Nocovani = request_body['Nocovani']
    Tipy = request_body['Tipy']
    
    print("read")
    # Connect to the PostgreSQL database
    connection = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_user,
        password=db_password,
        port=db_port
    )
    print("Connected")
    
    try:
        # Create a cursor to execute SQL commands
        with connection.cursor() as cursor:
            # Define your SQL insert statement
            sql = """INSERT INTO "EJ"."Hoste" ("Jmeno", "Prijmeni", "Email", "Telefon", "Intolerance", "Vegetarian", "Alkohol", "Nocovani", "Tipy") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            data = (Jmeno, Prijmeni, Email, Telefon, Intolerance, Vegetarian, Alkohol, Nocovani, Tipy)
            
            # Execute the insert statement
            cursor.execute(sql, data)
        
        # Commit the transaction
        connection.commit()
        
        # Return a successful response
        return {
            'statusCode': 200,
            'body': json.dumps('Data inserted successfully!')
        }
    
    except Exception as e:
        # Return an error response if something goes wrong
        return {
            'statusCode': 500,
            'body': json.dumps('Error inserting data into the database: ' + str(e))
        }
    
    finally:
        # Close the database connection
        connection.close()
