
from  dataiku.apinode.predict.predictor import RegressionPredictor
import pandas as pd
class MyPredictor(RegressionPredictor):
    """The class for a regression Custom API node predictor"""

    def __init__(self, data_folder = None):
        """data_folder is the absolute path to the managed folder storing the data for the model
        (if any)"""
        self.data_folder = data_folder

    def predict(self, features_df):
        """
        The main prediction method.

        :param: df: a dataframe of 1 or several records to predict

        :return: Either:
            ``prediction_series`` or
            ``(prediction_series, custom_keys_list)``

        prediction_series must be a Pandas Series of decisions

        custom_keys_list is optional and must contain one entry per input row. Each entry of
        custom_keys_list must be a Python dictionary. These custom keys will be sent in the
        output result

        prediction_series and custom_keys_list must have the same number of rows than df.
        """

        # Note: this sample uses the first form: precision_series

        # Note: this sample "cheats" and always returns 4 predictions.
        # You should actually return 1 prediction per row in the features_df

        print "Features DataFrame %s" % features_df

        # predictions, one per features_df row
        return pd.Series([.4, 17.2, 21, 9.3])
