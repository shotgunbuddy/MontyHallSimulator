import random

should_switch = 0
should_not_switch = 0
door_total = 0
on = True
while on == True:
    def pick_door_total(doors):   # define function to prompt for number of doors
        try:
            doors = int(input("How many doors do you want to have? Must be an integer of 3 or more."))
            if doors >= 3:
                print(f"You chose {doors} doors!")
                return doors
            else:
                print("Invalid entry, Try again!")
                return 0 # if number is less than 3, sets doors to 0 again so that while loop will continue and repeat prompt for entry.

        except:
            print("Invalid entry, Try again!")
            return 0 # if entry throws an error, set doors to 0 to continue while loop so prompt will repeat.

    while door_total == 0:
        door_total = pick_door_total(door_total)
    # print(f"after func {door_total}")
    options_total = []

    for x in range(0,door_total):
        options_total.append(x)

    # print(options_total)

    trial_total = 0

    def pick_trial_total(trials):
        try:
            trials = int(input("How many trials do you want to have? Must be an integer of 1 or more."))
            if trials >= 1:
                print(f"You chose {trials} trials!")
                return trials
            else:
                return 0 # if number is less than 1, sets doors to 0 again so that while loop will continue and repeat prompt for entry.

        except:
            print("Invalid entry, Try again!")
            return 0 # if entry throws an error, set doors to 0 to continue while loop so prompt will repeat.

    while door_total == 0: # while loop so the function continues until a proper answer is received
        door_total = pick_door_total(door_total)

    while trial_total == 0: # while loop so the function continues until a proper answer is received
        trial_total = pick_trial_total(trial_total)

    for x in range(0,trial_total): #range is exclusive, so total trials remains the same

        prize = random.randint(0,door_total-1) #randint is inclusive, so door total has 1 subtracted to preserve list indices
        # print(prize)
        guess = random.randint(0,door_total-1) #randint is inclusive, so door total has 1 subtracted to preserve list indices
        # print(guess)

        options1 = list(options_total) # create a duplicate list to options total. Without list() this would point the variables to the original list and cause that list to be modified, breaking the program after the first trial
        # print(options1)
        options2 = list(options_total) # create a duplicate list to options total. Without list() this would point the variables to the original list and cause that list to be modified, breaking the program after the first trial
        # print(options2)

        options1.remove(prize) #remove the prize door from the list of doors to open
        options2.remove(guess) #remove the guess from the list of doors to open


    # debugging print statements
        # print(f"prize {prize}")
        # print(f"guess {guess}")
        # print(f"options {options}")
        # print(f"options_minus_prize {options_minus_prize}")
        # print(f"options_minus_guess {options_minus_guess}")
        # print(f"options1 {options1}")
        # print(f"options2 {options2}")

        door_to_open = list(set(options1) & set(options2)) #creates list of doors to choose from to open
        opened_door = random.choice(door_to_open) #opens one door and random from the available doors, in case the guess and prize are equal to each other. Pointless over 3 doors.
        # print(f"door to open {door_to_open}")
        # print(f"opened door {opened_door}")

    #ultimately the other door option doesn't matter because the only time you shouldn't switch would be if your door was correct.
        if guess == prize:
            # print("should not switch")
            should_not_switch += 1

        if guess != prize:
            # print("should switch")
            should_switch += 1


    switch_percent_rounded = round((should_switch/trial_total),2)
    print(switch_percent_rounded)
    print(f"Your intitial guess was incorrect {should_switch} times, so you should have switched {switch_percent_rounded*100}% of the time")
    print(f"Your initial guess was correct {should_not_switch} times, so you would benefit from not switching {100-(switch_percent_rounded*100)}% of the time")
    print("As the number of doors increases, the times you should have switched will increase towards 100%. Increasing the number of trials increases the accuracy of the percentage.")
    print("Since the odds of you being correct are always 1 out of however many doors there are, your initial guess accuracy should approach 1% as the number of doors and trials increases.")
    print("")
    should_switch = 0
    should_not_switch = 0
    door_total = 0
    trial_total = 0