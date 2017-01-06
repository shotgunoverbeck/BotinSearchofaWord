#User-customizable settings
#Changing these to incorrect values may cause the
#script to function incorrectly.

#Number of seconds to wait after typing each word
#. Smaller values have a higher chance of stutter
#ing the output.
wordSleepTime = 0.001

#Number of seconds to allow for letters to around
# the screen. Important to have some delay betwee
#n entering words and then trying to capture the 
#new letter images.
letterShiftTime = 0.5

#X and Y coordinates around which to frame the sc
#reen capture. These are the coordinates of the t
#op pixel of the first "I" in "INSTRUCTIONS" on t
#he main screen of the single player game. This a
#ssumes that the game is running in 650 by 480 re
#solution, otherwise it will not work properly. T
#he exact coordinates may be found using "Print S
#creen" and a basic image editor.
bboxSetX = 343
bboxSetY = 593
#The default setting is exact for a 1920 by 1080 
#Windows 7 display, with the game running in a Go
#ogle Chrome window locked to the left side of th
#e screen.

#Maximum number of seconds between rounds that th
#e bot will wait for full confirmation before jus
#t attempting to do the round anyway.
maxWaitingTime = 30

#Boolean value, whether or not to continually shu
#ffle the letters and attempt to reread them. Thi
#s minimizes the chance of missing a letter.
keepTrying = False