
from Place import Place, Door
from Item import *
from Container import Container

intro_text = 'You wake up feeling terrible. Your head is aching, and you are sitting against a wall with a broken window on it. You have multiple cuts and bruises on you, and you are very tired and injured. You see a man who you recognise to be your best friend laying on the ground with a pool of blood around him. To your horror, you realize that he is dead with a knife in his heart, and he too has multiple cuts and bruises on his body. The last thing you remember is your friend\'s horrified face as he fell to the ground, dying.'

cabin_exterior = Place('Cabin Exterior', 'The ground around the cabin is muddy, but a gravel path leads to the front door of the cabin.', door_north=Door(description='A worn front door to the log cabin.', key_id='cabin_door', locked=True))
cabin_livingroom = Place(name='Cabin Living Room',
                         description='In the main room of the log cabin, there is a lit fireplace that crackles as it gives off heat, and there are two chairs next to the fireplace.  You see your friend\'s dead body on the ground, and you are reminded of his gruesome death.', 
                         things_here=[Key(name='key', description='A simple worn metal key.', key_id='cabin_door')])
cabin_bedroom = Place(name='Cabin Bedroom', description='The bedroom has two beds with a drawer between them.  A candle-lit table with book on it lies at the end of the room')
cabin_shed = Place(name='Shed', description='A simple wood shed with a variety of tools.', door_west=Door(description='A large simple door to the shed.', key_id='cabin_door', locked=True), things_here=[Battery(name='battery', description='A small flashlight battery.', battery_id='flashlight'), Flashlight(name='flashlight', description='A small flashlight battery.', battery_id='flashlight')])

cabin_exterior.north = cabin_livingroom
cabin_livingroom.west = cabin_bedroom
cabin_shed.west = cabin_exterior

initial_location = cabin_livingroom