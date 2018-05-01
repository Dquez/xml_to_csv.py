import xml.etree.ElementTree as ET
import csv
def xml_converter():
    tree = ET.parse("book_catalog.xml")
    root = tree.getroot()
    csv = []
    for child in root:
        book = ["{0} id={1}".format(child.tag, child.get("id"))]
        csv.append(book)
        row = []
        if (len(csv) == 1):
            csv.append([child[0].tag,child[1].tag, child[0].tag, child[3].tag, child[4].tag, child[5].tag])
        for sub_child in child:
            row.append(sub_child.text)
        csv.append(row)
    return csv

with open("csv_converted.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(xml_converter())
