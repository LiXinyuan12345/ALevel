def elastic_collision(m1,u1,m2,u2, v1):
    print("elastic collision test")
    print("-"*80)
    print("before:  m1={}kg   u1={}m/s ; m2={}kg   u2={}m/s ".format(m1,u1,m2,u2))
    print("after:   v1={}m/s ".format(v1))
    print("-"*80)

    before_total_momentum = m1*u1+m2*u2
    before_total_Ke       = 1/2*m1*(u1**2) + 1/2*m2*(u2**2)
    print("Momentum(before):  = m1 * u1 + m2 * u2 = {} kgm/s".format(  round(before_total_momentum,3) ))
    print("Ke(before):        = 1/2* m1 * u1^2 + 1/2 * m2 * u2^2 = {} J".format( round(before_total_Ke,3)) )
    print("-"*80)

    v2 = (before_total_momentum - m1 * v1)/m2
    after_total_momentum =  m1*v1+m2*v2
    after_total_Ke       = 1/2*m1*(v1**2) + 1/2*m2*(v2**2)
    print("v2 = {} m/s".format( round(v2,3)) )
    print("Momentum(after):   = m1 * v1 + m2 * v2 = {} kgm/s ".format( round(after_total_momentum,3)) )
    print("Ke(after):         = 1/2* m1 * v1^2 + 1/2 * m2 * v2^2 = {} J".format( round(after_total_Ke,3)) )

    if  round(before_total_Ke,3) == round(after_total_Ke,3):
        print("---> elastic collision")
    else:
        print("---> inelastic collision")


elastic_collision(m1=7.9, u1=0 , m2=2.7, u2=10, v1=5.1 )
#elastic_collision(m1=0.4, u1=0.36 , m2=0.4, u2=-0.36, v1=-0.36 )
print()
print()
#elastic_collision(m1=0.14, u1=3.54 , m2=0.62, u2=0, v1=0 )