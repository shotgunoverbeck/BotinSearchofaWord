Bot in Search of a Word - by ShotgunOverbeck

This is a bot for the game Eight Letters in Search of a Word. It will read the player's screen and then entire all scoring words almost immediately. This bot simulates human input, albiet at superhuman speeds, meaning that its input is indistinguishable from that of a human player. It does not rely on reading machine-level data.

The bot is run via bot.py, included in the same directory as this file. In order for it to work correctly, the entirety of the game must be unobscured on the user screen, and the cursor must be hovering over the game's flash object. Once the game is running, the user should not interact with the computer unless they wish to stop the script.

The script requires:
* Windows 7
* Python 3.4+
* PIL (recommended Pillow for Python 3+)

Users are recommended to customize their settings in settings.py. Customization of the bounding box may be needed. The actual performance of the script may be affected if run on a low-grade computer. A benchmark of the actual speed can be tested with benchmark.py, included in the same directory as the bot.py script.

It uses the PyTesser implementation of the Google OCR project Tesseract to process images to text. All files required for Tesseract are included. Keypress simulation is shamelessly stolen from a StackOverflow answer by user noctis-skytower (Stephen Chappel). The click simulation is stolen from a StackOverflow answer by user luc (Luc Jean). The word lists are provided by SCOWL. Many thanks to all.

Known bugs:
* Not all acceptable Eight1 words are known to the bot
* The letters W and Q are often mistaken by Tesseract as being X and O, respectively. Whether or not the bot will recognize them seems all but entirely random. The bot may fail when trying to recognize these characters.
* When joining a multiplayer round in progress, the bot will not recognize the round title, and thus not begin participating in the round until maxWaitingTime (variable in settings.py) has been reached.

Contact can be made to joe@shotgunoverbeck.com.

Eight Letters in Search of a Word can be found at the following URLs:
* Main Page: http://www.eastoftheweb.com/cgi-bin/top_scores.pl?game=eight
* Singleplayer: http://www.eastoftheweb.com/games/Eight1.html
* Multiplayer Lobbies: http://www.eastoftheweb.com/cgi-bin/top_scores.pl?game=multieight