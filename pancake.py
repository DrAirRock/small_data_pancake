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
                return self.Bottom_Pancake.return_center()
           else:
                raise ValueError('This is a unit pancake radius is 0 or 1')
        elif z==1:
            if( r == 1):
                return self.Top_Pancake.get_val(theta)
            elif( r==0):
                return self.Top_Pancake.return_center()
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

    def grow(self, grow_number): 
        center_top = self.Top_Pancake.return_center()
        center_bottom = self.Bottom_Pancake.return_center() 
       # print center_top
      #  print center_bottom
        size_top = self.Top_Pancake.get_size()
        size_bottom = self.Bottom_Pancake.get_size() 
        size_top += grow_number
        size_bottom += grow_number
        self.Top_Pancake.set_size(size_top)
        self.Bottom_Pancake.set_size(size_bottom)
        self.Top_Pancake.resize(grow_number , 1)
        self.Bottom_Pancake.resize(grow_number, 1)
        self.Top_Pancake.redefine_center(size_top-1)
        self.Bottom_Pancake.redefine_center(size_bottom-1)
        self.Top_Pancake.set_center(center_top)
        self.Bottom_Pancake.set_center(center_bottom)
        print self.Top_Pancake.return_center()
        print self.Bottom_Pancake.return_center()  

    def glution_free(self, value): 
        if value > 2:
            return true
        else: 
            return false

    def shrink(selg, shrink_number):
        center_top = self.Top_Pancake.return_center()
        center_bottom = self.Bottom.return_center() 
        size_top = self.Top_Pancake.get_size()
        size_bottom = self.Bottom_Pancake.get_size() 
        size_top -= grow_number
        size_bottom -= grow_number
        if (glution_free(size_top)): 
            self.Top_Pancake.set_size(size_top)
            self.Bottom_Pancake.set_size(size_bottom)
            self.Top_Pancake.redefine_center(size_top-1)
            self.Bottom_Pancake.redefine_center(size_bottom-1)
            self.Top_Pancake.set_center(center)
            self.Bottom_Pancake.set_center(center)
        else: 
            raise ValueError("okay panckaes have to be Gluttion free (you pancake be too small)")

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


    def redefine_center(self, value): 
        self.center = value

    def resize(self, value, direction): 
        if direction == 1: 
            for i in range(value): 
                #print i
                self.list.append(0)
        else: 
            ()

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

    def set_size(self, value): 
        self.size = value; 

    def to_string(self):
        return str(self.list)