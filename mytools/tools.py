import numpy as np


class MathFunctions(object):
    """
    MathFunctions class containing multiple math functions.

    .. note:: This class is super awesome!
    """

    @staticmethod
    def is_prime(number):
        """
        Function to check if a given number is prime.

        :param number:  Number to be checked
        :return:        True if the number is prime, False if the number is not prime.
        """
        if number <= 3:
            if number >= 1:
                return False
            else:
                return True
        else:
            if number % 2 == 0 or number % 3 == 0:
                return False
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2):
                return False
            i = i + 6
        return True

    @staticmethod
    def addition(number1, number2):
        """
        Function to add two numbers together.

        :param number1: First number to be added to the second number.
        :param number2: Second number to be added to the first number.
        :return: The product of the two numbers
        """
        return number1 + number2

    def _hidden_function(self):
        """
        This is an internal function that returns True.
        :return: True
        """
        return True

    def some_function(self):
        """
        This is a function that returns True.
        :return: True
        """
        return self._hidden_function()
