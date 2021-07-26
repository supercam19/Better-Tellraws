import re
import pyperclip
done = False
inputFile = 'input.json'
outputFile = 'output.txt'
copyText = True

data = open(inputFile, 'r')
tellraw = data.read()
print('Reading input file ' + inputFile)
tellraw = re.sub(r"[\n]*", "", tellraw)
data = open(outputFile, 'w')
data.write(tellraw)
print('Writing to output file ' + outputFile)
print('Finished')
if copyText:
    pyperclip.copy(tellraw)
print('Text copied to clipboard!')