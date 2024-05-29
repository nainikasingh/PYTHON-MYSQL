import mysql.connector
import pywhatkit
from datetime import datetime

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="****",
    password="****",
    database="my_database"
)
cursor = db.cursor()


def send_whatsapp_message(phone_number, message):
    # Use PyWhatKit to send message
    pywhatkit.sendwhatmsg(f"+{phone_number}", message, datetime.now().hour, datetime.now().minute + 1)


def fetch_contacts():
    # Fetch contacts from database
    cursor.execute("SELECT name, phone_number FROM whats_mess")
    whats_mess = cursor.fetchall()
    return whats_mess


def main():
    # Fetch contacts
    whats_mess = fetch_contacts()

    # Iterate over contacts and send messages
    for contact in whats_mess:
        name, phone_number = contact
        message = f"Hi {name}, this is a customized message for you!"
        send_whatsapp_message(phone_number, message)


if __name__ == "__main__":
    main()

# Close database connection
db.close()
