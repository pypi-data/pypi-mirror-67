#!usr/bin/env python3
# -*- coding: UTF-8 -*-
"""常用自定义的网络层"""

from .layer import Swish,get_swish,HSwish,get_relu6
from .layer import SEConvEfnet2D
from .layer import GlobalAveragePooling2DKeepDim, \
    CONV_KERNEL_INITIALIZER, DENSE_KERNEL_INITIALIZER
