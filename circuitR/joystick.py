from kmk.keys import AX
from kmk.modules import Module

import digitalio
from analogio import AnalogIn

def get_voltage(pin):
        
        return (pin.value * 16) / 65536
    
class JOYstick(Module):
    
    
    def __init__(self, x, y):
        self.x_pin = AnalogIn(x)
        self.y_pin = AnalogIn(y)
        

        
    def during_bootup(self, keyboard):
        return

    def before_matrix_scan(self, keyboard):
        x=get_voltage(self.x_pin)
        y=get_voltage(self.y_pin)
        x_value=int(x)-8
        y_value=int(y)-7
        
        if abs(x_value)>2 :
            #print('Delta: ', x_value, ' ', y_value)
            AX.X.move(keyboard, x_value)
        if abs(y_value)>2 :
            #print('Delta: ', x_value, ' ', y_value)
            AX.Y.move(keyboard, y_value)
        #print('Delta: ', x_value, ' ', y_value)
        
    def after_matrix_scan(self, keyboard):
        return

    def before_hid_send(self, keyboard):
        return

    def after_hid_send(self, keyboard):
        return

    def on_powersave_enable(self, keyboard):
        return

    def on_powersave_disable(self, keyboard):
        return