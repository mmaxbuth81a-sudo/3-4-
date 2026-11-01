
def first(size, *args):
    for arg in args:
        return f'first ({size}, {args}) #Результат: {size + len(args)}'
print (first(5,"first", "second", "third"))

def second(size, **kwargs):
    for key in kwargs:
        return f'second ({size}, {kwargs}) #Результат: {size + len(kwargs)}'
print (second(3, comment_one="first", comment_two="second", comment_third="third"))