# Ariel Tynan
# Euler Problem_045 Triangular, pentagonal, and hexagonal
# Started and Solved 4March2022


from numpy import sqrt 

hexNums = []
n = 100000 #number of hexNums analyzed

for i in range(1,n):
    pentCheck = 0.5*(sqrt(8*(i*(2*i - 1)) + 1) - 1) 
    triCheck = 1/6*(1 + sqrt(24*(i*(2*i - 1)) + 1))
    
    if triCheck.is_integer() and pentCheck.is_integer(): #hex/pent, hex/tri
        print(i, 2*i*i - i)

#Output gives next valid number, which is answer      


# Strategy
# Make array of hex numbers, they scale the fastest
# Check if each number is triangle and pentagonal
