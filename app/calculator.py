class Calculator:
    def add(self, x: int | float, y: int | float) -> int | float:

        return x + y

    def subtract(self, x: int | float, y: int | float) -> int | float:
        return x - y

    def multiply(self, x: int | float, y: int | float) -> int | float:
        return x * y

    def divide(self, x: int | float, y: int | float) -> int | float:
        """_summary_

        Args:
            x (int | float): _description_
            y (int | float): _description_

        Raises:
            ValueError: _description_

        Returns:
            int | float: _description_
        """
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y
