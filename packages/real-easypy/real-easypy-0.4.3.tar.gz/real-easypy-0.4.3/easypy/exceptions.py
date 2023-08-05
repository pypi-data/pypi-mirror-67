from __future__ import absolute_import
import sys
import traceback
from time import time
from datetime import datetime
from contextlib import contextmanager
from textwrap import indent
from logging import getLogger
_logger = getLogger(__name__)


class PException(Exception):

    """An exception object that can accept kwargs as attributes"""

    def __init__(self, message="", *args, **params):
        if args or params:
            message = message.format(*args, **params)
        Exception.__init__(self, message)
        self.context = params.pop("context", None)
        self.traceback = params.pop("traceback", None)
        if self.traceback is True:
            self.traceback = traceback.format_exc()
        self.message = message
        self.timestamp = params.pop('timestamp', time())
        if 'tip' not in params:
            # sometimes it's on the class
            params['tip'] = getattr(self, 'tip', None)
        self._params = {}
        self.add_params(**params)

    def __reduce__(self):
        return (self.__class__.__new__, (self.__class__,), self.__getstate__())

    def __getstate__(self):
        return (self.message, self.context, self.traceback, self.timestamp, self._params)

    def __setstate__(self, state):
        self.message, self.context, self.traceback, self.timestamp, params = state
        self._params = {}
        self.add_params(**params)

    def add_params(self, **params):
        for k, v in params.items():
            setattr(self, k, v)
        self._params.update(params)

    def __repr__(self):
        if self._params:
            kw = sorted("%s=%r" % (k, v) for k, v in self._params.items())
            return "%s(%r, %s)" % (self.__class__.__name__, self.message, ", ".join(kw))
        else:
            return "%s(%r)" % (self.__class__.__name__, self.message)

    def __str__(self):
        return self.render(traceback=False, color=False)

    def render(self, params=True, context=True, traceback=True, timestamp=True, color=True):
        text = ""

        if self.message:
            text += "".join("WHITE<<%s>>\n" % line for line in self.message.splitlines())

        if params and self._params:
            tip = self._params.pop('tip', None)
            text += indent("".join(make_block(self._params)), " " * 4)
            if tip:
                tip = tip.format(**self._params)
                lines = tip.splitlines()
                text += indent("GREEN(BLUE)@{tip = %s}@\n" % lines[0], " " * 4)
                for line in lines[1:]:
                    text += indent("GREEN(BLUE)@{      %s}@\n" % lines[0], " " * 4)
                self._params['tip'] = tip  # put it back in params, even though it might've been on the class

        if timestamp and self.timestamp:
            ts = datetime.fromtimestamp(self.timestamp).isoformat()
            text += indent("MAGENTA<<timestamp = %s>>\n" % ts, " " * 4)

        if context and self.context:
            text += "Context:\n" + indent("".join(make_block(self.context, skip={"indentation"})), " " * 4)

        if traceback and self.traceback:
            fmt = "DARK_GRAY@{{{}}}@"
            text += "\n".join(map(fmt.format, self.traceback.splitlines()))

        if not color:
            from easypy.colors import uncolored
            text = uncolored(text)

        return text

    @classmethod
    def make(cls, name):
        return type(name, (cls,), {})

    @classmethod
    @contextmanager
    def on_exception(cls, acceptable=Exception, **kwargs):
        try:
            yield
        except cls:
            # don't mess with exceptions of this type
            raise
        except acceptable as exc:
            exc_info = sys.exc_info()
            _logger.debug("'%s' raised; Raising as '%s'" % (type(exc), cls), exc_info=exc_info)
            raise cls(traceback=True, **kwargs) from None


def make_block(d, skip={}):
    for k in sorted(d):
        if k.startswith("_"):
            continue
        if k in skip:
            continue
        v = d[k]
        if isinstance(v, datetime):
            v = v.isoformat()
        elif not isinstance(v, str):
            v = repr(v)
        dark = False
        if k.startswith("~"):
            k = k[1:]
            dark = True
        head = "%s = " % k
        block = indent(v, " " * len(head))
        block = head + block[len(head):]
        if dark:
            block = "DARK_GRAY@{%s}@" % block
        yield block + "\n"


class TException(PException):

    @property
    def template(self):
        raise NotImplementedError("Must implement template")

    def __init__(self, *args, **params):
        super(TException, self).__init__(self.template, *args, **params)

    @classmethod
    def make(cls, name, template):
        return type(name, (cls,), dict(template=template))


def convert_traceback_to_list(tb):
    # convert to list of dictionaries that contain file, line_no and function
    traceback_list = [dict(file=file, line_no=line_no, function=function)
                      for file, line_no, function, _ in traceback.extract_tb(tb)]
    return traceback_list


def apply_timestamp(exc, now=None):
    timestamp = now or time()
    if getattr(exc, "timestamp", "__missing__") == "__missing__":
        try:
            exc.timestamp = timestamp
        except Exception:
            pass
    return exc
