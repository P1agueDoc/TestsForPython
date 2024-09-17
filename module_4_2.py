def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()
#inner_function() - can't do it "NameError: name 'inner_function' is not defined"