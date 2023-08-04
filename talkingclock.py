class Solution:    
    def ClockTalker(self, input_time):
            first_dict = {"1": "one:am", "2":"two:am", "3":"three:am", "4":"four:am", "5":"five:am", "6":"six:am", "7":"seven:am", "8":"eight:am", "9":"nine:am","l0":"ten:am","11":"eleven:am","12":"twelve:pm","13":"one:pm","14":"two:pm","15":"three:pm","16":"four:pm","17":"five:pm","18":"six:pm","19":"seven:pm","20":"eight:pm","21":"nine:pm","22":"ten:pm","23":"eleven:pm","24":"twelve:am"}
            ty_case = {"0":"oh", "2":"twenty", "3":"thirty", "4":"fourty", "5":"fifty"}
            teen_case={"1":"eleven","2":"twelve","3":"thirteen","4":"fourteen","5":"fifteen"}
            second_section = 0
            #type input_time: string
            #return type: string
            print(type(input_time))
            fisttime = 0
            timestamp = 0
            firstpart, secondpart = input_time.split(":")
            print(firstpart,secondpart)
            
            #TODO: Write code below to return a string with the solution to the prompt.
            pass

def main():
     str1=input()
     tc1= Solution()
     ans=tc1.ClockTalker(str1)
     print(ans)
    
if __name__ == '__main__': 
    main()
        
