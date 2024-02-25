import pygame

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

def main():
    
    # initialization
    screen = pygame.display.set_mode((500, 700))
    pygame.display.set_caption("Joystick example")

    clock = pygame.time.Clock()
    text_print = TextPrint()
    
    j = pygame.joystick.Joystick(0)
    joysticks = {}

    done = False
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

        for joystick in joysticks.values():
            
            # sets joystick buttons / axis to values
            
            jid = joystick.get_instance_id()
            guid = joystick.get_guid()
            
            a_lt = deadzone(joystick.get_axis(4) + 1)
            a_rt = deadzone(joystick.get_axis(5) + 1)
            b_lbumper = joystick.get_button(9)
            b_rbumper = joystick.get_button(10)
            
            a_leftx = deadzone(joystick.get_axis(0))
            a_lefty =  deadzone(joystick.get_axis(1) * -1)
            a_rightx = deadzone(joystick.get_axis(2))
            a_righty =  deadzone(joystick.get_axis(3) * -1)
            
            b_leftIn = joystick.get_button(7)
            b_rightIn = joystick.get_button(8)
                                    
            b_x = joystick.get_button(0)
            b_circle = joystick.get_button(1)
            b_square = joystick.get_button(2)
            b_triangle = joystick.get_button(3)
            
            b_padUp = joystick.get_button(11)
            b_padDown = joystick.get_button(12)
            b_padLeft = joystick.get_button(13)
            b_padRight = joystick.get_button(14)
            
            b_touchpad = joystick.get_button(15)
            
            # Print out the values
            
            text_print.tprint(screen, f"GUID: {guid}")
            
            text_print.tprint(screen, f"")
            
            text_print.tprint(screen, f"Left bumper: {b_lbumper}")
            text_print.tprint(screen, f"Right pumper: {b_rbumper}")
            text_print.tprint(screen, f"Left trigger: {a_lt}")
            text_print.tprint(screen, f"Right trigger: {a_rt}")
            
            text_print.tprint(screen, f"")
            
            text_print.tprint(screen, f"Left joystick in: {b_leftIn}")
            text_print.tprint(screen, f"Right joystick in: {b_rightIn}")
            
            text_print.tprint(screen, f"")
            
            text_print.tprint(screen, f"Left joystick x: {a_leftx}")
            text_print.tprint(screen, f"Right joystick y: {a_lefty}")
            text_print.tprint(screen, f"Right joystick x: {a_rightx}")
            text_print.tprint(screen, f"Right joystick y: {a_righty}")
            
            text_print.tprint(screen, f"")
            
            text_print.tprint(screen, f"X button: {b_x}")
            text_print.tprint(screen, f"Circle button: {b_circle}")
            text_print.tprint(screen, f"Square button: {b_square}")
            text_print.tprint(screen, f"Triangle button: {b_triangle}")
            
            text_print.tprint(screen, f"")
            
            text_print.tprint(screen, f"Up D-Pad: {b_padUp}")
            text_print.tprint(screen, f"Down D-Pad: {b_padDown}")
            text_print.tprint(screen, f"Left D-Pad: {b_padLeft}")
            text_print.tprint(screen, f"Right D-Pad: {b_padRight}")
            
            text_print.tprint(screen, f"")
            
            text_print.tprint(screen, f"Touchpad: {b_touchpad}")

        pygame.display.flip()

        clock.tick(30)

def deadzone(button):
    
    # applies deadzone and shortens to c_roundAxis number of decimal places
    
    if abs(button) < c_deadzone:
        return 0
    else:
        return round(button, c_roundAxis)

if __name__ == "__main__":
    main()
    pygame.quit()