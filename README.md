# worldpic
Program to find the location from the picture.
# for education

#############################################
#                                           #
#  #     #  #######  ######  #      #####   #
#  #  #  #  #     #  #   ##  #      #    #  #
#  #  #  #  #     #  # ##    #      #    #  #
#  #######  #######  #   ##  #####  #####   #
#                                           #
#           ######   #####   #####          #
#           #     #    #    #               #
#           ######     #    #               #
#           #        #####   #####          #
#                                           #
#############################################

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

# There can be errors if the image has no location.
# It works well with photos taken with a phone.

# Creator
donutapn : Thailand : RPCA Cyber Club, Stringsme, R0_bocop, FourthHUNTER
