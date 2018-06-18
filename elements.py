import pandas as pd
import numpy as np


def K2C(K):
    return K - 273.15


def K2F(K):
    return 1.8*K - 459.67


def gcc2lbin(g):
    return g*0.0361273


class Elements:
    def __init__(self):
        self._table = pd.read_csv('elements.csv', index_col='Element')

        self._table['Melting Point (C)'] = self._table.apply(
            lambda row: K2C(row['Melting Point (K)']), axis=1)

        self._table['Melting Point (F)'] = self._table.apply(
            lambda row: K2F(row['Melting Point (K)']), axis=1)

        self._table['Boiling Point (C)'] = self._table.apply(
            lambda row: K2C(row['Boiling Point (K)']), axis=1)

        self._table['Boiling Point (F)'] = self._table.apply(
            lambda row: K2F(row['Boiling Point (K)']), axis=1)

        self._table['Density (lb/in^(3))'] = self._table.apply(
            lambda row: gcc2lbin(row['Density (g/cm^(3))']), axis=1)

        myRounds = {'Atomic Weight': 3,
                    'Density (g/cm^(3))': 3,
                    'Density (lb/in^(3))': 3,
                    'Melting Point (C)': 1,
                    'Melting Point (F)': 1,
                    'Boiling Point (C)': 1,
                    'Boiling Point (F)': 1,
                    'Specific Heat Capacity': 3}

        myProps = ['Atomic Number', 'Symbol', 'Atomic Weight', 'Group',
                   'Density (g/cm^(3))', 'Density (lb/in^(3))',
                   'Melting Point (C)', 'Melting Point (F)', 'Boiling Point (C)',
                   'Boiling Point (F)', 'Discoverer', 'Year of Discovery', 'Type']

        self._table = self._table.round(myRounds)
        self._table = self._table[myProps]
        self._table = self._table.sort_index(axis=1)
        self._table = self._table.transpose()
        self._table = self._table.rename_axis('Element')

    def matrix(self, elements):
        if not isinstance(elements, list):
            elements = [elements]
        mytable = self._table[elements]
        headers = [mytable.index.name] + [i for i in mytable.columns]
        matrix = [[i for i in row] for row in mytable.itertuples()]
        matrix.insert(0, headers)
        return matrix

    def markdown(self, elements):
        if not isinstance(elements, list):
            elements = [elements]
        data = self.matrix(elements)
        markdownTable = ''
        headerRow = '|' + '|'.join(data[0]) + '|'
        markdownTable += headerRow
        cols = len(data[1]) - 1
        markdownTable += '\n' + '|' + ':--|' + '--:|'*cols
        for i, row in enumerate(data):
            if i > 0:
                line = '\n|**' + row[0] + '**|'
                for j, item in enumerate(row):
                    if j > 0:
                        line += str(item) + '|'
                markdownTable += line
        return markdownTable

    def markdownFullTable(self):
        return ('|T|H|E||P|E|R|I|O|D|I|C||T|A|B|L|E|'
                    '|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|'
                    '|||||||||||||||||||'
                    '|||||||||||||||||||'
                    '|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|'
                    '|||||||||||||||||||'
                    '|||||||||||||||||||'
                    '|H^1|||||||||||||||||He^2|'
                    '|Li^3|Be^4|||||||||||B^5|C^6|N^7|O^8|F^9|Ne^10|'
                    '|Na^11|Mg^12|||||||||||Al^13|Si^14|P^15|S^16|Cl^17|Ar^18|'
                    '|K^19|Ca^20|Sc^21|Ti^22|V^23|Cr^24|Mn^25|Fe^26|Co^27|Ni^28|Cu^29|Zn^30|Ga^31|Ge^32|As^33|Se^34|Br^35|Kr^36|'
                    '|Rb^37|Sr^38|Y^39|Zr^40|Nb^41|Mo^42|Tc^43|Ru^44|Rh^45|Pd^46|Ag^47|Cd^48|In^49|Sn^50|Sb^51|Te^52|I^53|Xe^54|'
                    '|Cs^55|Ba^56|La^57|Hf^72|Ta^73|W^74|Re^75|Os^76|Ir^77|Pt^78|Au^79|Hg^80|Ti^81|Pb^82|Bi^83|Po^84|At^85|Rn^86|'
                    '|Fr^87|Ra^88|Ac^89|Rf^104|Db^105|Sg^106|Bh^107|Hs^108|Mt^109|Ds^110|Rg^111|Cn^112|Nh^113|Fl^114|Mc^115|Lv^116|Ts^117|Og^118|'
                    '|||||||||||||||||||'
                    '|||||||||||||||||||'
                    '||||Ce^^58|Pr^59|Nd^60|Pm^61|Sm^62|Eu^63|Gd^64|Tb^65|Dy^66|Ho^67|Er^68|Tm^69|Yb^70|Lu^71|||'
                    '||||Th^90|Pa^91|U^92|Np^93|Pu^94|Am^95|Cm^96|Bk^97|Cf^98|Es^99|Fm^100|Md^101|No^102|Lr^103|||')
