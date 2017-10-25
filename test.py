import pancake as p 
import randomcake as rc  

sdp = rc.random_pancake()
print "pancake print"
sdp.print_cake()
p_string = sdp.to_string()
print "string print"
print p_string
test_p = p.Pancake()
print "test pancake"
test_p.print_cake()
test_p.from_string(p_string)
test_p.print_cake()