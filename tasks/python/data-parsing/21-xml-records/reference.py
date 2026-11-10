import xml.etree.ElementTree as ET

def xml_cases(text):
    try:
        root = ET.fromstring(text)
    except ET.ParseError as e:
        raise ValueError('xml') from e
    if root.tag != 'report':
        raise ValueError('root')
    out = []
    for child in root.findall('case'):
        if 'name' not in child.attrib:
            raise ValueError('name')
        message = child.find('message')
        text = ''.join(message.itertext()) if message is not None else ''
        out.append((child.attrib['name'], child.attrib.get('status', 'unknown'), text))
    return out
