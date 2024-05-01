import math
import statistics


#setting output frame

outputframe = None

def setoutputframe(frame):

    global outputframe

    outputframe = frame

#HCF of 2 numbers (meg)
def gcd(n1,n2):
    '''Finds the HCF of two numbers.
Takes two positive integers as input and returns a single positive integer (HCF).''' 
    if n1>n2:
        smaller = n2
    else:
        smaller = n1
    for i in range (1, smaller+1):
        if ((n1%i==0) and (n2%i==0)):
            hcf = i

    return hcf


#AP (meg)
def ap(a,r,n):
    '''Displays the Arithmetic Progression.
Accepts the starting term (float), common difference (float) and the number of terms (positive integer).
Returns a series.'''

    ap_list=[]

    for i in range(0,n):
        ele=(a+(i*r))
        ap_list.append(ele)  

    return (ap_list)


#GP (meg)
def gp(a,r,n):
    '''Displays the Geometric Progression.
Accepts the starting term (float), common ratio (float) and the number of terms (positive integer).
Returns a series.'''

    gp_list=[]

    for i in range(0,n):
        ele =(a*(r**i))
        gp_list.append(ele)

    return (gp_list)


#area of scalene triangle (kav)
def tri_area_scalene(a,b,c):
    '''Displays the Area of a Scalene Triangle.
Accepts the lengths of the three sides (positive floats).
Returns the area (positive float).'''

    s=(a+b+c)/2
    area=round(((s*(s-a)*(s-b)*(s-c))**0.5),3)
    
    return (area)


#area of isosceles triangle (kav)
def tri_area_isosceles(a,b):
    '''Displays the Area of an Isosceles Triangle.
Accepts the lengths of equal and unequal sides (positive sides).
Returns the area (positive float).'''

    area=round(((b/2)*(((4*a**2)-((b)**2))/4)**0.5),3)
    
    return(area)


#area of equilateral triangle (kav)

def tri_area_equilateral(a):
    ''''Displys the Area of an Equilateral Triangle.
Accepts the lengths of the equal sides (postive float).
Return the area (positive float).'''

    area= round((((3)**0.5/4)*a*a),3)
    
    return (area)


#area of right angled triangle (kav)

def tri_area_right(b,h):
    '''Displays the Area of a Right-Angled Triangle.
Accepts the base and height as inputs (positve floats).
Returns the area (positive float).'''

    area=round((0.5*b*h),3)
    
    return (area)


#area of circle (meg)

def circle_area(radius):
    '''Displays the Area of a Circle.
Accepts the radius as input (positive float).
Return the area (positive float).'''

    area = round((3.14*(radius**2)),3)
    
    return (area)



#area of trapezium (meg)

def trap_area(a,b,h):
    '''Displays the Area of a Trapezium.
Accepts the length of the parallel sides and height as inputs (positive floats).
Returns the area (positive float).'''

    area = round((0.5*(a+b)*h),3)
    return (area)


# area of hexagon (kav)
def area_hexagon(a):
    '''Displays the Area of a Regular Hexagon.
Accepts the length of the 6 equal sides as input (positive float).
Retuens the area (positive float).'''
  
    area=round(((3*(3**0.5)*(a**2))/2),3)
    
    return (area)


#area of ellipse (kav)

def area_ell(a,b):
    '''Displays the Area of an Ellipse.
Accepts the lengths of the semi major and semi axes (positive floats).
Returns the area (positive float).'''

    area=round((3.14*a*b),3)
    
    return (area)


#volume of sphere (meg)

def sphere_vol(radius):
    '''Displays the Volume of a Sphere.
Accepts the radius of the sphere (positive float).
Returns the volume (positive float).'''

    vol = round(((4/3)*3.14*(radius**3)),3)
    
    return (vol)


#volume of cylinder (kav)

def vol_cyl(r,h):
    '''Displays the Volume of a Cylinder.
Acepts the radius of the base and the height of the cylinder (positive floats).
Returns the volume (positive float).'''

    vol=round((3.14*r*r*h),3)
    
    return (vol)


#Volume of Ellipsoid (Mus)

def vol_ellipsoid(r1, r2, r3):
    '''Displays the Volume of an Ellipsoid.
Accepts the radii of the first, second and third axes (positive floats).
Returns the volume of the ellipsoid (positive float).'''

    vol = round((1.33 * math.pi * r1 * r2 * r3), 3)
    
    return vol


#Area of Tetrahedron (Mus)

def area_tetrahedron(side):
    '''Displays the Area of a Regular Tetrahedron.
Accepts the length of the equal sides (positive float).
Returns the area (positive float).'''
    
    vol = round((math.sqrt(3)*(side*side)), 3)
    
    return vol


#volume of cone (kav)

def vol_cone(h,r):
    '''Displays the Volume of a Cone.
Accepts the radius of the base and the height (positive floats).
Returns the volume (positive float).'''
  
    volume=round((0.33*(r**2)*h),3)
    
    return (volume)


#SFA of cube (kav)

def sfa_cube(a):
    '''Displays the Surface Area of a Cube.
Accepts the length of the equal sides (positive floats).
Returns the surface area (positive float).'''

    sfa=round((6*a*a),3)
    
    return (sfa)


#SFA of cuboid (kav)

def sfa_cuboid(l,b,h):
    '''Displays the Surface Area of a Cuboid.
Accepts the length, breadth and height (positive floats).
Returns the surface area (positive float).'''

    sfa=round((2*((l*b) + (b*h) + (l*h))),3)
    
    return(sfa)


#SFA of sphere (kav)

def sfa_sphere(r):
    '''Displays the Surface Area of a Sphere.
Accepts the radius of the sphere (positive float).
Returns the surface area (positive float).'''

    sfa=round((4*3.14*r*r),3)
    
    return (sfa)


#SFA of cylinder (kav)

def sfa_cyl(r,h):
    '''Displays the Surface Area of a Cylinder.
Accepts the radius of the base and the height of the cylinder (positive floats).
Returns the surface area (positive float).'''

    sfa=round((2*3.14*r*h),3)
    return (sfa)


#area of paralleogram using diagonals (meg)

def pllgm_area_diagonals(d1, d2, y):
    '''Displays the Area of a Parallelogram using its Diagonals to calculate.
Accepts the lengths of the diagonals (positive float) and the the angle situated between the diagonals (degrees).
Returns the area (positive float).'''

    y = (math.pi*y/180)
    area = round(0.5*d1*d2*(math.sin(y)), 3)
    
    return (area)


#area of parallelogram using base and height (meg)

def pllgm_area_bh(b,h):
    '''Displays the Area of a Parallelogram using its Base and Height to calculate.
Accepts the lengths of the base and height (positive float).
Returns the area (positive float).'''

    area = round(b*h, 3)
     
    return (area)
    

#area of parallelogram using trigonometry (meg)

def pllgm_area_trigo(a,b,x):
    '''Displays the Area of a Parallelogram using Trigonometry to calculate.
Accepts the lengths of the sides (positive float) and the angle situated between the angles (degrees).
Returns the area (positive float).'''
    
    x = (math.pi*x/180)
    area = round(a*b*math.sin(x), 3)
    
    return (area)


#to find mode(kav)

def find_mode(l):
    '''Displays the Mode (Entry with the Highest Frequency).
Accepts a list of entries/values (floats).
Returns a single value (float).'''
    
    return (statistics.mode(l))


#to find median (kav)

def find_median(l):
    '''Displays the Median (Middle-Most Entry).
Accepts a list of entries/values (floats).
Returns a single value (float).'''

    l.sort()
    n = len(l)
    if n%2==0:
        median=int(((n/2)+(((n/2)+1))/2))
        
        return (l[median])
    else:
        median=int((n+1)/2)

        print(median)
        
        return (l[median])

#to find mean (kav)
    
def find_mean(l):
    '''Displays the Mean (Average of All Entries).
Accepts a list of entries/values (floats).
Returns a single value (float).'''

    s=sum(l)
    n = len(l)
    mean=s/n
    
    return (mean)


#profit and loss

def profit_loss(cp, sp):
    '''Displays the Profit or Loss Percentage.
Acccepts the Cost and Selling Price (positive floats).
Returns the percentage (positive float).'''

    profit=sp-cp
    if (profit<=0):
        loss=cp-sp
        lossp=round((loss*100)/cp, 3)
        return("The loss percent is ",lossp)
    else :
        profitp=round((profit*100)/cp, 3)
        return("The profit percentage is",profitp)


# sum of cubes of first n numbers (kav)

def sum_cubes(n):
    '''Displays the sum of the cubes of the values from 1 till n.
Accepts the number of terms (positive integer).
Returns the sum (positive integer).'''

    sum=((n*(n+1))/2)**2
    return (sum)


#Sum of squares of first n nos (kav)

def sum_squares(n):
    '''Displays the sum of the squares of the values from 1 till n.
Accepts the number of terms (positive integer).
Returns the sum (positive integer).'''
    
    sum=(n*(n+1)*((2*n)+1))/6
    return (sum)


# sum of first n numbers  (kav)

def sum_num(n):
    '''Displays the sum of the values 1 till n.
Accpets the number of terms (positive integer).
Returns the sum (positive inetger).'''
    sum=(n*(n+1))/2
    return (sum)


#check divisibility (meg)

def divisibility(num):
    '''Displays whether the entered number is divisible by 2, 3, 5, 7 and 11.'''

    if(num%2==0):
        div2=("divisible by 2")
    else:
        div2=("not divisible by 2")

    if(num%3==0):
        div3=("divisible by 3")
    else:
        div3=("not divisible by 3")

    if(num%5==0):
        div5=("divisible by 5")
    else:
        div5=("not divisible by 5")

    if(num%7==0):
        div7=("divisible by 7")
    else:
        div7=("not divisible by 7")

    if(num%11==0):
        div11=("divisible by 11")
    else:
        div11=("not divisible by 11")

    return (div2, div3, div5, div7, div11)



#degree to radian conversion (mus)

def deg_rad(degree):
    '''Converts the entered degree value to radians (positive float).'''

    pi=22/7
    radian = round(degree*(pi/180), 3)

    return(radian)


#radian to degree conversion (mus)

def rad_deg(radian):
    '''Converts the entered radian value to degrees (positive float).'''

    pi=22/7
    degree = round(radian*(180/pi), 3)

    return(degree)


#volume of rectangular prism (mus)

def vol_prism(l,b,w):
    '''Displays the Volume of a Rectangular Prism.
Accepts the length, breadth and height of the prism (positive floats).
Returns the area (positive float).'''

    vol=(l*w*h)

    return(vol)


#pie chart (meg)

def pie_chart(args):
    '''Displays the graphical representation of the entered values.
The values are converted to percentages which are then mapped onto a chart.'''


    import tkinter as tk


    lbl = tk.Label(outputframe, text = "Pie Chart", font = 'Garamond 13 bold', bg = '#fafac3')
    lbl.grid(row = 0, column = 4)

    c = tk.Canvas(outputframe, width = 200, height = 200, bg = '#fafac3')
    c.grid(row = 1, column = 4)

    sectors = args

    angles = []

    coord = 10, 10, 200, 200

    colors = []

    legend = []
    
    start = 0x63f786

    for i in range(0, 20):
        colors.append('#' + format(start + (i*30), 'X'))


    for i in range (0, len(sectors)):

        angles.append((sectors[i])*360/100)
        
        if i == 0:

            c.create_arc(coord, fill = colors[i], outline = 'black', start = 0, extent = angles[i])

            prev_angle = angles[i]

        else:
          
            c.create_arc(coord, fill = colors[i], outline = 'black', start = prev_angle, extent = angles[i])

            prev_angle += angles[i]

        legend.append(tk.Label(outputframe, bg = colors[i], fg = 'black', text = str(sectors[i])+'%'))
        legend[i].grid(row = i+2, column = 0)
  

#roots or quadratic equation (meg)

def qdrtc_eqn(a,b,c):
    import math

    dscrm = ((b**2)-(4*a*c))

    if (dscrm < 0):
        root1=(-b/(2*a), "+i")
        root2=(-b/(2*a), "-i")

    else:
        root1 = round((-b+math.sqrt(dscrm))/(2*a),3)
        root2 = round((-b-math.sqrt(dscrm))/(2*a),3)

        
    return(root1, root2)
