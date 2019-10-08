_operation_table = {} #variables with prefixed with an _ are by convention, for internal use and should not be touched.

def attach_tag(tag, content):
    return (tag, content)


def type_tag(datum):
    if type(datum) == tuple and len(datum) == 2:
        return datum[0]
    raise Exception('Bad tagged datum -- type_tag ', datum)


def content(datum):
    if type(datum) == tuple and len(datum) == 2:
        return datum[1]
    raise Exception('Bad tagged datum -- content ', datum)


def put(op, types, value):
    if op not in _operation_table:
        _operation_table[op] = {}
    _operation_table[op][types] = value


def get(op, types):
    if op in _operation_table and types in _operation_table[op]:
        return _operation_table[op][types]
    else:
        return None

def apply_generic(op, *args):
    type_tags = tuple(map(type_tag, args))
    proc = get(op, type_tags)
    if proc:
        return proc(*map(content, args))
    raise Exception('No method for these types -- apply_generic', (op, type_tags))

##########################
# Generic Number Package #
##########################

#generic operators we want to support
def add(x,y):
    return apply_generic("add", x, y)

def sub(x,y):
    return apply_generic("sub", x, y)

def mul(x,y):
    return apply_generic("mul", x, y)

def div(x,y):
    return apply_generic("div", x, y)

def negate(x):
    return apply_generic("negate", x)

def is_zero(x):
    return apply_generic("is_zero", x)

def is_equal(x, y):
    return apply_generic("is_equal", x, y)

#composite generic operators

def square(x):
    return mul(x,x)

#Generic ordinary number package

def install_ordinary_package():
    def make_ord(x):
        return tag(x)
    def tag(x):
        return attach_tag("ordinary", x)
    # add,sub,mul,div: (RepOrd, RepOrd) -> Generic-OrdNum
    def add_ord(x,y):
        return make_ord(x+y)
    def sub_ord(x,y):
        return make_ord(x-y)
    def mul_ord(x,y):
        return make_ord(x*y)
    def div_ord(x,y):
        return make_ord(x/y)
    def negate_ord(x): # (RepOrd) -> Generic-Ord
        return make_ord(-x)
    def is_zero_ord(x): # (RepOrd) -> Py-Bool
        return x == 0
    def is_equal_ord(x,y): # (RepOrd, RepOrd) -> Py-Bool
        return x == y
    put("make","ordinary", make_ord)
    put("negate",("ordinary",), negate_ord)
    put("is_zero",("ordinary",), is_zero_ord)
    put("add",("ordinary","ordinary"), add_ord)
    put("sub",("ordinary","ordinary"), sub_ord)
    put("mul",("ordinary","ordinary"), mul_ord)
    put("div",("ordinary","ordinary"), div_ord)
    put("is_equal",("ordinary","ordinary"), is_equal_ord)

install_ordinary_package()

def create_ordinary(x):
    return get("make", "ordinary")(x)
