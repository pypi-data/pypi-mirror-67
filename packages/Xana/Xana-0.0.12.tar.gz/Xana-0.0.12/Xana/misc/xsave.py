import os
import re
import glob
import pickle


def make_filename(obj, attr=None, filename=None):

    def splitpath(path):
        if path is None:
            print('No valid file specified.')
        tmp = path.split('/')
        fname = tmp[-1]
        path = os.path.abspath('/'.join(tmp[:-1])) + '/'
        return path, fname

    if attr is None and filename is None:
        raise ValueError(
            'Both attribute name and filename are None. Cannot create filename.')

    savdir = obj.savdir
    if attr is not None:
        orgname = obj.__dict__[attr]
    if filename is None:
        savdir, filename = splitpath(orgname)
    else:
        if '/' in filename:
            filename = os.path.abspath(filename)
            savdir, filename = splitpath(filename)
    return savdir, filename


def mksavdir(sample_name=None, savhome='./', handle_existing='use'):
    """
    Create a directory for saving results.\n
    Usage is: mksavdir(sample_name, savhome, handling_existing)\n
    handling_existig\n
    'use'\tuse same direcotry\n
    'next'\tadd counter
    """
    savhome = os.path.abspath(savhome) + '/'
    if sample_name is None:
        sample_name = input(('Chose a sample name for saving in {}\n'
                             + 'or enter full path.').format(savhome))
    # if '/' in sample_name:
    #     savdir = os.path.abspath(sample_name.rstrip('/')) + '/'
    # else:
    savdir = savhome.rstrip('/') + '/' + sample_name.rstrip('/') + '/'

    try:
        os.makedirs(savdir)
    except FileExistsError:
        if handle_existing == 'use':
            pass
        elif handle_existing == 'next':
            searchstr = '_\d{2}$'
            savsplit = savdir.split('/')
            reg = re.search(searchstr, savsplit[-2])
            folderlist = glob.glob(savdir[:-1]+'_*')
            if reg is None and len(folderlist) == 0:
                savsplit[-2] += '_02'
            else:
                counter = max(list(map(lambda x: int(re.search(searchstr, x).group().lstrip('_')),
                                       folderlist)))
                savsplit[-2] += '_{:02d}'.format(counter+1)
            savdir = '/'.join(savsplit)
            os.makedirs(savdir)
        else:
            print('Could not create directory.')
    savdir = os.path.abspath(savdir) + '/'
    print('Changing savdir to:\n\t{}'.format(savdir))
    return savdir


def save_result(savobj, restype, savdir, filename="", handle_existing='raise', prompt=True):
    savdir = os.path.abspath(savdir)
    filename = re.sub(r'^((' + restype + ')_*)', '', filename)
    filename = re.sub(r'(\.(pkl)*)$', '', filename)
    savname = savdir + '/' + restype + '_' + filename + '.pkl'

    save = True
    if handle_existing == 'next':
        savname = savname.rstrip('.pkl')
        searchstr = '\d{4}$'

        def reg(x): return re.search(searchstr, x.rstrip('.pkl'))
        filelist = glob.glob(savname+'*')
        counter = [int(reg(x).group()) for x in filelist if reg(x) is not None]
        counter.append(-1)
        counter = max(counter) + 1
        savname += '_{:04d}'.format(counter) + '.pkl'
    elif handle_existing in ['overwrite', 'w']:
        pass
    elif handle_existing == 'raise':
        if os.path.isfile(savname) and not prompt:
            raise OSError(('File {} already exists. Change overwrite to ' +
                           'True or choose different name.').format(savname))
        elif os.path.isfile(savname) and prompt:
            user_input = input('File exists. Save anyway? (No/Yes)\t')
            if user_input == 'yes' or user_input == 'Yes':
                pass
            else:
                save = False
    else:
        raise ValueError('{} is not a valid option'.format(handle_existing))

    if save:
        pickle.dump(savobj, open(savname, 'wb'))
        print('\nResults saved to:\n\t{}'.format(savname))
        return savname
    else:
        print('Result has not been saved.')
