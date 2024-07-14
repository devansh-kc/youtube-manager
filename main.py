# import json

# file = "youtubeData.txt"

# def list_all_videos(video):
#     for index, vid in enumerate(video,start=1):
#         print("\n")
#         print("*"*70)
#         print(f"  index : { index}  NAME: { vid["name"]} duration {vid["time"]}")
#     print("*"*70)
        

    
    
# def add_videos(video):
#     name = input("enter the video name:\t")
#     time = input("enter the video time:\t")
#     video.append({"name":name,"time":time})
#     save_data_helper(video)
# def update_video(video):
#     list_all_videos(video)
#     index = int(input("Enter the video number to update the video:\t"))
#     if 1<= index <=len(video):
#         name = input("Enter the new Video name:\t")
#         time = input("Enter the new Video duration:\t")
#         video[index-1] = {"name":name ,"time":time}  
#         save_data_helper(video)
#     else: print("invalid index selected")
    
# def delete_video(video):
#     list_all_videos(video)
#     index = int(input("Enter the video number to delete the video"))
#     if 1<= index <=len(video):
#         del video[index-1]
#         save_data_helper(video)
#     else: print("invalid index selected")



# def load_data():
#     try:
        
#         with open("youtube.txt","r") as file:
#             tepe= json.load(file)
#             print(type(tepe))
#             return tepe
        

#     except FileNotFoundError:
#             return []


# def save_data_helper(videos):
#     with open( "youtube.txt","w")as file:
#         return json.dump(videos,file)





# def main ():
#     videos = load_data()
#     while True:
#         print("/n youtube manager | choose an option")
#         print("1. List all youtube video:\t")
#         print("2. update a youtube video detail:\t")
#         print("3. add a youtube video:\t")
#         print("4. Delete a youtube video:\t")
#         print("5. Exit the app:\t")
#         choice =input("enter your choice:\t")
#         print( videos)

#         match choice:
#             case "1":
#                 list_all_videos(videos)
#             case "2":
#                 update_video(videos)
#             case "3":
#                 add_videos(videos)
#             case "4":
#                 delete_video(videos)    
#             case "5":
#                 break
#             case _:
#                 print("invalid choice")



# if __name__ == "__main__":
#     main()
    
    
    

# SQLITE#

import sqlite3

connection =  sqlite3.connect("youtube_video.db")
cursor = connection.cursor()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos(
                   id INTEGER PRIMARY KEY ,
                   name TEXT NOT NULL ,
                   time TEXT NOT NULL 
    )''')

def main():
    def list_video():
        cursor.execute("SELECT * FROM videos")
        
        for row in cursor.fetchall():
            if(row != None):
                print(row)
            else:
                return []
    def add_video(name,time):
        cursor.execute("INSERT INTO videos(name,time) VALUES(?,?)", (name, time))
        connection.commit()
    def update_video(new_name, new_time,id):
        
        cursor.execute("UPDATE videos SET name=?,time=? WHERE id = ?",( new_name, new_time,id))
        connection.commit()
    def delete_video(video_id):
        cursor.execute("DELETE FROM videos where id=? ",(video_id,))
        connection.commit()
    while True:
        print("/n youtube manager | choose an option")
        print("1. List all youtube video:\t")
        print("2. add a youtube video:\t")
        print("3. update a youtube video detail:\t")
        print("4. Delete a youtube video:\t")
        print("5. Exit the app:\t")
        choice =input("enter your choice:\t")
        if choice =="1":
            list_video()
        elif choice =="2":
            name = input("enter the video name:\t")
            time =  input("enter the duration:\t")
            add_video(name,time)
        elif choice=="3":
            list_video()
            id  = input("enter the id of the video which you want to update:\n")

            video_name  = input("enter the name of the video which you want to update:\n")
            time = input("enter the duration of the video which you want to update:\n")

            update_video(video_name,time, id)
        elif choice=="4":
            list_video()
            id  = input("enter the ID  of the video which you want to delete:\n")

            delete_video(id)
        elif choice =="5":
            exit()
        else: print("you have entered an invalid input. Please try again ")
    connection.close()
            
            
        

if __name__ =="__main__":
    main() 