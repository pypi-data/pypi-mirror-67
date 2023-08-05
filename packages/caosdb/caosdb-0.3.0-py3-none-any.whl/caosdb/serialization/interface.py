from abc import ABCMeta, abstractmethod, abstractproperty
import logging

# meta class compatible with Python 2 *and* 3:
ABC = ABCMeta('ABC', (object, ), {'__slots__': ()})


class AbstractSerializer(ABC):

    @abstractmethod
    def serialize(self, source):
        pass


class AbstractDeserializer(ABC):

    @abstractmethod
    def deserialize(self, source):
        pass
