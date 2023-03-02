from jinja2 import Template
name = "Gregory"
tm = Template("Hi {{name}}")
msg = tm.render(name=name)
print(msg)