"""This module allows for opening a PkPass interactive interpreter"""
# Look, I know what I did; I'm sorry about the following file.
# I pray that there exists a better way to do this. This file
# Should be burned to the ground and never spoken of again.
# You know it, I know it, everybody knows it.

# We need to disable unused import linting because the command classes *are* actually used...
# pylint: disable=unused-import
import os
import sys
import glob
import subprocess
from cmd import Cmd
from inspect import getmembers, isclass
import yaml
from libpkpass.commands.command import Command
import libpkpass.util as util
import libpkpass.commands.card as card
import libpkpass.commands.clip as clip
import libpkpass.commands.create as create
import libpkpass.commands.delete as delete
import libpkpass.commands.distribute as distribute
import libpkpass.commands.export as export
import libpkpass.commands.fileimport as pkimport
import libpkpass.commands.generate as generate
import libpkpass.commands.info as info
import libpkpass.commands.list as pklist
import libpkpass.commands.listrecipients as listrecipients
import libpkpass.commands.modify as modify
import libpkpass.commands.recover as recover
import libpkpass.commands.rename as rename
import libpkpass.commands.show as show
import libpkpass.commands.update as update
import libpkpass.commands.pkinterface as pkinterface
from libpkpass.errors import PKPassError

VERSION = util.show_version()

    ####################################################################
class Interpreter(Command):
    """This class implements a skeleton to call the interpreter"""
    name = 'interpreter'
    description = 'Interactive mode for pkpass'
    selected_args = Command.selected_args + ['card_slot', 'connect', 'escrow_users', 'min_escrow',
                                             'groups', 'keypath', 'pwstore']
    ####################################################################

        ####################################################################
    def _run_command_execution(self):
        """ Run function for class. """
        ####################################################################
        Interactive(self.args, self.identities).cmdloop_with_keyboard_interrupt()

        ####################################################################
    def _validate_args(self):
        ####################################################################
        pass

# This is to keep argparse from sys.exiting all over the place
    ####################################################################
def pkparse_error(message):
    ####################################################################
    raise PKPassError(message)

    ####################################################################
class Interactive(Cmd, pkinterface.PkInterface):
    """This class implements the interactive interpreter functionality"""
    intro = """Welcome to PKPass (Public Key Based Password Manager) v%s!
Type ? to list commands""" % VERSION
    prompt = 'pkpass> '
    ####################################################################

        ####################################################################
    def __init__(self, args, recipients_database):
        ####################################################################
        Cmd.__init__(self)
        # manually remove interpreter from command line so that argparse doesn't try to use it
        # This needs to be removed before the PkInterace init
        sys.argv.remove('interpreter')

        pkinterface.PkInterface.__init__(self)

        self.recipients_database = recipients_database
        self.parser.error = pkparse_error

        # Hold onto args passed on the command line
        self.pre_args = args
        # change our cwd so users can tab complete
        self._change_pwstore()

        # We basically need to grab the first argument and ditch it
        self.parsedargs = {}

        ####################################################################
    def cmdloop_with_keyboard_interrupt(self):
        """handle keyboard interrupts"""
        ####################################################################
        breaker = False
        first = True
        while breaker is not True:
            try:
                if first:
                    self.cmdloop()
                else:
                    self.cmdloop(intro='')
                breaker = True
            except KeyboardInterrupt:
                first = False
                sys.stdout.write('\n')

        ####################################################################
    def _change_pwstore(self):
        """Change directory"""
        ####################################################################
        direc = self.pre_args['pwstore']
        if 'pwstore' in self.pre_args and direc and os.path.isdir(direc):
            os.chdir(direc)

        ####################################################################
    def _reload_config(self):
        """Change affected globals in interpreter"""
        ####################################################################
        # We still need to be able to reload other things like recipients
        # database
        config = self.pre_args['config']
        try:
            with open(config, 'r') as fname:
                config_args = yaml.safe_load(fname)
            if config_args is None:
                config_args = {}
        except IOError:
            print("No .pkpassrc file found, consider running ./setup.sh")
        finally:
            self.pre_args['pwstore'] = config_args['pwstore']
            self._change_pwstore()

        ####################################################################
    def precmd(self, line):
        """ Fix command line arguments, this is a hack to allow argparse
        function as we expect """
        ####################################################################
        sys.argv = [sys.argv[0]]
        sys.argv.extend(line.split())
        return line

        ####################################################################
    def postcmd(self, stop, line):
        """ Fix command line arguments, this is a hack to allow argparse
        function as we expect """
        ####################################################################
        if str(line) == "edit":
            self._reload_config()
        return Cmd.postcmd(self, stop, line)

        ####################################################################
    def _append_slash_if_dir(self, path_arg):
        """ Appending slashes for autocomplete_file_path """
        ####################################################################
        if path_arg and os.path.isdir(path_arg) and path_arg[-1] != os.sep:
            return path_arg + os.sep
        return path_arg

        ####################################################################
    def autocomplete_file_path(self, _, line, begidx, endidx):
        """ File path autocompletion, used with the cmd module complete_* series functions"""
        ####################################################################
        before_arg = line.rfind(" ", 0, begidx)
        if before_arg == -1:
            return None # arg not found

        fixed = line[before_arg+1:begidx]  # fixed portion of the arg
        arg = line[before_arg+1:endidx]
        pattern = arg + '*'

        completions = []
        for path in glob.glob(pattern):
            path = self._append_slash_if_dir(path)
            completions.append(path.replace(fixed, "", 1))
        return completions

        ####################################################################
    def default(self, line):
        """If we don't have a proper subcommand passed"""
        ####################################################################
        print("Command '%s' not found, see help (?) for available commands"
              % line)
        return False

        ####################################################################
    def do_exit(self, _):
        """Exit the application"""
        ####################################################################
        return True

        ####################################################################
    def do_version(self, _):
        """Print the version of PkPass"""
        ####################################################################
        print(VERSION)

        ####################################################################
    def do_edit(self, _):
        """Edit your configuration file, with $EDITOR"""
        ####################################################################
        try:
            subprocess.call([os.environ['EDITOR'], self.pre_args['config']])
            return False
        except (IOError, SystemExit):
            return False

        ####################################################################
    def do_git(self, line):
        """If your password store is git back, you can control git from here"""
        ####################################################################
        subprocess.call(["git"] + line.split())
        return False

    ##############################################################################
def add_dynamic_function(module_name, class_name):
    """This allows repetitive do_* and complete_* functions to be condensed"""
    ##############################################################################
    swap_name = module_name
    if "pk" in module_name:
        swap_name = module_name[2:]
    fn_name = "do_" + swap_name
    complete_name = "complete_" + swap_name

        ############################################
    def do_fn(self, _):
        """Use -h or --help for information"""
        ############################################
        try:
            pk_class = [o for o in getmembers(globals()[module_name], isclass)
                        if str(o[0]) == class_name][0][1]
            pk_class(self, iddb=self.recipients_database)
            self.actions[swap_name].run(self.parser.parse_args())
            return False
        except PKPassError as err:
            print(err)
            return False
        except SystemExit:
            return False

        ##################################################
    def complete_fn(self, text, line, begidx, endidx):
        ##################################################
        return self.autocomplete_file_path(text, line, begidx, endidx)

    setattr(Interactive, fn_name, do_fn)
    setattr(Interactive, complete_name, complete_fn)

for command in [('card', 'Card'), ('clip', 'Clip'), ('create', 'Create'), ('delete', 'Delete'),
                ('distribute', 'Distribute'), ('export', 'Export'),
                ('generate', 'Generate'), ('pkimport', 'Import'), ('info', 'Info'),
                ('pklist', 'List'), ('listrecipients', 'Listrecipients'),
                ('modify', 'Modify'), ('recover', 'Recover'), ('rename', 'Rename'),
                ('show', 'Show'), ('update', 'Update')]:
    add_dynamic_function(command[0], command[1])
