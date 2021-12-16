""" This is the increment function"""
from calc.history.calculations import Calculations
class Calculator:
    """ This is the Calculator class"""
    @staticmethod
    def get_last_result_value():
        """ This is the gets the result of the calculation"""
        return Calculations.get_last_calculation_result_value()

    @staticmethod
    def addition(tuple_values: tuple):
        """ adds list of numbers"""
        Calculations.add_addition(tuple_values)
        return True

    @staticmethod
    def subtraction(tuple_values: tuple):
        """ subtract a list of numbers from result"""
        Calculations.add_subtraction(tuple_values)
        return True

    @staticmethod
    def multiplication(tuple_values: tuple):
        """ multiplication number from result"""
        Calculations.add_multiplication(tuple_values)
        return True

    @staticmethod
    def division(tuple_values: tuple):
        """ division number from result"""
        Calculations.add_division(tuple_values)
        return True

    # @staticmethod
    # def getHistory():
    # """ Get history """
    # ret_list = []
    #    ret_list.append(Calculations.history[i].get_result())
    # return ret_list
