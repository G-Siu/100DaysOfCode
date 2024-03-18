# Demonstration of using Global & Local Variables (SCOPE)

# Global Variable - Available through-out the whole program
nameGlobal = "Jimmy"

def PrintName():
    global nameGlobal
    nameLocal = "Paul" # Local Variable - Only available in function
    print(nameLocal)

print(nameGlobal)
PrintName()