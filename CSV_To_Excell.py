import xml.etree.ElementTree as ET
import csv 
import re 

tree = ET.parse('XML_To_Process.xml')
repeatingSegments = []
list1 = []
data = []
def simplify(s):

     # Remove all non-word characters (everything except numbers and letters)
     s = re.sub(r"[^\w\s]", '_', s)

     # Replace all runs of whitespace with a single dash
     s = re.sub(r"\s+", '_', s)

     return s

def loop(element, prefix, alreadyHit):
    count = 1
    for node in element.iter('Segment'):
        print(node.attrib['name'])
        # list1.append(node.attrib['name']) # Title of segment
        
        if(node.attrib['type'] == 'N9'):
            print("FOUND AN N9 Segment!!!!!")
            
            for item in node.iter('Element'):
                name = item.attrib['name']
                list1.append(prefix + "_" + simplify(name) +"_" + str(count))
                data.append(item.text)
                
            count +=1
        else:
            for item in node.iter('Element'):
                name = item.attrib['name']

                print(name)
                print("Prefix: " + prefix + ", Name: " + simplify(name))
                list1.append(prefix + "_" + simplify(name))
                data.append(item.text)
                print(item.text)

root = tree.getroot()
print(root)
count = 0
for node in tree.iter('RepeatingSegment'):
    count += 1
    print(node.attrib['type'])
    prefix = node.attrib['type']
    alreadyHitPrefix = prefix in list1
    if(alreadyHitPrefix == True):
        print("REPEAT FOUND FOR " + prefix)
    else:    
        repeatingSegments.append(prefix)

    loop(node, prefix, alreadyHitPrefix)
    # print(node.attrib['type'])
alreadyHitPrefix = prefix in list1
print("Count: " + str(count))
print(list1)
print("************************* ITEMS: *************************")
print(data)

print("<root>")
for i in list1:
    
    print("<" + simplify(i) + "/>")

print("</root>")
with open('ConvertedData2.csv' ,'wb') as myfile: 
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(list1)
    wr.writerow(data)



print("=========================================")
for item in list1:
    #to generate Flat File Schema
    #string = "<Field xmlType='Element' startPosition='1' endPosition='1' trimspaces='None' alignment='LEFT' mapIfNull='YES' name='" + item + "'> <DataType format=''>String</DataType> </Field>"
    # print(string)
    # To generate XSLT
    #string2 = "<xsl:value-of select='root/" + item +"'/>"
    print(string2)

