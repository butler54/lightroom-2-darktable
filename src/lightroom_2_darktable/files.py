# SPDX-FileCopyrightText: 2025-present Chris Butler <chris@thebutlers.me>
#
# SPDX-License-Identifier: Apache-2.0
import pathlib
import lightroom_2_darktable.console as console

def validate_lrcat(lrcat: pathlib.Path) -> bool:
    """Validate expectations of lightroom catalog"""
    if not lrcat.exists():
        console.err.print(f"lrcat file: {lrcat} does not exist")
        return False
    if not lrcat.suffix == '.lrcat':
        return False
    
    helper = a.parent / a.stem + ' Helper.lrdata'
    previews = a.parent / a.stem + ' Previews.lrdata'
    data = a.parent / a.stem + '.lrcat-data'

    if not (helper.exists() and helper.is_dir()):
        console.err.print(f"catalog helper file: {helper} does not exist")
        return False
    
    if not (previews.exists() and previews.is_dir()):
        console.err.print(f"catalog previews directoryls : {previews} does not exist")
        return False
    
    if not data.exists() and data.is_dir()):
        console.err.print(f"lrcat file: {data} does not exist")
        return False


    






