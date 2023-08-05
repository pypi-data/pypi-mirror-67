from .encoder_methods import (
    BinaryEncoder,
    HashingEncoder,
    LeaveOneOutEncoder,
    OneHotEncoder,
    OrdinalEncoder,
    TargetEncoder
)


class Encoder():
    """
        Encodes specified columns of categorical values.

        Parameters:
        cols: [str]
            list of column names to encode.

        Functions:
        fit:
            fits encoder to data table
            returns self
        transform:
            encodes matrix and updates features accordingly
            returns encoded matrix (dataframe)
        fit_transform:
            first fits, then transforms matrix
            returns encoded matrix (dataframe)
        get_mapping:
            gets the mapping for the encoder (binary, ordinal only)
        get_hash_method:
            gets the hash_method of the encoder (hashing only)
            return hash_method (str)
        get_n_components:
            gets the number of columns used in the encoder (hashing only)
            returns n_components (int)
    """

    def __init__(self, method='one_hot', to_encode=None):
        encoder_list = {'ordinal': OrdinalEncoder(cols=to_encode),
                        'binary': BinaryEncoder(cols=to_encode),
                        'hashing': HashingEncoder(cols=to_encode),
                        'one_hot': OneHotEncoder(cols=to_encode),
                        'target': TargetEncoder(cols=to_encode),
                        'leave_one_out': LeaveOneOutEncoder(cols=to_encode)}
        if method in encoder_list:
            method = encoder_list[method]
        elif isinstance(method, str):
            raise ValueError("'%s' is not a supported encoder. The list of supported String encoder method names is: %s" % (method, encoder_list.keys()))

        self.method = method

    def fit(self, X, features, y=None):
        self.method.fit(X, features, y)
        return self

    def transform(self, X):
        return self.method.transform(X)

    def fit_transform(self, X, features, y=None):
        return self.method.fit_transform(X, features, y)

    def get_features(self):
        return self.method.get_features()

    def get_mapping(self, category=0):
        return self.method.get_mapping(category)

    def get_hash_method(self):
        if not isinstance(self.method, HashingEncoder):
            raise TypeError("Must be HashingEncoder")
        return self.method.hash_method

    def get_n_components(self):
        if not isinstance(self.method, HashingEncoder):
            raise TypeError("Must be HashingEncoder")
        return self.method.n_components

    def _encode_features_list(self, X, features):
        self.method.encode_features_list(X, features)

    def get_name(self):
        return self.method.get_name()
