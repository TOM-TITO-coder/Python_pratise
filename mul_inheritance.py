class Father():
    def skills(self):
        print("gardening, porgramming")

class Mother():
    #def cooking(self):
    def skills(self):
        print("cooking, art")

class Child(Father, Mother):
    def sports(self):
        print("I enjoy sports")
        Father.skills(self)
        Mother.skills(self)

c = Child()
c.skills()
c.sports()
