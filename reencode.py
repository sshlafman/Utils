def reencode_file(srcfilename, trgfilename, chunksize=1024*1024, 
                  srcencoding='866', trgencoding='utf8'):
    "Re-encodes source file's content and writes it to target file"
    #print('Re-encoding', srcfilename.encode('utf-8'), 'from', srcencoding, 'to', trgencoding+'.', 
    #     'Saving as', trgfilename.encode('utf-8'))
    with open(srcfilename, 'rb') as srcfile, \
           open(trgfilename, 'wb') as trgfile:
        chunk = srcfile.read(chunksize)
        while chunk:
            trgfile.write(chunk.decode(srcencoding).encode(trgencoding))
            chunk = srcfile.read(chunksize)
    
def reencode_files_recursively(rootdir, removeSrcFiles=False):
    import os
    import fnmatch
    for (thisDir, subsHere, filesHere) in os.walk(rootdir):
        for filename in filesHere:
            if not fnmatch.fnmatch(filename, '*.*'):
                srcFileFullName = os.path.join(thisDir, filename)
                trgFileFullName = os.path.join(thisDir, filename + '.txt')
                reencode_file(srcFileFullName, trgFileFullName)
                if removeSrcFiles:
                    os.remove(srcFileFullName)
                
if __name__ == '__main__':
    import sys, os
    rootdir = sys.argv[1]  if len(sys.argv) > 1 else os.getcwd() 
    reencode_files_recursively(rootdir, removeSrcFiles=True)
                
                