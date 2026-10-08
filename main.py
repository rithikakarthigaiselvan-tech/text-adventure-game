import time
import sys


def print_pause(text, delay=1.5):
    """Prints text smoothly with a small delay for dramatic reading."""
    print(text)
    time.sleep(delay)


def show_status(health, inventory):
    """Displays current player health and items."""
    print("\n" + "=" * 40)
    print(f"  HEALTH: {health}/100")
    print(f"  INVENTORY: {', '.join(inventory) if inventory else 'Empty'}")
    print("=" * 40 + "\n")


def game_over(reason):
    """Triggers game over screen and asks to restart."""
    print_pause("\n" + "*" * 40)
    print_pause(f"GAME OVER: {reason}")
    print_pause("*" * 40 + "\n")
    
    replay = input("Would you like to play again? (yes/no): ").strip().lower()
    if replay in ["yes", "y"]:
        start_game()
    else:
        print_pause("Thanks for playing Dungeon Explorer!")
        sys.exit()


def victory():
    """Triggers winning screen."""
    print_pause("\n" + "#" * 40)
    print_pause("VICTORY! You unlocked the main gate and escaped into the sunlight!")
    print_pause("#" * 40 + "\n")
    
    replay = input("Would you like to play again? (yes/no): ").strip().lower()
    if replay in ["yes", "y"]:
        start_game()
    else:
        print_pause("Thanks for playing Dungeon Explorer!")
        sys.exit()


def boss_room(health, inventory):
    """The final room where victory depends on items collected."""
    print_pause("\nYou step into a grand chamber guarded by a massive Obsidian Golem.")
    show_status(health, inventory)

    if "Golden Key" not in inventory:
        print_pause("The Golem slams the door shut behind you!")
        print_pause("Without the Golden Key to unlock the escape gate, you are trapped.")
        game_over("Trapped in the boss room forever.")
        return

    print_pause("You dodge the Golem's heavy swing and race toward the Golden Gate!")
    
    if "Shield" in inventory:
        print_pause("The Golem throws a boulder, but you block it with your Iron Shield!")
    else:
        print_pause("The Golem strikes you as you run past!")
        health -= 40
        print_pause(f"You took 40 damage! Current Health: {health}")
        if health <= 0:
            game_over("Crushed by the Golem before reaching the gate.")
            return

    print_pause("You insert the Golden Key into the lock... it turns smoothly!")
    victory()


def armory_room(health, inventory):
    """Option 1: The Armory path."""
    print_pause("\nYou walk down a dusty corridor into an abandoned Armory.")
    
    if "Shield" not in inventory:
        print_pause("You spot a sturdy Iron Shield resting against a wall weapon rack.")
        choice = input("Do you take the shield? (yes/no): ").strip().lower()
        if choice in ["yes", "y"]:
            inventory.append("Shield")
            print_pause("Item added: Iron Shield!")
        else:
            print_pause("You decide to leave the shield behind.")
    else:
        print_pause("The armory is empty now. You've already scavenged everything.")

    show_status(health, inventory)
    print_pause("The only way forward leads toward the Boss Chamber.")
    input("Press Enter to proceed to the main chamber...")
    boss_room(health, inventory)


def crypt_room(health, inventory):
    """Option 2: The Crypt path."""
    print_pause("\nYou descend slippery stone steps into a damp Crypt.")
    
    if "Golden Key" not in inventory:
        print_pause("A skeleton guards a sparkling Golden Key on an altar!")
        print_pause("1. Fight the skeleton with your bare hands.")
        print_pause("2. Attempt to sneak past and grab the key.")
        
        choice = input("Choose 1 or 2: ").strip()
        
        if choice == "1":
            print_pause("You charge the skeleton and shatter it, but take 25 damage in the brawl.")
            health -= 25
            inventory.append("Golden Key")
            print_pause("You picked up the Golden Key!")
        elif choice == "2":
            print_pause("You quietly slip around the sarcophagus and snatch the key without waking the skeleton!")
            inventory.append("Golden Key")
            print_pause("You picked up the Golden Key!")
        else:
            print_pause("You hesitate! The skeleton strikes first!")
            health -= 35
            inventory.append("Golden Key")
            print_pause("You grab the key and retreat, taking 35 damage!")
    else:
        print_pause("The crypt is silent. The altar is bare.")

    if health <= 0:
        game_over("Succumbed to your wounds in the Crypt.")
        return

    show_status(health, inventory)
    print_pause("A secret doorway opens leading toward the Boss Chamber.")
    input("Press Enter to proceed...")
    boss_room(health, inventory)


def start_game():
    """Initializes game state and starts the main story."""
    health = 100
    inventory = []

    print_pause("=========================================")
    print_pause("      WELCOME TO DUNGEON EXPLORER        ")
    print_pause("=========================================")
    print_pause("You wake up on a cold stone floor inside a dark dungeon.")
    
    show_status(health, inventory)

    while True:
        print("You see two passages before you:")
        print("1. Enter the Armory (Left Door)")
        print("2. Descend into the Crypt (Right Door)")
        
        choice = input("Where do you want to go? (1 or 2): ").strip()
        
        if choice == "1":
            armory_room(health, inventory)
            break
        elif choice == "2":
            crypt_room(health, inventory)
            break
        else:
            print_pause("Invalid selection. Please choose 1 or 2.\n", delay=0.5)


if __name__ == "__main__":
    start_game()