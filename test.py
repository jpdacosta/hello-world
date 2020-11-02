class JPTest:
    x=0
    y=0

    def __init__(self,x,y):
        self.x = x
        self.y = y
        #print(x)
        #print(y)

    def mymessage(self,message):
        print(str(message))

    def sum(self):
        print(x)
        print(y)
        ans = x+y
        return ans

message = input("Enter a message: ")
mytest = JPTest(1,2)
mytest.mymessage(message)
mytest.mymessage(mytest.sum)