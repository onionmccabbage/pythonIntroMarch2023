# it is extremely easy to write to a file
# we need a file access object
fao = open('easy.txt', 'at') # 'at' means append text
# NB the text file will exist in the SAME location as where we invoke Python
print('are we there yet', file=fao)
# its a reeally good idea to tidy up
fao.close() # this drops our file access object and releases resource

fin = open('easy.txt', 'rt') # 'rt' means read text
# received = fin.read() # reads in from the file as a SINGLE text string
# received = fin.readlines() # reads in from the file as a list of text strings
received = fin.readline(5) # reads in from the file as the next line (or just n characters)
fin.close()

print(received)