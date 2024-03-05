import random
class RandomNumbers:
    def generateRandomnumbers(self,number):
        list = []
        for i in range(number):
           num = random.randint(0,100) #  Generate a random integer between 0 and  99
           list.append(num)
        return list
        
        
        
print(RandomNumbers().generateRandomnumbers(5))