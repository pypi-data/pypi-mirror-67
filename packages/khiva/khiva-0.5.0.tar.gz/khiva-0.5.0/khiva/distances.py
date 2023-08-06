#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Shapelets.io
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

########################################################################################################################
# IMPORT
########################################################################################################################
import ctypes
from khiva.library import KhivaLibrary, KHIVA_ERROR_LENGTH
from khiva.array import Array


########################################################################################################################


def euclidean(tss):
    """ Calculates euclidean distances between time series.

    :param tss: Expects an input array whose dimension zero is the length of the time series (all the same) and
                dimension one indicates the number of time series.
    :return: Array with an upper triangular matrix where each position corresponds to the distance between two
            time series. Diagonal elements will be zero. For example: Position row 0 column 1 records the distance
            between time series 0 and time series 1.
    """
    b = ctypes.c_void_p(0)
    error_code = ctypes.c_int(0)
    error_message = ctypes.create_string_buffer(KHIVA_ERROR_LENGTH)
    KhivaLibrary().c_khiva_library.euclidean(ctypes.pointer(tss.arr_reference), ctypes.pointer(b), ctypes.pointer(error_code), error_message)
    if error_code.value != 0:
        raise Exception(str(error_message.value.decode()))

    return Array(array_reference=b)


def dtw(tss):
    """ Calculates the Dynamic Time Warping Distance.

    :param tss: Expects an input array whose dimension zero is the length of the time series (all the same) and
                dimension one indicates the number of time series.
    :return: Array with an upper triangular matrix where each position corresponds to the distance between
            two time series. Diagonal elements will be zero. For example: Position row 0 column 1 records the
            distance between time series 0 and time series 1.
    """
    b = ctypes.c_void_p(0)
    error_code = ctypes.c_int(0)
    error_message = ctypes.create_string_buffer(KHIVA_ERROR_LENGTH)
    KhivaLibrary().c_khiva_library.dtw(ctypes.pointer(tss.arr_reference), ctypes.pointer(b), ctypes.pointer(error_code), error_message)
    if error_code.value != 0:
        raise Exception(str(error_message.value.decode()))

    return Array(array_reference=b)


def hamming(tss):
    """ Calculates Hamming distances between time series.

    :param tss: Expects an input array whose dimension zero is the length of the time series (all the same) and
                dimension one indicates the number of time series.
    :return: Array with an upper triangular matrix where each position corresponds to the distance between two
            time series. Diagonal elements will be zero. For example: Position row 0 column 1 records the distance
            between time series 0 and time series 1.
    """
    b = ctypes.c_void_p(0)
    error_code = ctypes.c_int(0)
    error_message = ctypes.create_string_buffer(KHIVA_ERROR_LENGTH)
    KhivaLibrary().c_khiva_library.hamming(ctypes.pointer(tss.arr_reference), ctypes.pointer(b), ctypes.pointer(error_code), error_message)
    if error_code.value != 0:
        raise Exception(str(error_message.value.decode()))

    return Array(array_reference=b)


def manhattan(tss):
    """ Calculates Manhattan distances between time series.

    :param tss: Expects an input array whose dimension zero is the length of the time series (all the same) and
                dimension one indicates the number of time series.
    :return: Array with an upper triangular matrix where each position corresponds to the distance between two
            time series. Diagonal elements will be zero. For example: Position row 0 column 1 records the distance
            between time series 0 and time series 1.
    """
    b = ctypes.c_void_p(0)
    error_code = ctypes.c_int(0)
    error_message = ctypes.create_string_buffer(KHIVA_ERROR_LENGTH)
    KhivaLibrary().c_khiva_library.manhattan(ctypes.pointer(tss.arr_reference), ctypes.pointer(b), ctypes.pointer(error_code), error_message)
    if error_code.value != 0:
        raise Exception(str(error_message.value.decode()))

    return Array(array_reference=b)


def sbd(tss):
    """ Calculates the Shape-Based distance (SBD). It computes the normalized cross-correlation and
    it returns the value that maximizes the correlation value between time series.

    :param tss: Expects an input array whose dimension zero is the length of the time series (all the same) and
                dimension one indicates the number of time series.
    :return: Array with an upper triangular matrix where each position corresponds to the distance between two time series.
            Diagonal elements will be zero. For example: Position row 0 column 1 records the distance between time series 0
            and time series 1.
    """
    b = ctypes.c_void_p(0)
    error_code = ctypes.c_int(0)
    error_message = ctypes.create_string_buffer(KHIVA_ERROR_LENGTH)
    KhivaLibrary().c_khiva_library.sbd(ctypes.pointer(tss.arr_reference), ctypes.pointer(b), ctypes.pointer(error_code), error_message)
    if error_code.value != 0:
        raise Exception(str(error_message.value.decode()))

    return Array(array_reference=b)


def squared_euclidean(tss):
    """ Calculates the non squared version of the euclidean distance.

    :param tss: Expects an input array whose dimension zero is the length of the time series (all the same) and
                dimension one indicates the number of time series.
    :return: Array with an upper triangular matrix where each position corresponds to the distance between two time series.
            Diagonal elements will be zero. For example: Position row 0 column 1 records the distance between time series 0
            and time series 1.
    """
    b = ctypes.c_void_p(0)
    error_code = ctypes.c_int(0)
    error_message = ctypes.create_string_buffer(KHIVA_ERROR_LENGTH)
    KhivaLibrary().c_khiva_library.squared_euclidean(ctypes.pointer(tss.arr_reference), ctypes.pointer(b), ctypes.pointer(error_code), error_message)
    if error_code.value != 0:
        raise Exception(str(error_message.value.decode()))

    return Array(array_reference=b)
