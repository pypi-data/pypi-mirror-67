import asyncio
from typing import DefaultDict, Union, List, Callable, Any, Awaitable
from collections import defaultdict
from dataclasses import dataclass
import signal
from .log import create_logger, install_logger

from .bot import Bot
from .models.Event import Event, EventTypes
from .exceptions import SessionException, NetworkException, AuthenticationException, ServerException


class Updater:
    def __init__(self, bot: Bot, use_websocket: bool = True):
        """
        Initialize Updater

        :param bot: the Bot object to use
        :param use_websocket: bool. whether websocket (recommended) should be used
        """
        self.bot = bot
        self.loop = bot.loop
        self.logger = create_logger('Updater')
        self.event_handlers: DefaultDict[EventTypes, List[EventHandler]] = defaultdict(lambda: list())
        self.use_websocket = use_websocket

    async def run_task(self, shutdown_hook: callable = None):
        """
        return awaitable coroutine to run in event loop (must be the same loop as bot object)

        :param shutdown_hook: callable, if running in main thread, this must be set. Trigger is called on shutdown
        """
        self.logger.debug('Run tasks')
        tasks = [
            self.handshake()
        ]
        if not self.use_websocket:
            tasks.append(self.message_polling())
        if shutdown_hook:
            tasks.append(self.raise_shutdown(shutdown_hook))
        await asyncio.wait(tasks)

    def add_handler(self, event: Union[EventTypes, List[EventTypes]]):
        """
        Decorator for event listeners
        Catch all is not supported at this time

        :param event: events.Events
        """
        def receiver_wrapper(func):
            if not asyncio.iscoroutinefunction(func):
                raise TypeError("event body must be a coroutine function.")

            # save function and its parameter types
            event_handler = EventHandler(func)
            if isinstance(event, EventTypes):
                # add listener
                self.event_handlers[event].append(event_handler)
            else:
                for e in event:
                    if isinstance(e, EventTypes):
                        self.event_handlers[e].append(event_handler)
            return func

        return receiver_wrapper

    def run(self, log_to_stderr=True) -> None:
        """
        Start the Updater and block the thread

        :param log_to_stderr: if you are setting other loggers that capture the log from this Library, set to False
        """
        asyncio.set_event_loop(self.loop)

        shutdown_event = asyncio.Event()

        def _signal_handler(*_: Any) -> None:
            shutdown_event.set()

        try:
            self.loop.add_signal_handler(signal.SIGTERM, _signal_handler)
            self.loop.add_signal_handler(signal.SIGINT, _signal_handler)
        except (AttributeError, NotImplementedError):
            pass

        if log_to_stderr:
            install_logger()

        self.loop.create_task(self.run_task(shutdown_hook=shutdown_event.wait))
        self.loop.run_forever()

    async def handshake(self):
        """
        Internal use only, automatic handshake
        Called when launch or websocket disconnects

        :return:
        """
        try:
            await self.bot.handshake()
            if self.use_websocket:
                asyncio.run_coroutine_threadsafe(
                    self.bot.create_websocket(self.event_caller, self.handshake), self.loop)
            return
        except NetworkException:
            self.logger.warning('Unable to communicate with Mirai console, retrying in 5 seconds')
            await asyncio.sleep(5)
            asyncio.run_coroutine_threadsafe(self.handshake(), self.loop)
        except Exception as e:
            self.logger.exception(f'retrying in 5 seconds')
            await asyncio.sleep(5)
            asyncio.run_coroutine_threadsafe(self.handshake(), self.loop)

    async def message_polling(self, count=5, interval=0.5) -> None:
        """
        Internal use only, polling message and fire events

        :param count: maximum message count for each polling
        :param interval: minimum interval between two polling
        """
        while True:
            await asyncio.sleep(interval)
            try:
                results: List[Event] = await self.bot.fetch_message(count)
                if len(results) > 0:
                    self.logger.debug('Received messages:\n' + '\n'.join([str(result) for result in results]))
                for result in results:
                    asyncio.run_coroutine_threadsafe(self.event_caller(result), self.loop)
            except Exception as e:
                self.logger.warning(f'{e}, new handshake initiated')
                await self.handshake()

    async def event_caller(self, event: Event) -> None:
        """
        Internal use only, call the event handlers sequentially

        :param event: the event
        """
        for handler in self.event_handlers[event.type]:
            if await handler.func(event):  # if the function returns True, stop calling next event
                break

    async def raise_shutdown(self, shutdown_event: Callable[..., Awaitable[None]]) -> None:
        """
        Internal use only, shutdown

        :param shutdown_event: callable
        """
        await shutdown_event()
        await self.bot.release()
        raise Shutdown()


@dataclass
class EventHandler:
    """
    Contains the callback function
    """
    func: Callable


class Shutdown(Exception):
    """
    Internal use only
    Shutdown Event
    """
    pass
