from abc import ABCMeta, abstractmethod, asbtractproperty

class ExecutionProvider(metaclass=ABCMeta):
    """ Define the strict interface for all Execution Provider

    script_string ------->  submit
           id     <-----------+

    [ ids ]       ------->  status
    [statuses]   <------------+

    [ ids ]       ------->  cancel
    [cancel]     <------------+

    """

    @abstractmethod
    def submit(self, *args, **kwargs):
        ''' We haven't yet decided on what the args to this can be,
        whether it should just be func, args, kwargs or be the partially evaluated
        fn
        '''

        pass

    @abstractmethod
    def status(self, ids, **kwargs):
        ''' We haven't yet decided on what the args to this can be,
        whether it should just be func, args, kwargs or be the partially evaluated
        fn
        '''

        pass

    @abstractmethod
    def cancel(self, ids, **kwargs):
        ''' We haven't yet decided on what the args to this can be,
        whether it should just be func, args, kwargs or be the partially evaluated
        fn
        '''

        pass

    @abstractmethod
    def scale_out(self, *args, **kwargs):
        ''' Scale out method. We should have the scale out method simply take resource object
        which will have the scaling methods, scale_out itself should be a coroutine, since
        scaling tasks can be slow.
        '''
        pass

    @abstractmethod
    def scale_in(self, *args, **kwargs):
        ''' Scale in method. We should have the scale in method simply take resource object
        which will have the scaling methods, scale_in itself should be a corinine, since
        scaling tasks can be slow.
        '''

        pass


    @abstractmethod
    def status (self, *args, **kwargs):
        ''' Scale in method. We should have the scale in method simply take resource object
        which will have the scaling methods, scale_in itself should be a corinine, since
        scaling tasks can be slow.
        '''

        pass

    @abstractproperty
    def scaling_enabled(self):
        ''' The callers of ParslExecutors need to differentiate between Executors
        and Executors wrapped in a resource provider
        '''
        pass
