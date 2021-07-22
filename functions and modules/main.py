import utilities as util

#-------------------------------------------------------------------------------------------
# @author Booh-rm
#-------------------------------------------------------------------------------------------

def test_function():
  creature= util.appear_creature().capitalize()
  location=util.appear_location().capitalize()
  print( creature, location)

  if  creature.startswith("K") and location.startswith("P"):
    print("Ahoy! captain, one", creature, "to", location)
  elif  creature.startswith("K") and location.startswith("Sta"):
    print("Ahoy! captain, one", creature, "to", location)
  elif  creature.startswith("K"):
    print("Ahoy! captain, one", creature, "by the", location)

  if  creature.startswith("Mer") and location.startswith("P"):
    print("Ahoy! captain, some", creature, "to", location)
  elif  creature.startswith("Mer") and location.startswith("Sta"):
    print("Ahoy! captain, some", creature, "to", location)
  elif  creature.startswith("Mer"):
    print("Ahoy! captain, some", creature, "by the", location)

  if  creature.startswith("W") and location.startswith("P"):
    print("Ahoy! captain, a", creature, "to", location)
  elif  creature.startswith("W") and location.startswith("Sta"):
    print("Ahoy! captain, a", creature, "to", location)
  elif  creature.startswith("W"):
    print("Ahoy! captain, a", creature, "by the", location)

  if  creature.startswith("Hip") and location.startswith("P"):
    print("Ahoy! captain, one", creature, "to", location)
  elif  creature.startswith("Hip") and location.startswith("Sta"):
    print("Ahoy! captain, one", creature, "to", location)
  elif  creature.startswith("Hip"):
    print("Ahoy! captain, one", creature, "by the", location)

  if  creature.startswith("Mac") and location.startswith("P"):
    print("Ahoy! captain, one", creature, "to", location)
  elif  creature.startswith("Mac") and location.startswith("Sta"):
    print("Ahoy! captain, one", creature, "to", location)
  elif  creature.startswith("Mac"):
    print("Ahoy! captain, one", creature, "by the", location)

  if  creature.startswith("O") and location.startswith("P"):
    print("Ahoy! captain, an", creature, "to", location)
  elif  creature.startswith("O") and location.startswith("Sta"):
    print("Ahoy! captain, an", creature, "to", location)
  elif  creature.startswith("O"):
    print("Ahoy! captain, an", creature, "by the", location)

  if  creature.startswith("L") and location.startswith("P"):
    print("Ahoy! captain, a few", creature, "to", location)
  elif  creature.startswith("L") and location.startswith("Sta"):
    print("Ahoy! captain, a few", creature, "to", location)
  elif  creature.startswith("L"):
    print("Ahoy! captain, a few", creature, "by the", location)

  if  creature.startswith("Hyd") and location.startswith("P") :
    print("Ahoy! captain, some", creature, "to", location)
  elif  creature.startswith("Hyd") and location.startswith("Sta"):
    print("Ahoy! captain, some", creature, "to", location)
  elif  creature.startswith("Hyd"):
    print("Ahoy! captain, some", creature, "by the", location)

#======================================================================
#        E n t r y   p o i n t   t o   a p p l i c a t i o n
# =====================================================================

test_function()