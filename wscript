#! /usr/bin/env python
# encoding: utf-8
#
# Altruistic Control Systems
# Control Node base wscript
# Kenneth Wells, 2015

def configure(conf):
    pass

def build(bld):

    bld(
        target='node_proxy',
        install_path='${PREFIX}/bin',
        features=['cxx', 'cxxshlib','package', 'qt5'],
        manifest='node_proxy.package',
        uselib=['QT5CORE','QT5BASE','QTDBUS','DBUS-1'],
        defines='WAF=1'
        )

    bld(
        target='server_proxy',
        install_path='${PREFIX}/bin',
        features=['cxx', 'cxxshlib','package', 'qt5'],
        manifest='server_proxy.package',
        uselib=['QT5CORE','QT5BASE','QTDBUS','DBUS-1'],
        defines='WAF=1'
        )

