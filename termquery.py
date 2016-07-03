#!/usr/bin/env python3

"""
Usage:
  termquery <command> [<args>...]
  termquery [options]

Options:
  -h, --help    Show this screen.
  --version     Show version.

Some common termquery commands are:
  init          Initialize database
  import        Import new keywords into existing database
  query         Queries the database
  help          Shows extensive help message

See 'termquery help <command>' for more information on a specific command.
"""

from collections import namedtuple
from docopt import docopt, DocoptExit
import os
import sys


CONFIGFILE=os.path.expanduser("~/.config/termquery/config")


# TODO: Review example entry from our terminology database
# HINT: due to the design decisions, the key term is NOT included
entry = namedtuple('entry',
                   (# a list of possible other terms
                    'terms',
                    # type of the term: adj (=adjective), noun, verb
                    'type',
                    # exhaustive definition of the term
                    'definition',
                    # list of rejected terms
                    'rejected',
                    )
                   )


# Metclass for a subcommand
class MetaCommand(type):
    """Meta class for commands

    Adds a .registry variable to the class' dictionary
    Expects a 'subcommand' class variable
    """
    def __init__(cls, name, bases, attrdict):
        super().__init__(name, bases, attrdict)
        try:
            cmd = attrdict['subcommand']
        except KeyError:
            raise ValueError("Missing class variable 'subcommand'")
        if not hasattr(cls, 'registry'):
            cls.registry = dict()
        # Remove base class
        if cmd is not None:
            cls.registry[cmd] = cls

    # Metamethods, called on class objects:
    def __iter__(cls):
        return iter(cls.registry)
    def __str__(cls):
        if cls in cls.registry:
            return cls.__name__
        return cls.__name__ + ": " + ", ".join([sc.__name__ for sc in cls])


# Class for each subcommand, using the metaclass
class SubCommand(metaclass=MetaCommand):
    # As this is a subclass, we don't need a subcommand, but we still have
    # to define it (as 'subcommand' is used by the metaclass)
    subcommand = None

    def __repr__(self):
        return "%s: %s" % (self.__class__.__name__, self.subcommand)

    @classmethod
    def cli(cls):
        """Method to return dict object from docopt parsing

        HINT: Use this method in the derived class if you need to validate
              or check some options
        """
        if cls.__doc__ is None:
            return {}
        # Save the result of CLI parsing in its class under the
        # 'clires' variable:
        cls.clires = docopt(cls.__doc__, options_first=True)
        return cls.clires

    @classmethod
    def process(cls):
        """Method which is called after parsing CLI arguments

        HINT: Use this method in the derived class if you want to do
              something with the options.
              The options are parsed through the cli() method. In general,
              it's enough to just define this method.
              After CLI parsing you can find the dictionary in cls.clires
        """
        return cls.cli()


class SubHelp(SubCommand):
    """Show extensive help of a subcommand

Usage:
    termquery help [<command>]
    """
    subcommand = "help"

    @classmethod
    def process(cls):
        """Process help of a subcommand"""
        super().process()
        cmd = cls.clires['<command>']
        othercls = SubCommand.registry.get(cmd)
        if cmd is None:
            print(__doc__)
        elif cmd in ('-h', '--help'):
            print(cls.__doc__)
        else:
            print(othercls.__doc__)
        return


class SubImport(SubCommand):
    """Import data from CSV file into terminology database

Steps:
   1. Open configuration file
   2. Determine location and type
   3. Open CSV file
   4. Import CSV data into database; skip existing entries

Usage:
   termquery import [options] <csvfilename>
   termquery import -h | --help

Options:
   -h, --help    Show this screen.

Arguments:
   csvfilename   Path to the CSV file
    """
    subcommand = "import"

    @classmethod
    def process(cls):
        super().process()
        print("Importing CSV file %r" % cls.clires['<csvfilename>'])


class SubInit(SubCommand):
    """Initialize terminology database

Steps:
   1. Initialize the database
   2. Write type and location/path into config file

Usage:
   termquery init [options] <type> <filename>
   termquery init -h | --help

Options:
   -h, --help    Show this screen.
   -f, --force   Overwrite existing database

Arguments:
   type          the type of the database
   filename      the filename of the database
    """
    subcommand = "init"
    VALIDTYPES = ('pickle', 'shelve')

    @classmethod
    def cli(cls):
        super().cli()
        dbtype = cls.clires.get('<type>')
        if dbtype not in cls.VALIDTYPES:
            raise ValueError("Not a valid type: %r. "
                             "Only these are possible: %s." % (
                             dbtype,
                             ", ".join(cls.VALIDTYPES))
                             )
        # Prepare a _call key which contains a map of all possible
        # valid database types to the class method
        # We use "_" in "_call" to avoid possible name clashes with
        # docopt (which should not happen)
        cls.clires['_call'] = {item: getattr(cls, "db_" + item)
                               for item in cls.VALIDTYPES}
        return cls.clires

    @classmethod
    def process(cls):
        super().process()
        filename = cls.clires['<filename>']
        func = cls.clires['_call'][cls.clires['<type>']]
        func(cls, filename)
        cls.config()
        return

    def db_shelve(cls, filename):
        print("TODO: use the shelve module to create the %r file." % filename)

    def db_pickle(cls, filename):
        print("TODO: use the pickle module to create the %r file." % filename)

    @classmethod
    def config(cls):
        print("TODO: Writing config parameters")


class SubQuery(SubCommand):
    """Queries the terminology database

Usage:
   termquery query [options] <querystring>
   termquery query -h | --help

Options:
   -h, --help    Show this screen.
    """
    subcommand = "query"

    @classmethod
    def process(cls):
        super().process()
        return "queryresult"


def main():
    """Our main function"""
    cli = docopt(__doc__,
                 version='termquery v0.1.0',
                 options_first=True,
                 )
    cmd = SubCommand.registry.get(cli['<command>'])
    if cmd is None:
        raise ValueError("Subcommand %r not found" % cli['<command>'])
    # result = cmd.cli()
    result = cmd.process()
    return result


if __name__ == "__main__":
    try:
        cli = main()
        if cli is not None:
            print("result:", cli)
    except ValueError as error:
        print("ERROR:", error, file=sys.stderr)
        sys.exit(10)
