import logging
logger = logging.getLogger(__name__)

from prettytable import PrettyTable

from .. import common, types

class Thread(object):

    def __init__(self, process, info):
        """Defines a process thread.

        Args:
            info (dict): frida thread info dict

        Examples:
            .. code-block:: python
                
                # Grab your thread
                thread = process.threads[tid]
                
                # Wait for this thread to return
                thread.join()

                # Check out any exceptions that may have been thrown on this thread
                thread.exceptions

                # Check out the attached trace object
                thread.trace
        """

        self._process = process
        self.pthread_id = None
        self._info = info
        self.context = CPUContext(self._process, **self._info['context'])

    def join(self):
        """Traditional thread join. Wait for thread to exit and return the thread's return value."""

        if self.pthread_id is not None:
            # TODO: pthread_out cache pool
            # TODO: generalize memory cache pools
            pthread_join = self._process.memory['pthread_join']
            pthread_join.argument_types = types.Int64, types.Pointer
            pthread_out = self._process.memory.alloc(8)
            pthread_join(self.pthread_id, pthread_out.address)
            val = pthread_out.cast(types.Pointer)
            pthread_out.free()
            return val

        else:
            logger.error("Thread join not yet supported on {}".format(self.device_platform))

    def kill(self):
        """Attempts to kill this thread.
        
        Note:
            If you're having trouble killing the thread, be sure your thread is
            killable.

            For pthreads, that means: pthread_setcancelstate(0, 0); pthread_setcanceltype(1,0)
        """

        if self.pthread_id is not None:
            pthread_cancel = self._process.memory['pthread_cancel']
            pthread_cancel(self.pthread_id)

        else:
            logger.error("Thread kill not yet supported on {}".format(self.device_platform))

    def __repr__(self):
        attrs = ['Thread', hex(self.id), '@', hex(self.pc), self.state, self.module]
        if self.trace is not None:
            attrs.append('tracing')
        return "<{}>".format(' '.join(attrs))

    def __getattr__(self, elm):
        return common.auto_int(self._info['context'][elm])

    def __str__(self):

        table = PrettyTable(['attr', 'value'])

        table.add_row(['TID', str(self.id)])
        table.add_row(["State", self.state])
        table.add_row(["Module", self.module])
        table.add_row(["Tracing?", "Yes" if self.trace is not None else "No"])

        """
        for reg in self._info['context']:
            table.add_row([reg, hex(getattr(self, reg))])
        
        """
        table.header = False
        table.align = "l"

        return str(table) + '\n' + str(self.context)


    @property
    def id(self) -> int:
        """Thread ID"""
        return self._info['id']

    @property
    def state(self) -> str:
        """Thread state, such as 'waiting', 'suspended'"""
        return self._info['state']

    @property
    def pc(self) -> int:
        """The current program counter/instruction pointer."""
        return int(self._info['context']['pc'],16)

    @property
    def module(self) -> str:
        """What module is the thread's program counter in? i.e.:
        libc-2.27.so."""
        mod = self._process.modules[self.pc]
        return mod.name if mod is not None else "Unknown"
    
    @property
    def trace(self):
        """revenge.tracer.instruction_tracer.Trace: Returns Trace object if this thread is currently being traced, otherwise None."""
        if self.id in self._process.techniques._active_stalks:
            return self._process.techniques._active_stalks[self.id]

    @property
    def exceptions(self):
        """list: Exceptions that have been caught generically for this thread."""
        return self._process.threads._exceptions[self.id]

from ..cpu import CPUContext

# Doc fixup
Thread.__doc__ = Thread.__init__.__doc__
