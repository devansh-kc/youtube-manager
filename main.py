def list_all_videos(vide):
    pass
def add_videos(video):
    pass
def update_video(video):
    pass

def delete_video(video):
    pass


video =[]
def main ():
        while True:
            print("/n youtube manager | choose an option")
            print("1. List all youtube video")
            print("2. update a youtube video detail")
            print("3. add a youtube video")
            print("4. Delete a youtube video")
            print("5. Exit the app")
            choice =input("enter your choice:")

            match choice:
                case "1":
                    list_all_videos(video)
                case "2":
                    update_video(video)
                case "3":
                    add_videos(video)
                case "4":
                    delete_video(video)    
                case "5":
                    break
                case _:
                    print("invalid choice")
