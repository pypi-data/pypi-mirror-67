from __future__ import division, print_function

import os
import re
import requests
import ast
import inspect
import six
from glob import glob
from os.path import join, sep
from random import choice, sample
from collections import OrderedDict
from sdss_access import tree
from sdss_access import is_posix

pathlib = None
try:
    import pathlib
except ImportError:
    import pathlib2 as pathlib

try:
    from ConfigParser import RawConfigParser
except ImportError:
    from configparser import RawConfigParser

"""
Module for constructing paths to SDSS files.

Example use case:

    from sdss_access.path import Path
    sdss_path = Path()
    filename = sdss_path.full('photoObj', run=94, rerun='301', camcol=1, field=100)

Depends on the tree product. In particular requires path templates in:
  $TREE_DIR/data/sdss_paths.ini
"""


class BasePath(object):
    """Class for construction of paths in general.

    Attributes
    ----------
    templates : dict
        The set of templates read from the configuration file.
    """

    _netloc = {"dtn": "sdss@dtn01.sdss.org", "sdss": "data.sdss.org", "mirror": "data.mirror.sdss.org"}

    def __init__(self, pathfile, mirror=False, public=False, release=None, verbose=False):
        self.mirror = mirror
        self.public = public
        self.release = release
        self.verbose = verbose
        self.set_netloc()
        self.set_remote_base()
        self._pathfile = pathfile
        self._config = RawConfigParser()
        self._config.optionxform = str
        self.templates = OrderedDict()
        self._input_templates()
        if release != tree.config_name:
            self.replant_tree()

    def replant_tree(self):
        ''' replants the tree based on release '''
        release = self.release.lower() if self.release else None
        tree.replant_tree(release)

    def _input_templates(self):
        """Read the path template file.
        """
        foo = self._config.read([self._pathfile])
        if len(foo) == 1:
            for k, v in self._config.items('paths'):
                self.templates[k] = v
        else:
            raise ValueError("Could not read {0}!".format(self._pathfile))
        return

    def lookup_keys(self, name):
        ''' Lookup the keyword arguments needed for a given path name

        Parameters:
            name (str):
                The name of the path

        Returns:
            A list of keywords needed for filepath generation

        '''

        assert name, 'Must specify a path name'
        assert name in self.templates.keys(), '{0} must be defined in the path templates'.format(name)
        # find all words inside brackets
        keys = list(set(re.findall(r'{(.*?)}', self.templates[name])))
        # lookup any keys referenced inside special functions
        skeys = self._check_special_kwargs(name)
        keys.extend(skeys)
        # remove any duplicates
        keys = list(set(keys))
        # remove the type : descriptor
        keys = [k.split(':')[0] for k in keys]
        return keys

    def _check_special_kwargs(self, name):
        ''' check special functions for kwargs

        Checks the content of the special functions (%methodname) for
        any keyword arguments referenced within

        Parameters:
            name (str):
                A path key name

        Returns:
            A list of keyword arguments found in any special functions
        '''
        keys = []
        # find any %method names in the template string
        functions = re.findall(r"\%\w+", self.templates[name])
        if not functions:
            return keys

        # loop over special method names and extract keywords
        for function in functions:
            method = getattr(self, function[1:])
            # get source code of special method
            source = self._find_source(method)
            fkeys = re.findall(r'kwargs\[(.*?)\]', source)
            if fkeys:
                # evaluate to proper string
                fkeys = [ast.literal_eval(k) for k in fkeys]
                keys.extend(fkeys)
        return keys

    @staticmethod
    def _find_source(method):
        ''' find source code of a given method

        Find and extract the source code of a given method in a module.
        Uses inspect.findsource to get all source code and performs some
        selection magic to identify method source code.  Doing it this way
        because inspect.getsource returns wrong method.

        Parameters:
            method (obj):
                A method object

        Returns:
            A string containing the source code of a given method

        Example:
            >>> from sdss_access.path import Path
            >>> path = Path()
            >>> path._find_source(path.full)
        '''

        # get source code lines of entire module method is in
        source = inspect.findsource(method)
        is_method = inspect.ismethod(method)
        # create single source code string
        source_str = '\n'.join(source[0])
        # define search pattern
        if is_method:
            pattern = r'def\s{0}\(self'.format(method.__name__)
        # search for pattern within the string
        start = re.search(pattern, source_str)
        if start:
            # find start and end positions of source code
            startpos = start.start()
            endpos = source_str.find('def ', startpos + 1)
            code = source_str[startpos:endpos]
        else:
            code = None
        return code

    def lookup_names(self):
        ''' Lookup what path names are available

        Returns a list of the available path names in sdss_access.
        Use with lookup_keys to find the required keyword arguments for a
        given path name.

        Returns:
            A list of the available path names.
        '''
        return self.templates.keys()

    def extract(self, name, example):
        ''' Extract keywords from an example path '''

        # if pathlib not available do nothing
        if not pathlib:
            return None

        # ensure example is a string
        if isinstance(example, pathlib.Path):
            example = str(example)
        assert isinstance(example, six.string_types), 'example file must be a string'

        # get the template
        assert name in self.lookup_names(), '{0} must be a valid template name'.format(name)
        template = self.templates[name]

        # expand the environment variable
        template = os.path.expandvars(template)

        # handle special functions; perform a drop in replacement
        if re.match('%spectrodir', template):
            template = re.sub('%spectrodir', os.environ['BOSS_SPECTRO_REDUX'], template)
        elif re.search('%platedir', template):
            template = re.sub('%platedir', '(.*)/{plateid:0>6}', template)
        elif re.search('%definitiondir', template):
            template = re.sub('%definitiondir', '{designid:0>6}', template)
        if re.search('%plateid6', template):
            template = re.sub('%plateid6', '{plateid:0>6}', template)

        # check if template has any brackets
        haskwargs = re.search('[{}]', template)
        if not haskwargs:
            return None

        # escape the envvar $ and any dots
        subtemp = template.replace('$', '\\$').replace('.', '\\.')
        # define search pattern; replace all template keywords with regex "(.*)" group
        research = re.sub('{(.*?)}', '(.*)', subtemp)
        # look for matches in template and example
        pmatch = re.search(research, template)
        tmatch = re.search(research, example)

        path_dict = {}
        # if example match extract keys and values from the match groups
        if tmatch:
            values = tmatch.groups(0)
            keys = pmatch.groups(0)
            assert len(keys) == len(values), 'pattern and template matches must have same length'
            parts = zip(keys, values)
            # parse into dictionary
            for part in parts:
                value = part[1]
                if re.findall('{(.*?)}', part[0]):
                    # get the key name inside the brackets
                    keys = re.findall('{(.*?)}', part[0])
                    # remove the type : designation
                    keys = [k.split(':')[0] for k in keys]
                    # handle double bracket edge cases; remove this when better solution found
                    if len(keys) > 1:
                        if keys[0] == 'dr':
                            # for {dr}{version}
                            drval = re.match('^DR[1-9][0-9]', value).group(0)
                            otherval = value.split(drval)[-1]
                            pdict = {keys[0]: drval, keys[1]: otherval}
                        elif keys[0] in ['rc', 'br', 'filter', 'camrow']:
                            # for {camrow}{camcol}, {filter}{camcol}, {br}{id}, etc
                            pdict = {keys[0]: value[0], keys[1]: value[1:]}
                        else:
                            raise ValueError('This case has not yet been accounted for.')
                        path_dict.update(pdict)
                    else:
                        path_dict[keys[0]] = value
        return path_dict

    def dir(self, filetype, **kwargs):
        """Return the directory containing a file of a given type.

        Parameters
        ----------
        filetype : str
            File type parameter.

        Returns
        -------
        dir : str
            Directory containing the file.
        """

        full = kwargs.get('full', None)
        if not full:
            full = self.full(filetype, **kwargs)

        return os.path.dirname(full)

    def name(self, filetype, **kwargs):
        """Return the name of a file of a given type.

        Parameters
        ----------
        filetype : str
            File type parameter.

        Returns
        -------
        name : str
            Name of a file with no directory information.
        """

        full = kwargs.get('full', None)
        if not full:
            full = self.full(filetype, **kwargs)

        return os.path.basename(full)

    def exists(self, filetype, remote=None, **kwargs):
        '''Checks if the given type of file exists locally

        Parameters
        ----------
        filetype : str
            File type parameter.

        remote : bool
            If True, checks for remote existence of the file

        Returns
        -------
        exists : bool
            Boolean indicating if the file exists.

        '''

        full = kwargs.get('full', None)
        if not full:
            full = self.full(filetype, **kwargs)

        if remote:
            # check for remote existence using a HEAD request
            url = self.url('', full=full)
            try:
                resp = requests.head(url, allow_redirects=True)
            except Exception as e:
                raise AccessError('Cannot check for remote file existence for {0}: {1}'.format(url, e))
            else:
                return resp.ok
        else:
            return os.path.isfile(full)

    def expand(self, filetype, **kwargs):
        ''' Expand a wildcard path locally

        Parameters
        ----------
        filetype : str
            File type parameter.

        as_url: bool
            Boolean to return SAS urls

        refine: str
            Regular expression string to filter the list of files by
            before random selection

        Returns
        -------
        expand : list
            List of expanded full paths of the given type.

        '''

        full = kwargs.get('full', None)
        if not full:
            full = self.full(filetype, **kwargs)

        # assert '*' in full, 'Wildcard must be present in full path'
        files = glob(full)

        # return as urls?
        as_url = kwargs.get('as_url', None)
        newfiles = [self.url('', full=full) for full in files] if as_url else files

        # optionally refine the results
        refine = kwargs.get('refine', None)
        if refine:
            newfiles = self.refine(newfiles, refine, **kwargs)

        return newfiles

    def any(self, filetype, **kwargs):
        ''' Checks if the local directory contains any of the type of file

        Parameters
        ----------
        filetype : str
            File type parameter.

        Returns
        -------
        any : bool
            Boolean indicating if the any files exist in the expanded path on disk.

        '''
        expanded_files = self.expand(filetype, **kwargs)
        return any(expanded_files)

    def one(self, filetype, **kwargs):
        ''' Returns random one of the given type of file

        Parameters
        ----------
        filetype : str
            File type parameter.

        as_url: bool
            Boolean to return SAS urls

        refine: str
            Regular expression string to filter the list of files by
            before random selection

        Returns
        -------
        one : str
            Random file selected from the expanded list of full paths on disk.

        '''
        expanded_files = self.expand(filetype, **kwargs)
        isany = self.any(filetype, **kwargs)
        return choice(expanded_files) if isany else None

    def random(self, filetype, **kwargs):
        ''' Returns random number of the given type of file

        Parameters
        ----------
        filetype : str
            File type parameter.

        num : int
            The number of files to return

        as_url: bool
            Boolean to return SAS urls

        refine: str
            Regular expression string to filter the list of files by
            before random selection

        Returns
        -------
        random : list
            Random file selected from the expanded list of full paths on disk.

        '''
        expanded_files = self.expand(filetype, **kwargs)
        isany = self.any(filetype, **kwargs)
        if isany:
            # get the desired number
            num = kwargs.get('num', 1)
            assert num <= len(expanded_files), 'Requested number must be larger the sample.  Reduce your number.'
            return sample(expanded_files, num)
        else:
            return None

    def refine(self, filelist, regex, filterdir='out', **kwargs):
        ''' Returns a list of files filterd by a regular expression

        Parameters
        ----------
        filelist : list
            A list of files to filter on.

        regex : str
            The regular expression string to filter your list

        filterdir: {'in', 'out'}
            Indicates the filter to be inclusive or exclusive
            'out' removes the items satisfying the regular expression
            'in' keeps the items satisfying the regular expression

        Returns
        -------
        refine : list
            A file list refined by an input regular expression.

        '''
        assert filelist, 'Must provide a list of filenames to refine on'
        assert regex, 'Must provide a regular expression to refine the file list'
        r = re.compile(regex)

        # icheck filter direction; default is out
        assert filterdir in ['in', 'out'], 'Filter direction must be either "in" or "out"'
        if filterdir == 'out':
            subset = list(filter(lambda i: r.search(i), filelist))
        elif filterdir == 'in':
            subset = list(filter(lambda i: not r.search(i), filelist))
        return subset

    def full(self, filetype, **kwargs):
        """Return the full name of a given type of file.

        Parameters
        ----------
        filetype : str
            File type parameter.

        Returns
        -------
        full : str
            The full path to the file.
        """

        # check if full already in kwargs
        if 'full' in kwargs:
            return kwargs.get('full')

        # check for filetype in template
        assert filetype in self.templates, ('No entry {0} found. Filetype must '
                                            'be one of the designated templates '
                                            'in the currently loaded tree'.format(filetype))
        template = self.templates[filetype]
        if not is_posix:
            template = template.replace('/',sep)

        # Now replace {} items
        if template:
            # check for missing keyword arguments
            keys = self.lookup_keys(filetype)
            # split keys to remove :format from any "key:format"
            keys = [k.split(':')[0] for k in keys]
            missing_keys = set(keys) - set(kwargs.keys())
            if missing_keys:
                raise KeyError('Missing required keyword arguments: {0}'.format(list(missing_keys)))
            else:
                template = template.format(**kwargs)

        if template:
            # Now replace environmental variables
            template = os.path.expandvars(template)

            # Now call special functions as appropriate
            template = self._call_special_functions(filetype, template, **kwargs)

        return template

    def _call_special_functions(self, filetype, template, **kwargs):
        ''' Call the special functions found in a template path

        Calls special functions indicated by %methodname found in the
        sdss_paths.ini template file, and replaces the %location in the path
        with the returned content.

        Parameters:
            filetype (str):
                template name of file
            template (str):
                the template path
            kwargs (dict):
                Any kwargs needed to pass into the methods

        Returns:
            The expanded template path
        '''
        # Now call special functions as appropriate
        functions = re.findall(r"\%\w+", template)
        if not functions:
            return template

        for function in functions:
            try:
                method = getattr(self, function[1:])
            except AttributeError:
                return None
            else:
                value = method(filetype, **kwargs)
                template = template.replace(function, value)

        return template

    def set_netloc(self, netloc=None, sdss=None, dtn=None):
        if netloc:
            self.netloc = netloc
            return

        if dtn:
            self.netloc = self._netloc["dtn"]
        elif sdss:
            self.netloc = self._netloc['sdss']
        elif self.mirror:
            self.netloc = self._netloc["mirror"]
        else:
            self.netloc = self._netloc['sdss']
        #self.netloc = netloc if netloc else self._netloc["sdss"] if sdss else self._netloc["dtn"] if dtn else self._netloc["mirror"] if self.mirror else self._netloc["sdss"]

    def set_remote_base(self, scheme=None):
        self.remote_base = self.get_remote_base(scheme=scheme) if scheme else self.get_remote_base()

    def get_remote_base(self, scheme="https"):
        return "{scheme}://{netloc}".format(scheme=scheme, netloc=self.netloc)

    def set_base_dir(self, base_dir=None):

        if base_dir:
            self.base_dir = base_dir
        else:
            try:
                self.base_dir = join(os.environ['SAS_BASE_DIR'], '')
            except Exception:
                pass

    def location(self, filetype, base_dir=None, **kwargs):
        """Return the location of the relative sas path of a given type of file.

        Parameters
        ----------
        filetype : str
            File type parameter.

        Returns
        -------
        full : str
            The relative sas path to the file.
        """

        full = kwargs.get('full', None)
        if not full:
            full = self.full(filetype, **kwargs)

        self.set_base_dir(base_dir=base_dir)
        location = full[len(self.base_dir):] if full and full.startswith(self.base_dir) else None

        if location and '//' in location:
            location = location.replace('//', '/')

        return location

    def url(self, filetype, base_dir=None, sasdir='sas', **kwargs):
        """Return the url of a given type of file.

        Parameters
        ----------
        filetype : str
            File type parameter.

        Returns
        -------
        full : str
            The sas url to the file.
        """

        location = self.location(filetype, **kwargs)
        url = join(self.remote_base, sasdir, location) if self.remote_base and location else None
        if not is_posix:
            url = url.replace(sep,'/')
        return url


class Path(BasePath):
    """Class for construction of paths in general.  Sets a particular template file.
    """
    def __init__(self, mirror=False, public=False, release=None, verbose=False):
        try:
            tree_dir = os.environ['TREE_DIR']
        except KeyError:
            raise NameError("Could not find TREE_DIR in the environment!  Did you load the tree product?")
        pathfile = os.path.join(tree_dir, 'data', 'sdss_paths.ini')

        super(Path, self).__init__(pathfile, mirror=mirror, public=public, release=release, verbose=verbose)

    def plateid6(self, filetype, **kwargs):
        """Print plate ID, accounting for 5-6 digit plate IDs.

        Parameters
        ----------
        filetype : str
            File type parameter.
        plateid : int or str
            Plate ID number.  Will be converted to int internally.

        Returns
        -------
        plateid6 : str
            Plate ID formatted to a string of 6 characters.
        """
        plateid = int(kwargs['plateid'])
        if plateid < 10000:
            return "{:0>6d}".format(plateid)
        else:
            return "{:d}".format(plateid)

    def platedir(self, filetype, **kwargs):
        """Returns plate subdirectory in :envvar:`PLATELIST_DIR` of the form: ``NNNNXX/NNNNNN``.

        Parameters
        ----------
        filetype : str
            File type parameter.
        plateid : int or str
            Plate ID number.  Will be converted to int internally.

        Returns
        -------
        platedir : str
            Plate directory in the format ``NNNNXX/NNNNNN``.
        """
        plateid = int(kwargs['plateid'])
        plateid100 = plateid // 100
        subdir = "{:0>4d}".format(plateid100) + "XX"
        return os.path.join(subdir, "{:0>6d}".format(plateid))

    def spectrodir(self, filetype, **kwargs):
        """Returns :envvar:`SPECTRO_REDUX` or :envvar:`BOSS_SPECTRO_REDUX`
        depending on the value of `run2d`.

        Parameters
        ----------
        filetype : str
            File type parameter.
        run2d : int or str
            2D Reduction ID.

        Returns
        -------
        spectrodir : str
            Value of the appropriate environment variable.
        """
        if str(kwargs['run2d']) in ('26', '103', '104'):
            return os.environ['SPECTRO_REDUX']
        else:
            return os.environ['BOSS_SPECTRO_REDUX']

    def definitiondir(self, filetype, **kwargs):
        """Returns definition subdirectory in :envvar:`PLATELIST_DIR` of the form: ``NNNNXX``.

        Parameters
        ----------
        filetype : str
            File type parameter.
        designid : int or str
            Design ID number.  Will be converted to int internally.

        Returns
        -------
        definitiondir : str
            Definition directory in the format ``NNNNXX``.
        """

        designid = int(kwargs['designid'])
        designid100 = designid // 100
        subdir = "{:0>4d}".format(designid100) + "XX"
        return subdir


class AccessError(Exception):
    pass
