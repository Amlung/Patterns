from Model import Person
import View

def showAll():
   people_in_db = Person.getAll()
   return View.showAllView(people_in_db)

def start():
   View.startView()
   inp = input()
   if inp == "y":
      return showAll()
   else:
      return View.endView()

if __name__ == "__main__":
   start()