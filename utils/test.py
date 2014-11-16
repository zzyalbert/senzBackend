#!/usr/bin/env python
# encoding: utf-8
#__author__ = 'wumao'

from __future__ import absolute_import
from avos.avos import AVObject
import arrow
import json


class TestClass(AVObject):
    def __init__(self):
        super(TestClass, self).__init__()


if __name__ == "__main__":

    date_iso = arrow.utcnow().isoformat()
    js_now = dict(
        __type='Date',
        iso=date_iso[:date_iso.rfind('+')][:-3]+'Z'
    )

    import settings
    TestClass.app_settings = [settings.avos_app_id, settings.avos_app_key]

    res = TestClass.save({'test_num': 111,'test_arr':['test_value'],'date':js_now})
    if 'createdAt' in json.loads(res.content):
        print '\nSucceeded in creating test object in TestClass!\n'
    else:
        print res.content