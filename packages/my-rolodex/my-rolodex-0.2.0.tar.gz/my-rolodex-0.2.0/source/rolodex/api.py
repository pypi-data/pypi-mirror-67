
import os
import functools
import pathlib
import pkg_resources

from .store import Store


def from_env():
    """
    Create API instance from the current environment.
    """
    storage = os.getenv("ROLODEX_STORE", "json")
    store = load_plugin("storage", storage)
    store.init()

    api = API(store)
    api.readers = load_plugins("readers")
    api.writers = load_plugins("writers")

    return api


class API:
    """
    API

    This class represents the animal API. It is the entry point
    for performing functionality such as:

        * Addting items in the store
        * Getting items from the store
        * Checking all available reader/parser plugins
        * Checking all available writer/formatter plugins
    """

    def __init__(self, store):
        self.store = store
        self.readers = {}
        self.writers = {}

    def get_reader(self, key):
        """
        Get reader

        Get the reader for the given key. The key can be a file path,
        suffix/extension or the name of the reader plugin.
        """
        match = None
        for reader in self.readers.values():
            if reader.is_compatible(key):
                match = reader
                break

        if not match:
            msg = f"Cannot find compatible reader for: {key}"
            raise ValueError(msg)

        return match

    def get_writer(self, key):
        """
        Get writer

        Get the writer for the given key. The key can be a file path,
        suffix/extension or the name of the reader plugin.
        """
        match = None
        for writer in self.writers.values():
            if writer.is_compatible(key):
                match = writer
                break

        if not match:
            msg = f"Cannot find compatible writer for: {key}"
            raise ValueError(msg)

        return match

    def get_formats(self):
        """
        Get formats

        Get all supported I/O formats.
        """
        return {
            "readers": list(self.readers.keys()),
            "writers": list(self.writers.keys())
        }

    def add(self, dataset):
        """
        Add all the given items in the data store.
        """
        return self.store.add(dataset)

    def get(self, contact_ids=None):
        """
        Get the given items from the data store
        """
        return self.store.get(contact_ids or [])

    def remove(self, contact_ids):
        """
        Remove all given contacts
        """
        return self.store.remove(contact_ids)

    def clear(self):
        """
        Remove all contacts (reset data store).
        """
        contacts = self.store.get([])
        self.store.remove([c.id for c in contacts])

    def read(self, path):
        """
        Read file at the given location.
        """
        path = pathlib.Path(path)
        reader = self.get_reader(path)
        data = reader.read(path)
        dataset = [data] if not isinstance(data, list) else data
        return dataset

    def dumps(self, dataset, fmt="json"):
        """
        Dump the given dataset as text.
        """
        writer = self.get_writer(fmt)
        return writer.dumps(dataset)


@functools.lru_cache()
def load_plugins(group):
    """
    Load all available plugins.

    Note:
        Plugins are defined in the pyproject.toml file. (See
        documentation for more information about this approach)
    """
    plugins = {}
    group_name = f"rolodex.{group}"
    for plugin in pkg_resources.iter_entry_points(group_name):
        plugin_class = plugin.load()
        plugins[plugin.name] = plugin_class()

    return plugins


def load_plugin(group, name):
    """
    Load a specific plugin from the given plugin group.

    Note:
        Plugins are defined in the pyproject.toml file. (See
        documentation for more information about this approach)
    """
    plugin = load_plugins(group).get(name)
    if not plugin:
        msg = f"Cannot find plugin for: group={group} name={name}"
        raise ValueError(msg)

    return plugin
