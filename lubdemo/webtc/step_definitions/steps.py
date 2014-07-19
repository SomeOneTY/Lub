# -*- coding:utf-8 -*-
# step definitions

# -*- coding:utf-8 -*-
# step definitions

from Lub.webtools.actions import *
from lettuce import *

@step(u'打开 "(.*)"')
def openurl(step,url):
    world.browser.get(url)

@step(u'在 "(.*)" 为 "(.*)" 的框中输入 "(.*)"')
def typekey(step,typename,typekey,typeval):
    lubfind(world.browser,typename,typekey).send_keys(typeval)

@step(u'点击 "(.*)" 为 "(.*)" 的按钮')
def clickelem(step,typename,typekey):
    lubfind(world.browser,typename,typekey).click()