# class Vehicles():
    
#     color="white"

#     def __init__(self,max_speed,mileage):
#         self.max_speed=max_speed
#         self.mileage=mileage
#         self.seating_capacity=None
        
#     def seatingcapacity(self,seating_capacity):
#         self.seating_capacity=seating_capacity

        
#     def properties(self):
#         print("Max speed:",self.max_speed)
#         print("Mileage:",self.mileage)
#         print("Color:",Vehicles.color)
#         print("Seating capacity:",self.seating_capacity)

    


# car1=Vehicles(220,30)
# car1.seatingcapacity(5)
# car1.properties()


# car2=Vehicles(200,40)
# car2.seatingcapacity(4)
# car2.properties()



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



