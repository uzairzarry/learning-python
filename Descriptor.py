class SerializerMethodField:
    def __init__(self, method_name):
        self.method_name = method_name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        method = getattr(instance, self.method_name)
        return method()

class MyClass:
    def __init__(self, value):
        self.value = value

    def get_my_value(self):
        return self.value * 2
    def __str__(self) -> str:
        return f"{self.__class__.__name__}"

    my_value = SerializerMethodField('get_my_value')

obj = MyClass(10)

print(obj.my_value)

