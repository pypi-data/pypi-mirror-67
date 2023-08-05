#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © Nekokatt 2019-2020
#
# This file is part of Hikari.
#
# Hikari is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hikari is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Hikari. If not, see <https://www.gnu.org/licenses/>.
"""Core errors that may be raised by this API implementation."""

from __future__ import annotations

__all__ = [
    "HikariError",
    "HikariWarning",
    "NotFoundHTTPError",
    "UnauthorizedHTTPError",
    "ForbiddenHTTPError",
    "BadRequestHTTPError",
    "ClientHTTPError",
    "ServerHTTPError",
    "CodedHTTPError",
    "HTTPError",
    "GatewayZombiedError",
    "GatewayNeedsShardingError",
    "GatewayMustReconnectError",
    "GatewayInvalidSessionError",
    "GatewayInvalidTokenError",
    "GatewayServerClosedConnectionError",
    "GatewayClientClosedError",
    "GatewayClientDisconnectedError",
    "GatewayError",
]

import typing

from hikari.net import codes

if typing.TYPE_CHECKING:
    from hikari.net import routes


class HikariError(RuntimeError):
    """Base for an error raised by this API.

    Any exceptions should derive from this.

    !!! note
        You should never initialize this exception directly.
    """

    __slots__ = ()


class HikariWarning(RuntimeWarning):
    """Base for a warning raised by this API.

    Any warnings should derive from this.

    !!! note
        You should never initialize this warning directly.
    """

    __slots__ = ()


class GatewayError(HikariError):
    """A base exception type for anything that can be thrown by the Gateway.

    Parameters
    ----------
    reason : st
        A string explaining the issue.
    """

    reason: str
    """A string to explain the issue."""

    def __init__(self, reason: str) -> None:
        super().__init__()
        self.reason = reason

    def __str__(self) -> str:
        return self.reason


class GatewayClientClosedError(GatewayError):
    """An exception raised when you programmatically shut down the bot client-side.

    Parameters
    ----------
    reason : str
        A string explaining the issue.
    """

    def __init__(self, reason: str = "The gateway client has been closed") -> None:
        super().__init__(reason)


class GatewayClientDisconnectedError(GatewayError):
    """An exception raised when the bot client-side disconnects unexpectedly.

    Parameters
    ----------
    reason : str
        A string explaining the issue.
    """

    def __init__(self, reason: str = "The gateway client has disconnected unexpectedly") -> None:
        super().__init__(reason)


class GatewayServerClosedConnectionError(GatewayError):
    """An exception raised when the server closes the connection.

    Parameters
    ----------
    close_code : typing.Union[hikari.net.codes.GatewayCloseCode, int], optional
        The close code provided by the server, if there was one.
    reason : str, optional
        A string explaining the issue.
    """

    close_code: typing.Union[codes.GatewayCloseCode, int, None]

    def __init__(
        self,
        close_code: typing.Optional[typing.Union[codes.GatewayCloseCode, int]] = None,
        reason: typing.Optional[str] = None,
    ) -> None:
        try:
            name = close_code.name
        except AttributeError:
            name = str(close_code) if close_code is not None else "no reason"

        if reason is None:
            reason = f"Gateway connection closed by server ({name})"

        self.close_code = close_code
        super().__init__(reason)


class GatewayInvalidTokenError(GatewayServerClosedConnectionError):
    """An exception that is raised if you failed to authenticate with a valid token to the Gateway."""

    def __init__(self) -> None:
        super().__init__(
            codes.GatewayCloseCode.AUTHENTICATION_FAILED,
            "The account token specified is invalid for the gateway connection",
        )


class GatewayInvalidSessionError(GatewayServerClosedConnectionError):
    """An exception raised if a Gateway session becomes invalid.

    Parameters
    ----------
    can_resume : bool
        `True` if the connection will be able to RESUME next time it starts
        rather than re-IDENTIFYing, or `False` if you need to IDENTIFY
        again instead.
    """

    can_resume: bool
    """`True` if the next reconnection can be RESUMED,
    `False` if it has to be coordinated by re-IDENFITYing.
    """

    def __init__(self, can_resume: bool) -> None:
        self.can_resume = can_resume
        instruction = "restart the shard and RESUME" if can_resume else "restart the shard with a fresh session"
        super().__init__(reason=f"The session has been invalidated; {instruction}")


class GatewayMustReconnectError(GatewayServerClosedConnectionError):
    """An exception raised when the Gateway has to re-connect with a new session.

    This will cause a re-IDENTIFY.
    """

    def __init__(self) -> None:
        super().__init__(reason="The gateway server has requested that the client reconnects with a new session")


class GatewayNeedsShardingError(GatewayServerClosedConnectionError):
    """An exception raised if you have too many guilds on one of the current Gateway shards.

    This is a sign you need to increase the number of shards that your bot is
    running with in order to connect to Discord.
    """

    def __init__(self) -> None:
        super().__init__(
            codes.GatewayCloseCode.SHARDING_REQUIRED, "You are in too many guilds. Shard the bot to connect",
        )


class GatewayZombiedError(GatewayClientClosedError):
    """An exception raised if a shard becomes zombied.

    This means that Discord is no longer responding to us, and we have
    disconnected due to a timeout.
    """

    def __init__(self) -> None:
        super().__init__("No heartbeat was received, the connection has been closed")


class HTTPError(HikariError):
    """Base exception raised if an HTTP error occurs.

    Parameters
    ----------
    reason : str
        A meaningful explanation of the problem.
    """

    reason: str
    """A meaningful explanation of the problem."""

    def __init__(self, reason: str) -> None:
        super().__init__()
        self.reason = reason

    def __str__(self) -> str:
        return self.reason


class CodedHTTPError(HTTPError):
    """An HTTP exception that has contextual response information with it.

    Parameters
    ----------
    status : int or hikari.net.codes.HTTPStatusCode
        The HTTP status code that was returned by the server.
    route : hikari.net.routes.CompiledRoute
        The HTTP route that was being invoked when this exception occurred.
    message : str, optional
        An optional message if provided in the response payload.
    json_code : hikari.net.codes.JSONErrorCode, int, optional
        An optional error code the server provided us.
    """

    status: typing.Union[int, codes.HTTPStatusCode]
    """The HTTP status code that was returned by the server."""

    route: routes.CompiledRoute
    """The HTTP route that was being invoked when this exception occurred."""

    message: typing.Optional[str]
    """An optional contextual message the server provided us with in the response body."""

    json_code: typing.Union[codes.JSONErrorCode, int, None]
    """An optional contextual error code the server provided us with in the response body."""

    def __init__(
        self,
        status: typing.Union[int, codes.HTTPStatusCode],
        route: routes.CompiledRoute,
        message: typing.Optional[str],
        json_code: typing.Union[codes.JSONErrorCode, int, None],
    ) -> None:
        super().__init__(str(status))
        self.status = status
        self.route = route
        self.message = message
        self.json_code = json_code

    def __str__(self) -> str:
        return f"{self.reason}: ({self.json_code}) {self.message}"


class ServerHTTPError(CodedHTTPError):
    """An exception raised if a server-side error occurs when interacting with the REST API.

    If you get these, DO NOT PANIC! Your bot is working perfectly fine. Discord
    have probably broken something again.
    """


class ClientHTTPError(CodedHTTPError):
    """An exception raised if a server-side error occurs when interacting with the REST API.

    If you get one of these, you most likely have a mistake in your code, or
    have found a bug with this library.

    If you are sure that your code is correct, please register a bug at
    https://gitlab.com/nekokatt/hikari/issues and we will take a look for you.
    """


class BadRequestHTTPError(CodedHTTPError):
    """A specific case of CodedHTTPError.

    This can occur hat occurs when you send Discord information in an unexpected
    format, miss required information out, or give bad values for stuff.

    An example might be sending a message without any content, or an embed with
    more than 6000 characters.

    Parameters
    ----------
    route : hikari.net.routes.CompiledRoute
        The HTTP route that was being invoked when this exception occurred.
    message : str, optional
        An optional message if provided in the response payload.
    json_code : hikari.net.codes.JSONErrorCode, int, optional
        An optional error code the server provided us.
    """

    def __init__(
        self,
        route: routes.CompiledRoute,
        message: typing.Optional[str],
        json_code: typing.Optional[typing.Union[codes.JSONErrorCode, int]],
    ) -> None:
        super().__init__(codes.HTTPStatusCode.BAD_REQUEST, route, message, json_code)


class UnauthorizedHTTPError(ClientHTTPError):
    """A specific case of ClientHTTPError.

    This occurs when you have invalid authorization details to access
    the given resource.

    This usually means that you have an incorrect token.

    Parameters
    ----------
    route : hikari.net.routes.CompiledRoute
        The HTTP route that was being invoked when this exception occurred.
    message : str, optional
        An optional message if provided in the response payload.
    json_code : hikari.net.codes.JSONErrorCode, int, optional
        An optional error code the server provided us.
    """

    def __init__(
        self,
        route: routes.CompiledRoute,
        message: typing.Optional[str],
        json_code: typing.Optional[typing.Union[codes.JSONErrorCode, int]],
    ) -> None:
        super().__init__(codes.HTTPStatusCode.UNAUTHORIZED, route, message, json_code)


class ForbiddenHTTPError(ClientHTTPError):
    """A specific case of ClientHTTPError.

    This occurs when you are missing permissions, or are using an endpoint that
    your account is not allowed to see without being whitelisted.

    This will not occur if your token is invalid.

    Parameters
    ----------
    route : hikari.net.routes.CompiledRoute
        The HTTP route that was being invoked when this exception occurred.
    message : str, optional
        An optional message if provided in the response payload.
    json_code : hikari.net.codes.JSONErrorCode, int, optional
        An optional error code the server provided us.
    """

    def __init__(
        self,
        route: routes.CompiledRoute,
        message: typing.Optional[str],
        json_code: typing.Optional[typing.Union[codes.JSONErrorCode, int]],
    ) -> None:
        super().__init__(codes.HTTPStatusCode.FORBIDDEN, route, message, json_code)


class NotFoundHTTPError(ClientHTTPError):
    """A specific case of ClientHTTPError.

    This occurs when you try to refer to something that doesn't exist on Discord.
    This might be referring to a user ID, channel ID, guild ID, etc that does
    not exist, or it might be attempting to use an HTTP endpoint that is not
    found.

    Parameters
    ----------
    route : hikari.net.routes.CompiledRoute
        The HTTP route that was being invoked when this exception occurred.
    message : str, optional
        An optional message if provided in the response payload.
    json_code : hikari.net.codes.JSONErrorCode, int, optional
        An optional error code the server provided us.
    """

    def __init__(
        self,
        route: routes.CompiledRoute,
        message: typing.Optional[str],
        json_code: typing.Optional[typing.Union[codes.JSONErrorCode, int]],
    ) -> None:
        super().__init__(codes.HTTPStatusCode.NOT_FOUND, route, message, json_code)


class IntentWarning(HikariWarning):
    """Warning raised when subscribing to an event that cannot be fired.

    This is caused by your application missing certain intents.
    """
