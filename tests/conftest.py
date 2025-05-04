# SPDX-FileCopyrightText: 2024-present Chris Butler <chris@thebutlers.me>
#
# SPDX-License-Identifier: Apache-2.0

import pytest
import ray


################BAD HACK################
import sys
from pathlib import Path
src = Path(__file__).parents[1] / "src"
sys.path.append(str(src))
################BAD HACK################

@pytest.fixture(scope="session")
def ray_session():
    if not ray.is_initialized():
        ray.init()
    yield None
    if ray.is_initialized():
        ray.shutdown()
