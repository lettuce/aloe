# -*- coding: utf-8 -*-
# <Lettuce - Behaviour Driven Development for python>
# Copyright (C) <2010-2012>  Gabriel Falc達o <gabriel@nacaolivre.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from os.path import dirname, abspath, join
from nose.tools import with_setup
from tests.asserts import prepare_stdout
from tests.asserts import assert_stdout_lines

from lettuce import Runner

current_dir = abspath(dirname(__file__))
join_path = lambda *x: join(current_dir, *x)

@with_setup(prepare_stdout)
def test_output_with_success_colorless():
    "Language: zh-TW -> sucess colorless"

    runner = Runner(join_path('zh-TW', 'success', 'dumb.feature'), verbosity=3)
    runner.run()

    assert_stdout_lines(
        u"\n"
        u"功能: 簡單測試           # tests/functional/language_specific_features/zh-TW/success/dumb.feature:3\n"
        u"  什麽都不做應該運行成功 # tests/functional/language_specific_features/zh-TW/success/dumb.feature:4\n"
        u"\n"
        u"  場景: 什麽都不做       # tests/functional/language_specific_features/zh-TW/success/dumb.feature:6\n"
        u"    假如 什麽都不做      # tests/functional/language_specific_features/zh-TW/success/dumb_steps.py:6\n"
        u"\n"
        u"1 feature (1 passed)\n"
        u"1 scenario (1 passed)\n"
        u"1 step (1 passed)\n"
    )

@with_setup(prepare_stdout)
def test_output_of_table_with_success_colorless():
    "Language: zh-TW -> sucess table colorless"

    runner = Runner(join_path('zh-TW', 'success', 'table.feature'), verbosity=3)
    runner.run()

    assert_stdout_lines(
        u"\n"
        u"功能: 步驟中包含表格             # tests/functional/language_specific_features/zh-TW/success/table.feature:3\n"
        u"  繁體中文表格步驟的成功測試     # tests/functional/language_specific_features/zh-TW/success/table.feature:4\n"
        u"\n"
        u"  場景: 什麽都不做的表格步驟測試 # tests/functional/language_specific_features/zh-TW/success/table.feature:6\n"
        u"    假如 輸入數據如下:           # tests/functional/language_specific_features/zh-TW/success/table_steps.py:6\n"
        u"      | id | 名稱   |\n"
        u"      | 12 | 名稱一 |\n"
        u"      | 64 | 名稱二 |\n"
        u"\n"
        u"1 feature (1 passed)\n"
        u"1 scenario (1 passed)\n"
        u"1 step (1 passed)\n"
    )

@with_setup(prepare_stdout)
def test_output_outlines_success_colorless():
    """Language: zh-TW -> success outlines colorless"""

    runner = Runner(join_path('zh-TW', 'success', 'outlines.feature'),
                    verbosity=3)
    runner.run()

    assert_stdout_lines(u"""
功能: 中文場景模板                 # tests/functional/language_specific_features/zh-TW/success/outlines.feature:3
  中文場景模板圖表測試             # tests/functional/language_specific_features/zh-TW/success/outlines.feature:4

  場景大綱: 用表格描述場景         # tests/functional/language_specific_features/zh-TW/success/outlines.feature:6
    假如 輸入是<輸入>              # tests/functional/language_specific_features/zh-TW/success/outlines_steps.py:13
    當 執行<處理>時                # tests/functional/language_specific_features/zh-TW/success/outlines_steps.py:22
    那麼 得到<結果>                # tests/functional/language_specific_features/zh-TW/success/outlines_steps.py:31

  例如
    | 輸入 | 處理 | 結果         |
    | 什麽 | 這個 | 功能         |
    | 其他 | 這裏 | 一樣         |
    | 數據 | 動作 | unicode輸出! |

1 feature (1 passed)
3 scenarios (3 passed)
9 steps (9 passed)
    """)

@with_setup(prepare_stdout)
def test_output_outlines_success_colorful():
    "Language: zh-TW -> sucess outlines colorful"

    runner = Runner(join_path('zh-TW', 'success', 'outlines.feature'), verbosity=4)
    runner.run()

    return

    assert_stdout_lines(
        u'\n'
        u"\033[1;37m特性: 中文場景模板           \033[1;30m# tests/functional/language_specific_features/zh-TW/success/outlines.feature:3\033[0m\n"
        u"\033[1;37m  中文場景模板圖表測試       \033[1;30m# tests/functional/language_specific_features/zh-TW/success/outlines.feature:4\033[0m\n"
        u'\n'
        u"\033[1;37m  場景模板: 用表格描述場景   \033[1;30m# tests/functional/language_specific_features/zh-TW/success/outlines.feature:6\033[0m\n"
        u"\033[0;36m    如果 輸入是<輸入>        \033[1;30m# tests/functional/language_specific_features/zh-TW/success/outlines_steps.py:13\033[0m\n"
        u"\033[0;36m    當 執行<處理>時          \033[1;30m# tests/functional/language_specific_features/zh-TW/success/outlines_steps.py:22\033[0m\n"
        u"\033[0;36m    那麽 得到<結果>          \033[1;30m# tests/functional/language_specific_features/zh-TW/success/outlines_steps.py:31\033[0m\n"
        u'\n'
        u"\033[1;37m  例如:\033[0m\n"
        u"\033[0;36m   \033[1;37m |\033[0;36m 輸入\033[1;37m |\033[0;36m 處理\033[1;37m |\033[0;36m 結果        \033[1;37m |\033[0;36m\033[0m\n"
        u"\033[1;32m   \033[1;37m |\033[1;32m 什麽\033[1;37m |\033[1;32m 這個\033[1;37m |\033[1;32m 功能        \033[1;37m |\033[1;32m\033[0m\n"
        u"\033[1;32m   \033[1;37m |\033[1;32m 其他\033[1;37m |\033[1;32m 這裏\033[1;37m |\033[1;32m 一樣        \033[1;37m |\033[1;32m\033[0m\n"
        u"\033[1;32m   \033[1;37m |\033[1;32m 數據\033[1;37m |\033[1;32m 動作\033[1;37m |\033[1;32m unicode輸出!\033[1;37m |\033[1;32m\033[0m\n"
        u'\n'
        u"\033[1;37m1 feature (\033[1;32m1 passed\033[1;37m)\033[0m\n"
        u"\033[1;37m3 scenarios (\033[1;32m3 passed\033[1;37m)\033[0m\n"
        u"\033[1;37m9 steps (\033[1;32m9 passed\033[1;37m)\033[0m\n"
    )

