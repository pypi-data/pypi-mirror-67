"""
Tests for the utility functions.

Pyro - Python Remote Objects.  Copyright by Irmen de Jong (irmen@razorvine.net).
"""

import sys
import os
import unittest
import Pyro4.util
from Pyro4.configuration import config
from testsupport import *


# noinspection PyUnusedLocal
def crash(arg=100):
    pre1 = "black"
    pre2 = 999

    # noinspection PyUnusedLocal
    def nest(p1, p2):
        q = "white" + pre1
        x = pre2
        y = arg // 2
        p3 = p1 // p2
        return p3

    a = 10
    b = 0
    s = "hello"
    c = nest(a, b)
    return c


class TestUtils(unittest.TestCase):
    def testFormatTracebackNormal(self):
        try:
            crash()
            self.fail("must crash with ZeroDivisionError")
        except ZeroDivisionError:
            tb = "".join(Pyro4.util.formatTraceback(detailed=False))
            self.assertIn("p3 = p1 // p2", tb)
            self.assertIn("ZeroDivisionError", tb)
            self.assertNotIn(" a = 10", tb)
            self.assertNotIn(" s = 'whiteblack'", tb)
            self.assertNotIn(" pre2 = 999", tb)
            self.assertNotIn(" x = 999", tb)

    def testFormatTracebackDetail(self):
        try:
            crash()
            self.fail("must crash with ZeroDivisionError")
        except ZeroDivisionError:
            tb = "".join(Pyro4.util.formatTraceback(detailed=True))
            self.assertIn("p3 = p1 // p2", tb)
            self.assertIn("ZeroDivisionError", tb)
            if sys.platform != "cli":
                self.assertIn(" a = 10", tb)
                self.assertIn(" q = 'whiteblack'", tb)
                self.assertIn(" pre2 = 999", tb)
                self.assertIn(" x = 999", tb)

    def testPyroTraceback(self):
        try:
            crash()
            self.fail("must crash with ZeroDivisionError")
        except ZeroDivisionError:
            pyro_tb = Pyro4.util.formatTraceback(detailed=True)
            if sys.platform != "cli":
                self.assertIn(" Extended stacktrace follows (most recent call last)\n", pyro_tb)
        try:
            crash("stringvalue")
            self.fail("must crash with TypeError")
        except TypeError as x:
            x._pyroTraceback = pyro_tb  # set the remote traceback info
            pyrotb = "".join(Pyro4.util.getPyroTraceback())
            self.assertIn("Remote traceback", pyrotb)
            self.assertIn("crash(\"stringvalue\")", pyrotb)
            self.assertIn("TypeError:", pyrotb)
            self.assertIn("ZeroDivisionError", pyrotb)
            del x._pyroTraceback
            pyrotb = "".join(Pyro4.util.getPyroTraceback())
            self.assertNotIn("Remote traceback", pyrotb)
            self.assertNotIn("ZeroDivisionError", pyrotb)
            self.assertIn("crash(\"stringvalue\")", pyrotb)
            self.assertIn("TypeError:", pyrotb)

    def testPyroTracebackArgs(self):
        try:
            crash()
            self.fail("must crash with ZeroDivisionError")
        except ZeroDivisionError:
            ex_type, ex_value, ex_tb = sys.exc_info()
            x = ex_value
            tb1 = Pyro4.util.getPyroTraceback()
            tb2 = Pyro4.util.getPyroTraceback(ex_type, ex_value, ex_tb)
            self.assertEqual(tb1, tb2)
            tb1 = Pyro4.util.formatTraceback()
            tb2 = Pyro4.util.formatTraceback(ex_type, ex_value, ex_tb)
            self.assertEqual(tb1, tb2)
            tb2 = Pyro4.util.formatTraceback(detailed=True)
            if sys.platform != "cli":
                self.assertNotEqual(tb1, tb2)
            # old call syntax, should get an error now:
            self.assertRaises(TypeError, Pyro4.util.getPyroTraceback, x)
            self.assertRaises(TypeError, Pyro4.util.formatTraceback, x)

    def testExcepthook(self):
        # simply test the excepthook by calling it the way Python would
        try:
            crash()
            self.fail("must crash with ZeroDivisionError")
        except ZeroDivisionError:
            pyro_tb = Pyro4.util.formatTraceback()
        try:
            crash("stringvalue")
            self.fail("must crash with TypeError")
        except TypeError:
            ex_type, ex_value, ex_tb = sys.exc_info()
            ex_value._pyroTraceback = pyro_tb  # set the remote traceback info
            oldstderr = sys.stderr
            try:
                sys.stderr = StringIO()
                Pyro4.util.excepthook(ex_type, ex_value, ex_tb)
                output = sys.stderr.getvalue()
                self.assertIn("Remote traceback", output)
                self.assertIn("crash(\"stringvalue\")", output)
                self.assertIn("TypeError:", output)
                self.assertIn("ZeroDivisionError", output)
            finally:
                sys.stderr = oldstderr

    def clearEnv(self):
        if "PYRO_HOST" in os.environ:
            del os.environ["PYRO_HOST"]
        if "PYRO_NS_PORT" in os.environ:
            del os.environ["PYRO_NS_PORT"]
        if "PYRO_COMPRESSION" in os.environ:
            del os.environ["PYRO_COMPRESSION"]
        config.reset()

    def testConfig(self):
        self.clearEnv()
        try:
            self.assertEqual(9090, config.NS_PORT)
            self.assertEqual("localhost", config.HOST)
            self.assertEqual(False, config.COMPRESSION)
            os.environ["NS_PORT"] = "4444"
            config.reset()
            self.assertEqual(9090, config.NS_PORT)
            os.environ["PYRO_NS_PORT"] = "4444"
            os.environ["PYRO_HOST"] = "something.com"
            os.environ["PYRO_COMPRESSION"] = "OFF"
            config.reset()
            self.assertEqual(4444, config.NS_PORT)
            self.assertEqual("something.com", config.HOST)
            self.assertEqual(False, config.COMPRESSION)
        finally:
            self.clearEnv()
            self.assertEqual(9090, config.NS_PORT)
            self.assertEqual("localhost", config.HOST)
            self.assertEqual(False, config.COMPRESSION)

    def testConfigReset(self):
        try:
            config.reset()
            self.assertEqual("localhost", config.HOST)
            config.HOST = "foobar"
            self.assertEqual("foobar", config.HOST)
            config.reset()
            self.assertEqual("localhost", config.HOST)
            os.environ["PYRO_HOST"] = "foobar"
            config.reset()
            self.assertEqual("foobar", config.HOST)
            del os.environ["PYRO_HOST"]
            config.reset()
            self.assertEqual("localhost", config.HOST)
        finally:
            self.clearEnv()

    def testResolveAttr(self):
        config.REQUIRE_EXPOSE = True
        @Pyro4.core.expose
        class Exposed(object):
            def __init__(self, value):
                self.propvalue = value
                self.__value__ = value   # is not affected by the @expose

            def __str__(self):
                return "<%s>" % self.value

            def _p(self):
                return "should not be allowed"

            def __p(self):
                return "should not be allowed"

            def __p__(self):
                return "should be allowed (dunder)"

            @property
            def value(self):
                return self.propvalue

        class Unexposed(object):
            def __init__(self):
                self.value = 42

            def __value__(self):
                return self.value

        obj = Exposed("hello")
        obj.a = Exposed("a")
        obj.a.b = Exposed("b")
        obj.a.b.c = Exposed("c")
        obj.a._p = Exposed("p1")
        obj.a._p.q = Exposed("q1")
        obj.a.__p = Exposed("p2")
        obj.a.__p.q = Exposed("q2")
        obj.u = Unexposed()
        obj.u.v = Unexposed()
        # check the accessible attributes
        self.assertEqual("<a>", str(Pyro4.util.getAttribute(obj, "a")))
        dunder = str(Pyro4.util.getAttribute(obj, "__p__"))
        self.assertTrue(dunder.startswith("<bound method "))  # dunder is not private, part 1 of the check
        self.assertTrue("Exposed.__p__ of" in dunder)  # dunder is not private, part 2 of the check
        # check what should not be accessible
        self.assertRaises(AttributeError, Pyro4.util.getAttribute, obj, "value")
        self.assertRaises(AttributeError, Pyro4.util.getAttribute, obj, "propvalue")
        self.assertRaises(AttributeError, Pyro4.util.getAttribute, obj, "__value__")  # is not affected by the @expose
        self.assertRaises(AttributeError, Pyro4.util.getAttribute, obj, "_p")  # private
        self.assertRaises(AttributeError, Pyro4.util.getAttribute, obj, "__p")  # private
        self.assertRaises(AttributeError, Pyro4.util.getAttribute, obj, "a.b")
        self.assertRaises(AttributeError, Pyro4.util.getAttribute, obj, "a.b.c")
        self.assertRaises(AttributeError, Pyro4.util.getAttribute, obj, "a.b.c.d")
        self.assertRaises(AttributeError, Pyro4.util.getAttribute, obj, "a._p")
        self.assertRaises(AttributeError, Pyro4.util.getAttribute, obj, "a._p.q")
        self.assertRaises(AttributeError, Pyro4.util.getAttribute, obj, "a.__p.q")
        self.assertRaises(AttributeError, Pyro4.util.getAttribute, obj, "u")
        self.assertRaises(AttributeError, Pyro4.util.getAttribute, obj, "u.v")
        self.assertRaises(AttributeError, Pyro4.util.getAttribute, obj, "u.v.value")
        # try again but with require expose disabled
        config.REQUIRE_EXPOSE = False
        self.assertIsInstance(Pyro4.util.getAttribute(obj, "u"), Unexposed)
        self.assertEqual("<a>", str(Pyro4.util.getAttribute(obj, "a")))
        self.assertRaises(AttributeError, Pyro4.util.getAttribute, obj, "u.v")  # still not allowed to follow the dots
        self.assertRaises(AttributeError, Pyro4.util.getAttribute, obj, "u.v.value")  # still not allowed to follow the dots
        config.REQUIRE_EXPOSE = True

    def testUnicodeKwargs(self):
        # test the way the interpreter deals with unicode function kwargs
        def function(*args, **kwargs):
            return args, kwargs

        processed_args = function(*(1, 2, 3), **{unichr(65): 42})
        self.assertEqual(((1, 2, 3), {unichr(65): 42}), processed_args)
        processed_args = function(*(1, 2, 3), **{unichr(0x20ac): 42})
        key = list(processed_args[1].keys())[0]
        self.assertEqual(key, unichr(0x20ac))
        self.assertEqual(((1, 2, 3), {unichr(0x20ac): 42}), processed_args)


class TestMetaAndExpose(unittest.TestCase):
    def setUp(self):
        config.REQUIRE_EXPOSE = True

    def testBasic(self):
        o = MyThingFullExposed("irmen")
        m1 = Pyro4.util.get_exposed_members(o)
        m2 = Pyro4.util.get_exposed_members(MyThingFullExposed)
        self.assertEqual(m1, m2)
        keys = m1.keys()
        self.assertEqual(3, len(keys))
        self.assertIn("methods", keys)
        self.assertIn("attrs", keys)
        self.assertIn("oneway", keys)

    def testResetExposedCache(self):
        o = MyThingFullExposed("irmen")
        m1 = Pyro4.util.get_exposed_members(o)
        self.assertNotIn("newly_added_method", m1["methods"])
        MyThingFullExposed.newly_added_method = Pyro4.core.expose(lambda self: None)
        m2 = Pyro4.util.get_exposed_members(o)
        self.assertNotIn("newly_added_method", m2["methods"])
        Pyro4.util.reset_exposed_members(o)
        m3 = Pyro4.util.get_exposed_members(o)
        self.assertIn("newly_added_method", m3["methods"])

    def testGetExposedCacheWorks(self):
        class Thingy(object):
            def method1(self):
                pass
            @property
            def prop(self):
                return 1
            def notexposed(self):
                pass
        m1 = Pyro4.util.get_exposed_members(Thingy, only_exposed=False)
        def new_method(self, arg):
            return arg
        Thingy.new_method = new_method
        m2 = Pyro4.util.get_exposed_members(Thingy, only_exposed=False)
        self.assertEqual(m1, m2, "should still be equal because result from cache")
        m2 = Pyro4.util.get_exposed_members(Thingy, only_exposed=False, use_cache=False)
        self.assertNotEqual(m1, m2, "should not be equal because new result not from cache")

    def testPrivateNotExposed(self):
        o = MyThingFullExposed("irmen")
        m = Pyro4.util.get_exposed_members(o)
        self.assertEqual({"classmethod", "staticmethod", "method", "__dunder__", "oneway", "exposed"}, m["methods"])
        self.assertEqual({"prop1", "readonly_prop1", "prop2"}, m["attrs"])
        self.assertEqual({"oneway"}, m["oneway"])
        o = MyThingPartlyExposed("irmen")
        m = Pyro4.util.get_exposed_members(o)
        self.assertEqual({"oneway", "exposed"}, m["methods"])
        self.assertEqual({"prop1", "readonly_prop1"}, m["attrs"])
        self.assertEqual({"oneway"}, m["oneway"])

    def testNotOnlyExposed(self):
        o = MyThingPartlyExposed("irmen")
        m = Pyro4.util.get_exposed_members(o, only_exposed=False)
        self.assertEqual({"classmethod", "staticmethod", "method", "__dunder__", "oneway", "exposed"}, m["methods"])
        self.assertEqual({"prop1", "readonly_prop1", "prop2"}, m["attrs"])
        self.assertEqual({"oneway"}, m["oneway"])

    def testPartlyExposedSubclass(self):
        o = MyThingPartlyExposedSub("irmen")
        m = Pyro4.util.get_exposed_members(o)
        self.assertEqual({"prop1", "readonly_prop1"}, m["attrs"])
        self.assertEqual({"oneway"}, m["oneway"])
        self.assertEqual({"sub_exposed", "exposed", "oneway"}, m["methods"])

    def testExposedSubclass(self):
        o = MyThingExposedSub("irmen")
        m = Pyro4.util.get_exposed_members(o)
        self.assertEqual({"readonly_prop1", "prop1", "prop2"}, m["attrs"])
        self.assertEqual({"oneway", "oneway2"}, m["oneway"])
        self.assertEqual({"classmethod", "staticmethod", "oneway", "__dunder__", "method", "exposed",
                          "oneway2", "sub_exposed", "sub_unexposed"}, m["methods"])

    def testExposePrivateFails(self):
        with self.assertRaises(AttributeError):
            class Test1(object):
                @Pyro4.core.expose
                def _private(self):
                    pass
        with self.assertRaises(AttributeError):
            class Test3(object):
                @Pyro4.core.expose
                def __private(self):
                    pass
        with self.assertRaises(AttributeError):
            @Pyro4.core.expose
            class _Test4(object):
                pass
        with self.assertRaises(AttributeError):
            @Pyro4.core.expose
            class __Test5(object):
                pass

    def testExposeDunderOk(self):
        class Test1(object):
            @Pyro4.core.expose
            def __dunder__(self):
                pass
        self.assertTrue(Test1.__dunder__._pyroExposed)
        @Pyro4.core.expose
        class Test2(object):
            def __dunder__(self):
                pass
        self.assertTrue(Test2._pyroExposed)
        self.assertTrue(Test2.__dunder__._pyroExposed)

    def testClassmethodExposeWrongOrderFail(self):
        with self.assertRaises(AttributeError) as ax:
            class TestClass:
                @Pyro4.core.expose
                @classmethod
                def cmethod(cls):
                    pass
        self.assertTrue("must be done after" in str(ax.exception))
        with self.assertRaises(AttributeError) as ax:
            class TestClass:
                @Pyro4.core.expose
                @staticmethod
                def smethod(cls):
                    pass
        self.assertTrue("must be done after" in str(ax.exception))

    def testClassmethodExposeCorrectOrderOkay(self):
        class TestClass:
            @classmethod
            @Pyro4.core.expose
            def cmethod(cls):
                pass
            @staticmethod
            @Pyro4.core.expose
            def smethod(cls):
                pass
        self.assertTrue(TestClass.cmethod._pyroExposed)
        self.assertTrue(TestClass.smethod._pyroExposed)

    def testGetExposedProperty(self):
        o = MyThingFullExposed("irmen")
        with self.assertRaises(AttributeError):
            Pyro4.util.get_exposed_property_value(o, "name")
        with self.assertRaises(AttributeError):
            Pyro4.util.get_exposed_property_value(o, "c_attr")
        with self.assertRaises(AttributeError):
            Pyro4.util.get_exposed_property_value(o, "propvalue")
        with self.assertRaises(AttributeError):
            Pyro4.util.get_exposed_property_value(o, "unexisting_attribute")
        self.assertEqual(42, Pyro4.util.get_exposed_property_value(o, "prop1"))
        self.assertEqual(42, Pyro4.util.get_exposed_property_value(o, "prop2"))

    def testGetExposedPropertyFromPartiallyExposed(self):
        o = MyThingPartlyExposed("irmen")
        with self.assertRaises(AttributeError):
            Pyro4.util.get_exposed_property_value(o, "name")
        with self.assertRaises(AttributeError):
            Pyro4.util.get_exposed_property_value(o, "c_attr")
        with self.assertRaises(AttributeError):
            Pyro4.util.get_exposed_property_value(o, "propvalue")
        with self.assertRaises(AttributeError):
            Pyro4.util.get_exposed_property_value(o, "unexisting_attribute")
        self.assertEqual(42, Pyro4.util.get_exposed_property_value(o, "prop1"))
        with self.assertRaises(AttributeError):
            Pyro4.util.get_exposed_property_value(o, "prop2")

    def testSetExposedProperty(self):
        o = MyThingFullExposed("irmen")
        with self.assertRaises(AttributeError):
            Pyro4.util.set_exposed_property_value(o, "name", "erorr")
        with self.assertRaises(AttributeError):
            Pyro4.util.set_exposed_property_value(o, "unexisting_attribute", 42)
        with self.assertRaises(AttributeError):
            Pyro4.util.set_exposed_property_value(o, "readonly_prop1", 42)
        with self.assertRaises(AttributeError):
            Pyro4.util.set_exposed_property_value(o, "propvalue", 999)
        self.assertEqual(42, o.prop1)
        self.assertEqual(42, o.prop2)
        Pyro4.util.set_exposed_property_value(o, "prop1", 999)
        self.assertEqual(999, o.propvalue)
        Pyro4.util.set_exposed_property_value(o, "prop2", 8888)
        self.assertEqual(8888, o.propvalue)

    def testSetExposedPropertyFromPartiallyExposed(self):
        o = MyThingPartlyExposed("irmen")
        with self.assertRaises(AttributeError):
            Pyro4.util.set_exposed_property_value(o, "name", "erorr")
        with self.assertRaises(AttributeError):
            Pyro4.util.set_exposed_property_value(o, "unexisting_attribute", 42)
        with self.assertRaises(AttributeError):
            Pyro4.util.set_exposed_property_value(o, "readonly_prop1", 42)
        with self.assertRaises(AttributeError):
            Pyro4.util.set_exposed_property_value(o, "propvalue", 999)
        self.assertEqual(42, o.prop1)
        self.assertEqual(42, o.prop2)
        Pyro4.util.set_exposed_property_value(o, "prop1", 999)
        self.assertEqual(999, o.propvalue)
        with self.assertRaises(AttributeError):
            Pyro4.util.set_exposed_property_value(o, "prop2", 8888)

    def testIsPrivateName(self):
        self.assertTrue(Pyro4.util.is_private_attribute("_"))
        self.assertTrue(Pyro4.util.is_private_attribute("__"))
        self.assertTrue(Pyro4.util.is_private_attribute("___"))
        self.assertTrue(Pyro4.util.is_private_attribute("_p"))
        self.assertTrue(Pyro4.util.is_private_attribute("_pp"))
        self.assertTrue(Pyro4.util.is_private_attribute("_p_"))
        self.assertTrue(Pyro4.util.is_private_attribute("_p__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__p"))
        self.assertTrue(Pyro4.util.is_private_attribute("___p"))
        self.assertFalse(Pyro4.util.is_private_attribute("__dunder__"))  # dunder methods should not be private except a list of exceptions as tested below
        self.assertTrue(Pyro4.util.is_private_attribute("__init__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__call__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__new__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__del__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__repr__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__unicode__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__str__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__format__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__nonzero__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__bool__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__coerce__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__cmp__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__eq__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__ne__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__lt__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__gt__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__le__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__ge__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__hash__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__dir__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__enter__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__exit__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__copy__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__deepcopy__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__sizeof__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__getattr__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__setattr__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__hasattr__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__delattr__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__getattribute__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__instancecheck__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__subclasscheck__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__subclasshook__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__getinitargs__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__getnewargs__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__getstate__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__setstate__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__reduce__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__reduce_ex__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__getstate_for_dict__"))
        self.assertTrue(Pyro4.util.is_private_attribute("__setstate_from_dict__"))


if __name__ == "__main__":
    # import sys; sys.argv = ['', 'Test.testName']
    unittest.main()
