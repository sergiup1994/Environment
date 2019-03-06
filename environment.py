 class River(Object):
     def __init__(self, n_room = 10, n_animal = 8):
         self._n_room = n_room
         self._eco = []
         self._n_bear = np.random.randint(0, n_animal)
         self._n_fish = n_animal - self._n_bear
         for i in range(self._n_bear):
             self.eco.append("B")   #Bear
         for i in range(self._n_fish):
             self.eco.append("F")   #Fish
         for i in range(n_room - n_animal):
             self._eco.append("N")   #None
         np.random.shuffle(self._eco)




     def get_eco(self):
         print("Eco Status: ", self._eco)
         print("Number of Bears: ", self._n_bear)
         print("Number of Fishes: ", self._n_fish)

     def add_bear(self, n):
         if self._eco[n] == "B":
             print("Rejected: Already Occupied.")
         elif self._eco[n] == "N":
             self._eco[n] == "B"
             self._n_bear += 1

         else:
             print("Bear eats Fish!")
             self._eco[n] = "B"
             self._n_bear += 1
             self._n_fish -= 1

     def add_fish(self, n):
         if self._echo[n] = "F":
             print("Rejected: Already occupied by another fish.")
         elif self._eco[n] == "N":
             self._eco[n] = "F"
             self._n_fish += 1

         else:
             print("Rejected: Already occupied by a bear.")
    
     def kill(self, n):
         if self._eco[n] == "B":
             self._eco[n] == "N"
             self._n_bear -= 1
         elif self._eco[n] == "F":
             self._eco[n] == "N"
             self._n_fish -= 1

         else:
             print("Already Empty")
