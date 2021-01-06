import os
import getpass
import Error

username = getpass.getuser()
path = 'C:\\Users\\{}\\'.format(username)
global name, directory, file_root


def word(filename):
    file_list = []
    global file_root, directory, name
    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
            # for specific file type
            if name.endswith('.docx'):
                if filename in name.lower():
                    file_list.append(name)
                    print('\n'f'Found in: {root}')
                    print((len(file_list)), ')', name)
                    file_root = root
    if len(file_list) > 1:
        print(f'[SUCCESS]: {len(file_list)} files found for {filename}.')
        choice = int(input('Lex:\\User\\command\\docx\\{}\\choice|return[0]> '.format(filename)))
        for file in file_list:
            try:
                if choice == file_list.index(file) + 1:
                    directory = (os.path.join(file_root, file))
                    return os.startfile(directory)
                elif 0 == choice:
                    break
            except FileNotFoundError:
                Error.printline('[ERROR|docx]: File unavailable.\n')
    elif len(file_list) == 1:
        print(f'[SUCCESS]: {len(file_list)} file found for {filename}.')
        choice = int(input('Lex:\\User\\command\\docx\\{}\\choice|return[0]> '.format(filename)))
        for file in file_list:
            try:
                if choice == file_list.index(file) + 1:
                    directory = (os.path.join(file_root, file))
                    return os.startfile(directory)
                elif 0 == choice:
                    break
            except FileNotFoundError:
                Error.printline('[ERROR|docx]: File unavailable.\n')
    else:
        Error.printline('[ERROR|docx]: 0 file found.\n')


def powerpoint(filename):
    file_list = []
    global file_root, directory, name
    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
            # for specific file type
            if name.endswith('.pptx'):
                if filename in name.lower():
                    file_list.append(name)
                    print('\n'f'Found in: {root}')
                    print((len(file_list)), ')', name)
                    file_root = root
    if len(file_list) > 1:
        print(f'[SUCCESS]: {len(file_list)} files found for {filename}.')
        choice = int(input('Lex:\\User\\command\\pptx\\{}\\choice|return[0]> '.format(filename)))
        for file in file_list:
            try:
                if choice == file_list.index(file) + 1:
                    directory = (os.path.join(file_root, file))
                    return os.startfile(directory)
                elif 0 == choice:
                    break
            except FileNotFoundError:
                Error.printline('[ERROR|pptx]: File unavailable.\n')
    elif len(file_list) == 1:
        print(f'[SUCCESS]: {len(file_list)} file found for {filename}.')
        choice = int(input('Lex:\\User\\command\\pptx\\{}\\choice|return[0]> '.format(filename)))
        for file in file_list:
            try:
                if choice == file_list.index(file) + 1:
                    directory = (os.path.join(file_root, file))
                    return os.startfile(directory)
                elif 0 == choice:
                    break
            except FileNotFoundError:
                Error.printline('[ERROR|pptx]: File unavailable.\n')
    else:
        Error.printline('[ERROR|pptx]: 0 file found.\n')


def portable_document_format(filename):
    file_list = []
    global file_root, directory, name
    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
            # for specific file type
            if name.endswith('.pdf'):
                if filename in name.lower():
                    file_list.append(name)
                    print('\n'f'Found in: {root}')
                    print((len(file_list)), ')', name)
                    file_root = root
    if len(file_list) > 1:
        print('\n'f'[SUCCESS]: {len(file_list)} files found for {filename}.')
        choice = int(input('Lex:\\User\\command\\pdf\\{}\\choice|return[0]> '.format(filename)))
        for file in file_list:
            try:
                if choice == file_list.index(file) + 1:
                    directory = (os.path.join(file_root, file))
                    return os.startfile(directory)
                elif 0 == choice:
                    break
            except FileNotFoundError:
                Error.printline('[ERROR|pdf]: File unavailable.\n')
    elif len(file_list) == 1:
        print(f'[SUCCESS]: {len(file_list)} file found for {filename}.')
        choice = int(input('Lex:\\User\\command\\pdf\\{}\\choice|return[0]> '.format(filename)))
        for file in file_list:
            try:
                if choice == file_list.index(file) + 1:
                    directory = (os.path.join(file_root, file))
                    return os.startfile(directory)
                elif 0 == choice:
                    break
            except FileNotFoundError:
                Error.printline('[ERROR|pdf]: File unavailable.\n')
    else:
        Error.printline('[ERROR|pdf]: 0 file found.\n')


def portable_network_graphics(filename):
    file_list = []
    global file_root, directory, name
    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
            # for specific file type
            if name.endswith('.PNG'):
                if filename in name.lower():
                    file_list.append(name)
                    print('\n'f'Found in: {root}')
                    print((len(file_list)), ')', name)
                    file_root = root
    if len(file_list) > 1:
        print('\n'f'[SUCCESS]: {len(file_list)} files found for {filename}.')
        choice = int(input('Lex:\\User\\command\\PNG\\{}\\choice|return[0]> '.format(filename)))
        for file in file_list:
            try:
                if choice == file_list.index(file) + 1:
                    directory = (os.path.join(file_root, file))
                    return os.startfile(directory)
                elif 0 == choice:
                    break
            except FileNotFoundError:
                Error.printline('[ERROR|PNG]: File unavailable.\n')
    elif len(file_list) == 1:
        print(f'[SUCCESS]: {len(file_list)} file found for {filename}.')
        choice = int(input('Lex:\\User\\command\\PNG\\{}\\choice|return[0]> '.format(filename)))
        for file in file_list:
            try:
                if choice == file_list.index(file) + 1:
                    directory = (os.path.join(file_root, file))
                    return os.startfile(directory)
                elif 0 == choice:
                    break
            except FileNotFoundError:
                Error.printline('[ERROR|PNG]: File unavailable.\n')
    else:
        Error.printline('[ERROR|PNG]: 0 file found.\n')


def locate():
    filetype = str(input('Lex:\\User\\command\\Filetype> ')).lower()
    if 'docx' in filetype:
        filename = str(input('Lex:\\User\\command\\docx\\Filename> '))
        word(filename)
    elif 'pptx' in filetype:
        filename = str(input('Lex:\\User\\command\\pptx\\Filename> '))
        powerpoint(filename)
    elif 'pdf' in filetype:
        filename = str(input('Lex:\\User\\command\\pdf\\Filename> '))
        portable_document_format(filename)
    elif 'png' in filetype:
        filename = str(input('Lex:\\User\\command\\PNG\\Filename> '))
        portable_network_graphics(filename)
    elif '-exit' in filetype:
        exit()
    else:
        Error.printline('[ERROR]: Filetype unavailable.\n')
