#extend()  >>>> used to add one list to another list
l1= ["python", "java"]
l2= ["django", "flask"]

l1.extend(l2)
print(l1)

x = [2,4,6,8]
y = [1,3,5,7]
y.extend(x)
print(y)

#remove() >>>>> it removes specific element from the list(first occurence element)
nums= [10,20,30,40,50,10]
nums.remove(10)
print(nums)


l1.remove("java")
print(l1)

#pop() >>>>> removes and returns the last element in the list
# >>>>> we remove using index values also 
n = [10,20,"python",18.9,"ram"]
print(n.pop(3))
print(n)

#ordering of elements 
#reverse()
n = [10,20,"python",18.9,"ram"]
n.reverse()
print(n)

print(n[::-1])

#sort()  >>>>it returns list elememnts according to the natural order
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
a.sort(reverse=True)
print(a)

s = ["dog","cat","fish","apple","boll"]
s.sort()
print(s)

#aliasing and clonning of an list object
var = [1,2,3,4]
v = var
print(v)

print(id(var))
print(id(v))

# 1 cloning by slice operater
var = [1,2,3,4,5]
y = var[:]
y[1] = 10
print(var)
print(y)
print(id(var))
print(id(y))

#2 cloning by copy() function

q = [9,8,7,6]
z = q.copy()
z[3] = 30
print(q)
print(z)
print(id(q))
print(id(z))

#Mathemetical operaters in list
#addition operater (+) >>>> similer to the extend()
c=[10,20,30]
d =[40,50,60]
print(c+d) 

#repetation(*)
print(c*2)

#comparing of two list 
c=[10,20,30]
d =[10,20,30,40]

print(c<d)
print(c>d)
print(c==d)


x = ["dog","rat","cat"]
y=["Dog","Rat","Cat"]
z= ["Cat","Rat","Dog"]

print(x==y)
print(x==z)
print(x!=z)