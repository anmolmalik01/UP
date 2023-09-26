from subprocess import call
import pyscreenshot
  
name = 0
def callll():  
    global name
    name +=1
    image = pyscreenshot.grab()
    image.save(str(name) + '.png' )

callll()
callll()
