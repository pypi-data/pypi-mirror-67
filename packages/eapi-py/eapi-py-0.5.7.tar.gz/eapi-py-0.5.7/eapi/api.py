# -*- coding: utf-8 -*-
# Copyright (c) 2020 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import math
import re
import time

from typing import Callable, List, Optional

from eapi.structures import Auth, Certificate, Command
from eapi.messages import Response
from eapi import session
from eapi import util

NEVER_RE = r'(?!x)x'

def new(target: str, auth: Optional[Auth] = None,
        cert: Optional[Certificate] = None, **kwargs) -> None:
    """Create an eAPI session

    :param target: eAPI target 
    :param type: Target
    :param auth: username, password tuple
    :param type: Auth
    :param cert: client certificate or (certificate, key) tuple
    :param type: Certificate
    :param \*\*options: pass through `requests` options
    :param type: RequestsOptions
    """
    session.new(target, auth=auth, cert=cert, **kwargs)


login = new


def close(target: str, **kwargs):
    """End an eAPI session

    :param target: eAPI target 
    :param type: Target
    :param \*\*kwargs: pass through `requests` options
    :param type: RequestsOptions
    """
    session.close(target, **kwargs)


logout = close


def execute(target: str, commands: List[Command],
        encoding: Optional[str] = None, **kwargs) -> Response:
    """Send an eAPI request

    :param target: eAPI target 
    :param type: Target
    :param commmands: List of commands to send to target
    :param type: list
    :param encoding: json or text (default: json)
    :param type: str
    :param \*\*kwargs: pass through `requests` options
    :param type: RequestsOptions

    :return: :class:`Response <Response>` object
    :rtype: eapi.messages.Response
    """

    response = session.send(target, commands, encoding, **kwargs)

    return response


def enable(target: str, commands: List[Command], secret: str = "",
        encoding: Optional[str] = None, **kwargs) -> Response:
    """Prepend 'enable' command
    :param target: eAPI target 
    :param type: Target
    :param commmands: List of commands to send to target
    :param type: list
    :param encoding: json or text (default: json)
    :param type: str
    :param \*\*kwargs: Optional arguments that ``execute`` takes.

    :return: :class:`Response <Response>` object
    :rtype: eapi.messages.Response
    """
    commands.insert(0, {"cmd": "enable", "input": secret})
    return execute(target, commands, encoding, **kwargs)


def configure(target: str, commands: List[Command],
        encoding: Optional[str] = None, **kwargs) -> Response:
    """Wrap commands in a 'configure'/'end' block

    :param target: eAPI target 
    :param type: Target
    :param commmands: List of commands to send to target
    :param type: list
    :param encoding: json or text (default: json)
    :param type: str
    :param \*\*kwargs: Optional arguments that ``execute`` takes.

    :return: :class:`Response <Response>` object
    :rtype: eapi.messages.Response
    """
    commands.insert(0, "configure")
    commands.append("end")
    return execute(target, commands, encoding, **kwargs)


def watch(target: str,
        command: Command,
        encoding: Optional[str] = None,
        interval: Optional[int] = None,
        deadline: Optional[float] = None,
        exclude: bool = False,
        condition: Optional[str] = None,
        callback: Optional[Callable] = None,
        **kwargs) -> bool:
    """Watch a command until deadline or condition matches

    :param target: eAPI target 
    :param type: Target
    :param commmand: A single command to send
    :param type: list
    :param encoding: json or text (default: json)
    :param type: str
    :param interval: time between repeating command
    :param type: int
    :param deadline: End loop after specified time
    :param type: float
    :param exclude: return if condition patter is NOT matched
    :param type: bool
    :param condition: search for pattern in output, return if matched
    :param type: str
    :param \*\*kwargs: Optional arguments that ``execute`` takes.

    :return: :class:`Response <Response>` object
    :rtype: eapi.messages.Response
    """

    exclude = bool(exclude)

    if not interval:
        interval = 5

    if not deadline:
        deadline = math.inf

    if not condition:
        condition = NEVER_RE

    start = time.time()
    check = start
    
    while (check - deadline) < start:
        response = execute(target, [command], encoding, **kwargs)
        match = re.search(condition, str(response))

        if callback:
            callback(response)

        if exclude:
            if not match:
                return True
        elif match:
            return True

        time.sleep(interval)
        check = time.time()

    return False