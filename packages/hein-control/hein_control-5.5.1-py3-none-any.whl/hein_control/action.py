"""
Contains classes for managing and applying context to "actions" (functions).

`Action` is a function register which enables default arg/kwarg specification and retrieval of action by function name.

`ConfiguredAction` is an action that is configured to run (allows for multiple configurations of `Action` classes.

`TrackedAction` is an action that may be run with storage of context (duration, time started, function return,
args/kwargs that were used for execution, and error details if any).

"""
import time
import datetime
import copy
import inspect
import logging
from typing import List, Union, Callable


# todo figure out how to trigger a pre-trigger event (e.g. turn on instrument and condition)
#   - executed contextually
#   - or rely on the user to specify pre-events in provided methods

# dictionary of action states
ACTION_STATES = {
    -1: 'ERROR',
    0: 'CONFIGURED',
    1: 'PENDING',
    2: 'EXECUTING',
    3: 'COMPLETE',
}

logger = logging.getLogger(__name__)


class Action:
    # registry of defined actions
    _registry: List["Action"] = []

    def __init__(self,
                 action: Callable,
                 *default_args,
                 **default_kwargs,
                 ):
        """
        Class for storing and tracking registered methods.

        :param action: action method to execute when called
        :param default_args: default arguments for the action
        :param default_kwargs: default kwargs for the action
        """
        # todo consider implementing action removal
        if self.action_is_registered(action) is True:
            raise ValueError(
                f'The action "{action}" is already registered, use SchedulerAction.register_action instead'
            )
        self.action = action
        self.__doc__ = inspect.getdoc(action)
        self.signature = inspect.signature(action)
        self.default_args = default_args
        self.logger = logger.getChild(f'{self.__class__.__name__}.{self.name}')
        fn_kwargs = {
            name: param.default
            for name, param in self.signature.parameters.items() if param.default is not inspect._empty
        }
        fn_kwargs.update(default_kwargs)
        self.default_kwargs = fn_kwargs
        Action._registry.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.action.__name__})'

    def __call__(self, *args, **kwargs):
        self.logger.debug(f'calling {self.name} with args {args} and kwargs {kwargs}')
        return self.action(*args, **kwargs)

    @property
    def name(self) -> str:
        """action method name"""
        return self.action.__name__

    @property
    def return_type(self):
        """the return type of the action"""
        if self.signature.return_annotation is inspect._empty:
            return None
        return self.signature.return_annotation

    @classmethod
    def action_is_registered(cls,
                             action: Union[str, Callable, "Action"]
                             ) -> bool:
        """
        Checks whether the provided action is registered as a SchedulerAction instance.

        :param action: action to check
        :return: whether action is registered
        """
        for instance in cls._registry:
            if any([
                instance.name == action,
                instance == action,
                instance.action == action,
            ]):
                return True
        return False

    @classmethod
    def register_action(cls,
                        action: Union[str, Callable, "Action"],
                        ) -> "Action":
        """
        Registers a new instance or returns an existing instance if the action is already registered.

        :param action: action method
        :return: Action instance
        """
        # todo consider logging that a new action has been registered
        # catch class instance
        if isinstance(action, Action):
            return action
        elif hasattr(action, 'action') and isinstance(action.action, Action):
            return action.action
        # search for action name
        elif type(action) is str:
            for instance in cls._registry:
                if instance.name == action:
                    return instance
            # if no action matched, raise
            raise ValueError(f'The action "{action}" is not registered')
        else:
            # check for preexisting actions
            for instance in cls._registry:
                if instance.name == action.__name__:
                    return instance
            # if not found, create and return
            return cls(
                action
            )

    @classmethod
    def register_actions(cls, *actions: Union[str, Callable, "Action"]) -> List["Action"]:
        """
        Registers multiple actions

        :param actions: action methods to be registered
        :return: list of actions which were registered
        """
        return [
            cls.register_action(action) for action in actions
        ]

    @classmethod
    def get_registered_actions(cls) -> List["Action"]:
        """returns a list of registered Scheduler Actions"""
        return cls._registry

    @classmethod
    def get_registered_action_names(cls) -> List[str]:
        """returns a list of the names of the registered Scheduler Actions"""
        return [action.name for action in cls._registry]


def _update_args(original_args: tuple,
                 new_args: tuple,
                 ) -> tuple:
    """
    Updates the original argument tuple with the new arguments.

    :param original_args: original argument tuple
    :param new_args: new argument tuple
    :return: updated argument tuple
    """
    original_args = list(original_args)
    for ind, val in enumerate(new_args):
        try:
            original_args[ind] = val
        except IndexError:
            original_args.append(val)
    return tuple(original_args)


def is_builtin_type(obj):
    """returns whether the object is a builtin type"""
    return obj.__class__.__module__ == 'builtins'


def _update_kwargs(original_kwargs: dict,
                   new_kwargs: dict,
                   ) -> dict:
    """
    Updates the original kwargs with the new kwargs. Prevents mutation of the original kwargs.

    Only perform deepcopy on builtin types and interface instances that have specified the deepcopy method.

    :param original_kwargs: original keyword arguments
    :param new_kwargs: new keyword arguments
    :return: consolidated and updated keyword arguments
    """
    # todo compare provided types with signature types
    # create deepcopies of supporting types
    dct = {
        key: copy.deepcopy(value)
        for key, value in original_kwargs.items()
        if hasattr(value, '__deepcopy__') or is_builtin_type(value)
    }
    # add direct references for non-copyable types
    dct.update({
        key: original_kwargs[key] for key in original_kwargs.keys() - dct.keys()
    })
    # finally update with new kwargs
    dct.update(new_kwargs)
    return dct


class ConfiguredAction:
    # configured action registry
    _config_registry: List['ConfiguredAction'] = []

    def __init__(self,
                 action: Union[Callable, Action, str],
                 *args,
                 configuration_name: str = None,
                 **kwargs,
                 ):
        """
        An action that is configured for execution

        :param action: action to perform (callable)
        :param args: arguments for the action
        :param configuration_name: optional name for the configuration (for key retrieval)
        :param kwargs: keyword arguments for the action
        """
        self._action: Action = None
        self._config_name: str = None
        # register action and store attribute
        self.action = action
        self.args = _update_args(self.action.default_args, args)
        self.kwargs = _update_kwargs(self.action.default_kwargs, kwargs)
        # generate name if not specified
        if configuration_name is None:
            configuration_name = self._generate_unique_name(self.action)
        else:
            if configuration_name in self.get_configuration_names():
                raise NameError(f'The configuration name "{configuration_name}" is already used, please choose a '
                                f'unique name for the configuration. ')
        self.name = configuration_name
        self._config_registry.append(self)

    def __str__(self):
        return f'{self.__class__.__name__} {self.name}'

    def __repr__(self):
        return self.__str__()

    def __call__(self, *args, **kwargs):
        raise NotImplementedError(f'{self.__class__.__name__} instances may not be called')

    def __copy__(self):
        return self.__class__(
            self.action,
            self.args,
            self.name,
            self.kwargs,
        )

    def __deepcopy__(self, memodict={}):
        return self.__copy__()

    @property
    def action(self) -> Action:
        """The action to be tracked"""
        return self._action

    @action.setter
    def action(self, value: Union[Callable, Action, str]):
        if value is not None:
            self._action = Action.register_action(value)

    @property
    def name(self) -> str:
        """name for the configuration"""
        return self._config_name

    @name.setter
    def name(self, value: str):
        if value is not None:
            # check if already defined
            if value in self.get_configuration_names():
                raise NameError(f'The configuration name "{value}" is already used, please choose a '
                                f'unique name for the configuration. ')
            self._config_name = value

    def update_args(self, *args):
        """Updates the arguments for the Action"""
        self.args = _update_args(
            self.args,
            args
        )

    def update_kwargs(self, **kwargs):
        """updates the keyword arguments for the Action"""
        self.kwargs = _update_kwargs(
            self.kwargs,
            kwargs
        )

    @property
    def status_code(self) -> int:
        """returns a status code representative of the state of the Action"""
        return 0

    @property
    def status_string(self) -> str:
        """string meaning of status code"""
        return ACTION_STATES[self.status_code]

    @property
    def status(self) -> str:
        """status string for the Action"""
        return f'{self.status_code}: {self.status_string}'

    @classmethod
    def _generate_unique_name(cls, action: Action) -> str:
        """
        Generates a unique numbered name based on an Action instance. The resulting name will be unique in the
        registry.

        :param action: action to base naming off of
        :return: generated name
        """
        i = 1
        current_names = cls.get_configuration_names()
        while True:
            target_name = f'{action.name}_{i}'
            if f'{action.name}_{i}' not in current_names:
                return target_name
            i += 1

    @classmethod
    def get_configuration_by_name(cls, configuration_name: str) -> 'ConfiguredAction':
        """
        Retrieves a ConfiguredAction by name

        :param configuration_name: name identifier of configuration
        :return: ConfiguredAction
        """
        for config in cls._config_registry:
            if config.name == configuration_name:
                return config
        raise NameError(f'The key "{configuration_name}" does not match any ConfiguredAction instances')

    @classmethod
    def get_configuration_names(cls) -> List[str]:
        """
        Retrieves the names of all configurations.

        Warning: return will be sorted, but order does not correspond to order in registry (indexing based on this
        return is not recommended).
        """
        return sorted([config.name for config in cls._config_registry])

    @classmethod
    def get_configurations_of_action(cls, action: Union[str, Action]) -> List['ConfiguredAction']:
        """
        Retrieves all of the Configurations associated with the specified action

        :param action: action to reference
        :return: list of ConfiguredAction instances
        """
        if isinstance(action, Action) is False:
            action = Action.register_action(action)
        return [
            config
            for config in cls._config_registry
            if config.action is action
        ]

    def as_dict(self) -> dict:
        """dictionary of relevant information"""
        out = {
            'name': self.name,
            'arguments': self.args,
            'keyword_arguments': self.kwargs,
            'status_code': self.status_code,
            'status': self.status_string,
        }
        return out


class TrackedAction(ConfiguredAction):
    logger = logger.getChild('TrackedAction')

    def __init__(self,
                 action: Union[str, Callable, ConfiguredAction],
                 *args,
                 **kwargs,
                 ):
        """
        Creates a wrapped action which will track the time of start, completion, and return of the action.

        :param action: action to perform (callable)
        :param args: arguments for the action
        :param kwargs: keyword arguments for the action
        """
        # if provided with a configured action, extract parameters
        if isinstance(action, ConfiguredAction):
            args = action.args
            kwargs = action.kwargs
            action = action.action
        ConfiguredAction.__init__(
            self,
            action,
            *args,
            **kwargs,
        )
        # error state tracker
        self.error: bool = False
        self.error_details = None
        self._time_started = None
        self._time_completed = None
        self._action_return = None

    def __call__(self, *args, **kwargs):
        if self._time_completed is not None:
            raise RuntimeError(f'multiple executions of a {self.__class__.__name__} instance is not permitted')
        # update args and kwargs and store
        self.update_args(*args)
        self.update_kwargs(**kwargs)
        self.logger.debug('beginning action execution')
        self._time_started = time.time()  # set start time
        try:
            self._action_return = self.action(
                *self.args,
                **self.kwargs
            )
            self.logger.debug('action completed successfully')
        except Exception as e:
            self.logger.error(f'error encountered when executing action {self.action.name}: {e}')
            self.error = True
            self.error_details = e
        self._time_completed = time.time()  # save completed time

    @property
    def time_started(self) -> float:
        """time stamp when the action was started"""
        return self._time_started

    @property
    def time_completed(self) -> float:
        """time stamp when the action was completed"""
        return self._time_completed

    @property
    def started_timestamp(self) -> datetime.datetime:
        """timestamp for when the action was started"""
        if self.time_started is not None:
            return datetime.datetime.fromtimestamp(self.time_started)

    @property
    def action_duration(self) -> float:
        """task duration (s)"""
        if self._time_completed is not None:
            return self._time_completed - self._time_started

    @property
    def method_return(self):
        """the return of the method once complete"""
        return self._action_return

    @property
    def status_code(self) -> int:
        """returns a status code representative of the state of the Action"""
        if self.error is True:
            code = -1
        elif self.time_started is None:
            code = 1
        elif self.time_completed is None:
            code = 2
        else:
            code = 3
        return code

    def as_dict(self) -> dict:
        """dictionary of relevant information"""
        out = {
            'name': self.action.name,
            'configuration_name': self.name,  # todo add configuration name when it's sorted out
            'arguments': self.args,
            'keyword_arguments': self.kwargs,
            'status_code': self.status_code,
            'status': self.status_string,
        }
        if self.time_started is not None:
            out['time_started'] = self.time_started
            out['timestamp'] = str(self.started_timestamp)
        if self.time_completed is not None:
            out['time_completed'] = self.time_completed
            out['duration'] = self.time_completed - self.time_started
            if self.error is True:
                out['error_during_execution'] = True
                out['error_details'] = str(self.error_details)
            else:  # if completed and no error, include the method return
                out['action_return'] = self.method_return
        return out

    @classmethod
    def create_from_configured(cls, source: Union[Action, ConfiguredAction]) -> "TrackedAction":
        """
        Creates a TrackedAction instance from a provided Action or ConfiguredAction

        :param source: action to generate from
        :return: instantiated TrackedAction
        """
        if isinstance(source, Action):
            args = ()
            kwargs = {}
            action = source.action
        elif isinstance(source, ConfiguredAction):
            args = source.args
            kwargs = source.kwargs
            action = source.action
        else:
            raise TypeError(f'the provided source is not an interpretable type: {type(source)}')
        out = cls(action=action)
        out.update_args(*args)
        out.update_kwargs(**kwargs)
        return out
