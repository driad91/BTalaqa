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
    def __init__(self, mandatory=True, type=None,
                 column_to_check=None, ref_column=None):
        """

        :param mandatory:
        :param passed:
        :param type:
        :param column_to_check:
        :param ref_column:
        """
        self.mandatory = mandatory
        self.type = type
        self.column_to_check = column_to_check
        self.ref_column = ref_column
        self.passed = False
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

    def dtype_check(self, expected_dtype):
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
    def duplicates_check(self):
        """
        check if there are any duplicates the to be_checked_column
        :return:  Boolean
        """
        if len (self.column_to_check) > len(self.column_to_check.unique())
            return False
        else:
            return True
    def check_column_names(self, df, expected_column_names):
        """
        :param df:
        :param expected_column_names:
        :return:
        """
        all_exist = True
        expected_column_names = expected_column_names.apply\
            (lambda x: x.lower().strip())
        columns_df = df.columns
        columns_df = columns_df.apply(lambda x: x.lower().strip())
        if len(columns_df) == len(expected_column_names):
            for column in columns_df:
                if not column in expected_column_names:
                    all_exist = False

        else:
            return False
        if all_exist:
            return True
        else:
            return False

    def execute_check(self):
        """

        :return:
        """
        if self.type == 1:
            self.passed = self.rows_filled_check()
        elif self.type == 2:
            self.passed = self.fk_existence_check()
        elif self.type == 3:
            self.passed = self.dtype_check()
        elif self.type==4:
            self.passed = self.duplicates_check()
        elif self.type ==5:
            self.passed = self.check_column_names()
