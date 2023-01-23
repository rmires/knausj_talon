from talon import Context, Module, actions, settings, resource, fs
from typing import Tuple, Dict
import os
import json
import pathlib
import sqlite3

mod = Module()
ctx = Context()

mod.list("cpp_tips", desc="C++ tips.")
ctx.lists["user.cpp_tips"] = {
        "include": "inc",
        "local include": "linc",
        "class": "class",
        "struct": "struct",
        "name space": "namespace",
        "header": "header",
        "range": "range",
        "vector": "vector",
        "array": "array",
        "map": "map",
        "template": "template",
        "see out": "cout",
        "log": "log",
        "state if": "#if",
        "for": "for",
        "for size": "fori",
        "for you": "foru",
        "for range": "forr",
        "while": "while",
        "do": "do",
        "switch": "switch",
        "case": "case",
        "default": "default",
        "if": "if",
        "else": "else",
        "if else": "ifel",
        "function": "func",
        "function declaration": "dfunc",
        "enumeration": "enum",
        "main": "main",
        "to do": "todo"
        }

mod.list("cpp_integral", desc="C++ integral types.")
ctx.lists["user.cpp_integral"] = {
    "char": "char",
    "byte": "int8",
    "short": "int16",
    "integer": "int",
    "long": "int64",
    "float": "float",
    "double": "double",
    "size": "std::size_t",

    "you byte": "uint8",
    "you short": "uint16",
    "you long": "uint64",
    "you integer": "int",

    "auto": "auto",
    "boolean": "bool",
    "void": "void",
}

mod.list("cpp_modifiers", desc="C++ modifiers.")
ctx.lists["user.cpp_modifiers"] = {
    "constant reference": "const&",
    "constant pointer": "const*",
    "pointer": "*",
    "star": "*",
    "reference": "&",
    "ampersand": "&",
    "constant": "const",
    "inline": "inline",
    "volatile": "volatile",
    "virtual": "virtual",
    "static": "static"
}

mod.list("cpp_known_namespaces", desc = "Known C++ namespaces.")
ctx.lists["user.cpp_known_namespaces"] = {
    "standard": "std",
    "boost": "boost"
        }

@mod.capture
def cpp_known_namespaces(m) -> Dict:
    "Returns a JSON dict of the namespace."

@ctx.capture('self.cpp_known_namespaces', rule="{self.cpp_known_namespaces}")
def cpp_known_namespaces(m) -> Dict:
    return json_namespace_table[m[0]]


@mod.capture
def cpp_tips(m) -> str:
    "Returns an tips type."

@ctx.capture('user.cpp_tips', rule="{user.cpp_tips}")
def cpp_tips(m) -> str:
    return m.cpp_tips

@mod.capture
def cpp_integral(m) -> str:
    "Returns an integral type."

@ctx.capture('self.cpp_integral', rule="{self.cpp_integral}")
def cpp_integral(m) -> str:
    return m.cpp_integral

@mod.capture
def cpp_modifiers(m) -> str:
    "Returns a C++ modifier."

@ctx.capture('self.cpp_modifiers', rule = "{self.cpp_modifiers}+")
def cpp_modifiers(m) -> str:
    return " ".join(m.cpp_modifiers_list)


@mod.action_class
class Actions:
    def cpp_namespace_with_joiner(ns: Dict) -> str:
        """Returns a namespace and its joiner, e.g. 'std::' """
        return ns['namespace'] + ns['joiner']
    def cpp_naked_namespace(ns: Dict) -> str:
        """Gets only the namespace part of a namespace."""
        return ns['namespace']
    pass

