#!/bin/bash

# -------------------------------------------------------------------------
#  Copyright 2026 Ratha SIV. All rights reserved.
#  Apache-2.0 license
# -------------------------------------------------------------------------

set -e
cd "$(dirname "$0")"
python3  -W ignore indexation.py
