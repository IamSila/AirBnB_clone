#!/usr/bin/python3
"""This initializes the package inside basemeodel"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
