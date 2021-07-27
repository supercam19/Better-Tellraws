import re
import pyperclip
done = False
inputFile = 'input.json'
outputFile = 'output.txt'
copyText = True


settings = input(' ?? | Compile with default settings?(y/n): ')
if settings == 'n':
    print(' I  | Press enter to leave setting as default')
    inputFile = input(' ?? | Input file? (default is input.json): ')
    if inputFile == '':
        inputFile = 'input.json'
    outputFile = input(' ?? | Output file? (default is output.txt): ')
    if outputFile == '':
        outputFile = 'output.txt'
    copyText = input(' ?? | Copy text to clipboard? (default is true)(y/n): ')
    if copyText == 'n':
        copyText = False
    else:
        copyText = True
elif settings == 'y':
    print(' >> | Proceeding with default settings')
else:
    print(' !! | Invalid response, proceeding with default settings')


print(' >> | Reading input file ' + inputFile)
data = open(inputFile, 'r')
tellraw = data.read()
tellraw = re.sub(r"[\n]*", "", tellraw)
data = open(outputFile, 'w')
data.write(tellraw)
print(' >> | Writing to output file ' + outputFile)
print(' >> | Finished')
if copyText:
    pyperclip.copy(tellraw)
    print(' !! | Text copied to clipboard!')
