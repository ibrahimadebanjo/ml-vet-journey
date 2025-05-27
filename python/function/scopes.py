 # Local Variables cannot be used in global scope.
def spam1():
    eggs = 103094
spam1()
print(eggs)    
# local scopes cannot use variables in other local scopes 
def spam2():
    eggs = 90
    bacon()
    print(eggs)
def bacon():
    eggs = 0
    ham = 101
spam2()   
# Global variables cna be read from a local scope 
def read():
    print(cakes)
cakes = 30
read()
print(cakes)    
# Local and global variables wiht the same name
def spamLocal():
    eggs="spam Local"
    print(eggs)
def baconLocal():
    eggs = "bacon Local"
    print(eggs)
    spamLocal()
    print(eggs)
eggs= "global"
baconLocal()
print(eggs)    