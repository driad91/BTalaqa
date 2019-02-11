import pandas as pd
from . import constants
class Check:
    """
    Check object represents a specific check on the data to be done having
    attributes as follows:
    - mandatory: a boolean attribute to indicate whether the check is mandatory
    to be passed or if it is just a warning
    - passed: A boolean attribute indicating if the check has passed or not.
    - type: one of the specified type checks, i.e. column check, duplicates,
    FK exists...etc.
    """
    mandatory = True
    passed = False
    type = None
    column_to_check = None
    ref_column = None

    def rows_filled_check(self):
        """
        check if all rows have values in them, i.e. neither empty nor none
        :return:
        """
        if self.column_to_check[self.column_to_check.isnull()].empty:
            if self.column_to_check[self.column_to_check == ''].empty:
                return True
            else:
                return False
        else:
            return False

    def fk_existence_check(self):
        """

        :return:
        """
        df_check_column = self.column_to_check.to_frame()
        df_ref_column = self.ref_column.to_frame()
        df_check_size = self.shape[0]
        df_merged_size = \
            pd.merge(left=df_check_column, right=df_ref_column, how='left').shape[0]
        if df_check_size == df_merged_size:
            return True
        else:
            return False

    def dtype_check (self, expected_dtype):
        """

        :param expected_dtype:
        :return:
        """
        if expected_dtype == constants.DTYPE_NUMERIC:
            try:
               self.column_to_check.to_numeric()
            except ValueError:
                return False
        elif expected_dtype == constants.DTYPE_BOOL:
            for value in expected_dtype:
                if value!= True or value!=False or value!=1 or value!=0:
                    return False
                else:
                    return True
        else:
            return True

