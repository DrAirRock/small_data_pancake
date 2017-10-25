#implamentaion of a unit pancake of size 7 which is classifed as small
class Pancake:
    def __init__(self):
        self.Top_Pancake = layer_array()
        self.Bottom_Pancake = layer_array()

    def get_val(self,r,theta,z):
        if z==0:
           if (r == 1):
                return self.Bottom_Pancake.get_val(theta)
           elif (r ==0):
                return self.Bottom_Pancake.center
           else:
                raise ValueError('This is a unit pancake radius is 0 or 1')
        elif z==1:
            if( r == 1):
                return self.Top_Pancake.get_val(theta)
            elif( r==0):
                return self.Top_Pancake.return_center
            else:
                raise ValueError('This is a unit pancake radius is 0 or 1')
        else:
            raise ValueError('Pancakes are short, and therefore only one high')
    #add item to the index of the pancake
    def set_val(self,r,theta,z,value):
        if z==0:
           if (r ==1 ):
                self.Bottom_Pancake.set_val(theta,value)
           elif(r==0):
                self.Bottom_Pancake.set_center(value)
           else:
                raise ValueError('This is a unit pancake radius is 0 or 1')
        elif(z==1):
            if( r == 1):
                self.Top_Pancake.set_val(theta,value)
            elif (r == 0):
                return self.Top_Pancake.set_center(value)
            else:
                raise ValueError('This is a unit pancake radius is 0 or 1')
        else:
            raise ValueError('Pancakes are short, and therefore only one high')

    def print_cake(self):
        print "Top: "
        self.Top_Pancake.print_layer()
        print "Bottom: "
        self.Bottom_Pancake.print_layer()
    
    def to_string(self):
        Pancake_array = []
        Pancake_array.append(self.Top_Pancake.to_string())
        Pancake_array.append(self.Bottom_Pancake.to_string())
        print Pancake_array
        return str(Pancake_array)

    def from_string(self, Pancake_string): 
        Pancake_array = Pancake_string.split(',')
        Top_p = Pancake_array[:self.Top_Pancake.get_size()]
        for index in range(len(Top_p)-1): 
            self.Top_Pancake.set_val(index,Top_p[index])
        self.Top_Pancake.set_center(Top_p[self.Top_Pancake.get_size()-1])

        Bottom_p= Pancake_array[self.Bottom_Pancake.get_size():]
        for index in range(len(Bottom_p)-1):
            self.Bottom_Pancake.set_val(index,Bottom_p[index])
        self.Bottom_Pancake.set_center(Bottom_p[self.Bottom_Pancake.get_size()-1])

        

#this is a circular array with a center element:
class layer_array:

    def __init__(self):
        self.size = 7
        self.value = 0
        self.list = []
        for i in range(self.size):
            self.list.append(self.value)
        self.center = self.size - 1

    #these are kosher pancakes
    def make_kosher(self,index):
        #make it circlular
        index = index % (self.size - 1)
        return index
    
    def get_val(self,index):
        index = self.make_kosher(index)
        return self.list[index]

    def set_val(self,index,value):
        index = self.make_kosher(index)
        self.list[index] = value 

    def return_center(self):
        return self.list[self.center]

    def set_center(self,value):
        self.list[self.center] = value

    def print_layer(self):
        print "Edge: "
        for item in range(self.size - 1):
            print self.list[item]
        print "Center: "
        print self.list[self.center]
        print "\n"

    def get_size(self):
        return self.size
    
    def to_string(self):
        return str(self.list)