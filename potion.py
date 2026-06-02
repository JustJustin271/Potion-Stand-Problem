"""
Potion Stand - STARTER FILE

You run a potion stand at the market. Customers line up, order potions,
and you ring them up. Fill in the TODOs below.

Read input from standard input (stdin).

See the problem statement for the exact input/output format.
"""

# The menu: potion name (lowercase) -> price in gold
MENU = {
    "healing": 5,
    "invisibility": 12,
    "luck": 15,
    "mana": 7,
    "strength": 9,
}

VIP_THRESHOLD = 30   # subtotal must reach this (or more) to earn the discount
VIP_DISCOUNT = 5     # gold taken off the subtotal


def main():
   
    customer_count = int(input(""))
   
    total_gold = 0
    total_potion = 0
   
    sold_dict = {}
   
    for person in range(customer_count):
       
        subtotal = 0
       
        name = input("")
       
        item_count = int(input(""))
       
        print(f"=== {name}'s order ===")
       
        for good in range(item_count):
            item_name = input("")
           
            if item_name.lower().strip() not in MENU:
                print(f"We don't stock '{item_name}'!")
           
            else:
                print(f"{item_name.capitalize()} potion: {MENU[item_name.lower().strip()]} gold")
                subtotal += MENU[item_name.lower().strip()]
               
                total_potion += 1
               
                sold_dict[item_name.lower().strip()] = sold_dict.get(item_name.lower().strip(), 0) + 1
       
        print(f"Subtotal: {subtotal} gold")
       
        if subtotal >= VIP_THRESHOLD:
            print("VIP discount: -5 gold")
           
            subtotal -= 5
       
        print(f"Total: {subtotal} gold")
       
        total_gold += subtotal
       
        print("")
   
    print("=== End of Day ===")
    print(f"Gold earned: {total_gold} gold")
    print(f"Potions sold: {total_potion}")
   
    if not sold_dict:
        print("Best seller: none")
    else:
        print(f"Best seller: {min(sold_dict, key=lambda k: (-sold_dict[k], k)).capitalize()} ({max(sold_dict.values())} sold)")


if __name__ == "__main__":
    main()

# June 2nd, 2026
# This is the potion stand problem from today's class
