import xml.etree.ElementTree as ET

class Person(object):
    def __init__(self, first_name = None, last_name = None):
        self.first_name = first_name
        self.last_name = last_name

    def name(self):
        return(self.first_name + " " + self.last_name)

    @classmethod     
    def getAll(self):
        db = ET.parse("D:\\GitHub\Patterns\\5.MVC_pattern\\db.xml")
        root = db.getroot()
        result = []
        for child in root:
            person = Person(child.find("First_Name").text, child.find("Last_Name").text)
            result.append(person)
        return result


