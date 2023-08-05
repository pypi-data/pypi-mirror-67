# This file exists within 'dob-viewer':
#
#   https://github.com/hotoffthehamster/dob-viewer
#
# Copyright © 2018-2020 Landon Bouma. All rights reserved.
#
# This program is free software:  you can redistribute it  and/or  modify it under the
# terms of the GNU General Public License as published by the Free Software Foundation,
# either version 3  of the License,  or  (at your option)  any later version  (GPLv3+).
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY;  without even the implied warranty of MERCHANTABILITY or  FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU  General  Public  License  for  more  details.
#
# If you lost the GNU General Public License that ships with this software
# repository (read the 'LICENSE' file), see <http://www.gnu.org/licenses/>.

import os
import platform
import tempfile

from gettext import gettext as _

import editor

from nark.items.activity import Activity

from dob_bright.termio import dob_in_user_warning

# Lazy-load AwesomePrompt to save ~0.1 seconds when not needed.
from dob_prompt import prompters

__all__ = (
    'ask_user_for_edits',
    'ask_edit_with_editor',
    'run_editor_safe',
)


# ***

def ask_user_for_edits(
    controller,
    fact,
    always_ask=False,
    prompt_agent=None,
    restrict_edit='',
    no_completion=None,
):
    """
    """

    def _ask_user_for_edits():
        verify_always_ask()

        prompter = get_prompter()

        ask_act_cat(prompter, fact)

        ask_for_tags(prompter, fact)

        fact_ask_description(fact)

        return prompter

    # ***

    def verify_always_ask():
        assert always_ask in [
            True, False, 'actegory', 'tags', 'description',
        ]

    # ***

    def get_prompter():
        if prompt_agent is None:
            return prompters.path.AwesomePrompt(controller)
        else:
            assert isinstance(prompt_agent, prompters.path.PrompterCommon)
            return prompt_agent

    # ***

    def ask_act_cat(prompter, fact):
        filter_activity, filter_category = prepare_ask_act_cat(fact)
        if (
            (filter_activity and filter_category and always_ask is False)
            or ('' != restrict_edit and 'actegory' != restrict_edit)
        ):
            return

        no_completion_act = None
        no_completion_cat = None
        if no_completion is not None:
            no_completion_act = no_completion.re_act
            no_completion_cat = no_completion.re_cat

        act_name, cat_name = prompter.ask_act_cat(
            filter_activity,
            filter_category,
            no_completion_act=no_completion_act,
            no_completion_cat=no_completion_cat,
        )
        set_actegory(fact, act_name, cat_name)

    def prepare_ask_act_cat(fact):
        filter_activity = ''
        if fact.activity and fact.activity.name:
            filter_activity = fact.activity.name

        filter_category = ''
        if fact.activity and fact.activity.category and fact.activity.category.name:
            filter_category = fact.activity.category.name

        return filter_activity, filter_category

    def set_actegory(fact, act_name, cat_name):
        fact.activity = Activity.create_from_composite(act_name, cat_name)
        try:
            fact.activity = controller.activities.get_by_composite(
                fact.activity.name, fact.activity.category, raw=False,
            )
        except KeyError:
            pass

    # ***

    def ask_for_tags(prompter, fact):
        if (
            (fact.tags and always_ask is False)
            or ('' != restrict_edit and 'tags' != restrict_edit)
        ):
            return

        no_complete_tag = None
        if no_completion is not None:
            no_complete_tag = no_completion.re_tag

        chosen_tags = prompter.ask_for_tags(
            already_selected=fact.tags,
            activity=fact.activity,
            no_completion=no_complete_tag,
        )
        fact.tags_replace(chosen_tags)

    # ***

    def fact_ask_description(fact):
        if (
            (fact.description and always_ask is False)
            or ('' != restrict_edit and 'description' != restrict_edit)
        ):
            return

        # (lb): Strip whitespace from the description. This is how `git` works.
        # Not that we have to be like git. But it makes parsed results match
        # the input, i.e., it we didn't strip() and then re-parsed the non-
        # stripped description, the parser would strip, and we'd see a difference
        # between the pre-parsed and post-parsed description, albeit only
        # leading and/or trailing whitespace. (If we wanted to preserve whitespace,
        # we'd have to make the parser a little more intelligent, but currently
        # the parser strip()s while it parses, to simplify the parsing algorithm.)
        raw_description = ask_edit_with_editor(controller, fact, fact.description)
        if raw_description is not None:
            fact.description = raw_description.strip()

    # ***

    return _ask_user_for_edits()


# ***

def ask_edit_with_editor(controller, fact=None, content=''):
    def _ask_edit_with_editor():
        contents = prepare_contents(content)
        filename = temp_filename()
        return run_editor_safe(filename, contents)

    def prepare_contents(content):
        content = content if content else ''
        # # FIXME: py2 compatible? Or need to six.b()?
        # #contents = six.b(str(content))  # NOPE: Has problems with Unicode, like: ½
        # contents = text_type(content).encode()
        # FIXME/2020-01-26: (lb): Verify no longer an issue.
        contents = str(content).encode()
        return contents

    def temp_filename():
        tmpfile = tempfile.NamedTemporaryFile(
            prefix=prepare_prefix(),
            suffix=prepare_suffix(),
        )
        filename = tmpfile.name
        return filename

    def prepare_prefix():
        # Vim names the terminal with the file's basename, which is
        # normally meaningless, e.g., "tmprvapy77w.rst (/tmp)", but
        # we can give the randomly-named temp file a prefix to make
        # the title more meaningful.
        prefix = None
        if fact is not None:
            # (lb): Reminder that colon is not acceptable for Windows paths.
            #   (I originally had a ':' in the clock time here.)
            # E.g., "2018_04_07_1733_"
            timefmt = '%Y_%m_%d_%H%M_'
            if fact.start:
                prefix = fact.start.strftime(timefmt)
            elif fact.end:
                prefix = fact.end.strftime(timefmt)
        return prefix

    def prepare_suffix():
        # User can set a suffix, which can be useful so, e.g., Vim
        # sees the extension and set filetype appropriately.
        # (lb): I like my Hamster logs to look like reST documents!
        suffix = controller.config['term.editor_suffix'] or None
        return suffix

    return _ask_edit_with_editor()


def run_editor_safe(filename, contents=None):
    def _run_editor_safe():
        try:
            return run_editor()
        except Exception as err:
            msg = _('Unable to run $EDITOR: {}').format(str(err))
            dob_in_user_warning(msg)
            return ''

    def run_editor():
        if is_editor_set() or not running_windows():
            # If Linux and EDITOR not set, editor.edit runs Vim.
            return run_editor_normal()
        else:
            return run_editor_windows()

    def is_editor_set():
        try:
            return bool(os.environ['EDITOR'])
        except KeyError:
            return False

    def running_windows():
        return platform.system() == 'Windows'

    def run_editor_normal():
        # NOTE: You'll find EDITOR features in multiple libraries.
        #       The UX should be indistinguishable to the user.
        #       E.g., we could use click's `edit` instead of editor's:
        #
        #           click.edit(text=None,
        #                      editor=None,
        #                      env=None,
        #                      require_save=True,
        #                      extension='.txt',
        #                      filename=None)
        #
        #       Except that dob-viewer does not have click as a dependency.
        #
        # NOTE: Neither editor.edit nor click.edit appreciate arguments, e.g.,
        #       you might want to start Vim in insert mode and send cursor home:
        #
        #           export EDITOR="vim -c 'startinsert' -c 'norm! gg'"
        #
        #       but this'll crash (they treat the complete $EDITOR string as a
        #       path). (lb): But I'm not wrong expecting this! It works fine in
        #       other tools, e.g., `git commit -v` is perfectly happy with it.
        #
        #       As a work-around, you can put the command in an executable on
        #       PATH, e.g.,
        #
        #           echo -e '#!/bin/sh\nvim -c "startinsert" -c "norm! gg" "${@}"' \
        #               > ~/.local/bin/vim-wrap
        #           chmod 755 ~/.local/bin/vim-wrap
        #           export EDITOR="vim-wrap"
        #
        result = editor.edit(filename=filename, contents=contents)
        edited = result.decode()
        # Necessary?:
        #   edited = result.decode('utf-8')
        return edited

    def run_editor_windows():
        # NOTE: On Windows, EDITOR is not set by default, but neither is Vim, so
        #       editor.edit() will not work.
        #       - To set via PowerShell, try, e.g.,
        #           $Env:EDITOR = "notepad.exe"
        #       - In CMD.exe, use setx to set *persistent* variable (and then start
        #         another CMD prompt), e.g.,
        #           setx EDITOR "notepad.exe"
        # NOTE: There's a Windows-only os.startfile() that acts like double-clicking
        #       the file -- it opens the text file with the user's preferred editor --
        #       but it runs asynchronously. And we need to block. E.g., not this:
        #           os.startfile(filename, 'open')
        #       so just default to notepad, which will be installed. User should set
        #       EDITOR if they want to use a different text editor on Windows.
        with open(filename, 'wb') as temp_f:
            temp_f.write(contents)
        import subprocess
        subprocess.call(['notepad.exe', filename])
        with open(filename, 'r') as temp_f:
            edited = temp_f.read()
        return edited

    return _run_editor_safe()

