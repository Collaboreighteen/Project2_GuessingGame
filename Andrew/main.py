import googlemaps
import random

gmaps = googlemaps.Client(key="AIzaSyDNzBo4vhDEfJ63lwJ56vk-ILwvnfIrUF4")

def getDistance(start, stop):
    directions_result = gmaps.directions(
        start,
        stop,
        mode="driving",
        departure_time="now"
    )
    return { "distance": directions_result[0]['legs'][0]['distance'] }

def getLocationFromGeocode(geoCode):
  return geoCode[0]['geometry']['location']

def locIsNorth(start, end):
  return start["lat"] > end["lat"]

def locIsEast(start, end):
  return start["lng"] > end["lng"]

def getDirection(start, stop):
  startGeocode = gmaps.geocode(start)
  stopGeocode = gmaps.geocode(stop)

  startLoc = getLocationFromGeocode(startGeocode)
  stopLoc = getLocationFromGeocode(stopGeocode)

  return {
    "isNorth": locIsNorth(startLoc, stopLoc),
    "isEast": locIsNorth(startLoc, stopLoc)
  }


def getDirectionString(feedback): 
  direction =  feedback["distance"]["text"] + ' to the '
  direction += 'North' if feedback["isNorth"] else "South"
  direction += 'east' if feedback["isEast"] else "west"

  return direction

def getHintString(guess, actual): 
  directionDict = getDirection(guess, actual)
  distanceDict = getDistance(guess, actual)

  feedbackDict = {**directionDict, **distanceDict}

  directionString = getDirectionString(feedbackDict)
  return 'Nope, but the real answer is ' + directionString






GUESS_SPACE = [
  'Victoria',
  'Edmonton',
  'Regina',
  'Winnipeg',
  'Ottawa',
  'Quebec City',
  'Yellowknife',
  'Whitehorse',
  'Iqaluit',
  'Moncton',
  'Halifax',
  'Saint Johns',
  'Charlottetown'
]


playAgain = 'y'
while playAgain == 'y':
    answer = GUESS_SPACE[random.randint(0, len(GUESS_SPACE) - 1)]

    # A curried version of getHintString with the Answer pre-supplied
    # # Call with each subsequent guess against the same answer
    def getAnswerHint(guess):
      return getHintString(answer, guess) 

    playerStr = input('You have three chances, guess what city it is! ')
    retries = 2
    while answer != playerStr and retries > 0:
        playerStr = input(getAnswerHint(playerStr))
        retries = retries - 1
    if answer != playerStr:
        print('Yup! I was thinking ' + playerStr + '!')
    else:
        print('Sorry, that\'s your three guesses, I was thinking ' + answer + '.')
    playAgain = input('Play again? (y/n) ')
    while playAgain != 'y' and playAgain != 'n':
        playAgain = input('Play again? (y/n) ')
