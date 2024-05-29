import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDialog, QHBoxLayout
import mysql.connector

class AddContactDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Contact")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.phone_label = QLabel("Phone Number:")
        self.phone_entry = QLineEdit()
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_entry)

        self.name_label = QLabel("Name (optional):")
        self.name_entry = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_entry)

        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_contact)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def add_contact(self):
        phone_number = self.phone_entry.text().strip()
        name = self.name_entry.text().strip()

        if not phone_number:
            print("Please enter a phone number.")
            return

        # Connect to MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="3693",
            database="my_database"
        )
        cursor = db.cursor()

        # Insert data into the database
        insert_query = "INSERT INTO whats_mess (name, phone_number) VALUES (%s, %s)"
        cursor.execute(insert_query, (name, phone_number))
        db.commit()

        db.close()
        self.phone_entry.clear()
        self.name_entry.clear()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WhatsApp Message Sender")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.add_contact_button = QPushButton("Add Contact")
        self.add_contact_button.clicked.connect(self.open_add_contact_dialog)
        layout.addWidget(self.add_contact_button)

        self.new_contacts_over_button = QPushButton("New Contacts Over")
        self.new_contacts_over_button.clicked.connect(self.enable_send_button)
        layout.addWidget(self.new_contacts_over_button)

        self.send_message_button = QPushButton("SEND MESSAGE NOW")
        self.send_message_button.setEnabled(False)
        self.send_message_button.clicked.connect(self.send_messages)
        layout.addWidget(self.send_message_button)

        self.setLayout(layout)

    def open_add_contact_dialog(self):
        dialog = AddContactDialog()
        dialog.exec_()

    def enable_send_button(self):
        self.send_message_button.setEnabled(True)
        self.add_contact_button.setEnabled(False)

    def send_messages(self):
        # Connect to MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="3693",
            database="my_database"
        )
        cursor = db.cursor()

        # Fetch contacts from the database
        cursor.execute("SELECT name, phone_number FROM whats_mess")
        contacts = cursor.fetchall()

        # Print contacts for debugging purposes
        print("Contacts in the database:")
        for contact in contacts:
            print(contact)

        db.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
