## @file
## @brief @ref minsky
## @copyright Dmitry Ponyatov <dponyatov@gmail.com> CC-NC-ND
## github: https://github.com/ponyatov/metapy430

## @defgroup frame Frame
## @brief @ref minsky
## @{

## @ref minsky
class Frame:
    
    ## construct with given name or primitive object (number, string,..) 
    ## @param[in] V primitive object (number, string,..)
    def __init__(self,V):
        ## frame type
        self.type  = self.__class__.__name__.lower()
        ## primitive/atomic value (stored in implementation language type)
        self.value = V
        ## slots/attributes /associative name-keyed array/
        self.attr  = {}
        ## nested objects /ordered container/
        self.nest  = []
    
    ## @name dumping
    
    ## print in full tree-formatted text
    def __repr__(self):
        return self.dump()

print Frame('hello')

## @defgroup prim Primitive
## @brief atomic types
## @{

## atomic primitive
class Primitive(Frame): pass

## `s`ymbol names objects, variables, modules,..
class Symbol(Primitive): pass
## text string
class String(Primitive): pass

## generic number
class Number(Primitive): pass
## `i`nteger number
class Integer(Number): pass
## machine hex number
class Hex(Integer): pass
## machine binary number / bit stream
class Bin(Integer): pass

## @}

## @}
