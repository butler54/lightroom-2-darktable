import pathlib
import lightroom_2_darktable.table_utils as table_utils

def test_list_tables():
    path = pathlib.Path('/Users/chbutler/Pictures/work/work.lrcat')
    table_utils.list_tables(path)