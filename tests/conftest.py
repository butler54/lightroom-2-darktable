# SPDX-FileCopyrightText: 2024-present Chris Butler <chris@thebutlers.me>
#
# SPDX-License-Identifier: Apache-2.0

import pytest
import ray
import yaml

import sys
from pathlib import Path
src = Path(__file__).parents[1] / "src"
sys.path.append(str(src))

def pytest_addoption(parser):
    parser.addoption(
        "--test-data-dir",
        type=Path,
        default=Path("~/Pictures/test_catalog").expanduser(),
        help="Base directory for external test files"
    )

@pytest.fixture(scope="session")
def test_data_dir(request):
    return request.config.getoption("--test-data-dir")




@pytest.fixture(scope="session")
def lightroom_facts(test_data_dir):
    test_fact_files = test_data_dir / "lightroom-facts.yaml"
    if not test_fact_files.exists():
        pytest.fail(f'Test facts file is missing: {test_fact_files}')
    
    with test_fact_files.open('r') as file:
        data = yaml.safe_load(file)
    return data

@pytest.fixture(scope="session")
def ray_session():
    if not ray.is_initialized():
        ray.init()
    yield None
    if ray.is_initialized():
        ray.shutdown()
