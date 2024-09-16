




def __main ( _argv, _argc ):

    d1 = Storage ( )

    d1.filename ( './fruits.ds' )

    if not os.path.exists ( './fruits.ds' ):

        d1.create ( 16, 32, 64 )

    d1.open ( )

    print ( 'The header size is:  %d' % d1.headerSize )
    print ( 'Record length is:    %d' % d1.recSize )
    print ( 'Maximum records is:  %d' % d1.maxRecs )
    print ( 'Largest size(bytes): %d' % ( d1.headerSize + (d1.maxRecs * d1.recSize) + 6 ) )

    d1[0] = b'tea bags & milk\0'

    d1.close ( )

    return 0

    '''
    d1.setHeader ( b'0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF' )

    
    d1.write ( 0, b'grape' )
    d1.write ( 1, b'apple' )
    d1.write ( 2, b'kiwi' )
    d1.write ( 3, b'orange' )
    d1.write ( 4, b'pear' )
    d1.write ( 5, b'banana' )
    d1.write ( 6, b'cherry' )
    d1.write ( 7, b'lemon' )
    d1.write ( 8, b'melon' )
    d1.write ( 9, b'raspberry' )
    
    d1[5] = b'bangers and mash'
    '''

    '''
    d1.write ( 10, b'peach' )
    d1.write ( 11, b'mango' )
    d1.write ( 12, b'guava' )
    d1.write ( 13, b'gooseberry' )
    d1.write ( 14, b'quince' )
    d1.write ( 15, b'rhubarb' )
    d1.write ( 16, b'pineapple' )
    d1.write ( 17, b'blackberry' )
    d1.write ( 18, b'apricote' )
    d1.write ( 19, b'durian' )
    '''

    pos = 0

    while ( True ):

        if len ( d1[ pos ] ) == 0:

            break

        buf = d1[ pos ].decode ( 'utf-8' )

        print ( f'{pos} = {buf}' )

        pos += 1


    hdr = d1.getHeader ( )

    print ( hdr.decode ( 'utf-8' ) )


    d1.close ( )

    return 0




if __name__ == '__main__':

    import sys
    import os

    from ds.DataStore import DataStoreThing as Storage

    exit ( __main ( sys.argv, len ( sys.argv ) ) )

