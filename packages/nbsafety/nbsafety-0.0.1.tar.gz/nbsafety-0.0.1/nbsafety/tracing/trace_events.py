# -*- coding: utf-8 -*-
from __future__ import annotations
from enum import Enum


class TraceEvent(Enum):
    line = 'line'
    call = 'call'
    return_ = 'return'
    exception = 'exception'

    # these are included for completeness but will probably not be used
    c_call = 'c_call'
    c_return = 'c_return'
    c_exception = 'c_exception'
