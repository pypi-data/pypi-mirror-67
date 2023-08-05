import io
import logging
import sys
import unittest
import random
import json
from collections import OrderedDict

from logger_json.formatter import JSONFormatter


class TestsLoggerJson(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger("logging-test-{}".format(random.randint(1, 101)))
        self.logger.setLevel(logging.DEBUG)
        self.buffer = io.StringIO()

        self.logHandler = logging.StreamHandler(self.buffer)
        self.logger.addHandler(self.logHandler)

    def testDefaultFormat(self):
        fr = JSONFormatter()
        self.logHandler.setFormatter(fr)

        msg = "testing logging format"
        self.logger.info(msg)
        log = logging.getLogger("TestLog")
        log.debug(self.buffer.getvalue())
        logJson = json.loads(self.buffer.getvalue())

        self.assertEqual(logJson["msg"], msg)

    def testUnknownFormatKey(self):
        fr = JSONFormatter(['unknown'])

        self.logHandler.setFormatter(fr)
        msg = "testing unknown logging format"
        try:
            self.logger.info(msg)
        except AttributeError:
            self.assertTrue(False, "Should succeed")

    def testOrderedDictFormat(self):
        fr = JSONFormatter()
        self.logHandler.setFormatter(fr)
        ordered_dict = OrderedDict((('user', 'Fred'), ('query', 'Bujold'), ('results', 5)))
        self.logger.info(ordered_dict)
        log = logging.getLogger("TestLog")
        log.debug(self.buffer.getvalue())
        log_json = json.loads(self.buffer.getvalue())
        self.assertEqual(log_json["msg"]["query"], "Bujold")
        self.assertEqual(log_json["msg"]["user"], "Fred")
        self.assertEqual(log_json["msg"]["results"], 5)

    def testLogExtra(self):
        fr = JSONFormatter()
        self.logHandler.setFormatter(fr)

        extra = {"text": "testing logging", "num": 1, "9": "9",
                 "nested": {"more": "data"}}
        #self.logger = self.logger.LoggerAdapter(self.logger, extra={'abc': 'bcd'})
        #self.logger.info("hello", extra=extra)
        self.logger.info(extra)
        log = logging.getLogger("TestLog")
        log.debug(self.buffer.getvalue())
        #logJson = json.loads(self.buffer.getvalue())
        #self.assertEqual(logJson.get("text"), extra["text"])
        #self.assertEqual(logJson.get("num"), extra["num"])
        #self.assertEqual(logJson.get("5"), extra[5])
        #self.assertEqual(logJson.get("nested"), extra["nested"])
        #self.assertEqual(logJson["message"], "hello")


logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
if __name__ == '__main__':
    unittest.main()
