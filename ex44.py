class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

    def override(self):
        print "Parent override()"

    def alterred(self):
        print "Parent alterred()"

class Child(Parent):

    def override(self):
        print "Child override()"

    def alterred(self):
        print "Child, BEFORE PARENT alterred()"
        super(Child, self).alterred()
        print "Child, AFTER PARENT alterred()"

dad = Parent()
son = Child()

dad.alterred()
son.alterred()
