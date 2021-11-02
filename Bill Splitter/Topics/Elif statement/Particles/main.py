spin = input()
charge = input()
if spin == '1':
    print('Photon Boson')
else:
    if charge == '0':
        print('Neutrino Lepton')
    elif charge == '-1':
        print('Electron Lepton')
    elif charge == '2/3':
        print('Charm Quark')
    else:
        print('Strange Quark')
