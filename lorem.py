@decorated(somehow)
@extra
class Base(object):
    """This is the base class.
    """

    def method1(self):
        return

class Sub1(Base):
    """This is the first subclass.
    """

class MixinUser(Sub2, Mixin):
    """Overrides method1 and method2
    """

    def method1(self):
        return

    @manytimes
    @decorated
    def method2(self):
        return


def my_function():
    """Stand-alone function.
    """
    return

@deprecated
def my_decorated_function():
    """Stand-alone function.
    """
    return