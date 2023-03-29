# be careful - file access can be s-l-o-w
def writeParts(longtext):
    '''we can write chunks of data at a time'''
    try:
        fout = open('long.txt', 'at')
        # we can choose to send a bit of text at a time (rather than the whole lot)
        size   = len(longtext)
        offset = 0
        chunk  = 24 # here we choose 24 characters at a time
        while True:
            if offset > size:
                fout.write('\n')
                break # always make sure you can end a loop!!!
            else:
                fout.write(longtext[offset:offset+chunk])
                offset += chunk
        fout.close()
    except Exception as err:
        print(err)

def readParts():
    '''we can choose how much to read back'''
    with open('long.txt', 'rt') as fin:
        retrieved = fin.readlines() # all lines end up in a list
        print(retrieved)
        # no need to close - when 'with' terminates it will close 

if __name__ == '__main__':
    l = ''' Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tortor mi, venenatis et metus in, hendrerit vulputate diam. Morbi interdum dolor non eros iaculis, eget dapibus justo vehicula. Integer id libero ac turpis aliquam finibus nec sed neque. Vestibulum dictum eu magna in sollicitudin. Pellentesque lorem nisi, interdum a metus eget, volutpat porta mauris. Vestibulum viverra in erat vel accumsan. In vel tortor sed urna tincidunt accumsan. Suspendisse potenti. Duis venenatis risus lacus, suscipit elementum tortor luctus id. In tincidunt convallis enim non scelerisque. Morbi vitae blandit ex. Donec euismod auctor condimentum.
Suspendisse potenti. Aenean cursus nisl ac ante fermentum fermentum. Donec condimentum porttitor nisi, quis condimentum dui tincidunt vel. Maecenas rhoncus quis libero ac tempor. Nunc imperdiet nisi ut metus pharetra, quis feugiat lorem gravida. Aenean mattis id justo ullamcorper condimentum. Fusce hendrerit ligula eu sem maximus, at dapibus metus elementum. Vivamus pretium tincidunt est, sed aliquet nisi ultricies luctus. Quisque convallis a nibh vel varius. Vestibulum placerat, metus finibus tristique vestibulum, enim nunc molestie augue, eu luctus arcu nisi laoreet nunc. Maecenas finibus felis eu vulputate auctor.
Ut ultrices tincidunt nisl ac cursus. In vitae aliquet felis. Nullam sodales facilisis quam ut rutrum. Quisque vel sem augue. Proin luctus lacus vel nisl tristique, in consectetur velit eleifend. Curabitur sed commodo erat. Integer a ultrices eros. Maecenas eget efficitur sem.
Donec quis magna nec tortor finibus feugiat eu sit amet orci. Pellentesque pretium massa ac erat aliquam, nec fringilla purus dapibus. Sed pellentesque purus mollis lorem commodo sodales. Mauris risus lacus, posuere a tincidunt sit amet, luctus non tortor. Integer cursus turpis ligula, a convallis magna egestas non. Proin ut fermentum lorem. In at elit dui. Curabitur pellentesque nisi hendrerit, maximus nisi eu, feugiat augue. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Phasellus iaculis enim molestie, aliquet orci ut, porta erat. Phasellus dui elit, laoreet sit amet dapibus sit amet, vehicula ac nunc. Morbi accumsan ultrices est, id blandit quam gravida a. Aenean faucibus lorem quis blandit aliquet. Vivamus lacinia pharetra vulputate. '''
    writeParts(l)
    readParts()