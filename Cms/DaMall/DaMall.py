#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.DaMall import DaMallSystemSQLInjectionVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(DaMallSystemSQLInjectionVulnerability.medusa, Url, Values, UnixTimestamp)
    Prompt("DaMall")