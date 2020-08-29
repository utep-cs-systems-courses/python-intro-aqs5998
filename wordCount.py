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
        #Remove commas using regular expressions
        #line = re.sub(r'[^\-]', ' ', line)
        #Remove dashes using regular expressions
        line = re.sub(r'[\-]',' ', line)
        #Remove commas using regular expressions
        line = re.sub(r'[\,]',' ', line)
        #Remove quotations using regular expressions
        line = re.sub(r'[\"]',' ', line)
        #Remove non alphabetic characters using regular expressions
        line = re.sub(r'[^a-z]', ' ', line)
        #print("Line{}: {}".format(count, line.strip())) 
        count = count + 1
        word_containter = line.split()
        for word in word_containter:
            if word in word_map:
                word_map[word] += 1
            else: 
                word_map[word] = 1

        #iterate through the dictionary which I like to call map
        #for word in word_map:
            #print(word) 
            #print(word_map[word])
#remove symbols, move to lower case
#Itereate through the file
#While iterating through the file increment the "hasmap" or dicionary
#Pop the words by alphabetical order
#Write to the text file
    with open ('output.txt', 'w') as fp:
        for p in word_map.items():
            print(p)
            fp.write("%s:%s\n" % p)