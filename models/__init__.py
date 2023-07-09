#!/usr/bin/python3
"""Loads and reloads the file storage.

This code imports the `FileStorage` class from the `models.engine.file_storage`
module. Then, it creates an instance of `FileStorage` named `storage` and calls
the `reload()` method on that instance. This method loads and reloads the file
storage.

Usage:
    from models.engine.file_storage import FileStorage.

    storage = FileStorage()
    storage.reload()
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
