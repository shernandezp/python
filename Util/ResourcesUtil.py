from xml.etree import ElementTree

class ResourcesUtil:

    @staticmethod
    def GetEntryValue(entry):
        tree = ElementTree.parse("Resources/MySql/Sentences.xml")
        for i in range(len(tree.findall("entry"))):
            item = tree.getroot()[i]
            if (item.items()[0][1] == entry):
                return item.text
        return None