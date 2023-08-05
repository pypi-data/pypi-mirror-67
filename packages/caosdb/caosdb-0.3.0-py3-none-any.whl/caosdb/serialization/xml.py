from .interface import AbstractDeserializer, AbstractSerializer
import xmltodict


class XMLDeserializer(AbstractDeserializer):

    def deserialize(self, source):
        return xmltodict.parse(source)
