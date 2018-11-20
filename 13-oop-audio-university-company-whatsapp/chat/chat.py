#%%

class Room: 
    

    def __init__(self, name):
        self.name = name
        self.users = []
    
    def accept(self, user): 
        self.users.append(user)
        
    def boradcast(self, message): 
        for user in self.users:
            user.receive_notification(message)

class User: 
    
    
    def __init__(self, name): 
        self.name = name 
        
    def join_room(self, room):
        room.accept(self)
        
    def send_message(self, room, message): 
        room.broadcast(message)
    
    def receive_notification(self, room_name, message): 
        print.self.name + "receiver: " + message
        
        
        
        
