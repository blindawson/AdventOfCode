from AdventOfCode.support import support
from AdventOfCode.year_2021.src import day16_packet_decoder as pe

test_hex = 'D2FE28'
test_bin = support.hex_to_bin(test_hex)
test_input2 = support.hex_to_bin('38006F45291200')
test_input3 = support.hex_to_bin('EE00D40C823060')
test_input4 = support.hex_to_bin('8A004A801A8002F478')
test_input5 = support.hex_to_bin('620080001611562C8802118E34')
test_input6 = support.hex_to_bin('C0015000016115A2E0802F182340')
test_input7 = support.hex_to_bin('A0016C880162017C3686B18A3D4780')
test_input8 = support.hex_to_bin('9C0141080250320F1802104A08')


def test_read_transmission():
    v, lv = pe.read_transmission(test_bin)
    assert v == [6]
    v, lv = pe.read_transmission(test_input4)
    assert sum(v) == 16
    v, lv = pe.read_transmission(test_input5)
    assert sum(v) == 12
    v, lv = pe.read_transmission(test_input6)
    assert sum(v) == 23
    v, lv = pe.read_transmission(test_input7)
    assert sum(v) == 31
    _, lv = pe.read_transmission(test_input8)
    assert lv == [1]
    