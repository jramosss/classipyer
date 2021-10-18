# Classipyer

![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)

Have you ever wanted to classify a list of songs by decade and artist? Me neither.  
But this program does it.

You will need spotify credentials to run this script.

Just pass the path of your .xlsx file with a column named "Song" and the program will create a new sheets file with
"Artist" "Song" "Decade".

`python3 main.py mysheet.xlsx`

Built using `spotipy` and `xlsxwriter`