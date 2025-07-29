# 1 import the random module
import random as rd
# 2 creating subjects
Subjects = [
            "Shahruk khan",
            "Virat Kholi",
            "Salman Khan",
            "A Mubai Cat",
            "Auto Ricshaw DRiver from lahore"
            ,"Modi Gi"
            ,"Nawaz Shahrif",
            "Jon"
        ]
Actions =[
          "Launches",
          "Cancels",
          "Eats",
          "Dance With",
          "Orders",
          "Celebrates",
          "Declear War on",
          "jumping",
          "Sleeping"
          ,"riding",
          "running"
        ]
Places_or_Things =[
                   "in Mubai local Train",
                   "a Plote of Samosa",
                   "During ipl",
                   "At india Gate"
                   ,"At Gangna Ghat",
                   "At Lahore ",
                   "At Orangi Town",
                   "At Russia"
                ] 
# 3 Start headline generator
while True:
    subject = rd.choice(Subjects)
    action = rd.choice(Actions)
    place_or_thing = rd.choice(Places_or_Things)
    
    Headline = f"BREAKING NEWS:  {subject} {action} {place_or_thing}"
    print("\n" + Headline)
    
    User_input = input("Do you want to another Headline (Yes OR No)?").strip() 
    if User_input == "No":
        break
    
print("\n Thank you For  Using a fake Headline Genarator. Have a fun Day")  