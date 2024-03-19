import pygame
import socket
import pickle
import time

#host = "169.254.139.218"
host = "10.7.7.136"
#host = "localhost"
port = 5002

client = socket.socket()
client.connect((host, port))

pygame.init()

# constants
c_deadzone = 0.05
c_roundAxis = 4

# creates interface to print values
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 25)

    def tprint(self, screen, text):
        text_bitmap = self.font.render(text, True, (0, 0, 0))
        screen.blit(text_bitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10

def deadzone(button):
    
    # applies deadzone and shortens to c_roundAxis number of decimal places
    
    if abs(button) < c_deadzone:
        return 0
    else:
        return round(button, c_roundAxis)
    

def init():  
    # initialization
    screen = pygame.display.set_mode((500, 700))
    pygame.display.set_caption("Joystick example")

    clock = pygame.time.Clock()
    text_print = TextPrint()
    
    j = pygame.joystick.Joystick(0)
    joysticks = {}
    return joysticks, text_print, screen


def run(joysticks, text_print, screen):
    done = False
    optionsToggle = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.JOYDEVICEADDED:
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                print(f"Joystick {joy.get_instance_id()} connencted")

            if event.type == pygame.JOYDEVICEREMOVED:
                del joysticks[event.instance_id]
                print(f"Joystick {event.instance_id} disconnected")

        screen.fill((255, 255, 255))
        text_print.reset()
            
        # joystick 1 sets joystick buttons / axis to values

        if 0 in joysticks: 
            guid = joysticks[0].get_guid()
            
        a_lt1 = deadzone(joysticks[0].get_axis(4) + 1)
        a_rt1 = deadzone(joysticks[0].get_axis(5) + 1)
        b_lbumper1 = joysticks[0].get_button(9)
        b_rbumper1 = joysticks[0].get_button(10)
            
        a_leftx1 = deadzone(joysticks[0].get_axis(0))
        a_lefty1 =  deadzone(joysticks[0].get_axis(1) * -1)
        a_rightx1 = deadzone(joysticks[0].get_axis(2))
        a_righty1 =  deadzone(joysticks[0].get_axis(3) * -1)
            
        b_leftIn1 = joysticks[0].get_button(7)
        b_rightIn1 = joysticks[0].get_button(8)
                                    
        b_x1 = joysticks[0].get_button(0)
        b_circle1 = joysticks[0].get_button(1)
        b_square1 = joysticks[0].get_button(2)
        b_triangle1 = joysticks[0].get_button(3)
            
        b_padUp1 = joysticks[0].get_button(11)
        b_padDown1= joysticks[0].get_button(12)
        b_padLeft1 = joysticks[0].get_button(13)
        b_padRight1 = joysticks[0].get_button(14)
            
        b_touchpad1 = joysticks[0].get_button(15)
        optionsPress = joysticks[6].get_button(6)
        
        if (optionsPress == 1 and optionsToggle == False):
            optionsToggle = True;            
        text_print.tprint(screen, f"GUID: {guid}")
            
        text_print.tprint(screen, f"")
            
        text_print.tprint(screen, f"Left bumper: {b_lbumper1}")
        text_print.tprint(screen, f"Right pumper: {b_rbumper1}")
        text_print.tprint(screen, f"Left trigger: {a_lt1}")
        text_print.tprint(screen, f"Right trigger: {a_rt1}")
            
        text_print.tprint(screen, f"")
            
        text_print.tprint(screen, f"Left joystick in: {b_leftIn1}")
        text_print.tprint(screen, f"Right joystick in: {b_rightIn1}")
            
        text_print.tprint(screen, f"")
            
        text_print.tprint(screen, f"Left joystick x: {a_leftx1}")
        text_print.tprint(screen, f"Right joystick y: {a_lefty1}")
        text_print.tprint(screen, f"Right joystick x: {a_rightx1}")
        text_print.tprint(screen, f"Right joystick y: {a_righty1}")
            
        text_print.tprint(screen, f"")
            
        text_print.tprint(screen, f"X button: {b_x1}")
        text_print.tprint(screen, f"Circle button: {b_circle1}")
        text_print.tprint(screen, f"Square button: {b_square1}")
        text_print.tprint(screen, f"Triangle button: {b_triangle1}")
            
        text_print.tprint(screen, f"")
            
        text_print.tprint(screen, f"Up D-Pad: {b_padUp1}")
        text_print.tprint(screen, f"Down D-Pad: {b_padDown1}")
        text_print.tprint(screen, f"Left D-Pad: {b_padLeft1}")
        text_print.tprint(screen, f"Right D-Pad: {b_padRight1}")
            
        text_print.tprint(screen, f"")
            
        text_print.tprint(screen, f"Touchpad: {b_touchpad1}")
        
        text_print.tprint(screen, f"GUID: {guid}")
        text_print.tprint(screen, f"")
        text_print.tprint(screen, f"OptionsPress: {optionsPress}")
        text_print.tprint(screen, f"OptionsToggle: {optionsToggle}")
        text_print.tprint(screen, f"")


        pygame.display.flip()

        #send variables over socket

        joystick_data = [a_lt1, a_rt1, b_lbumper1, b_rbumper1, a_leftx1, a_lefty1, a_rightx1, a_righty1, b_leftIn1, b_rightIn1, b_x1, b_circle1, b_square1, b_triangle1, b_padUp1, b_padDown1, b_padLeft1, b_padRight1]
        data_enc = pickle.dumps(joystick_data)
        client.send(data_enc)
        time.sleep(0.02)

    client.close()

def main():
    joysticks, textprint, screen = init()
    run(joysticks, textprint, screen)
    pygame.quit()


if __name__ == "__main__":
    main()
