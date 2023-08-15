#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def monty_hall_stimulation(num_stimulations):
    stay_wins = 0
    switch_wins = 0
    
    for _ in range(num_stimulations):
        prize_door = random.randint(1, 3)
        contestant_choice = random.randint(1, 3)
        
        # Host opens a door with no prize
        remaining_doors = [door for door in [1, 2, 3] if door != contestant_choice and door != prize_door]
        opened_door = random.choice(remaining_doors)
        
        # Determine the door to switch to
        switch_door = 6 - contestant_choice - opened_door
        
        # Check if staying wins or switching wins
        stay_wins += (contestant_choice == prize_door)
        switch_wins += (switch_door == prize_door)
            
    stay_win_percentage = (stay_wins / num_stimulations) * 100
    switch_win_percentage = (switch_wins / num_stimulations) * 100
    
    print(f"Results after {num_stimulations} stimulations:")
    print(f"Staying wins: {stay_wins} times ({stay_win_percentage:.2f}%)")
    print(f"Switching wins: {switch_wins} times ({switch_win_percentage:.2f}%)")

if __name__ == "__main__":
    num_stimulations = int(input("Enter the number of stimulations: "))
    monty_hall_stimulation(num_stimulations)

