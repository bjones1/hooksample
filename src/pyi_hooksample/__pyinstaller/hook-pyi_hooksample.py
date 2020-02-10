#
# Copyright © 2020 PyInstaller Development Team
#
# This file is part of PyInstaller Hook Sample.
#
# PyInstaller Hook Sample is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or (at your
# option) any later version.
#
# PyInstaller Hook Sample is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# PyInstaller Hook Sample. If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from PyInstaller.utils.hooks import collect_data_files

hiddenimports = ["pyi_hooksample._hidden"]
datas = collect_data_files('pyi_hooksample')