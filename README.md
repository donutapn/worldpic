# worldpic
Program to find the location from the picture.
# for education

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
X                                           X
X  X     X  XXXXXXX  XXXXXX  X      XXXXX   X
X  X  X  X  X     X  X   XX  X      X    X  X
X  X  X  X  X     X  X XX    X      X    X  X
X  XXXXXXX  XXXXXXX  X   XX  XXXXX  XXXXX   X
X                                           X
X           XXXXXX   XXXXX   XXXXX          X
X           X     X    X    X               X
X           XXXXXX     X    X               X
X           X        XXXXX   XXXXX          X
X                                           X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Require*
1. python3
2. pip install pillow
3. pip install requests
4. pip install re
5. pip install os
6. pip install sys

# Usage
>> python3 worldpic.py [image]

# Example
>> python3 worldpic.py sample.jpg

# Operation
1. Get latitude and longitude from image metadata.
2. Convert Degrees Minutes Seconds(DMS) to Decimal Degrees(DD)
3. Find a location on the map(Geocode & Google Maps).

# Output
1. DMS
2. DD
3. location on Geocode
4. location on Google Maps

# Tips
- There can be errors if the image has no location.
- It works well with photos taken with a phone.

# Creator
donutapn : Thailand : RPCA Cyber Club, Stringsme, R0_bocop, FourthHUNTER
