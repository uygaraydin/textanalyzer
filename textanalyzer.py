
class TextAnalyzer(object):

    def __init__(self,text):
        newtext=text.replace("."," ").replace(","," ").replace("!"," ").replace("?"," ")
        newtext=newtext.lower()
        self.text=newtext
         
    def freqAll(self):        
        wordlist=self.text.split(" ")

        freq={}

        for word in wordlist:
            freq[word]=wordlist.count(word)

        
        return freq
    def freqOf(self,word):

        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
stringg="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet." 
text1=TextAnalyzer(stringg)
print(text1.text)   
freq=text1.freqAll()
print(freq)  
print(text1.freqOf("ipsum"))



