
#       funnction with optional params
# addition
def add(line1 : int , line2 : int , line3 : int = 0 ):
    print(line1+line2+line3)
add(200,300)
add(200,300,500)

# subraction

def sub(line1 : int , line2 : int , line3 : int = 0 ):
    print(line1-line2-line3)
sub(200,300)
sub(200,300,500)

#multiplicaation


def mul(line1 : int , line2 : int , line3 : int = 0 ):
    print(line1*line2*line3)
mul(200,300)
mul(200,300,500)

#division


def div(line1 : int , line3 : int = 0 ):
    print(line1/line3)
div(200,300)
# div(200,300,500)

#function with arbitary params
    #addition
def add_arb(*line):
    res : int = 0
    for item in line:
        res = res + item
        print(res)
add_arb(1,22,56,23,5,789)

#     subracation

def sub_arb(*line):
    res : int = 0
    for items in line:
        res-=items
        print(res)
sub_arb(1,5,3,55,88)


#multilation

def mul_arb(*line):
    res : int = 0
    for items in line:
        res = res * items
        print(res)
mul_arb(5,6,55,8,44)


#funnction with key arbitary param

def key_arb(**line):
    name = "sai"
    email = "sai@gmail.com"
    gender = "male"
    mob_no = 9347630879
    area = "kurnool"
    print(name,email,gender,mob_no,area)
key_arb()

# returnable function
#   addition
def ddd(line : int = 0 , line1 : int = 0 , line2 : int = 0 ):
    return line+line1+line2
rees = add(56,4,5)
print(rees)

#   subraction
def dad(line1 : int = 0 , line2 : int = 0 , line3 : int = 0):
    return line1-line2-line3
ss = sub(5,8,9)
print(ss)

#   multilcation
def mm(line1 : int = 0 , line2 : int = 0 ,line3 : int = 0):
    return line1*line2*line3
mm = mul(5,2,1)
print(mm)

#   division
def dfdf(line : int = 0 , si : int = 0):
    return line/si
dd = div(56,89)
print(dd)



