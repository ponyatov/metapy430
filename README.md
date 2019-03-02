# metapy430
## demo: metaprogramming in Python for microcontrollers
### Python metaprogramming system for msp430 microcontroller series

(c) Dmitry Ponyatov <<dponyatov@gmail.com>> CC-NC-ND

github: https://github.com/ponyatov/metapy430

**warning**: manual in [ru] , ask for [en] translation

## About

https://www.youtube.com/watch?v=vmUdCI1iZ3U

я сам на питоне все утилиты себе пишу, и считаю лучшим (императивным) языком,
но мысль засовывать пистон c его объектами и сборкой мусора
*в микроконтроллер* могла прийти в голову только обдолбанному фронтендеру

если хочется командную консоль и интерактивное программирование на устройстве, единственный вменяемый вариант -- только Форт https://www.forth.com/starting-forth/

он был изначально создан для этой задачи, работал на таких же ресурсах и
подобных ЭВМ в 70х годах, и все еще остается очень хорошим вариантом
в комплексе с кросс-компилятором embedded Си
(чтобы не писать низкоуровневый код на постфиксном ассемблере)﻿
