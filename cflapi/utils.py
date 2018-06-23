
def flatten(dd, prefix=''):
    def flatten_impl(dd):
        if (type(dd) == dict):
            nextKey = [*dd][0]
            return '[' + nextKey + ']' + flatten(dd[nextKey])
        else:
            return '=' + str(dd)
    return prefix + flatten_impl(dd)