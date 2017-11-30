import pancake as p 
import randomcake as rc  


print "python Pancke testing:::::::\n"
sdp = rc.random_pancake()
sdp.print_cake()
p_string = sdp.to_string()
print "string print"
print p_string
test_p = p.Pancake()
print "test pancake"
test_p.print_cake()
test_p.from_string(p_string)
test_p.print_cake()
print "test adding"
test_p.set_val(1,4,1,5000)
test_p.set_val(1,12,1,5000)
test_p.set_val(1,24,0,5000)
test_p.set_val(0,0,1,5000)
test_p.set_val(0,0,0,5000)
test_p.print_cake()
print "yo :"
print test_p.get_val(1,25,0)