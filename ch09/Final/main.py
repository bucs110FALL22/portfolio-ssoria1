import requests
import json
import random
from random import randrange

# First, I create a function to identify the setting that the user wants to use when the program is running. Taking an episode ( writing the number of a episode betwwen the total of 51 chronologically) of Rick and Morty as a scenary, handling the Rick and Morty API to executing a list.
#
#
# Of course, separating two lists, between human characters and others ( referenting to another beings)
#
def environment():
  number = str(input("What episode do you want to set:        "))
  link = f'https://rickandmortyapi.com/api/episode/{number}'
  r = requests.get(link)
  j = r.json()
  characters = j['characters']
  list_names = list()
  list_others = list()
  for persons in characters:
    req = requests.get(persons)
    js = req.json()
    name = js['name']
    if js['species'] == 'Human':
      list_names.append(name)
    else:
      list_others.append(name)

  print(list_names)
  print()
  print(list_others)

# 
#
# Then, I used the Pokemon API to get the information and data of the pokemons; specifically their abilities and their types. Having account a range of all pokemon launched and registrered until the generation 8, and has the possibility to include 6 pokemon referenting to the maximum amount of pokemon that you have in a team.  
#
# 
def abilities_pokemon(poke):
  print(f'Abilities of {pokemon}')
  for i in poke['abilities']:
    print(i['ability']['name'])


def types(poke):
  print(f'Respective types of {pokemon}:')
  for i in poke['types']:
    print(i['type']['name'])



def info(poke):
  pass
  
  
def pokedex():
  global pokemon
  for i in range(6):
    pokemon = str(input('Pokemon:   ')) 
    API = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    res = requests.get(API)
    poke = res.json()
    abilities_pokemon(poke)
    types(poke)
    print()



def main():
  environment()
  print()
  if __name__ == '__main__':
    pokedex()
    adding = input("Do you want more pokemons (Yes or No) :      ")
    if adding == "Yes":
      pokedex()
      
main()  
# 
#

