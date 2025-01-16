class Location():
"""
This class represents a location (room) with an ID, capacity, and availability status.
"""
    def __init__(self, room_id, capacity):
        self.room_id = room_id
        self.capacity = capacity
        self.available = True

    def __repr__(self) -> str:
        return f"{self.room_id} capacity: {self.capacity}"
