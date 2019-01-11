from mock import MagicMock

def test_with_metaclass():
    import momox.compat

    mc_new_called = MagicMock()

    class Meta(type):
        def __new__(mcls, name, bases, attrs):
            mc_new_called.assert_not_called()
            mc_new_called()

            assert name == 'TestClass'
            assert bases == (object,)
            assert attrs['testprop'] == 'hello'
            assert '__init__' in attrs

            new_attrs = attrs.copy()
            new_attrs['added_prop'] = 'world'

            return type.__new__(mcls, name, bases, new_attrs)

    class TestClass(momox.compat.with_metaclass(Meta, object)):
        testprop = 'hello'
        def __init__(self, var):
            self.var = var

    tc = TestClass(42)
    assert tc.var == 42
    assert tc.testprop == 'hello'
    assert tc.added_prop == 'world'

    tc2 = TestClass(45)

    mc_new_called.assert_called_once()
