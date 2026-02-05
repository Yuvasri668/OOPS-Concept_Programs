#Multilevel Inheritance

class grand_father:
    def __init__(self,property):
        self.grand_father_property=property

    def display_property1(self):
        print("The grand father is:",self.grand_father_property)

class father(grand_father):
    def __init__(self,property,g_f_property):
        self.father_property=property
        super().__init__(g_f_property)

    def display_property2(self):
        print("The father is:",self.father_property)

class son(father):
    def __init__(self,property,f_property,g_f_property):
        self.property=property
        super().__init__(f_property,g_f_property)

    def display_property3(self):
        print("The son property is:",self.property)

son.obj=son("bike","car","house")
son.obj.display_property1()
son.obj.display_property2()
son.obj.display_property3()