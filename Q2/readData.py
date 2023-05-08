import sys


  

class information:
    def __init__(self,text):
        self.text = text
        # print("data in file is \n" +text +"\n")

    def countAlp(self):
        alphabet_freq= {}
        lower=0
        upper=0
        for a in text:
            if a in alphabet_freq:
                alphabet_freq[a] += 1
            else:
                alphabet_freq[a] = 1
            if a.islower:
                lower +=1
            elif a.upper:
                upper +=1
        print("all characters in file before change is :\n "+ str(alphabet_freq) +"\n")
        print("lower case :" + str(lower))        
        print("upper case :" + str(upper))  

    def change(self):
        tranToLow = self.text.lower()
        newText = tranToLow.replace('\t','_')
        print("text after change:\n" + newText)    
    def Display(self):
        self.change()
        self.countAlp()
        return



with open(sys.argv[1], 'r') as source:
    text = source.read()
    data = information(text)
    data.Display()
    
  