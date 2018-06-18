from elements import Elements


def test_creation():
    mytable = Elements()
    myseries = mytable._table[mytable._table.columns[0]].tolist()
    assert myseries == [1, 1.008, -252.9,
                        -423.2, 0.0, 0.0,
                        'Cavendish', 1, -259.0,
                        -434.2, 'H', 'Nonmetal',
                        '1766']


def test_matrix():
    myelements = ['Hydrogen', 'Boron']
    mytable = Elements()
    mymatrix = mytable.matrix(myelements)
    assert mymatrix == [['Element', 'Hydrogen', 'Boron'],
                        ['Atomic Number', 1, 5],
                        ['Atomic Weight', 1.008, 10.811],
                        ['Boiling Point (C)', -252.9, 3926.8],
                        ['Boiling Point (F)', -423.2, 7100.3],
                        ['Density (g/cm^(3))', 0.0, 2.34],
                        ['Density (lb/in^(3))', 0.0, 0.085],
                        ['Discoverer', 'Cavendish', 'Gay-Lussac'],
                        ['Group', 1, 13],
                        ['Melting Point (C)', -259.0, 2300.0],
                        ['Melting Point (F)', -434.2, 4172.0],
                        ['Symbol', 'H', 'B'],
                        ['Type', 'Nonmetal', 'Metalloid'],
                        ['Year of Discovery', '1766', '1808']]


def test_matrix_one_element():
    myelements = 'Hydrogen'
    mytable = Elements()
    mymatrix = mytable.matrix(myelements)
    assert mymatrix == [['Element', 'Hydrogen'],
                        ['Atomic Number', 1],
                        ['Atomic Weight', 1.008],
                        ['Boiling Point (C)', -252.9],
                        ['Boiling Point (F)', -423.2],
                        ['Density (g/cm^(3))', 0.0],
                        ['Density (lb/in^(3))', 0.0],
                        ['Discoverer', 'Cavendish'],
                        ['Group', 1],
                        ['Melting Point (C)', -259.0],
                        ['Melting Point (F)', -434.2],
                        ['Symbol', 'H'],
                        ['Type', 'Nonmetal'],
                        ['Year of Discovery', '1766']]


def test_markdown():
    myelements = ['Hydrogen', 'Boron']
    mytable = Elements()
    mymarkdown = mytable.markdown(myelements)
    assert mymarkdown == ('|Element|Hydrogen|Boron|'
                          '\n|:--|--:|--:|'
                          '\n|**Atomic Number**|1|5|'
                          '\n|**Atomic Weight**|1.008|10.811|'
                          '\n|**Boiling Point (C)**|-252.9|3926.8|'
                          '\n|**Boiling Point (F)**|-423.2|7100.3|'
                          '\n|**Density (g/cm^(3))**|0.0|2.34|'
                          '\n|**Density (lb/in^(3))**|0.0|0.085|'
                          '\n|**Discoverer**|Cavendish|Gay-Lussac|'
                          '\n|**Group**|1|13|'
                          '\n|**Melting Point (C)**|-259.0|2300.0|'
                          '\n|**Melting Point (F)**|-434.2|4172.0|'
                          '\n|**Symbol**|H|B|'
                          '\n|**Type**|Nonmetal|Metalloid|'
                          '\n|**Year of Discovery**|1766|1808|')


def test_markdown_one_element():
    myelements = 'Hydrogen'
    mytable = Elements()
    mymarkdown = mytable.markdown(myelements)
    assert mymarkdown == ('|Element|Hydrogen|'
                          '\n|:--|--:|'
                          '\n|**Atomic Number**|1|'
                          '\n|**Atomic Weight**|1.008|'
                          '\n|**Boiling Point (C)**|-252.9|'
                          '\n|**Boiling Point (F)**|-423.2|'
                          '\n|**Density (g/cm^(3))**|0.0|'
                          '\n|**Density (lb/in^(3))**|0.0|'
                          '\n|**Discoverer**|Cavendish|'
                          '\n|**Group**|1|'
                          '\n|**Melting Point (C)**|-259.0|'
                          '\n|**Melting Point (F)**|-434.2|'
                          '\n|**Symbol**|H|'
                          '\n|**Type**|Nonmetal|'
                          '\n|**Year of Discovery**|1766|')
