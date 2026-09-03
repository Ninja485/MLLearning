"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes:
        (class) total_aliens_created (int): Total number of Alien instances.
        x_coordinate (int): Position on the x-axis.
        y_coordinate (int): Position on the y-axis.
        health (int): Number of health points.

    Methods:
        hit(): Decrement Alien health by one point.
        is_alive(): Return a boolean for if Alien is alive (if health is > 0).
        teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
        collision_detection(other): Implementation TBD.

    """
    total_aliens_created = 0
    def __init__(self,x_coord,y_coord):
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1
        
    def is_alive(self):
        return self.health > 0
        
    def teleport(self,new_x_coord,new_y_coord):
        self.x_coordinate = new_x_coord
        self.y_coordinate = new_y_coord
        
    def collision_detection(self,other_object):
        pass
    
#TODO (Student): Create the new_aliens_collection() function below to call your Alien class with a list of coordinates

def new_aliens_collection(alien_start_positions):
    aliens_list = []
    for location in alien_start_positions:
        alien = Alien(location[0],location[1])
        aliens_list.append(alien)
    return aliens_list