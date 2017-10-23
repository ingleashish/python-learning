def a_decorator_func(func):
    print("this is decorator  func")

    def wrap_func():
        print("This is decorator wrapper func")
        func()

    return wrap_func

def func_need_decorator():
    print("This function need decorator")

@a_decorator_func
def func_need_decorator_using_decorator():
    print("this function called using decorator")


func_need_decorator()

func_need_decorator = a_decorator_func(func_need_decorator)
func_need_decorator()

func_need_decorator_using_decorator()
