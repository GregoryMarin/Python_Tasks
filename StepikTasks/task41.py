from jinja2 import Template

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

per = Person('Fedor', 33)
tm = Template("I'm {{p.age}}, and my name is {{p.name}}. ")
msg = tm.render(p = per)

print(msg)