file = open("mylife.txt", "a") #OPENING FILE
resp = "yes" #DEFAULT VALUE TO INITIATE THE LOOP
while resp == "yes":
    def file_updater(): #CALLABLE SET OF FUNCTIONS FOR REPETITION
        sentence = input("Input the sentence you want to write on the file: ") #ASKING FOR SENTENCE
        file.write(f"{sentence}\n") 
    file_updater() #CALLING THE FUNCTION
    resp = input("Are there more lines? yes/no: ") #CONFIRMATION OF NEW VALUE OF "resp"
file.close() #CLOSE TO AVOID CORRUPTION
