######################################################################################
#NOTE: Blizzard nerfed Force of Nature, so the spawned Treants no longer have Charge.#
#Therefore, this calculator is invalid and no longer applicable.                     #
######################################################################################
print("Damage calculator for FoN/SR Combos. NOTE: It is assumed that your board has enough space for all the Treants.")
print("Which combo do you currently have?")
print("1. Standard FoN+SR") #Normal combo
print("2. 1x FoN+2 SR") #Thaurissan and/or Innervate
print("3. 2x FoN+1x SR") #Thaurissan and/or Innervate
print("4. 2x FoN+2x SR") #Thaurissan and/or Innervate. Almost always game over
combo_choice = int(input("Choose option 1, 2, 3, or 4: "))
if combo_choice != 1 and combo_choice != 2 and combo_choice != 3 and combo_choice != 4:
    print("You have selected an invalid option.")
    combo_choice = int(input("Please select option 1, 2, 3, or 4: "))
if combo_choice == 1:
    #base damage is 14
    minions = int(input("How many minions do you have on the board? "))
    total_attack = int(input("What is the total Attack of the minions you currently have on the board? "))
    total_damage = 14 + (minions * 2) + total_attack
    print("The Combo will deal a total of ",total_damage," damage.")
if combo_choice == 2:
    #base damage is 22
    minions = int(input("How many minions do you have on the board? "))
    total_attack = int(input("What is the total Attack of the minions you currently have on the board? "))
    total_damage = 22 + (minions * 4) + total_attack
    print("The Combo will deal a total of ",total_damage," damage.")
if combo_choice == 3:
    #base damage is 26
    #minions = 1 because you only have room for one minion
    total_attack = int(input("What is the Attack of your minion? "))
    total_damage = 28 + total_attack
    print("The Combo will deal a total of ",total_damage," damage.")
if combo_choice == 4:
    #base damage is 40
    #minions = 1 because you only have room for one minion
    total_attack = int(input("What is the Attack of your minion? "))
    total_damage = 42 + total_attack
    print("The Combo will deal a total of ",total_damage," damage.")
#Created by ryc9011 on 3/17/2016.
