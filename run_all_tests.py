""" A convenience to run all unit tests at once """

import unittest

from twitter_interface.tests.stream_reader_test import stream_reader_test
from twitter_interface.tests.message_parser_test import message_parser_test


unittest.main()