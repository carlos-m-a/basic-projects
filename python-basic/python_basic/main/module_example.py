"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

Typical usage example:

  myobject = MyClass()
  bar = myobject.public_method()
"""


CONSTANT_VARIABLE = 3.1416
"""int: Module level variable documented inline.

The docstring may span multiple lines. The type may optionally be specified
on the first line, separated by a colon.
"""

module_level_variable = 98765
"""Another docstring
"""


def model_function(param1: int, param2: str) -> bool:
    """Module level function documented inline.

    Here longer description of the function. Function parameters should be 
    documented in the ``Args`` section. The name of each parameter is required. 
    The type and description of each parameter is optional, but should be included
    if not obvious.

    Args:
        param1: The first parameter.
        param2: The second parameter.

    Returns:
        The return value. True for success, False otherwise.

    Raises:
        ValueError: If a paramaeter violates restriontions

    """
    pass


def model_function_yield(param1:int) -> int:
    """Other function docstring

    Args:
        param1: The first parameter.

    Yields:
        The yield value. True for success, False otherwise.

    """
    yield param1




class MyClass:
    """This is the summary line

    This is the further elaboration of the docstring. It could be
    require several lines.

    Attributes:
        instance_var (int): Some explanation

        class_var (str): Some explanation 
    """

    class_var = ''

    def __init__(self, var1):
        self._instance_var = var1

    def public_method(self, var1:int) -> int:
        """This is the summary line

        This is the further elaboration of the docstring. It could be
        require several lines.
        
        Complexity: T(n) = O(n)  <<average case>>
                    S(n) = O(log n)
                    *n = size of ...

        Args:
            var1 (int): indicates what means this variable
                0 <= var <= 1000

        Returns:
            Explanation about what is returned

        Raises:
            ValueError: If a specific restriction is violated
        """
        return var1 * 1
    
    @classmethod
    def public_class_method(cls, var1:str) -> None:
        """Some doc comments
        More description
        """
        cls.class_var = var1

    def _private_method(self):
        pass

    def __str__(self):
        return str(self._instance_var)
    
    @property
    def instance_var(self):
        return self._instance_var

    @instance_var.setter
    def instance_var(self, value:int):
        if(value < 0):
            raise ValueError("Negative integer")
        self._instance_var = value