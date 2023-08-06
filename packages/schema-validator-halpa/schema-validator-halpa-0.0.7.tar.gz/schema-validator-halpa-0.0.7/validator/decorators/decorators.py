from .. import is_valid, require, validate as base_validate
import json
import os

def validate(schema={}, required=[], where="body"):
    def decorator(inner_function):
        def validate_f(*args, **kwargs):

            data = args[0].get(where)

            if isinstance(data, str):
                # TODO: check if variable is JSON-parsable
                data = json.loads(data)

            if len(required) > 0 and not schema:
                require(required, data)
            else:
                base_validate(schema, data, required=required)
            # return function if validation passed
            return inner_function(*args, **kwargs)
        return validate_f
    return decorator
