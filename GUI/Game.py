from random import randint
from tkinter import *


class Person:
    def __init__(self, hp, mp, atk, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.magic = magic
        self.action = ["Attack", "Magic", "Items"]
        self.items = items

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def generate_damage(self, disad=1):
        return random.randrange(self.atkl, self.atkh) / disad

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_atk(self):
       atk = str(self.atkh) + "/" + str(self.atkl)
       return atk

    def choose_magic(self):
        i = 1
        print("Magic:")
        for spell in self.magic:
            print(str(i) +":", spell.name, "(Cost", str(spell.cost) +")")
            i += 1

    def choose_items(self):
        i = 1
        print("Items:")
        for item in self.items:
            print(str(i) + ":", item.name, "QTY: 5", "\n  ", item.description)
            i += 1

    def choose_action(self):
        i = 1
        print("Actions:")
        for item in self.action:
            print(str(i) + ":", item)
            i += 1
            2


class Item:
    def __init__(self, name, type, description, prop):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop


class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)

#Create offensive magic
spell_fire = Spell("Fire", 10, 100, "Earth")
spell_thunder = Spell("Thunder", 10, 120, "Weather")
spell_blizzard = Spell("Blizzard", 15, 140, "Weather")
spell_meteor = Spell("Meteor", 20, 220, "Black")
spell_quake = Spell("Quake", 20, 220, "Earth")

#Create def magic
spell_cure = Spell("Cure", 10, 120, "Life")
spell_cura = Spell("Cura", 15, 250, "Life")

# Create items
item_potion = Item("Potion", "Potion", "Heals for 50 HP", 50)
item_hipotion = Item("Hi-Potion", "Potion", "Heals for 150 HP", 150)
item_superpotion = Item("Super-Potion", "Potion", "Heals for 250 HP", 250)
item_elixer = Item("Elixir", "Elixir", "Fully restores HP/MP of target", 0)
item_megaelixer = Item("Mega-Elixir", "Elixir", "Fully restores HP/MP of party", 0)
item_fraggrenade = Item("Frag Grenade", "Thrown Weapon", "Short fuse grenade", 150)
item_hegrenade = Item("HE Grenade", "Thrown Weapon", "High Explosive grenade", 500)

player_spells = [spell_cure, spell_fire, spell_blizzard]
player_items = [item_fraggrenade, item_potion, item_superpotion, item_elixer]

player = Person(randint(400, 600), randint(50, 80), randint(50, 80), player_spells, player_items)
enemy = Person(1200, 65, 45, [spell_cure, spell_thunder, spell_meteor], [item_hegrenade])

def new_game():
    # Initialise characters
    player_spells = [spell_cure, spell_fire, spell_blizzard]
    player_items = [item_fraggrenade, item_potion, item_superpotion, item_elixer]

    player = Person(randint(400, 600), randint(50, 80),  randint(50, 80), player_spells, player_items)
    enemy = Person(1200, 65, 45, [spell_cure, spell_thunder, spell_meteor], [item_hegrenade])

    scroll_box.config(text="A monster attacks")

    playerStats_HP.config(text="Player HP is: " + str(player.get_hp()) + "/" + str(player.get_max_hp()))
    playerStats_MP.config(text="Player MP is: " + str(player.get_mp()) + "/" + str(player.get_max_mp()))
    playerStats_Atk.config(text="Player attack power is: " + str(player.get_atk()))

    enemyStats_HP.config(text="Enemy HP is: " + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()),
                          relief="ridge", borderwidth=3, width=25)
    enemyStats_MP = Label(root, text="Enemy MP is: " + str(enemy.get_mp()) + "/" + str(enemy.get_max_mp()),
                          relief="ridge", borderwidth=3, width=25)
    enemyStats_Atk = Label(root, text="Enemy attack power is: " + str(enemy.get_atk()), relief="ridge", borderwidth=3,
                           width=25)

## Begin building GUI window
root = Tk()

## Create menu bar at top of window
menuBar = Menu(root)
root.config(menu=menuBar)

## Create 'File' dropdown on menu bar
fileMenu = Menu(menuBar)
menuBar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New Game", command=new_game)
fileMenu.add_command(label="Exit", command=Frame.quit)

## Create 'Options' dropdown on menu bar
optionsMenu = Menu(menuBar)
menuBar.add_cascade(label="Options", menu=optionsMenu)
optionsMenu.add_command(label="Add Item")
optionsMenu.add_command(label="Add Spell")
optionsMenu.add_command(label="Reroll Player")

playerStats_HP = Label(root, text="Player HP is: " + str(player.get_hp()) + "/" + str(player.get_max_hp()), relief="ridge", borderwidth= 3, width = 25)
playerStats_MP = Label(root, text="Player MP is: " + str(player.get_mp()) + "/" + str(player.get_max_mp()), relief="ridge", borderwidth= 3, width = 25)
playerStats_Atk = Label(root, text="Player attack power is: " + str(player.get_atk()), relief="ridge", borderwidth= 3, width = 25)

playerStats_HP.grid(row=1, column=0, columnspan=1, rowspan=1)
playerStats_MP.grid(row=2, column=0, columnspan=1, rowspan=1)
playerStats_Atk.grid(row=3, column=0, columnspan=1, rowspan=1)

scroll_box = Label(root, text="Please start a new game from the file menu", relief="ridge", borderwidth= 3, width= 80, height=50)
scroll_box.grid(row=0, column=1, columnspan=5, rowspan=5)

action_box = Entry(root)
action_box.grid(row=6, column=2, columnspan=3)
action_button = Button(root, text="Take Action!")
action_button.grid(row=7, column=2, columnspan=3)

enemyStats_HP = Label(root, text="Enemy HP is: " + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()), relief="ridge", borderwidth= 3, width = 25)
enemyStats_MP = Label(root, text="Enemy MP is: " + str(enemy.get_mp()) + "/" + str(enemy.get_max_mp()), relief="ridge", borderwidth= 3, width = 25)
enemyStats_Atk = Label(root, text="Enemy attack power is: " + str(enemy.get_atk()), relief="ridge", borderwidth= 3, width = 25)

enemyStats_HP.grid(row=1, column=7, columnspan=1, rowspan=1)
enemyStats_MP.grid(row=2, column=7, columnspan=1, rowspan=1)
enemyStats_Atk.grid(row=3, column=7, columnspan=1, rowspan=1)

playerStats_HP.config(text="Player HP is: " + str(player.get_hp()) + "/" + str(player.get_max_hp()))
playerStats_MP.config(text="Player MP is: " + str(player.get_mp()) + "/" + str(player.get_max_mp()))

root.mainloop()