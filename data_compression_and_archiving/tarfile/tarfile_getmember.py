import tarfile
import time

with tarfile.open('example.tar', 'r') as t:
    for filename in ['README.txt', 'notthere.txt']:
        try:
            info = t.getmember(filename)
        except KeyError:
            print('Error: did not find {} in tar archive.'.format(
                filename
            ))
        else:
            print('{} is {:d}bytes.'.format(
                info.name, info.size
            ))
