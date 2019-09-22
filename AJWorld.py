import UI
from Place import *
from Item import *
from Player import *

cabin_livingroom = Place(name='Cabin Living Room', description='In the main room of the log cabin, there is a lit fireplace that crackles as it gives off heat, and there are two chairs next to the fireplace.  You see your friend\'s dead body on the ground, and you are reminded of his gruesome death.', things_here=[Key(name='key', description='A simple worn metal key.', key_id='cabin_door')])

cabin_exterior = Place(name='Cabin Exterior', description='The ground around the cabin is muddy, but a gravel path leads to the front door of the cabin. To the west is a thick wall of trees.', door_north=Door(description='A worn front door to the log cabin.', key_id='cabin_door', locked=True))

cabin_bedroom1 = Place(name='Cabin Bedroom', description='The bedroom has a large bed with a drawer beside it.  A candle-lit table is at the end of the room.')
      
cabin_shed = Place(name='Shed', description='A simple wood shed with a variety of tools.', door_west=Door(description='A large, simple door to the shed.', key_id='cabin_door', locked=True), things_here=[Battery(name='battery', description='A small flashlight battery.', battery_id='flashlight'), Flashlight(name='flashlight', description='A small flashlight battery.', battery_id='flashlight'), Trimmer(name='trimmer', description='A metal trimmer for plants.', cut_id='vinewallcutter')])

cabin_bedroom2 = Place(name='Cabin Bedroom', description='The bedroom has a large bed and a table with a chair on it.  There is also a storage closet on the north wall of the room.', door_north=Door(description='A small closet door.', key_id='cabin_door', locked = True))

cabin_closet = Place(name='Closet', description='A small closet with space for items.', things_here=[Key(name='key', description='A small metal key that has \'mine\' engraved in it.', key_id='mineshaft_entrance')])

crossroads1=Place(name='Crossroads', description='A windy and secluded path with 4 directions to travel.')

dark_path=Place(name='Path', description='A normal path leading through a small forest. Something feels wrong with this path, but you can\'t seem to figure out what it is. The path gets darker and darker the deeper you go.')

dark_entrance=Place(name='Deep Forest', description='A somewhat dark and spooky forest. A very dark and speeky forest lies ahead, and you can\'t shake the feeling that you shouldn\'t be here. Strange noises are coming from the dark forest, and the entrance to the dark forest is blocked by a wall of vines.')

dark_forest1=Place(name='Dark Forest', description='In the dark forest, something seems wrong. You hear strange noises near you, but cannot identify the source. There are even some warning signs. You can hardly see, and you feel like you should\'t be here. Something or someone is shifting in the dark trees near you.', vinewall_east=Vinewall(description='A wall of vines blocking the entrance to the dark forest.', cut_id='vinewallcutter', cut=False), things_here=[Immovable(name='sign', description='Go back! Enter at your own risk!'), Immovable(name='warning', description='Warning! Beware of the witch!')])

witchhut_exterior=Place(name='Witch\'s Hut Exterior', description='In the middle of the dark forest is a witch\'s hut. It seems worn down, but the door is open. It sounds like something or someone is approching you from the forest.', things_here=[Immovable(name='sign', description='Do not enter! Trespassers will be punished!')])

witchhut_interior=Place(name='Witch\'s Hut Interior', description='Inside the hut is a variety of potions and books. You feel the need to leave as quickly as possible, as someone is coming; you can just tell.')

dark_forest2=Place(name='Dark Forest Edge', description='At the edge of the spooky dark forest, you can hear a strange whirring, but you can\'t locate the source. Since there is nothing here, you really want to go back and away from the dark forest.')

secret_passage1=Place(name='Dark Forest Clearing', description='You reach a light clearing to the dark forest. A trapdoor leads down and to the south.', door_south=Door(description='A trapdoor leading somewhere', key_id='mineshaft_passage', locked = True))

mine_secret_dark_forest=Place('Mine Chamber', description='You are in a lit room with a trapdoor leading up and to the north.')


cabin_exterior.north = cabin_livingroom
cabin_livingroom.west = cabin_bedroom1
cabin_shed.west = cabin_exterior
cabin_livingroom.east = cabin_bedroom2
cabin_bedroom2.north = cabin_closet
cabin_exterior.south = crossroads1
crossroads1.west = dark_path
dark_path.west = dark_entrance
dark_entrance.west = dark_forest1
dark_forest1.north = witchhut_exterior
witchhut_exterior.north = witchhut_interior
dark_forest1.west = dark_forest2
dark_forest1.south = secret_passage1
secret_passage1.south = mine_secret_dark_forest

def start_adventure(player):
    '''
    You should do any one-time prints here and set the initial location of
    the player. Suggested code is below.
    '''
    UI.println('You wake up feeling terrible. Your head is aching, and you are sitting against a wall with a broken window on it. You have multiple cuts and bruises on you, and you are very tired and injured. You see a man who you recognise to be your best friend laying on the ground with a pool of blood around him. To your horror, you realize that he is dead with a knife in his heart, and he too has multiple cuts and bruises on his body. The last thing you remember is your friend\'s horrified face as he fell to the ground, dying.')

    # this line is important if you want debugging to work
    player.world = globals()

    player.location = cabin_livingroom

    # set the breakout condition to when you want to end the game
    while True:
        player.location.on_enter(player)

    end_adventure(player)


def end_adventure(player):

    '''
    Called when the adventure is ended. Put any final messages you want here
    like credits.
    '''

if __name__ == '__main__':
    start_adventure(Player())
