from abc import ABCMeta
from typing import Optional, List, Union, Dict, AnyStr

import pandas as pd


class Dataset(metaclass=ABCMeta):
    fixes: List = []
    data: Optional[Union[Dict, pd.DataFrame, pd.Series]] = None
    sources: Union[AnyStr, Dict] = None

    def register_fixes(self):
        pass

    def get(self, **kwargs) -> 'Dataset':
        ...
        return self

    def clean(self) -> 'Dataset':
        ...
        return self

    def to_df(self) -> pd.DataFrame:
        if isinstance(pd.DataFrame, self.data):
            return self.data
        else:  # assume it's something concatable
            return pd.concat(self.data)

    def _fix_dtypes(self):
        """Fortunately this is super easy, barely an inconvenience, thanks to the pandas built-in 'infer_objects()'"""
        self.data = self.data.infer_objects().reset_index(drop=True)
