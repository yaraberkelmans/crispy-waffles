from loading_data import Load_init_lists

class Location():
    def __init__(self, room_id, capacity):
        self.room_id = room_id
        self.capacity= capacity
        self.available = True
