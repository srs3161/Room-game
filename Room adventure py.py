#################################################################################################
# Name: Satyendra Raj Singh
# Date: 01/03/2024
# Description: Room Adventure
# Improvements: (1) Added Room 5 and Room 6
#               (2) Points for going in another room.
#               (3) Added drop function to drop items in another room.
#################################################################################################

class Room:
    def __init__(self, name):
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []
        playerpoints = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    def addExit(self, exit, room):
        self.exits.append(exit)
        self.exitLocations.append(room)

    def addItem(self, item, desc):
        self.items.append(item)
        self.itemDescriptions.append(desc)

    def addGrabbable(self, item):
        self.grabbables.append(item)

    def delGrabbable(self, item):
        self.grabbables.remove(item)

    def delItem(self, item):
        self.items.remove(item)
        index = self.itemDescriptions.index(item)
        del self.itemDescriptions[index]

    def dropItem(self, item, room):
        inventory.remove(item)
        room.addItem(item, f"{item} is lying on the floor.")

    def __str__(self):
        s = f"You are in {self.name}.\n"
        s += "You can see: "
        for item in self.items:
            s += item + " "
        s += "\n"
        s += "Exits are: "
        for exit in self.exits:
            s += exit + " "
        s += "\n"
        return s


def createRooms():
    global currentRoom
      #create the rooms
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")
    r5 = Room("Room 5")
    r6 = Room("Room 6")
  #add exits to room 1
    r1.addExit("east", r2)
    r1.addExit("south", r3)
  #add grabbables and items
    r1.addGrabbable("key")
    r1.addItem("table", "It is old and looks scary.")
    r1.addItem("chair", "It is made of iron is strong.")
  #add exits to room 2
    r2.addExit("west", r1)
    r2.addExit("south", r4)
  #add grabbables and items
    r2.addItem("rug", "It has a design of Nepali flag on it.")
    r2.addGrabbable("stick")
    r2.addItem("fireplace", "It is full of ashes.")
  #add exits to room 3
    r3.addExit("north", r1)
    r3.addExit("east", r4)
    r3.addExit("south", r5)
  #add grabbables and items
    r3.addItem("bookshelves", "There are some books in it.")
    r3.addGrabbable("book")
    r3.addItem("statue", "This is a statue of MESSI.")
    r3.addItem("desk", "The statue is on it.")
  #add exits to room 4
    r4.addExit("north", r2)
    r4.addExit("west", r3)
    r4.addExit( "south", r6)   
  #add grabbables and items
    r4.addItem("brew_rig", "It is full of beer.")
    r4.addGrabbable("beer")
  #add exits to room 5
    r5.addExit("north", r3)
    r5.addExit("east", r6)
  #add grabbables and Items
    r5.addItem("Laptop", "Laptop is made of aluminium and some basics wires.")
    r5.addGrabbable("mouse")
    r5.addItem("Keyboard", "The keyboard is black and made in China.")
    r5.addItem("Vault", "It is locked, it needs key to open")
  #add exits to room 6
    r6.addExit("west", r5)
    r6.addExit("north", r4)
    r6.addExit("south", None)   #DEATH!
  #add grabbables and Items
    r6.addItem("Harpic", "It is blue in color and used to clean toilet")
    r6.addGrabbable("brush")
    r6.addItem("Basin", "It is made of tiles")

    
    currentRoom = r1


def death():
    print("You are dead!!!")


inventory = []
playerpoints = 0
createRooms()

while True:
    status = f"{currentRoom}\nYou are carrying: {inventory}"
    if currentRoom is None:
        death()
        break

    print("=================================================================================")
    print(status)

    action = input("What to do? ")
    action = action.lower().strip()

    if action in ["quit", "exit", "bye"]:
        break

    response = "I don't understand... Try Verb/Noun. Valid verbs are go, look, take, and drop."

    words = action.split()
    if len(words) == 2:
        verb = words[0]
        noun = words[1]

        if verb == "go":
            response = "Invalid exit"
            for i in range(len(currentRoom.exits)):
                if noun == currentRoom.exits[i]:
                    currentRoom = currentRoom.exitLocations[i]
                    response = "Room Changed"
                    PointsForRoomChange = 2

                    playerpoints += PointsForRoomChange
                    print(
                        f"You earned {PointsForRoomChange} points for moving to a new room! Total points: {playerpoints} ")
                    break
        if verb == "look":
            response = "I don't see that item."
            for i in range(len(currentRoom.items)):
                if noun == currentRoom.items[i]:
                    response = currentRoom.itemDescriptions[i]
                    break
        if verb == "take":
            response = "I don't see that item"
            for grabbable in currentRoom.grabbables:
                if noun == grabbable:
                    inventory.append(grabbable)
                    currentRoom.delGrabbable(grabbable)
                    response = "Item grabbed."
                    break
        if verb == "drop":
            response = "You don't have that item."
            for item in inventory:
                if noun == item:
                    currentRoom.dropItem(item, currentRoom)  # Change room to where you want to drop the item
                    response = "Item dropped."
                    break

    print(f"\n{response}")
