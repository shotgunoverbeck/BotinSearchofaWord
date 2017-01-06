try:
	import os
	import time
	import sys
	import PIL
	import re
	from PIL import ImageGrab
	from PIL import Image
	import subprocess
	import util
	import errors
except Exception as error:
	print('Error while fetching dependencies:\n'+str(error)+'\nPlease fix this error and then try again.')
	input('>')
scriptDirectory = str(os.path.dirname(os.path.abspath(__file__)))

print('Running benchmark...\n')

estRoundTime = 0

#Test word loading times
start_time = time.time()
english_dict = []
for filename in os.listdir(scriptDirectory+'/wordlists'):
	newWordFile = open(scriptDirectory+'/wordlists/'+str(filename))
	for line in newWordFile:
		english_dict.append(re.sub(r'\W', '', line))
	newWordFile.close()
alternate_word_list = open(scriptDirectory + '/alternate_word_list.txt')
print('Loaded ' + str(len(english_dict))+' words into RAM:\n* Ttl: '+str(time.time() - start_time)+' seconds')

minTime = 1000
maxTime = 0
avgTime = 0
words = ['aardvark','aardwolf','aasvogel','abacuses','abalones']
for word in words:
	start_time = time.time()
	wordlist = []
	broken_word = []
	for letter in word:
		broken_word.append(letter.lower())
	for word in english_dict:
		breakable_word = []
		for letter in broken_word:
			breakable_word.append(letter)
		isValid = True
		for letter in word:
			if letter in breakable_word:
				breakable_word.pop(breakable_word.index(letter))
			else:
				isValid = False
				break
		if isValid:
			wordlist.append(word)
	wordlist = sorted(wordlist, key=len)
	wordlist.reverse()
	totalTime = time.time() - start_time
	if totalTime < minTime:
		minTime = totalTime
	elif totalTime > maxTime:
		maxTime = totalTime
	avgTime += totalTime
avgTime /= len(words)
estRoundTime += avgTime
print('Checking '+str(len(words))+' 8-character strings against wordlist: \n* Min: '+str(minTime)+' seconds\n* Max: '+str(maxTime)+' seconds\n* Avg: '+str(avgTime)+' seconds')

tesseract_exe_name = scriptDirectory + '/tesseract.exe' # Name of executable to be called at command line
scratch_image_name = "temp.bmp" # This file must be .bmp or other Tesseract-compatible format
scratch_text_name_root = "temp" # Leave out the .txt extension
cleanup_scratch_flag = True  # Temporary files cleaned up after OCR operation
def call_tesseract(input_filename, output_filename):
	args = [tesseract_exe_name, input_filename, output_filename]
	proc = subprocess.Popen(args)
	retcode = proc.wait()
	if retcode!=0:
		errors.check_for_errors()
def image_to_string(im, cleanup = cleanup_scratch_flag):
	try:
		util.image_to_scratch(im, scratch_image_name)
		call_tesseract(scratch_image_name, scratch_text_name_root)
		text = util.retrieve_text(scratch_text_name_root)
	finally:
		if cleanup:
			util.perform_cleanup(scratch_image_name, scratch_text_name_root)
	return text

checkRuns = 100
minTime = 1000000
maxTime = 0
avgTime = 0
for x in range(0, checkRuns):
	start_time = time.time()
	img = Image.open(scriptDirectory+'/images/k.bmp')
	text = image_to_string(img)
	totalTime = time.time() - start_time
	if totalTime < minTime:
		minTime = totalTime
	elif totalTime > maxTime:
		maxTime = totalTime
	avgTime += totalTime
avgTime /= checkRuns
print('Checked '+str(checkRuns)+' characters with PyTesser\n* Min: '+str(minTime)+' seconds\n* Max: '+str(maxTime)+' seconds\n* Avg: '+str(avgTime)+' seconds')

checkRuns = 100
minTime = 1000000
maxTime = 0
avgTime = 0
for x in range(0, checkRuns):
	start_time = time.time()
	img = Image.open(scriptDirectory+'/images/round2.bmp')
	text = image_to_string(img)
	totalTime = time.time() - start_time
	if totalTime < minTime:
		minTime = totalTime
	elif totalTime > maxTime:
		maxTime = totalTime
	avgTime += totalTime
avgTime /= checkRuns
estRoundTime += (avgTime * 8)
print('Checked '+str(checkRuns)+' round titles with PyTesser\n* Min: '+str(minTime)+' seconds\n* Max: '+str(maxTime)+' seconds\n* Avg: '+str(avgTime)+' seconds')

checkRuns = 100
minTime = 1000000
maxTime = 0
avgTime = 0
for x in range(0, checkRuns):
	start_time = time.time()
	img = ImageGrab.grab(bbox = (0, 0, 200, 200))
	totalTime = time.time() - start_time
	if totalTime < minTime:
		minTime = totalTime
	elif totalTime > maxTime:
		maxTime = totalTime
	avgTime += totalTime
avgTime /= checkRuns
estRoundTime += avgTime
print('Took '+str(checkRuns)+' screenshots with PIL\n* Min: '+str(minTime)+' seconds\n* Max: '+str(maxTime)+' seconds\n* Avg: '+str(avgTime)+' seconds')

print('\nEstimated Round Time: '+str(estRoundTime))
if estRoundTime < 2:
	print('Benchmark Review: Perfect')
elif estRoundTime < 5:
	print('Benchmark Review: Good')
elif estRoundTime < 15:
	print('Benchmark Review: Okay')
elif estRoundTime < 30:
	print('Benchmark Review: Not Good')
elif estRoundTime < 45:
	print('Benchmark Review: Bad')
elif estRoundTime < 60:
	print('Benchmark Review: Script Will Not Work')

print('\nFinished running benchmark')
input('Press enter to exit: ')