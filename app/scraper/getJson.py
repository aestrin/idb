import requests
import json


NUM_PEOPLE = 88
NUM_STARSHIPS = 200
NUM_PLANETS = 61
NUM_FILMS = 7
NUM_SPECIES = 37



def getJsonDict(model,numModel):
	jsondict = {}
	for i in range(1,numModel+1):
		url = "http://swapi.co/api/{0}/{1}".format(model,i) 	
		r = requests.get(url)
		if r.status_code != 404:
			jsondict[i]=r.json()
	return jsondict


peopleDict = getJsonDict("people",NUM_PEOPLE)
starshipDict = getJsonDict("starships",NUM_STARSHIPS)
filmDict = getJsonDict("films",NUM_FILMS)
planetDict = getJsonDict("planets",NUM_PLANETS)
speciesDict = getJsonDict("species",NUM_SPECIES)


with open('allPeople.json', 'w') as outfile:  
    json.dump(peopleDict, outfile,indent=4)
with open('allStarships.json', 'w') as outfile:  
    json.dump(starshipDict, outfile,indent=4)
with open('allFilms.json', 'w') as outfile:  
    json.dump(filmDict, outfile,indent=4)
with open('allPlanets.json', 'w') as outfile:  
    json.dump(planetDict, outfile,indent=4)
with open('allSpecies.json', 'w') as outfile:
    json.dump(speciesDict, outfile,indent=4)
