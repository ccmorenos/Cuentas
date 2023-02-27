"""Object to control the check."""
from data_mng import csv_saver


class CheckManager():
    """Object to control the ckeck."""

    def __init__(self, check_file, delimiter=","):
        """Create the check manager."""
        self.check_file = check_file

        header = ["Concept", "Value"]

        self.saver = csv_saver.CSVSaver(
            self.check_file, header, delimiter
        )

        self.total_spent = self.saver.get_column_values("Value").sum()

    def add_entry(self):
        """Add a new entry."""
        try:
            concept = input("Entry concept: ")
            value = float(input("Entry value: $"))

            print(
                "New entry:\n"
                f"Concept: {concept}\n"
                f"Value: $ {self.money_print(value)}\n"
            )

            while True:
                confirm = input("Confirm [y]/n: ")

                if confirm in ["", "Y", "y", "yes", "YES", "Yes"]:
                    self.saver.fill_row([concept, value])
                    self.saver.add_row_and_save()

                    self.total_spent = self.saver.get_column_values(
                        "Value"
                    ).sum()

                    return True

                elif confirm in ["N", "n", "no", "NO", "No"]:
                    return False

        except KeyboardInterrupt:
            return False

    def check_remove(self, ID):
        """Check the row removal."""
        print(
            "Entry to be removed:\n"
            f"Index: {ID}\n"
            "Concept: "
            f"{self.saver.get_column_value('Concept', ID)}\n"
            "Value: $ "
            f"{self.money_print(self.saver.get_column_value('Value', ID))}\n"
        )

        while True:
            confirm = input("Confirm [y]/n: ")

            if confirm in ["", "Y", "y", "yes", "YES", "Yes"]:
                self.saver.remove_row(ID)
                self.saver.save_data()

                self.total_spent = self.saver.get_column_values(
                    "Value"
                ).sum()

                break

            elif confirm in ["N", "n", "no", "NO", "No"]:
                break

    def remove_entry(self):
        """Add a new entry."""
        try:
            while True:

                concepts = self.saver.get_column_values("Concept")
                values = self.saver.get_column_values("Value")
                indexes = self.saver.get_index()

                message = (
                    "Actual entries in the check:\n"
                    "      Index | Concept | Value\n"
                    "     -------------------------\n"
                )

                for (concept, value, index) in zip(concepts, values, indexes):
                    message += (
                        " " * 6 +
                        f"{index} | {concept} | $ {self.money_print(value)}\n"
                    )

                print(message)

                try:
                    key_input = input(
                        "Enter the ID of the row to be removed.\n"
                        "Type 'q' to go back to the main menu.\n"
                        ">>> "
                    )
                    ID = int(key_input)

                except ValueError:
                    if key_input == "q":
                        break
                    continue

                if ID in indexes:
                    self.check_remove(ID)

        except KeyboardInterrupt:
            return

    def money_print(self, val):
        """Get the string for money value."""
        return f"{val:,.2f}".replace(",", " ")

    def get_check(self):
        """Print the check."""
        concepts = self.saver.get_column_values("Concept")
        values = self.saver.get_column_values("Value")

        message = "Check:\n"

        for (concept, value) in zip(concepts, values):
            l_chk = len(concept) + len(self.money_print(value))

            message += (
                f"      {concept} " + "." * (47 - l_chk) +
                f" $ {self.money_print(value)}\n"
            )

        message += "     -" + "-" * 50 + "-\n"

        l_chk = len("Total") + len(self.money_print(self.total_spent))

        message += (
            "      Total " + "." * (47 - l_chk) +
            f" $ {self.money_print(self.total_spent)}\n"
        )

        print(message)

        save = input("Save check [y]/n: ")

        if save in ["", "Y", "y", "yes", "YES", "Yes"]:
            save_file = input("Check file [Default: check.txt]: ")

            if save_file == "":
                save_file = "check.txt"

            save_output = open(save_file, "w")
            save_output.write(message)
            save_output.close()

        elif save in ["N", "n", "no", "NO", "No"]:
            return False
