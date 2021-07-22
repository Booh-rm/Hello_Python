import random

def appear_creature():
  
  creature=["Kraken", "Mermaids", "Whale", "Hippocampus", "Macaraprone", "Octopus", "Leviathans", "Hydras"]
  index = random.randint(0, 7)
  return creature[index]

def appear_location():
  
  location=["port", "starboard", "bow", "stern"]
  index = random.randint(0, 3)
  return location[index]