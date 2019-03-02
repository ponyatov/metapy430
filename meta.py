## @file
## @brief @ref meta
## @copyright Dmitry Ponyatov <dponyatov@gmail.com> CC-NC-ND
## github: https://github.com/ponyatov/metapy430

from frame import *

## @defgroup meta Meta
## @brief @ref meta
## @{

## @ref meta
class Meta(Frame): pass

## @defgroup hw Hardware
## @brief @ref hardware
## @{

## hardware
class HW(Meta): pass

## @defgroup arch ARCH
## @{

## architecture
class ARCH(HW): pass

## @}

## processor unit
class CPU(HW): pass

## @}

## @defgroup os OS
## @{

class OS(Meta): pass
## @}

## @}
