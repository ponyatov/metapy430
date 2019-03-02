## @file
## @brief @ref cortex
## @copyright Dmitry Ponyatov <dponyatov@gmail.com> CC-NC-ND
## github: https://github.com/ponyatov/metapy430

from frame import *

## @defgroup cortex Cortex
## @brief @ref cortex
## @ingroup mcu
## @{

class CortexM(ARM): pass

class CortexM0(CortexM): pass
class CortexM1(CortexM0): pass
class CortexM3(CortexM1): pass
class CortexM4(CortexM3): pass
class CortexM7(CortexM4): pass

## @}
