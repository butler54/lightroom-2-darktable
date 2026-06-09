import pathlib
import lightroom_2_darktable.table_utils as table_utils

def test_list_tables(lightroom_facts, test_data_dir: pathlib.Path) -> None:
    path = test_data_dir / lightroom_facts["lrcat"]
    table_utils.list_tables(path)


def test_print_db(lightroom_facts, test_data_dir, ray_session) -> None:
    path = test_data_dir / lightroom_facts["lrcat"]
    table_utils.print_db_size(path)