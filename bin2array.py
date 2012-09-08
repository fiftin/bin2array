"""
Использование: bin2cs_array <source_bin_file_name> <desc_cs_file_name>
Данные бинарного файла source_bin_file_name преобразует в массив байт на C# и сохранает его в 
файл desc_cs_file_name.
"""

import sys
import io
from io import FileIO

inputFileName = sys.argv[1]
outputFileName = sys.argv[2]
nInLine = 10
if len(sys.argv) >= 4:
    nInLine = int(sys.argv[4])

inputStream = FileIO(inputFileName, 'r')
outputFile = open(outputFileName, 'w')

inputData = inputStream.readall()
inputStream.close()

outputStr = ''

n = 0
for x in inputData:
    outputStr += str(ord(x)).rjust(3) + ", "
    n+=1
    if n >= nInLine:
        outputStr += '\n'
        n = 0

outputStr = "new byte[] {\n" + outputStr + "};"

outputFile.write(outputStr)
