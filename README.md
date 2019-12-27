<!-- Author (Created): Roger "Equah" Hürzeler -->
<!-- Date (Created): 12019.12.27 HE -->
<!-- License: apache-2.0 -->

**SBLInt [Python 3]**
================================================================================

[SBLInt](https://github.com/TheEquah/SBLInt/) Python 3 implementation.

--------------------------------------------------------------------------------

# Architecture

Overview of the SBLInt architecture.

## SBLInt

SBLInt starts with [SBSInt](https://github.com/TheEquah/SBSInt/) bytes, defining the amount of following bytes containing the integer. After this the following bytes are an integer staring with the MSB. This allows to write smaller integers using less bytes than larger integers. The exception is `0`, which will be directly printed as `0x00` without following bytes.

--------------------------------------------------------------------------------

# Install

SBLInt provedes a [`/src/setup.py`](https://github.com/TheEquah/SBLInt-python3/blob/master/src/setup.py) script to install the package. To use this script, `cd` into the [`/src/`](https://github.com/TheEquah/SBLInt-python3/tree/master/src/) directory, and execute the script with `python3 ./setup.py install`.

## Requirements

SBLInt requires the [SBSInt Python 3](https://github.com/TheEquah/SBSInt-python3/) package to be installed.

--------------------------------------------------------------------------------

# Examples

This repository provides the following example uses for SBSInt.

## Convert

Example which simply converts numbers between Integer and SBLInt.

Directory: [`/example/convert/`](https://github.com/TheEquah/SBLInt-python3/tree/master/example/convert/)

--------------------------------------------------------------------------------
