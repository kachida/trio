"""
This namespace represents the core functionality that has to be built-in
and deal with private internal data structures. Things in this namespace
are publicly available in either trio, trio.lowlevel, or trio.testing.
"""

import sys
import typing as _t

from ._entry_queue import TrioToken
from ._exceptions import (
    BrokenResourceError,
    BusyResourceError,
    Cancelled,
    ClosedResourceError,
    EndOfChannel,
    RunFinishedError,
    TrioInternalError,
    WouldBlock,
)
from ._ki import currently_ki_protected, disable_ki_protection, enable_ki_protection
from ._local import RunVar, RunVarToken
from ._mock_clock import MockClock
from ._parking_lot import (
    ParkingLot,
    ParkingLotStatistics,
    add_parking_lot_breaker,
    remove_parking_lot_breaker,
)

# Imports that always exist
from ._run import (
    TASK_STATUS_IGNORED,
    CancelScope,
    Nursery,
    RunStatistics,
    Task,
    TaskStatus,
    add_instrument,
    checkpoint,
    checkpoint_if_cancelled,
    current_clock,
    current_effective_deadline,
    current_root_task,
    current_statistics,
    current_task,
    current_time,
    current_trio_token,
    in_trio_run,
    in_trio_task,
    notify_closing,
    open_nursery,
    remove_instrument,
    reschedule,
    run,
    spawn_system_task,
    start_guest_run,
    wait_all_tasks_blocked,
    wait_readable,
    wait_writable,
)
from ._thread_cache import start_thread_soon

# Has to come after _run to resolve a circular import
from ._traps import (
    Abort,
    RaiseCancelT,
    cancel_shielded_checkpoint,
    permanently_detach_coroutine_object,
    reattach_detached_coroutine_object,
    temporarily_detach_coroutine_object,
    wait_task_rescheduled,
)
from ._unbounded_queue import UnboundedQueue, UnboundedQueueStatistics

# Windows imports
if sys.platform == "win32" or (
    not _t.TYPE_CHECKING and "sphinx.ext.autodoc" in sys.modules
):
    from ._run import (
        current_iocp,
        monitor_completion_key,
        readinto_overlapped,
        register_with_iocp,
        wait_overlapped,
        write_overlapped,
    )
# Kqueue imports
if (sys.platform != "linux" and sys.platform != "win32") or (
    not _t.TYPE_CHECKING and "sphinx.ext.autodoc" in sys.modules
):
    from ._run import current_kqueue, monitor_kevent, wait_kevent

del sys  # It would be better to import sys as _sys, but mypy does not understand it
