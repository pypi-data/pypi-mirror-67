from .prophet import Prophet
from .data_builder import DataFrameBuilder

def model_pool_factory(columns=None, args_dict=None, regressors={}, **kwargs):
    if args_dict:
        return _different_models_pool_factory(args_dict, regressors)
    else:
        return _equal_models_pool_factory(columns, regressors, **kwargs)

def dataframe_builder_factory(regressors):
    regressors = {c: _map_regressor_name(regressors[c]) for c in regressors.keys()}
    return DataFrameBuilder(regressors)

def _different_models_pool_factory(args_dict, regressors):
    return {
        c: _build_model(regressors.get(c, []), **kwargs)
        for c, kwargs in args_dict.items()
    }

def _equal_models_pool_factory(columns, regressors, **kwargs):
    return {c: _build_model(regressors.get(c, []), **kwargs) for c in columns}

def _build_model(regressors, **kwargs):
    m = Prophet(**kwargs)
    for r in regressors:
        m.add_regressor(**r)

    return m

def _map_regressor_name(regressors):
    return [r["name"] for r in regressors]
