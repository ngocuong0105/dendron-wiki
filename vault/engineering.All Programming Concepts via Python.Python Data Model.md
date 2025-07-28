---
id: 52wto1xcmhqo5e3qtle92x9
title: Python Data Model
desc: ''
updated: 1752649709079
created: 1752649707785
---

# Python Data Model

- [Data Model from Python Language Reference](https://docs.python.org/3/reference/datamodel.html)


Every object has identity (address of the place in memory), type and value. Only value can be changed (for mutable objects). Immutable objects cannot have their value changed.

`is` operator compares the identity of two objects `==` compares their value.

`id()` gives an integer representing the identity