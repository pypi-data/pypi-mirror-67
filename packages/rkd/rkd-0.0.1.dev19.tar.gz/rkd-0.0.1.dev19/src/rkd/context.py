
import os
from typing import Dict, List, Union
from importlib.machinery import SourceFileLoader
from .syntax import TaskDeclaration, TaskAliasDeclaration, GroupDeclaration
from .contract import ContextInterface
from .argparsing import CommandlineParsingHelper
from .inputoutput import SystemIO


CURRENT_SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))


class Context(ContextInterface):
    """
    Application context - collects all tasks together

    Each Context() is collecting tasks from selected directory.
    merge() static method is merging two Context() objects
    eg. merge(Context(), Context()) selecting second as a priority

    ContextFactory() is controlling the order.
    """

    _imported_tasks: Dict[str, TaskDeclaration]
    _task_aliases: Dict[str, TaskAliasDeclaration]
    _compiled: Dict[str, Union[TaskDeclaration, GroupDeclaration]]
    io: SystemIO

    def __init__(self, tasks: List[TaskDeclaration], aliases: List[TaskAliasDeclaration]):
        self._imported_tasks = {}
        self._task_aliases = {}

        for task in tasks:
            self._add_component(task)

        for alias in aliases:
            self._add_task(alias)

    @classmethod
    def merge(cls, first, second):
        """ Add one context to other context. Produces immutable new context. """

        new_ctx = cls([], [])

        for context in [first, second]:
            context: Context

            for name, component in context._imported_tasks.items():
                new_ctx._add_component(component)

            for name, task in context._task_aliases.items():
                new_ctx._add_task(task)

        return new_ctx

    def compile(self) -> None:
        """ Resolve all objects in the context. Should be called only, when all contexts were merged """

        self._compiled = self._imported_tasks

        for name, details in self._task_aliases.items():
            self._compiled[name] = self._resolve_alias(name, details)

    def find_task_by_name(self, name: str) -> Union[TaskDeclaration, GroupDeclaration]:
        try:
            return self._compiled[name]
        except KeyError:
            raise Exception(('Task "%s" is not defined. Check if it is defined, or' +
                            ' imported, or if the spelling is correct.') % name)

    def find_all_tasks(self) -> Dict[str, Union[TaskDeclaration, GroupDeclaration]]:
        return self._compiled

    def _add_component(self, component: TaskDeclaration) -> None:
        self._imported_tasks[component.to_full_name()] = component

    def _add_task(self, task: TaskAliasDeclaration) -> None:
        self._task_aliases[task.get_name()] = task

    def _resolve_alias(self, name: str, alias: TaskAliasDeclaration) -> GroupDeclaration:
        """
        Parse commandline args to fetch list of tasks to join into a group

        Produced result will be available to fetch via find_task_by_name()
        """

        args = CommandlineParsingHelper.create_grouped_arguments(alias.get_arguments())
        resolved_tasks = {}

        for argument_group in args:
            resolved_task = self.find_task_by_name(argument_group.name())
            resolved_tasks[argument_group.name()] = resolved_task\
                .with_env(alias.get_env()) \
                .with_args(argument_group.args())

        return GroupDeclaration(name, resolved_tasks)


class ContextFactory:
    """
    Takes responsibility of loading all tasks defined in USER PROJECT, USER HOME and GLOBALLY
    """

    @staticmethod
    def _load_context_from_directory(path: str) -> Context:
        if not os.path.isdir(path):
            raise Exception('Path "%s" font found' % path)

        makefile_path = path + '/makefile.py'

        if not os.path.isfile(makefile_path):
            raise Exception('makefile.py not found at path "%s"' % makefile_path)

        makefile = SourceFileLoader("Makefile", makefile_path).load_module()

        return Context(
            tasks=makefile.IMPORTS if "IMPORTS" in dir(makefile) else [],
            aliases=makefile.TASKS if "TASKS" in dir(makefile) else []
        )

    def create_unified_context(self, chdir: str = '') -> Context:
        """
        Creates a merged context in order:
        - Internal/Core (this package)
        - System-wide (/usr/lib/rkd)
        - User-home ~/.rkd
        - Application (current directory ./.rkd)
        :return:
        """

        paths = [
            CURRENT_SCRIPT_PATH + '/internal',
            '/usr/lib/rkd',
            os.path.expanduser('~/.rkd'),
            chdir + './.rkd'
        ]

        ctx = Context([], [])

        for path in paths:
            if os.path.isdir(path) and os.path.isfile(path + '/makefile.py'):
                ctx = Context.merge(ctx, self._load_context_from_directory(path))

        ctx.compile()
        ctx.io = SystemIO()
        ctx.io.silent = True

        return ctx
