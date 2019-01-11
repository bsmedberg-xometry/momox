# This syntax is invalid in python3, so we use a separate file and only import
# it in python 2
def reraise(exctype, value, trace=None):
    raise exctype, str(value), trace
