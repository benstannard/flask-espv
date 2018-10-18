# Utility functions and decorators.
# from flask_login import current_user
from functools import wraps


def chunks(seq, n=2):
    """Input a string 'aabbcc' which returns a tuple ('aa', 'bb', 'cc') which can be used for member ship tests.
    if 'dd' not in chunks('aabbcc'): abort(401)
    if 'aa' in chunks(curent_user.access): return render_template('view.html')
    """
    return tuple((seq[i:i+n] for i in range(0, len(seq), n)))


# def access(*cu_access):
#     """Decorate view functions with @access("AA") to test if current_user has access to view."""
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             if cu_access[0] not in chunks(current_user.access, n=2):
#                 abort(401)
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator
