"""Class that stores data in a csv file."""
import pandas as pd


class CSVSaver():
    """Class that stores the data from a sensor in a csv file."""

    def __init__(self, filepath, header, delimiter=","):
        """Create the saver."""
        # Set the file path.
        self.filepath = filepath

        # Create the schemas.
        self.schema = {}
        self.row_schema = {}
        self.header = header

        self.set_schema(header)

        # Create the DataFrame.
        self.delimiter = delimiter

        self.filepath = filepath

        try:
            self.df = pd.read_csv(self.filepath, index_col=0)
        except Exception:
            self.df = pd.DataFrame(self.schema)

    def set_schema(self, header):
        """Configure the schema with the header given."""
        self.schema = {column: [] for column in header}
        self.reset_row_schema()

    def reset_row_schema(self):
        """Reset the schema for the new row."""
        self.row_schema = self.schema

    def add_row_value(self, column, value):
        """Add a value to the row schema."""
        self.row_schema[column] = value

    def fill_row(self, values):
        """Add a value to the row schema."""
        for index in range(len(self.header)):
            self.add_row_value(self.header[index], values[index])

    def add_row(self):
        """Add a new row to the DataFrame."""
        self.df = pd.concat(
            [self.df, pd.DataFrame(self.row_schema, index=[0])],
            ignore_index=True
        )
        self.reset_row_schema()

    def remove_row(self, index):
        """Add a new row to the DataFrame."""
        self.df = self.df.drop([index])
        self.df.index = range(len(self.df))

    def save_data(self):
        """Save the DataFrame to the csv file."""
        self.df.to_csv(self.filepath, sep=self.delimiter)

    def add_row_and_save(self):
        """Add a new row to the DataFrame."""
        self.add_row()
        self.save_data()

    def get_column_value(self, column, index):
        """Return the values of the given column."""
        return self.df[column][index]

    def get_column_values(self, column):
        """Return the values of the given column."""
        return self.df[column].values

    def get_index(self):
        """Return the values of the given column."""
        return self.df.index
