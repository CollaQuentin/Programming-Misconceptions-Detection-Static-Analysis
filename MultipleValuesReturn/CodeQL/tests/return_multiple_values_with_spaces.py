def foo(a, b):
    def bar(a, b):
        return   a  , b
    return bar(a, b)