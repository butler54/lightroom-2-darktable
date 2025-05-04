# SPDX-FileCopyrightText: 2025-present Chris Butler <chris@thebutlers.me>
#
# SPDX-License-Identifier: Apache-2.0

import rich.console

out = rich.console.Console()
err = rich.console.Console(stderr=True, style="bold red")