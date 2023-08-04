class Solution:    
    def ClockTalker(self, input_time):
            first_dict = {"1": "one:am", "2":"two:am", "3":"three:am", "4":"four:am":"5":"five:am"} 
            #type input_time: string
            #return type: string
            print(type(input_time))
            
            #TODO: Write code below to return a string with the solution to the prompt.
            pass

def main():
     str1=input()
     tc1= Solution()
     ans=tc1.ClockTalker(str1)
     print(ans)
    
if __name__ == '__main__': 
    main()
        
