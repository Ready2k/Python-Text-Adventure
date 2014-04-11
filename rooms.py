import main


def room1():
    possible_loot = True
    if main.monster_chance():
        main.random_monster()
        print """
The room is dimly lit by clumps of luminescent fungi growing in the cracks of
the stone walls."""
    else:
        print """
You open the door to a room dimly lit by clumps of luminescent fungi growing
in the cracks of the stone walls."""
    while True:
        if main.player.player_class == 'mage':
            choice = raw_input("\n[Search] | [Inventory] | [Spells] | [Status] | [Rest] | [Proceed] > ").lower()
        else:
            choice = raw_input("\n[Search] | [Inventory] | [Status] | [Rest] | [Proceed] > ").lower()
        if choice == "search":
            print """
You spot a pile of skeletal remains in the room's far corner.  As you approach
the pile it becomes clear the remains belonged to an orc clan, presumably
living somewhere in the mine.  The bodies were piled carelessly and much of
their clothing looks relatively intact."""
            search = raw_input("\nSearch the remains? > ").lower()
            if search == "yes":
                if possible_loot:
                    if main.loot_chance():
                        print "You sift through the remains and uncover some treasure!"
                        main.loot()
                        possible_loot = False
                        continue
                    else:
                        raw_input("You find nothing of value amongst the remains. > ")
                        continue
                else:
                    raw_input("You find nothing of value amongst the remains. > ")
                    continue
        elif choice == "inventory":
            main.player.inv()
            continue
        elif choice == "spells":
            main.player.spells(main.goblin)
            continue
        elif choice == "status":
            main.player.status()
            continue
        elif choice == "rest":
            main.player.back = False
            main.player.rest()
            if main.player.back:
                continue
        elif choice == "proceed":
            break
    print """
You are faced with two paths, a rusted [iron] door directly ahead and a simple
copper door down a [hallway] to your left."""
    while True:
        choice = raw_input('\nWhich do you choose? > ')
        if choice == "iron":
            if main.player.player_class == "thief":
                raw_input("The door is locked!  Attempt to unlock? > ")
                raw_input("You successfully unlock the door!")
                main.player.xp += 3
                raw_input("\nYou gain 3 experience!")
                main.room_selector()
            else:
                raw_input("The door is locked!")
        elif choice == "hallway":
            main.room_selector()
        else:
            print "\nChoose a door to continue."
            continue


def room2():
    possible_loot = True
    #if main.monster_chance():
    #    main.random_monster()
    print """
You have entered a large open chamber.  Iron tracks lead down three separate
tunnels, each blocked by a hastily constructed door.  A distant mechanical
CLANK momentarily disturbs the total silence."""
    while True:
        if main.player.player_class == 'mage':
            choice = raw_input("\n[Search] | [Inventory] | [Spells] | [Status] | [Rest] | [Proceed] > ").lower()
        else:
            choice = raw_input("\n[Search] | [Inventory] | [Status] | [Rest] | [Proceed] > ").lower()
        if choice == "search":
            print "\nYou see many orphaned mine carts along the tracks."
            search = raw_input("\nSearch the mine carts? > ").lower()
            if search == "yes":
                if possible_loot:
                    if main.loot_chance():
                        raw_input("You scour each mine cart, at last discovering some "
                                  "treasure!")
                        main.loot()
                        possible_loot = False
                        continue
                    else:
                        raw_input("You find only ore dust and ruined mining "
                                  "equipment. > ")
                        continue
                else:
                    raw_input("You find only ore dust and ruined mining "
                              "equipment. > ")
                    continue
        elif choice == "inventory":
            main.player.inv()
            continue
        elif choice == "spells":
            main.player.spells(main.goblin)
            continue
        elif choice == "status":
            main.player.status()
            continue
        elif choice == "rest":
            main.player.back = False
            main.player.rest()
            if main.player.back:
                continue
        elif choice == "proceed":
            break
    print """
There are three doors at the end of three tunnels ahead of you. One to the
[east], one to the [west], and one that continues to the [south]."""
    while True:
        choice = raw_input('\nWhich do you choose? > ')
        if choice == "west":
            if main.player.player_class == "thief":
                raw_input("The door is locked!  Attempt to unlock? > ")
                raw_input("You successfully unlock the door!")
                main.player.xp += 3
                raw_input("\nYou gain 3 experience!")
                main.room_selector()
            else:
                raw_input("The door is locked!")
        elif choice == "east" or choice == "south":
            shop_room()
        else:
            print "\nChoose a door to continue."
            continue


def room3():
    possible_loot = True
    if main.monster_chance():
        main.random_monster()
    print """
You find yourself in a short hallway connected to a large open chamber.  The
chamber itself is shaped like a great stone bowl, and as you approach the end
of the hallway you can see the floor down a thirty foot stairway below.  At
the center of the bowl is an ancient looking tree reaching nearly forty feet
upwards to meet the ceiling.  The tree is seemingly giving off its own curious
light, dimly illuminating the room.  On the other side of the great bowl are
two stairways leading to two more doors."""
    while True:
        if main.player.player_class == 'mage':
            choice = raw_input("\n[Search] | [Inventory] | [Spells] | [Status] | [Rest] | [Proceed] > ").lower()
        else:
            choice = raw_input("\n[Search] | [Inventory] | [Status] | [Rest] | [Proceed] > ").lower()
        if choice == "search":
            print """
You notice several pillars lining the upper-level of the bowl.  Many of these
pillars look to have some portion of their stonework hollowed out and a few
seem to contain various items hidden within."""
            search = raw_input("\nSearch the stone pillars? > ").lower()
            if search == "yes":
                if possible_loot:
                    if main.loot_chance():
                        raw_input("You comb through the hollow pillars,"
                                  " finally discovering some treasure! > ")
                        main.loot()
                        possible_loot = False
                        continue
                    else:
                        raw_input("You find only bits of stone and ruined "
                                  "paper. > ")
                        continue
                else:
                    raw_input("You find only bits of stone and ruined "
                              "paper. > ")
                    possible_loot = False
                    continue
        elif choice == "inventory":
            main.player.inv()
            continue
        elif choice == "spells":
            main.player.spells(main.goblin)
            continue
        elif choice == "status":
            main.player.status()
            continue
        elif choice == "rest":
            main.player.back = False
            main.player.rest()
            if main.player.back:
                continue
        elif choice == "proceed":
            break
    print"""
As you make your way down the many steps ahead you are suddenly aware of a
low hum, gradually increasing in volume to eventually reverberate across the
entire chamber and become a powerful roar of vibration."""
    raw_input("\nYou involuntarily clasp your hands to your ears. > ")
    print """
In an instant the clamor dissipates, returning the chamber to utter silence.
As you regain your composure you are addressed by a voice in the darkness."""
    raw_input('\n"Traveler...what purpose have you in this place?" > ')
    while True:
        choice1 = raw_input('''
[Who] are you?"
To [destroy] the evil within this mine."
To [plunder] the mine's lost treasures." > ''').lower()
        if choice1 == "who":
            raw_input("""
As the words leave your mouth the ancient tree before you vibrates softly.
Two large yellow eyes materialize in the bark and fix themselves upon
you. > """)
            print'''
"I have no name, and your kind has no words for my being. My very existence is
beyond anything in your experience - you can never fully understand my true
essence.  Be content to perceive me as your kind often does, simply as a
benevolent nature spirit."'''
            while True:
                choice2 = raw_input('''
[What] do you want?"
"You're a [talking] tree!" > ''').lower()
                if choice2 == "what":
                    raw_input('''
"My influence has been usurped by a nefarious  sorcerer seeking to enter the
upper planes by way of my own deep connection with them.  It is this
corruption that is responsible for the evil recently pouring forth from this
mine. Find the sorcerer deeper in the mines and destroy him." > ''')
                    raw_input('''
"If you refuse to help or fail in this task my connection with the planes will
be severed and I will slowly wither into nonexistence.  The evil lurking in
this region will gradually increase in ferocity and your civilization will be
overrun.  However, the higher order of the universe is not concerned with such
trivial matters, so your choice is ultimately meaningless.
\nI leave you now." > ''')
                    raw_input("""
The large yellow eyes disappear and the ancient tree gradually ceases its
vibration. The room is returned to stillness once more. > """)
                    break
                elif choice2 == "talking":
                    raw_input('''
"Yes.  I can see your intellect is not evolved enough to truly comprehend my
plight.  Our interaction will not be fruitful.  I leave you now to your
simplistic awe." > ''')
                    raw_input("""
The large yellow eyes disappear and the ancient tree gradually ceases its
vibration. The room is returned to stillness once more. > """)
                    break
                else:
                    print "\nChoose an option to continue."
                    continue
        elif choice1 == "destroy":
            raw_input("""
As the words leave your mouth the ancient tree before you vibrates softly.
Two large yellow eyes materialize in the bark and fix themselves upon you. > """)
            raw_input('''
"You are near the end of that particular quest, traveler. I am known to your
kind as a benevolent spirit.  My influence has been usurped by a nefarious
sorcerer seeking to enter the upper planes by way of my own deep connection
with them.  It is this corruption that is responsible for the evil recently
pouring forth from this mine. Find the sorcerer deeper in the mines and
destroy him." > ''')
            raw_input('''
"If you refuse to help or fail in this task my connection with the planes will
be severed and I will slowly wither into nonexistence.  The evil lurking in
this region will gradually increase in ferocity and your civilization will be
overrun.  However, the higher order of the universe is not concerned with such
trivial matters so your choice is ultimately meaningless.
I will leave you now." > ''')
            raw_input("""
The large yellow eyes disappear and the ancient tree gradually ceases its
vibration. The room is returned to stillness once more. > """)
            break
        elif choice1 == "plunder":
            raw_input("""
As the words leave your mouth the ancient tree before you vibrates softly.
Two large yellow eyes materialize in the bark and fix themselves upon you. > """)
            raw_input('''
"Simple creature!  Concerned only with earthly wealth and materials!  You are
no true champion.  Seek your plunder, mortal, your nonexistence draws near." > ''')
            raw_input("""
The large yellow eyes disappear and the ancient tree gradually ceases its
vibration. The room is returned to stillness once more. > """)
            break
        else:
            print '\nChoose an option to continue.'
            continue
        break
    print """
Ahead of you lie two stone stairways winding up the sides of the bowl
structure.  At their termination are two doors: one a dark [blue] color and
the other a soft [green]."""
    while True:
        choice3 = raw_input("\nWhich do you choose? > ").lower()
        if choice3 == "blue" or choice3 == "green":
            main.room_selector()
        else:
            print "\nChoose a door to continue"
            continue


def room4():
    if main.monster_chance():
        main.random_monster()
    print """
You find yourself in a dark and cluttered room.  The faint sound of dripping
water echoes in the darkness."""
    while True:
        if main.player.player_class == 'mage':
            choice = raw_input("\n[Search] | [Inventory] | [Spells] | [Status] | [Rest] | [Proceed] > ").lower()
        else:
            choice = raw_input("\n[Search] | [Inventory] | [Status] | [Rest] | [Proceed] > ").lower()
        if choice == "search":
            print """
You can see mundane mining tools in various stages of disrepair throughout
this large room.  Despite your best efforts you are unable to find anything
of value amongst them. """
        elif choice == "inventory":
            main.player.inv()
            continue
        elif choice == 'spells':
            main.player.spells(main.goblin)
            continue
        elif choice == "status":
            main.player.status()
            continue
        elif choice == "rest":
            main.player.back = False
            main.player.rest()
            if main.player.back:
                continue
        elif choice == "proceed":
            break
    print '''
The way forward is marked by two doors.  One made of [steel] and one of
[wood].'''
    while True:
        choice = raw_input('\nWhich do you choose? > ')
        if choice == "steel" or choice == "wood":
            main.room_selector()
        else:
            print "\nChoose a door to continue."
            continue


def shop_room():
    raw_input('''
You open the door and are greeted by a most curious sight.  A small goblin
sits behind a dusty wooden counter, his height extended by the stack of ancient
tomes serving as his chair.  Behind him are many rows of shelves containing
various weapons, armor, and items. > ''')
    raw_input('''
The goblin recognizes your surprise and is quick to address your fears. > ''')
    raw_input('''
"Woah there, human!  Stay your blade - I am not like my small minded brethren
you have no doubt encountered on your journey here.  I am but a simple merchant.
I seek only trade and riches, I have no desire to maim and kill. Sneezlebrixx
is my name.  Please, have a look at my wares!" > ''')
    while True:
        if main.player.player_class == 'mage':
            choice = raw_input("\n[Search] | [Shop] | [Inventory] | [Spells]"
                               " | [Status] | [Rest] | [Proceed] > ").lower()
        else:
            choice = raw_input("\n[Search] | [Shop] | [Inventory] | [Status]"
                               " | [Rest] | [Proceed] > ").lower()
        if choice == "search":
            print '''
The room is damp and dimly-lit, and the walls are all made of cold stone.
Sneezlebrixx's shop looks fairly well maintained, however, and many of the
items on display look to be in excellent condition.'''
        elif choice == 'shop':
            shop()
            continue
        elif choice == "inventory":
            main.player.inv()
            continue
        elif choice == 'spells':
            main.player.spells(main.goblin)
            continue
        elif choice == "status":
            main.player.status()
            continue
        elif choice == "rest":
            main.player.back = False
            main.player.rest()
            if main.player.back:
                continue
        elif choice == "proceed":
            break
    raw_input('''
Sneezlebrixx shows you to the shop's exit: a squat wooden door clearly
designed for smaller creatures such as kobolds or halflings.  The goblin
waves as you bend down to open the tiny door. > ''')
    main.room_selector()
def shop():
    print '\n"What would you like to see, human?"'
    while True:
        item_type = raw_input('\n[Weapons] | [Armor] | [Items] | [Magic] Items'
                              ' | [Back] > ').lower()
        if item_type == 'back':
            break
        elif item_type == 'weapons':
            print '\nWeapons:'
            for i in main.weapons:
                print main.weapons.index(i), i.name
            while True:
                choice = raw_input('\nInspect an item with its number or [Back] > ')
                if choice == 'back':
                    break
                else:
                    print '\n', main.weapons[int(choice)].name.title()
                    print 'Attack: %d \t AC Penalty: %d' % \
                          (main.weapons[int(choice)].attack,
                           main.weapons[int(choice)].ac_penalty)
                    print 'Price: %d gold' % main.weapons[int(choice)].price
                    while True:
                        confirm = raw_input('\n[Buy] | [Back] > ').lower()
                        if confirm == 'back':
                            break
                        elif confirm == 'buy':
                            if main.player.gold < main.weapons[int(choice)].price:
                                print 'You don\'t have enough gold!'
                            else:
                                main.player.gold -= main.weapons[int(choice)].price
                                main.player.equipment.append(main.weapons[int(choice)])
                                raw_input('\nYou have purchased the %s!' %
                                          main.weapons[int(choice)].name)
                                break
                    break
        elif item_type == 'armor':
            print '\nArmor:'
            for i in main.armor:
                print main.armor.index(i), i.name
            while True:
                choice = raw_input('\nInspect an item with its number or [Back] > ')
                if choice == 'back':
                    break
                else:
                    print '\n', main.armor[int(choice)].name.title()
                    print 'Defense: %d' % main.armor[int(choice)].defense
                    print 'Price: %d gold' % main.armor[int(choice)].price
                    while True:
                        confirm = raw_input('\n[Buy] | [Back] > ').lower()
                        if confirm == 'back':
                            break
                        elif confirm == 'buy':
                            if main.player.gold < main.armor[int(choice)].price:
                                print 'You don\'t have enough gold!'
                            else:
                                main.player.gold -= main.armor[int(choice)].price
                                main.player.equipment.append(main.armor[int(choice)])
                                raw_input('\nYou have purchased the %s!' %
                                          main.armor[int(choice)].name)
                                break
                    break
        elif item_type == 'items':
            print '\nItems:'
            for i in main.items:
                print main.items.index(i), i.name
            while True:
                choice = raw_input('\nInspect an item with its number or [Back] > ')
                if choice == 'back':
                    break
                else:
                    print '\n', main.items[int(choice)].name.title()
                    print 'HP Bonus: %d' % main.items[int(choice)].plus_hp, \
                          '\t', 'MP Bonus: %d' % main.items[int(choice)].plus_mana
                    print 'Damage: %d' % main.items[int(choice)].damage
                    print '\nPrice: %d gold' % main.items[int(choice)].price
                    while True:
                        confirm = raw_input('\n[Buy] | [Back] > ').lower()
                        if confirm == 'back':
                            break
                        elif confirm == 'buy':
                            if main.player.gold < main.items[int(choice)].price:
                                print 'You don\'t have enough gold!'
                            else:
                                main.player.gold -= main.items[int(choice)].price
                                main.player.items.append(main.items[int(choice)])
                                raw_input('\nYou have purchased the %s!' %
                                          main.items[int(choice)].name)
                                break
                    break
        elif item_type == 'magic':
            print '\nMagic Items:'
            for i in main.magic_items:
                print main.magic_items.index(i), i.name
            while True:
                choice = raw_input('\nInspect an item with its number or [Back] > ')
                if choice == 'back':
                    break
                else:
                    print '\n', main.magic_items[int(choice)].name.title()
                    print 'Attack: %d \t AC Penalty: %d' % \
                          (main.magic_items[int(choice)].attack,
                           main.magic_items[int(choice)].ac_penalty)
                    print 'Price: %d gold' % main.magic_items[int(choice)].price
                    while True:
                        confirm = raw_input('\n[Buy] | [Back] > ').lower()
                        if confirm == 'back':
                            break
                        elif confirm == 'buy':
                            if main.player.gold < main.magic_items[int(choice)].price:
                                print 'You don\'t have enough gold!'
                            else:
                                main.player.gold -= main.magic_items[int(choice)].price
                                main.player.equipment.append(main.magic_items[int(choice)])
                                raw_input('\nYou have purchased the %s!' %
                                          main.magic_items[int(choice)].name)
                                break
                    break
def final_room():
    raw_input('''
You fling open the door and are greeted by an intense gust of warm, earthy
air.  Before you stretches a long and cramped corridor with a downward
slope.  You're forced to crouch as you begin the descending trek. > ''')
    raw_input('''
As you descend the ambient temperature noticeably increases.  The stone
masonry in the walls, floor, and ceiling around you slowly give way to
formless mud and earth.  Finally you reach the corridor's end as it culminates
in a curious stone archway.
\nYou pass under the arch and into the chamber beyond. > ''')
    raw_input('''
You stand now in a truly immense underground chamber dominated by a
tremendous lake.  Though you can clearly hear the sounds of lapping water
nearby, much of the lake itself is obscured by the extreme darkness of the
chamber.  The gloom is sharply broken by a few lone rays of sunlight pouring
in from a crack in the chamber's ceiling.  The light partially illuminates a
small island at the lake's center and a narrow bridge leading to it from the
shore you now stand upon. > ''')
    while True:
        if main.player.player_class == 'mage':
            choice = raw_input("\n[Inventory] | [Spells] | [Status] | [Rest] | [Proceed] > ").lower()
        else:
            choice = raw_input("\n[Inventory] | [Status] | [Rest] | [Proceed] > ").lower()
        if choice == "inventory":
            main.player.inv()
            continue
        elif choice == 'spells':
            main.player.spells(main.goblin)
            continue
        elif choice == "status":
            main.player.status()
            continue
        elif choice == "rest":
            main.player.back = False
            main.player.rest()
            if main.player.back:
                continue
        elif choice == "proceed":
            break
    raw_input('''
You see the silhouette of a figure standing at a pedestal on the island.  The
figure's back is turned to you and the being is clearly preoccupied with some
complex task involving its hands. > ''')
    while True:
        choice = raw_input('''
Quietly [approach] the figure. | [Call] out to the figure. > ''').lower()
        if choice == 'approach':
            raw_input('''
You silently make your way across the bridge.  When you near the halfway mark
the figure's attention is seemingly broken from its present task as it slowly
turns around. > ''')
            raw_input('''
Suddenly you find yourself face to face with the figure, inexplicably
transported from your previous location some fifty feet behind.  The
figure is entirely shrouded in dark robes save for a ghostly white mouth
visible inside its deep cowl.  As the mouth begins to speak, small pebbles
nearby raise off the ground and you feel a curious tingling throughout your
body... > ''')
        elif choice == 'call':
            while True:
                choice1 = raw_input('''
[Who] are you?!
[What] are you doing?
[Stop] what you are doing at once! > ''').lower()
                if choice1 == 'who' or choice1 == 'what' or choice1 == 'stop':
                    raw_input('''
You call out to the figure, a moment passes and its attention is broken from
its task.  The figure slowly turns around. > ''')
                    raw_input('''
Suddenly you find yourself face to face with the figure, inexplicably
transported from your previous location some three-hundred feet behind.  The
figure is entirely shrouded in dark robes save for a ghostly white mouth
visible inside its deep cowl.  As the mouth begins to speak, small pebbles
nearby raise off the ground and you feel a curious tingling throughout your
body... > ''')
                    main.sorceror.boss_battle(main.player)
                else:
                    print '\nChoose an action to continue.'
                    continue
        else:
            print '\nChoose an action to continue.'
            continue
        main.sorceror.boss_battle(main.player)


# Function to enter the first room, begin function chain
def start():
    main.player.name = raw_input('''
As you enter the sweltering smithy a gruff looking man behind the counter
keeps his eyes fixed on the parchment sprawled in front of him.  He bellows in
your direction: \n\n\n"NAME?" > ''')
    raw_input('''
"Glad to meet ye, %s. I'm requisitions officer Fenton. I understand yer - " >
''' % main.player.name)
    raw_input("""
The hulking man pauses in mid-sentence to deftly crush a
large insect crawling near his hand.  He proceeds to clean
the sticky green mess by wiping his hand on his trousers. > """)
    print """
"My apologies.  Where were we? Ah yes - I'm told yer the one's been
appointed to clear Grogg's Mine.  About time, ye ask me!  Naught but evil
mischief comin' from that forsaken place these days.  In any case let's get
ye geared and on ye way.\" > """
    while True:
        main.player.player_class = raw_input("""
"Tell me, d'ye figure yerself more of a [fighter], [thief], or one of them
[mage] types?\" > """).lower()
        if main.player.player_class == "fighter":
            raw_input("""
\"We're gonna get along great, %s!  Let me just grab ye some suitable arms
and armor from the store room.\" > """ % main.player.name)
            raw_input("\nFenton returns with a well crafted bastard sword, set"
                      " of full plate, and a healing potion. > ")
            main.player.mp = 0
            main.player.equipment.append(main.bastard_sword)
            main.player.equipment.append(main.plate)
            main.player.items.append(main.healing_potion)
            main.player.equipment[0].equip()
            main.player.equipment[1].equip()
            raw_input("")
            print """
\"Now ye look like a proper warrior.  Head south and you'll come to the mine.
Best o' luck to ye!\""""
            mine_entrance()
        elif main.player.player_class == "thief":
            raw_input("""
\"Don't surprise me, %s.  Ye got that skulky look to ye.  Keep ye fingers
to yerself while I go fetch yer gear from the store room.\" > """ % main.player.name)
            raw_input('''
Fenton returns with a well crafted dagger, a tough looking leather jerkin, and
a healing potion. > ''')
            main.player.mp = 6
            main.player.equipment.append(main.dagger)
            main.player.equipment.append(main.leather)
            main.player.items.append(main.healing_potion)
            main.player.equipment[0].equip()
            main.player.equipment[1].equip()
            raw_input("")
            print """
\"Now ye look a bit more prepared.  Head south and you'll come to the mine.
Best o' luck to ye!\""""
            mine_entrance()
        elif main.player.player_class == "mage":
            main.player.max_mana = 35
            main.player.mana = 35
            raw_input("""
\"Fancy yerself one o' them fidgety wizards, eh %s? We ain't got much
'round here fer yer type, but I'll see what I can find.\" > """ % main.player.name)
            raw_input("""
Fenton returns with a gnarled looking staff, some freshly pressed robes, and
a mana potion. > """)
            main.player.equipment.append(main.staff)
            main.player.equipment.append(main.robes)
            main.player.items.append(main.mana_potion)
            main.player.equipment[0].equip()
            main.player.equipment[1].equip()
            raw_input("")
            print """
\"Now ye look ready to save our mine!  Just head south, ye can't miss 'er.
Best o' luck to ye!\""""
            mine_entrance()
        else:
            print "\nChoose a class to continue."
            continue


def mine_entrance():
    raw_input("""
You turn to leave the smithy.  The closing door behind you muffles the sound
of Fenton losing a struggle to contain his thunderous laughter. > """)
    raw_input("""
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
You journey south and eventually come upon the dismal looking mine.  A flash
of lightning many miles away briefly illuminates the mine's entrance in the
valley below.  The mine's neglected state strongly suggests that it has been
abandoned by humans for some time, though there are ominous signs of more
recent inhabitants.
\nA cold rain begins to drizzle. > """)
    raw_input("\nYou grit your teeth and begin the descent. > ")
    mine_start()


def mine_start():
    if main.monster_chance():
        raw_input("""
You carefully make your way down the rotting stairs to the mine's entrance.
The distant scuttle of a frightened mouse sounds as you approach the pitch
black opening. > """)
        raw_input("\nYou light a torch --")
        i = main.random.choice(main.random_monsters)
        raw_input("""
The sudden flame illuminates %s just ahead!  The creature snarls and rushes
toward you! > """ % i.name)
        main.combat(main.player, i)
        print "\n%s's corpse falls at the foot of the mine's door." % i.name
    else:
        print """
You carefully make your way down the rotting stairs to the mine's entrance.
The distant scuttle of a frightened mouse sounds as you approach the pitch
black opening.  You light a torch and extend your sight into the unknown dark
a short ways.  You finally glimpse the door to the mine."""
    while True:
        if main.player.player_class == 'mage':
            choice = raw_input("\n[Search] | [Inventory] | [Spells] | [Status] | [Rest] | [Proceed] > ").lower()
        else:
            choice = raw_input("\n[Search] | [Inventory] | [Status] | [Rest] | [Proceed] > ").lower()
        if choice == "search":
            print """
You stand in a dilapidated mining quarry, abandoned by the local townsfolk
for many years.  Nearby you can see bits of various mining tools, ruined from
their long exposure to the elements.  You see many piles of discarded half-
eaten food clearly not of human origin.  Ahead of you stands the door used to
enter the mine."""
            continue
        elif choice == "inventory":
            main.player.inv()
            continue
        elif choice == 'spells':
            main.player.spells(main.goblin)
            continue
        elif choice == "status":
            main.player.status()
            continue
        elif choice == "rest":
            main.player.rest()
        elif choice == "proceed":
            break
    raw_input("\nYou grasp the doorknob. > ")
    main.room_selector()