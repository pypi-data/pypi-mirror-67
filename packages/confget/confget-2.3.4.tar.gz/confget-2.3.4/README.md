confget - parse configuration files
===================================

The `confget` library parses configuration files (currently INI-style
files and CGI `QUERY_STRING` environment variable) and allows a program
to use the values defined in them.  It provides various options for
selecting the variable names and values to return and the configuration
file sections to fetch them from.

The `confget` library may also be used as a command-line tool with
the same interface as the C implementation.

The `confget` library is fully typed.

Specifying configuration values for the backends
------------------------------------------------

The `confget.defs` module defines the `Config` class that is used to
control the behavior of the various `confget` backends.  Its main
purpose is to specify the filename and, optionally, the section name for
INI-style files, but other backends may use its fields in different ways.

A `Config` object is created using the following parameters:
- a list of variable names to query (may be empty)
- `filename` (str, optional): the name of the file to open
- `section` (str, default ""): the name of the section within the file
- `section_specified` (bool, default false): if `section` is an empty
  string, only fetch variables from the unnamed section at the start of
  the file instead of defaulting to the first section in the file

Parsing INI-style configuration files
-------------------------------------

The `confget` library's "ini" backend parses an INI-style configuration
file.  Its `read_file()` method parses the file and returns a dictionary
of sections and the variables and their values within them:

    import confget
    
    cfg = confget.Config([], filename='config.ini')
    ini = confget.BACKENDS['ini'](cfg)
    data = ini.read_file()
    print('Section names: {names}'.format(names=sorted(data.keys())))
    print(data['server']['address'])

Letting variables in a section override the default ones
--------------------------------------------------------

In some cases it is useful to have default values before the first
named section in a file and then override some values in various
sections.  This may be useful for e.g. host-specific configuration
kept in a section with the same name as the host.

The `format` module in the `confget` library allows, among other
filtering modes, to get the list of variables with a section
overriding the default ones:

    from confget import backend, format

    cfg = format.FormatConfig(['foo'], filename='config.ini', section='first',
                              section_override=True)
    ini = backend.BACKENDS['ini'](cfg)
    data = ini.read_file()
    res = format.filter_vars(cfg, data)
    assert len(res) == 1, repr(res)
    print(res[0].output_full)

    cfg = format.FormatConfig(['foo'], filename='config.ini', section='second',
                              section_override=True)
    ini = backend.BACKENDS['ini'](cfg)
    data = ini.read_file()
    res = format.filter_vars(cfg, data)
    assert len(res) == 1, repr(res)
    print(res[0].output_full)

See the documentation of the `FormatConfig` class and the `filter_vars()`
function in the `confget.format` module for more information and for
a list of the various other filtering modes, all supported when
the library is used as a command-line tool.

Comments: Peter Pentchev <roam@ringlet.net>
