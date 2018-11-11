class Parent():
    def __init__(self, last_name, eye_color):
        print('Parent Constructor Called')
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print('Last Name: {}'.format(self.last_name))
        print('Eye Color: {}'.format(self.eye_color))

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print('Child Constructor Called')
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys
    #Overriding
    def show_info(self):
        print('# Informations #')
        print('Last Name: {}'.format(self.last_name))
        print('Eye Color: {}'.format(self.eye_color))
        print('Number of Toys: {}'.format(str(self.number_of_toys)))

#Object of Parent
billy_cyrus = Parent('Cyrus', 'Blue')
miley_cyrus = Child('Cyrus', 'Blue', 5)

miley_cyrus.show_info()
