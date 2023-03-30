import module as m
import guess_number as g
# print(m.max_number(4, 6, 34, 53, 67))

# g.guess_number(5)
# m.string('Gross')


def func_outer():
    x = 2
    print('x равно', x)
    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print('Локальное x сменилось на', x)
func_outer()