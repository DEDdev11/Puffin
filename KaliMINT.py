import random
import time

print("welcome")
x=input("username: ")
input("password: ")
time.sleep(1)
print("loading...")
time.sleep(5)
print("USER",x,"/ kaliMINT / puffin / home")
while True:
 s=input(">>")
 if s==("/downloads"):
  time.sleep(3)
  print("KaliMINT-home.py")
  print("URLchecker.pme")
  print("[web]")
 elif s==("/downloads/web"):
    print("webopener.web.pme")
    print("/web.shortcut")
 elif s==("/documents"):
   time.sleep(3)
   print("puffinopenorder.txt")
   print("allcomands.txt")
 elif s==("/documents(puffinopenorder)"):
    print("puffin is so happy for you to join KaliMINT.")
 elif s==("/documents(allcomands)"):
    print("/documents [shows your documents], /documents(#your document#) [allows you to open the documents], /downloads [show your downloads], /downloads/~folder~ [opens the folders with the square brakets], /apps [shows your apps], /apps(#your app#)")          
 elif s==("/apps"):
    print("URLchecker")
 elif s==("/apps(URLchecker)"):
    print("please write a URL")
    input("URL please")
    print("yes this is a correct URL")
 elif s==("/web"):
     search=input("webx ")
     if search==("KaliMINT"):
         print("your software being run right now.")
     elif search==("puffin"):
         print("a forkable software that wants people to make there own version of")
     elif search==("what is a better puffin software kaliMINT or ubu 0.1.9?"):
         print("acording to puffin kaliMINT is more for coder and people and ubu is for hackers but KaliMINT is better due to its web conection with webx")
     elif search==("micromanor"):
         print("micromanor is a type of hacking that can be done by accsessing the users  bank and take lots of money with a line of code.")
     else:
        print("your search is scratching our heads please enter it again")
 else:
  print("error")
