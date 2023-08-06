""" PIPE STEP PARENT - Version 1.0.0

    This module defines the HAWC pipeline step parent object. Pipe steps are
    the modules responsible for all HAWC data reduction. They are called by
    the pipeline and work with pipedata objects. All pipe step objects are
    descendants from this one. Pipe steps are callable objects that return
    the reduced data product (as pipedata object).

    @author: berthoud
"""

"""
    2DO:
    - later:
      - rename callstart/end -> runstart/end
      - remove parameter from callstart/end
"""

import time # time library
import logging # logging object library
import argparse # Argument parsing library
from configobj import ConfigObj # configuration object
from .dataparent import DataParent # data parent object

class StepParent(object):
    """ HAWC Pipeline Step Parent Object
        The object is callable. It requires a valid configuration input
        (file or object) when it runs.
    """

    stepver = '0.1.1' # pipe step version
    #testconf = 'config/pipeconf_master.txt' # Test configuration
    testconf = 'config/pipeconf_mgb.txt' # Default test configuration

    def __init__(self):
        """ Constructor: Initialize data objects and variables
            calls the setup function. Steps get the configuration
            from the datain that is handed to them.
        """
        # initialize input and output
        self.datain = DataParent()
        self.dataout = DataParent()
        # set names
        self.name = None
        self.procname = None
        # set parameters / logger
        self.arglist={} # Dictionary with current arguments
        self.paramlist=[] # List with possible parameters
        # set configuration / logger
        self.config = None
        self.log = None
        # specify whether this step runs on a single PipeData object with a
        # single output PipeData object (SISO), multiple input PipeData objects
        # with multiple output PipeData objects (MIMO), or multiple input Pipefile
        # objects with a single output PipeData object (MISO).
        self.iomode = 'SISO'
        # do local setup
        self.setup()
        self.log.debug('Init: done')

    def setup(self):
        """ ### Names and Prameters need to be Set Here ###
            Sets the internal names for the function and for saved files.
            Defines the input parameters for the current pipe step.
            Setup() is called at the end of __init__
            The parameters are stored in a list containing the following
            information:
            - name: The name for the parameter. This name is used when
                    calling the pipe step from command line or python shell.
                    It is also used to identify the parameter in the pipeline
                    configuration file.
            - default: A default value for the parameter. If nothing, set
                       '' for strings, 0 for integers and 0.0 for floats
            - help: A short description of the parameter.
        """
        ### Set Names
        # Name of the pipeline reduction step
        self.name='parent'
        # Shortcut for pipeline reduction step and identifier for
        # saved file names.
        self.procname = 'unk'
        # Set Logger for this pipe step
        self.log = logging.getLogger('pipe.step.%s' % self.name)
        ### Set Parameter list
        # Clear Parameter list
        self.paramlist = []
        # Append parameters
        self.paramlist.append(['sampar', 1.0,
            'Sample Parameter - parent only - no practical use'])

    def run(self):
        """ Runs the data reduction algorithm. The self.datain is run
            through the code, the result is in self.dataout.
        """
        # Log the value of sample parameter
        self.log.debug("Sample Parameter = %.2f" % self.getarg('sampar'))
        # Copy datain to dataout
        self.dataout = self.datain

    def __call__(self,datain, **arglist):
        """ Object Call: returns reduced input data
        """
        # Get input data
        self.datain = datain
        # Start Setup
        self.runstart(self.datain, arglist)
        # Call the run function
        self.run()
        # Finish - call end
        self.runend(self.dataout)
        # return result
        return self.dataout

    def runstart(self, data, arglist):
        """ Method to call at the beginning of the pipe step call.
            - Sends initial log message
            - Checks the validity of the input data
            - Gets configuration from input data and checks type
        """
        # Start Message
        self.log.info('Start Reduction: Pipe Step %s' % self.name)
        # Set input arguments
        for k in arglist.keys():
            self.arglist[k.lower()] = arglist[k]
        # Check input data type and set data config
        if issubclass(data.__class__, DataParent):
            self.config = data.config
        else:
            msg = 'Invalid input data type: DataParent child object is required'
            self.log.error(msg)
            raise TypeError('Runstart: '+msg)
        # Set Configuration
        if self.config is None: # no config specified, make an empty one
            self.config = ConfigObj()
            self.config[self.name] = {}
        # Check configuration
        if not isinstance(self.config,ConfigObj):
            msg='Invalid configuration information - aborting'
            self.log.error(msg)
            raise RuntimeError('Runstart: '+msg)

    def runend(self,data):
        """ Method to call at the end of pipe the pipe step call
            - Sends final log messages
        """
        # update header (status and history)
        self.updateheader(data)
        # clear input arguments
        self.arglist = {}
        self.log.info('Finished Reduction: Pipe Step %s' % self.name)

    def updateheader(self,data):
        """ Update the header for a single PipeData object
            - Updates filename with self.procname
            - Sets the PROCSTAT and PROCLEVL keywords in the data header
            - Adds a history entry to the data header
        """
        # Update PRODuct TYPE keyword with step name, add history keyword
        data.setheadval('PRODTYPE',self.name,'Product Type')
        histmsg = 'Reduced: ' + self.name + ' v' + self.stepver + ' '
        histmsg += time.strftime('%Y-%m-%d_%H:%M:%S')
        data.setheadval('HISTORY',histmsg)
        # Add input parameters to history
        for p in [par[0] for par in self.paramlist]:
            histmsg = ' %s: %s=%s' % (self.name, p, self.getarg(p))
            data.setheadval('HISTORY',histmsg)
        # Update file name with .PipeStepName.fits
        data.filename = data.filenamebegin + self.procname.upper() + data.filenameend
        # Add config file name if available and not already present
        # in HISTORY
        try:
            # This may fail if config has no filename - in that case,
            # don't add the message.
            conffilename = '' + self.config.filename
            # New history message
            histmsg = 'CONFIG: %s' % conffilename
            # Check history for presence of the full message or possibly
            # a truncated version (eg. for long filenames in FITS headers)
            full_history = data.getheadval('HISTORY')
            if len(histmsg) > 72:
                shortmsg = histmsg[0:72]
            else:
                shortmsg = histmsg
            if histmsg not in full_history and shortmsg not in full_history:
                self.log.debug('Recording config file name %s' % conffilename)
                data.setheadval('HISTORY',histmsg)
        except TypeError:
            pass

        # Send log messages

    def getarg(self, parname):
        """ Returns the argument value of the parameter parname. The parameter
            is first searched for in self.arglist['parname'], then in
            config['stepname']['parname']. If the parameter is not found,
            the default value from parameter list is returned.
            Should the parameter name not have an entry in the parameter list,
            a error is returned and a KeyError is raised.
            All name comparisons are made in lower case.
        """
        # list of strings that should parse to boolean true
        # we need to handle booleans separately, because bool("False")
        # evaluates to True
        booltrue = ['yes','true','1','t']

        parname = parname.lower() # so we don't have to worry about case

        # Get paramlist index and check if parameter is valid
        try:
            ind = [par[0].lower() for par in self.paramlist].index(parname)
        except ValueError:
            msg = 'GetArg: There is no parameter named %s' % parname
            self.log.error(msg)
            raise KeyError(msg)
        parnameraw = self.paramlist[ind][0] # ParName in original Case
        default = self.paramlist[ind][1]
        # get from arguments if possible
        if parname in self.arglist:
            # assumes that: if value is not default, then set on command line
            # by the user IF argparse parser is set
            if hasattr(self, 'parser'):
                if self.arglist[parname] != self.parser.get_default(parnameraw):
                    ret = self.arglist[parnameraw]
                    self.log.debug('GetArg: from command line, done (%s=%s)'
                                   % (parnameraw, repr(ret)) )
                    return ret
            # ELSE parameter set in python function call
            else:
                ret = self.arglist[parname]
                return ret
        # make temporary config entry with lowercase key names
        conftmp = {}
        if self.name in self.config: # skip if no step entry in config
            for keyname in self.config[self.name].keys():
                conftmp[keyname.lower()] = self.config[self.name][keyname]
        # get from config if possible
        if parname in conftmp:
            value = conftmp[parname]
            # If default is a sequence:
            if isinstance(default,(tuple,list)):
                # Get type for list elements
                # (if default is empty, convert to string)
                if len(default) > 0:
                    outtype = type(default[0])
                else:
                    outtype = str
                ret = []
                # Convert elements in list
                # Note: if the keyword only has one item in the list and there
                # is no trailing comma, configobj will read it as a string
                # instead of a 1-element list.  We force to list here.
                if isinstance(value,str):
                    value = [value]
                for i in range(len(value)):
                    # Check if it's boolean
                    if outtype == bool:
                        if value[i].lower() in booltrue:
                            ret.append(True)
                        else: # default to False
                            ret.append(False)
                    # Not boolean - just convert to type
                    else:
                        ret.append(outtype(value[i]))
                # convert to tuple
                self.log.debug('GetArg: from config file, done (%s=%s)' % (parname,repr(type(default)(ret))))
                return type(default)(ret)
            # Default is not a sequence
            else:
                # Check if it's boolean
                if isinstance(default,bool) and not isinstance(value,bool):
                    if value.lower() in booltrue:
                        self.log.debug('GetArg: from config file, done (%s=True)' % parname)
                        return True
                    else:
                        self.log.debug('GetArg: from config file, done (%s=False)' % parname)
                        return False
                # Not boolean - just convert to type
                else:
                    self.log.debug('GetArg: from config file, done (%s=%s)' % (parname,repr(type(default)(value))))
                    return type(default)(value)
        # get default from parameter list
        ret = self.paramlist[ind][1]
        # return parameter
        self.log.debug('GetArg: from param list, done (%s=%s)' % (parname,repr(ret)))
        return ret

    def getparam(self, parname):
        """ DEPRECATED - use getarg instead
            Returns the value of the parameter parname. The parameter is
            first searched for in self.arglist['parname'], then in
            config['stepname']['parname']. If the parameter is not found,
            a warning is returned and a KeyError is raised.
        """
        self.log.warn('GetParam is Decrecated - use GetArg')
        return self.getarg(parname)

    def reset(self):
        """ Resets the step to the same condition as it was when it was
            created. Internal variables are reset, any stored data is
            erased.
        """
        # initialize input and output
        self.datain = DataParent()
        self.dataout = DataParent()
        self.log.debug('Reset: done')

    def execute(self):
        """ Runs the pipe step as called from the command line:
            The first arguments are used as input file names. Other
            special arguments are:
            - config = name of the configuration file object
            - test = runs the test function using the input file
            - loglevel = name of logging level (INFO is default)
            Other arguments are used as parameters to the pipe step.
        """
        ### Read Arguments
        # Set up argument parser - Generic parameters
        self.parser = argparse.ArgumentParser(description="Pipeline Step %s" % self.name,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            epilog = 'Multipe --config entries are possible; config files are merged.')
        self.parser.add_argument('inputfiles', type=str, default='', nargs='*',
                            help='input files pathname',)
        self.parser.add_argument('-t','--test', action='store_true',
                            help='runs the selftest of this pipe step')
        self.parser.add_argument('--loglevel', default='INFO', type=str,
                            choices=['DEBUG','INFO','WARN',
                                     'ERROR','CRITICAL'],
                            help='log level')
        self.parser.add_argument('--logfile', default=None, type=str,
                            help='logging file')
        self.parser.add_argument('-c', '--config', default=[], type=str,
                            action='append', help='pipeline configuration file(s)')
        # Add step-specific parameters from parlist
        for param in self.paramlist:
            # Comment: default = None because getarg gets default value from
            #          paramlist
            if isinstance(param[1],(list,tuple)):
                try:
                    partype = type(param[1][0])
                    self.parser.add_argument('--%s' %param[0], type=partype,
                        nargs=len(param[1]),default=param[1],help=param[2])
                except IndexError: # empty list, so no type checking
                    self.parser.add_argument('--%s' %param[0],
                        nargs='*',default=None,help=param[2])
            else:
                self.parser.add_argument('--'+param[0], type=type(param[1]),
                    default=param[1], help=param[2])
        # Get arguments - store dict in arglist
        args = self.parser.parse_args()
        self.arglist = vars(args)
        ### Process generic arguments
        # Set logging (add file handler if logfile != '')
        level = getattr(logging, args.loglevel.upper(), None)
        logging.basicConfig(level=level)
        if args.logfile is not None:
            fhand = logging.FileHandler(args.logfile)
            fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            fhand.setFormatter(logging.Formatter(fmt))
            logging.getLogger().addHandler(fhand)
        # Set configuration (load if specified)
        if len(args.config) > 0:
            self.config = DataParent(config = args.config).config
        elif not args.test: # Set config unless test is requested
            self.config = ConfigObj()
            self.config[self.name]={}
        # Check for test
        if args.test:
            self.test()
            return
        ### Reduce data
        self.execfiles(args.inputfiles)
        self.log.info('Execute: done')

    def execfiles(self, inputfiles):
        """ Runs several files from execute.
            This function is overwritten in MISO and MIMO steps
        """

        if len(inputfiles) > 0:
            for filename in inputfiles:
                # Read input file: make dataparent, get child from load() ##-
                datain = DataParent(config = self.config)
                self.datain = datain.load(filename)
                # Call start - run and call end
                self.runstart(self.datain,self.arglist)
                self.run()
                self.runend(self.dataout)
                # Write output file
                self.dataout.save()
                self.log.info('Execute: Saved result %s' % self.dataout.filename)
        else:
            # Warning - no input file
            self.log.warn('Execute: Missing input File')

    def test(self):
        """ Test Pipe Step Parent Object:
            Runs a set of basic tests on the object
        """
        # log message
        self.log.info('Testing pipe step parent')
        # test function call
        #testout=self(1) # should raise TypeError
        if self.config != None:
            testin = DataParent(config=self.config)
        else:
            testin = DataParent(config=self.testconf)
        testin.filename = 'this.file.type.fts'
        testout=self(testin, sampar=5.0)
        print(testout.header)
        print(testout.filename)
        # test get and set parameters
        print("sampar=%.3f" % self.getarg('sampar'))
        # log message
        self.log.info('Testing pipe step parent - Done')

if __name__ == '__main__':
    """ Main function to run the pipe step from command line on a file.
        Command:
          python stepparent.py input.fits -arg1 -arg2 . . .
        Standard arguments:
          --config=ConfigFilePathName.txt : name of the configuration file
          -t, --test : runs the functionality test i.e. pipestep.test()
          --loglevel=LEVEL : configures the logging output for a particular level
          -h, --help : Returns a list of commands.
    """
    StepParent().execute()

""" === History ===
    2015-10-7  Marc Berthoud: Removed undo() and COMPLETE keyword from
               all pipe steps
    2014-3-14  Marc Berthoud: Renamed callstart/callend -> runstart/runend
               - Took out code for MI and MO steps (not separate objects)
    2013-12-18 Marc Berthoud:
               - added default test configuration file specification
               - removed config parameter for test() functions
    2012-12-23 Marc Berthoud: Added command line capability for pipe steps with
                              execute(), added paramlist.
    2009-10-27 Marc Berthoud, Ver0.1.1: Split call into callstart - run - callend
    2008-11-5 Marc Berthoud, Ver0.1: Wrote and tested (with HAWC text)
    2010-10-21 Marc Berthoud, Now configuration is loaded from datain
"""
