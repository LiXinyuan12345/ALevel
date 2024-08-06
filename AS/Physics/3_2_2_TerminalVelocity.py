
    
# print table header
column_widths = [20,20,20,20,20,30]
column_titles = ["time(s)","G(N)","volcity(m/s)","drag force(N)","resultant force(N)","acceleration(m/s^2)"]
for i in range(len(column_titles)):
    print(column_titles[i].rjust(column_widths[i]),end=" ")
print("\n","-"*140)    

#print the process of free fall
m = 1
g = 10
v = 0
drag_force = 0
G = m * g
resultant_force= G - drag_force
acceleration   = resultant_force / m

for t in range(0,6):

    print( "t={}s".format(t).rjust(     column_widths[0]  ),end=" ")
    print("{}N".format(G).rjust(        column_widths[1]  ),end=" ")
    print( str(v).rjust(                column_widths[2]  ),end=" ")    
    print( str(drag_force) .rjust(      column_widths[3]  ),end=" ")   
    print( str(resultant_force).rjust(  column_widths[4]  ),end=" ")   
    if acceleration == 0:
        print( "0(Terminal volecity)".rjust(  column_widths[5]  ))
    else:
        print( str(acceleration).rjust(  column_widths[5]  ))

    # calc  next second
    v = v + acceleration
    #阻力每秒增加2N
    drag_force += 0.2*G
    resultant_force= G - drag_force
    acceleration   = resultant_force / m


    
print("-"*140)    
print( " ".format(t).rjust(                 column_widths[0]  ),end=" ")
print("G=mg".rjust(                         column_widths[1]  ),end=" ")
print("v1=v0+a".rjust(                      column_widths[2]  ),end=" ")    
print("+{}N/s".format(0.2*G) .rjust(        column_widths[3]  ),end=" ")   
print("Fr = G - drag force".rjust(          column_widths[4]  ),end=" ")   
print("a = resultant force / m".rjust(      column_widths[5]  ))   


