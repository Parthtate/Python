import sqlite3

connection = sqlite3.connect('youtube_videos_db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
    )
''')

def list_all_videos():
    # cursor.execute() It hold result by default
    cursor.execute("SELECT * FROM videos")
    print("\n")
    print("*" * 40)
    for row in cursor.fetchall():
        print(f"ID: {row[0]}, name: {row[1]}, Duration: {row[2]}")
    print("*" * 40)


def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    connection.commit()
    print("\n Add video Successfully!")

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    connection.commit()
    print("\n Update video Successfully!")


def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    # , use because it store as a tuple multiple values
    connection.commit()
    print("\n Video Deleted")



def main():
    while True:
        print("\n Youtube Video Manager with DB | Choose your choice")
        print("1. List all videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit app")
        choice = input("Enter your option: ")

        if choice == '1':
            list_all_videos()
        elif choice == '2':
            name = input("Enter the video name: ")    
            time = input("Enter the video time: ")  
            add_video(name, time)  
        elif choice == '3':
            try:
                video_id = int(input("Enter the video ID to update: "))
            except ValueError:
                print("Invalid ID, Please enter number.")    
                continue
            name = input("Enter the video name: ")    
            time = input("Enter the video time: ")  
            update_video(video_id, name, time)  
        elif choice == '4':
            try: 
                video_id = int(input("Enter the video ID to be deleted: "))
            except ValueError:
                print("Invalid ID, Please enter number.")    
                continue
            delete_video(video_id)   
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid Choice, please try again!")        

    connection.close()        

if __name__ == "__main__":
    main()