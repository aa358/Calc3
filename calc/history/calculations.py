"""Calculation history Class"""
from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division


class Calculations:
    """Calculations class manages the history of calculations"""
    history = []

    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """clear the history of calculations"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """get number of items in history"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation_object():
        """get last calculation"""
        return Calculations.history[-1]

    @staticmethod
    def get_last_calculation_result_value():
        """get last calculation"""
        calculation = Calculations.get_last_calculation_object()
        return calculation.get_result()

    @staticmethod
    def get_first_calculation():
        """get first calculation"""
        return Calculations.history[0]

    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(calculation):
        """ get a generic calculation from history"""
        return Calculations.history.append(calculation)

    @staticmethod
    def add_addition(values):
        """create an addition and add object to history using factory method create"""
        Calculations.add_calculation(Addition.create(values))
        # Get the result of the calculation
        return True

    @staticmethod
    def add_subtraction(values):
        """create a subtraction and add object to history using factory method create"""
        Calculations.add_calculation(Subtraction.create(values))
        return True

    @staticmethod
    def add_multiplication(values):
        """Add a multiplication and add object to history using factory method create"""
        Calculations.add_calculation(Multiplication.create(values))
        return True

    @staticmethod
    def add_division(values):
        """Add a division and add object to history using factory method create"""
        Calculations.add_calculation(Division.create(values))
        return True
