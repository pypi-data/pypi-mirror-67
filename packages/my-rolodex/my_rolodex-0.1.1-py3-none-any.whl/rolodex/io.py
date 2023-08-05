import abc
import pathlib
import json
import yaml

import structlog


logger = structlog.get_logger(__name__)


class BaseIO:
    """
    Base I/O

    This is the base class for all readers and writers. It provides
    common functionality such as:

        * Checking file compatibility
        * Checking file format compatibility
        * Validating input files
    """

    NAME = ""
    SUFFIXES = []

    @classmethod
    def is_compatible(cls, key):
        """
        Check compatibility

        Check if the I/O plugin is compatible with the given file
        path, suffix or format.
        """
        status = cls.check_path(key)
        if not status:
             status = cls.check_suffix(key) or key == cls.NAME

        return status

    @classmethod
    def check_path(cls, path):
        """
        Check file compatibility

        Check if the I/O class is compatible with the given file path.
        """
        suffixes = pathlib.Path(path).suffixes
        return cls.check_suffix(*suffixes)

    @classmethod
    def check_suffix(cls, *suffixes):
        """
        Check file type compatibility

        Check if the I/O class is compatible with any of the
        given suffixes (i.e. file formats/extensions).
        """
        for suffix in suffixes:
            if suffix in cls.SUFFIXES:
                return True

        return False

    def validate(self, path):
        """
        Validate

        Check if the given file is valid.
        """
        # Check file format is compatible
        if not self.check_path(path):
            msg = (
                f"File format is not supported: {path.suffix} "
                f"(valid={self.SUFFIXES})"
            )
            raise ValueError(msg)

        # Check the file exists.
        if not path.exists():
            msg = f"File does not exist: {path}"
            raise IOError(msg)


class Reader(BaseIO, metaclass=abc.ABCMeta):
    """
    Reader

    This is the base class for all readers. It is an abstract class
    and cannot be directory instantiated. To create a reader for a
    specific format, make a subclass and implement the following
    methods:

        * loads
    """

    NAME = ""
    SUFFIXES = []

    def read(self, path):
        """
        Read

        Read file at the given location.
        """
        logger.info(f"Reading file: {path}")
        path = pathlib.Path(path)
        self.validate(path)
        text = path.read_text()
        return self.loads(text)

    @abc.abstractmethod
    def loads(self, text):
        """
        Loads

        Load the given text into python data.

        Note:
            This is an abstract method. All subclasses (i.e. format
            specific readers) must implement this method.
        """
        raise NotImplementedError("This is an abstract method")


class Writer(BaseIO, metaclass=abc.ABCMeta):
    """
    Writer

    This is the base class for all writers. It is an abstract class
    and cannot be directory instantiated. To create a writer for a
    specific format, make a subclass and implement the following
    methods:

        * dumps
    """

    NAME = ""
    SUFFIXES = []

    def write(self, data, path):
        """
        Write

        Write data to a file at the given location.
        """
        logger.info(f"Writing file: {path}")
        path = pathlib.Path(path)
        self.validate(path)
        text = self.dumps(data)
        path.write_text(text)

    @abc.abstractmethod
    def dumps(self, data):
        """
        Dumps

        Dump the given data to text.

        Note:
            This is an abstract method. All subclasses (i.e. format
            specific writers) must implement this method.
        """
        raise NotImplementedError("This is an abstract method")


# ----------------------------------------------------------------------
# Built-in I/O plugins
# ----------------------------------------------------------------------

class JSONReader(Reader):
    """
    JSON Reader

    JSON reader plugin used to read/load JSON data.
    """

    NAME = "json"
    SUFFIXES = [".json"]

    def loads(self, text):
        """
        Loads

        Convert JSON text to python data.
        """
        return json.loads(text)


class JSONWriter(Writer):
    """
    JSON Writer

    JSON writer plugin used to write/dump JSON data.
    """

    NAME = "json"
    SUFFIXES = [".json"]

    def dumps(self, data):
        """
        Dumps

        Dump the given data by converting it from python data to a
        JSON string.
        """
        return json.dumps(data, indent=2)


class YAMLReader(Reader):
    """
    YAML Reader

    YAML reader plugin used to read/load YAML data.
    """

    NAME = "yaml"
    SUFFIXES = [".yml", ".yaml"]

    def loads(self, text):
        """
        Loads

        Convert YAML text to python data.
        """
        return yaml.safe_load(text)


class YAMLWriter(Writer):
    """
    YAML Writer

    YAML writer plugin used to write/dump YAML data.
    """

    NAME = "yaml"
    SUFFIXES = [".yml", ".yaml"]

    def dumps(self, data):
        """
        Dumps

        Convert python data to YAML string.
        """
        return yaml.safe_dump(data)
