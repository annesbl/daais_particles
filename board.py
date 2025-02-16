import pygame




class Board:
    def __init__(self, width, height):   
        self.width = width   #stores the window width
        self.height = height    #stores the window height
        
        #initialize pygame and create the window
        pygame.init()   #initializes all pygame modules
        self.screen = pygame.display.set_mode((width, height))   #Creates a window with the specified size
        self.clock = pygame.time.Clock()   #Creates a clock object to manage the frame rate (FPS)

    
    def draw_particles(self, particles): 
        """
        Clears the screen and fills it with white before redrawing the particles
        """  
        self.screen.fill((255, 255, 255))  #fills the background with white
        
        #Loop through each particle and draw it on the screen
        for particle in particles:   #Iterates through the particles
            x, y = int(particle.position[0]), int(particle.position[1])   #Converts position to integer
            color = self.get_color_by_type(particle.particle_type)    #Gets color based on particle type
            pygame.draw.circle(self.screen, color, (x, y), 3)    #Draws the particle as a circle
                                                                 # - `self.screen`: Das Pygame-window
                                                                 # - `color`: color of circle.
                                                                 # - `(x, y)`:position of circle.
                                                                 # - `3`:  Radius in pixles.

        pygame.display.flip()   #Updates the window with the drawn particles
                                

    def update_display(self):   
        """
        Controls the speed of the simulation, limiting it to 60 frames per second
        """
        self.clock.tick(60)     #Keeps the frame rate at 60 FPS
        
    
    def get_color_by_type(self, particle_type):
        """
        Returns a color based on the particle's type for visual representation
        """
        colors = {
            "A": (255, 0, 0),  # Red
            "B": (0, 255, 0),  # Green
            "C": (0, 0, 255),  # Blue
            "D": (255, 255, 0)  # Yellow
        }
        return colors.get(particle_type, (255, 255, 255))  #Defaults to white if type not found

    
