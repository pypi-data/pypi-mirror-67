
import abc
import json
import pathlib
import structlog
import tempfile
import uuid

import pydantic


logger = structlog.get_logger(__name__)


class Item(pydantic.BaseModel):

    id: str
    name: str
    address: str = None
    phone: str = None


class Store(metaclass=abc.ABCMeta):
    """
    Store

    This is the base class for all storage implementations. It is an
    abstract class and cannot be directory instantiated. To create
    specific storage solution, make a subclass and implement the
    following methods:

        * get (used to get records from the store)
        * put (used to put records into the store)
    """

    NAME = ""

    @abc.abstractmethod
    def init(self, id_):
        """
        Initialize store (gets called when storage plugin is loaded)
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, id_):
        """
        Get item with the given identifier (ID).
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_all(self, ids):
        """
        Get items with the given identifiers (IDs).
        """
        raise NotImplementedError

    @abc.abstractmethod
    def put(self, data):
        """
        Put the given item in the data store.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def put_all(self, dataset):
        """
        Put the given items in the data store.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def clear(self):
        """
        Clear data store.
        """
        raise NotImplementedError


# ----------------------------------------------------------------------
# Built-in storage plugin
# ----------------------------------------------------------------------

class JSONStore(Store):
    """
    JSON Store

    This is the default storage solution for rolodex data. It stores
    the data as a JSON file.
    """

    NAME = "json"

    def __init__(self, path=None):
        self._path = path
        self._data = {}
        self.persist = True

    @property
    def path(self):
        if self._path is None:
            root = pathlib.Path(tempfile.gettempdir())
            self._path = root.joinpath("rolodex", "db.json")

        return self._path

    @property
    def data(self):
        return self._data

    def init(self):
        """
        Initialize storage
        """
        msg = f"Initializing data store: {self.path}"
        logger.info(msg)
        self.load()

    def get(self, id_):
        """
        Get item with the given ID.
        """
        data = self._data.get(id_)
        if not data:
            msg = f"Cannot find item with ID: {id_}"
            raise LookupError(msg)

        return Item(**data)

    def get_all(self, ids):
        """
        Get items with the given IDs.

        If no IDs are given, all items will be returned.
        """
        ids = ids or self._data.keys()
        return [self.get(id_) for id_ in ids]

    def put(self, data):
        """
        Put the given item in the data store.
        """
        item = self._put(data)
        self.save()
        return item

    def _put(self, data):
        try:
            uid = str(uuid.uuid4())
            item = Item(id=uid, **data)
            self._data[uid] = item.dict()
        except pydantic.ValidationError as err:
            raise ValueError(str(err))

        return item

    def put_all(self, dataset):
        """
        Put the given items in the data store.

        Note:
            If one item fails, the whole transaction fails.
        """
        # Create snapshot for rollback.
        snapshot = self._data.copy()
        items = []
        try:
            for data in dataset:
                item = self._put(data)
                items.append(item)
        except ValueError as err:
            # Something went wrong (rolling back)
            self._data = snapshot
            raise ValueError(str(err))

        self.save()
        return items

    def clear(self):
        """
        Clear data store
        """
        self._data = {}
        self.save()

    def save(self):
        """
        Save data to disk.
        """
        if self.persist:
            if not self.path.exists():
                self.path.parent.mkdir(parents=True)
                self.path.touch()

            self.path.write_text(json.dumps(self.data, indent=2))

    def load(self):
        """
        Load data from disk.
        """
        if self.path.exists() and self.persist:
            self._data = json.loads(self.path.read_text())
