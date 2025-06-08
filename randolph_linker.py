import sqlite3

conn = sqlite3.connect('randolph.db')

c = conn.cursor()
#c.execute("delete from sqlite_sequence where name='links'")  # Reset the auto-increment counter
# Create the links table if it doesn't exist
'''c.execute("""CREATE TABLE IF NOT EXISTS links (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        url TEXT NOT NULL
)""")'''

def add_link(name, url):
    c.execute(f"INSERT INTO links (name, url) VALUES (?, ?)", (name, url))
    conn.commit() 

def get_links():
    c.execute("SELECT * FROM links")
    for row in c.fetchall():
        print(f"id: {row[0]}, Name: {row[1]}, URL: {row[2]}")

def delete_link(name):
    c.execute("DELETE FROM links WHERE name = ?", (name,))
    conn.commit()

def reset_links():
    c.execute("delete from sqlite_sequence where name='links'") 
    conn.commit()

def edit_link(old_name, new_name, new_url):
    c.execute("UPDATE links SET name = ?, url = ? WHERE name = ?", (new_name, new_url, old_name))
    conn.commit()

def main():
    while True:
        print("\nOptions:")
        print("1. Add Link")
        print("2. View Links")
        print("3. Delete Link")
        print("4. Reset Links")
        print("5. Edit Link")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter link name: ")
            url = input("Enter link URL: ")
            add_link(name, url)
            print("Link added successfully.")
        elif choice == '2':
            get_links()
        elif choice == '3':
            name = input("Enter the name of the link to delete: ")
            delete_link(name)
            print("Link deleted successfully.")
        
        elif choice == '4':
            reset_links()
            print("Links reset successfully.")
        elif choice == '5':
            old_name = input("Enter the name of the link to edit: ")
            new_name = input("Enter the new name for the link: ")
            new_url = input("Enter the new URL for the link: ")
            edit_link(old_name, new_name, new_url)
            print("Link edited successfully.")  
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()

conn.close()

