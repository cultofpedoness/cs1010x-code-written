_operation_table = {} # variables with prefixed with an _ are by convention, for internal use and should not be touched.

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

# generic operators we want to support

def add(x, y):
    return apply_generic("add", x, y)

def sub(x, y):
    return apply_generic("sub", x, y)

def mul(x, y):
    return apply_generic("mul", x, y)

def div(x, y):
    return apply_generic("div", x, y)

# negate: (Generic-Num) -> Generic-Num
def negate(x):
    return apply_generic("negate", x)

# is_zero: (Generic-Num) -> Boolean
def is_zero(x):
    return apply_generic("is_zero", x)

# is_equal: (Generic-Num, Generic-Num) -> Boolean
def is_equal(x, y):
    return apply_generic("is_equal", x, y)

# composite generic operators

def square(x):
    return mul(x, x)

###################################
# Generic Ordinary Number Package #
###################################

def install_ordinary_package():
    def make_ord(x):
        return tag(x)
    def tag(x):
        return attach_tag("ordinary", x)
    
    # add, sub, mul, div: (RepOrd, RepOrd) -> Generic-Ord
    # Note the different output type. It is because the output
    # is tagged before returning.
    def add_ord(x, y):
        return make_ord(x + y)
    def sub_ord(x, y):
        return make_ord(x - y)
    def mul_ord(x, y):
        return make_ord(x * y)
    def div_ord(x, y):
        return make_ord(x / y)
    def negate_ord(x): # (RepOrd) -> Generic-Ord
        return make_ord(-x)
    def is_zero_ord(x): # (RepOrd) -> Py-Bool
        return x == 0
    def is_equal_ord(x, y): # (RepOrd, RepOrd) -> Py-Bool
        return x == y

    put("make", "ordinary", make_ord)
    put("negate", ("ordinary",), negate_ord)
    put("is_zero", ("ordinary",), is_zero_ord)
    put("add", ("ordinary", "ordinary"), add_ord)
    put("sub", ("ordinary", "ordinary"), sub_ord)
    put("mul", ("ordinary", "ordinary"), mul_ord)
    put("div", ("ordinary", "ordinary"), div_ord)
    put("is_equal", ("ordinary", "ordinary"), is_equal_ord)

install_ordinary_package()

def create_ordinary(x):
    return get("make", "ordinary")(x)

###################################
# Generic Rational Number Package #
###################################

def install_rational_package():
    def make_rat(x, y):
        return tag(reprat(x, y))
    def reprat(x, y):
        return (x, y)
    def numer(x):
        return x[0]
    def denom(x):
        return x[1]
    def tag(x):
        return attach_tag("rational", x)

    # add, sub, mul, div: (RepRat, RepRat) -> Generic-Rat
    def add_rat(x, y):
        return make_rat( add(mul(numer(x), denom(y)),
                             mul(denom(x), numer(y))),
                         mul(denom(x), denom(y)) )
    def sub_rat(x, y):
        return make_rat( sub(mul(numer(x), denom(y)),
                             mul(denom(x), numer(y))),
                         mul(denom(x), denom(y)) )
    def mul_rat(x, y):
        return make_rat( mul(numer(x), numer(y)),
                         mul(denom(x), denom(y)) )
    def div_rat(x, y):
        return make_rat( mul(numer(x), denom(y)),
                         mul(denom(x), numer(y)) )

    put("make", "rational", make_rat)
    put("add", ("rational", "rational"), add_rat)
    put("sub", ("rational", "rational"), sub_rat)
    put("mul", ("rational", "rational"), mul_rat)
    put("div", ("rational", "rational"), div_rat)

install_rational_package()

def create_rational(x, y):
    return get("make", "rational")(x, y)

##################################
# Generic Complex Number Package #
##################################

def install_complex_package():
    def make_com(x, y):
        return tag(repcom(x, y))
    def repcom(x, y):
        return (x, y)
    def real(x):
        return x[0]
    def imag(x):
        return x[1]
    def tag(x):
        return attach_tag("complex", x)
    
    # add, sub, mul, div: (RepCom, RepCom) -> Generic-Com
    def add_com(x, y):
        return make_com( add(real(x), real(y)),
                         add(imag(x), imag(y)) )
    def sub_com(x, y):
        return make_com( sub(real(x), real(y)),
                         sub(imag(x), imag(y)) )
    def mul_com(x, y):
        return make_com( sub(mul(real(x), real(y)),
                             mul(imag(x), imag(y))),
                         add(mul(real(x), imag(y)),
                             mul(real(y), imag(x))))
    def div_com(x, y):
        com_conj = complex_conjugate(y)
        x_times_com_conj = content(mul_com(x, com_conj))
        y_times_com_conj = content(mul_com(y, com_conj))
        return make_com( div(real(x_times_com_conj), real(y_times_com_conj)),
                         div(imag(x_times_com_conj), real(y_times_com_conj)))
    def complex_conjugate(x):
        return (real(x), negate(imag(x)))

    put("make", "complex", make_com)
    put("add", ("complex", "complex"), add_com)
    put("sub", ("complex", "complex"), sub_com)
    put("mul", ("complex", "complex"), mul_com)
    put("div", ("complex", "complex"), div_com)

install_complex_package()

def create_complex(x,y):
    return get("make", "complex")(x, y)
