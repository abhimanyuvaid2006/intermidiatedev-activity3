"""This module defines the State interface."""

# Tells Python to treat all type hints as strings rather than
# evaluating them when the module loads
from __future__ import annotations

# TYPE_CHECKING constant defined as True when static type
# checking is running (pylance VSCode Extension)
from typing import TYPE_CHECKING

# During type checking the import will be included; during runtime
# TYPE_CHECKING will be False and the import will not be used
if TYPE_CHECKING:
    from vending_machine.vending_machine import VendingMachine

__author__ = "Abhimanyu vaid"
__version__ = "1.0.0"

class State:
    """Represents the common interface for all vending machine states."""

    def receive_payment(self, machine: VendingMachine) -> None:
        """Accepts payment from the customer.

        Args:
            machine (VendingMachine): The vending machine that received
                the payment.
        """

    def select_item(self, machine: VendingMachine) -> None:
        """Customer selects the product to dispense.

        Args:
            machine (VendingMachine): The vending machine the customer
                selected the product from.
        """