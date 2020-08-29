import sys,re

len_arg = len(sys.argv)

print(len_arg)
if len (sys.argv) != 3 :
    print "Usage: python ex.py input.txt output.txt"
    sys.exit (1)
else:
    input_File = ''
    output_File = ''
    #Read file
    try:  
        input_File = open(sys.argv[1], 'r') #r means read 
    except: 
        print('Cannot read %s' % sys.argv[1])
        sys.exit(-1)
    #Write to file
    try:
        output_File = open(sys.argv[2], 'w') #w means write
        print('Cannot write to %s' % sys.argv[2])
    except:
        sys.exit(-1)

#Create a empty dictionary 
    word_map = {}
    # Using readlines() 
    Lines = input_File.readlines() 
    
    count = 0
    # Strips the newline character 
    for line in Lines: 
        #Convert to lower case
        line = line.lower()
        #Remove symbols using regular expressions
        line = re.sub(r'[^\w]', ' ', line).
        print("Line{}: {}".format(count, line.strip())) 
        count = count + 1

#remove symbols, move to lower case
#Itereate through the file
#While iterating through the file increment the "hasmap" or dicionary
#Pop the words by alphabetical order
#Write to the text file