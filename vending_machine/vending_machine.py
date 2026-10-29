"""Defines the VendingMachine class."""

from vending_machine.state import State
from vending_machine.no_payment_state import NoPaymentState
from vending_machine.out_of_stock_state import OutOfStockState

__author__ = "abhimanyu vaid"
__version__ = "1.0.0"

class VendingMachine:
    """Represents a vending machine."""

    def __init__(self, product_count: int) -> None:
        """Initializes a new instance of the VendingMachine class."""

        self.__product_count: int = product_count
        self.state = NoPaymentState()

    @property
    def state(self) -> State:
        """Returns the current state of the vending machine."""

        return self.__state

    @state.setter
    def state(self, state: State) -> None:
        """Sets the state of the vending machine."""

        self.__state = state

    def receive_payment(self) -> None:
        """Accepts pay payment from the customer."""

        self.state.receive_payment(self)

    def select_item(self) -> None:
        """Customer selects the product to dispense."""

        self.state.select_item(self)

    def dispense_product(self) -> None:
        """Dispenses the product to the customer."""

        if self.__product_count == 0:
            self.output_to_display("ERROR: OUT OF STOCK")
            self.state = OutOfStockState()
        else:
            self.__product_count -= 1
            self.output_to_display("ENJOY YOUR ITEM")

            self.state = OutOfStockState() \
                    if self.__product_count <= 0 else \
                    NoPaymentState()

    def output_to_display(self, message: str,
                          include_line_break: bool=True) -> None:
        """Outputs message to the machines display.

        If the message is blank, nothing is output to the display.

        Args:
            message (str): The message to display on the screen.
            include_line_break (bool): When True, includes a new line
                character at the end of message; otherwise a blank
                string.
        """

        if message.strip() != "":
            print(f"{message}{"\n" if include_line_break else ""}", end="")