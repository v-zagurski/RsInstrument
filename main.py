from RsInstrument import RsInstrument

instr = RsInstrument('TCPIP::192.168.56.101::hislip0', id_query=True, reset=True)
idn = instr.query_str('*IDN?')
print('Hello, I am: ' + idn)
