




class DataStoreThing ( ):

    def __init__ ( self ):

        self.recSize = 0
        self.headerSize = 0
        self.maxRecs = 0
        self.fieName = None

        self.fd = None

        return

    def __str__ ( self ):

        return ''
    
    def filename ( self, name : str ):

        self.fileName = name

        return self

    def create ( self, recSize: int = 32, maxRecs:int = 256, headerSize: int = 0 ):

        with open ( self.fileName, 'x+b' ) as fd:

            fd.write ( recSize.to_bytes ( 2, 'big' ) )
            fd.write ( maxRecs.to_bytes ( 2, 'big' ) )
            fd.write ( headerSize.to_bytes ( 2, 'big' ) )

            fd.close ( )

        return self


    def close ( self ):

        if self.fd != None:

            return

        self.fd.close ( )

        self.fd = None

        self.recSize = 0
        self.maxRecs = 0
        self.headerSize = 0

        return

    def open ( self ):

        if self.fd != None:

            return self

        fd = open ( self.fileName, "r+b" )

        self.fd = fd

        self.fd.seek ( 0 )

        self.recSize = int.from_bytes ( self.fd.read ( 2 ), 'big' )
        self.maxRecs = int.from_bytes ( self.fd.read ( 2 ), 'big' )
        self.headerSize = int.from_bytes ( self.fd.read ( 2 ), 'big' )

        print ( "r={0} m={1} h={2}".format ( self.recSize, self.maxRecs, self.headerSize ) )

        return self


    def __getitem__ ( self, key ):

        return self.read ( key )

    def read ( self, pos: int ):

        if self.fd == None:

            raise Exception ( 'data file not open' )

        if pos < 0:

            raise Exception ( 'subscript out of range' )


        print ( 'seeking to {0}'.format ( self.headerSize + (pos+self.recSize) ) )

        self.fd.seek ( 6 + self.headerSize + ( pos * self.recSize ) )

        return self.fd.read ( self.recSize )



    def __setitem__ ( self, key, value ) :

        return self.write ( key, value )


    def write ( self, pos: int, rec: bytes ):

        if self.fd == None:

            raise Exception ( 'data file not open' )

        if pos < 0:

            raise Exception ( 'subscript out of range' )

        self.fd.seek ( 6 + self.headerSize + ( pos * self.recSize ) )

        self.fd.write ( rec[0:self.recSize] )

        return self


    def setHeader ( self, data ):

        self.fd.seek ( 6 )

        self.fd.write ( data[0: self.headerSize ] )

        return self


    def getHeader ( self ):

        self.fd.seek ( 6 )

        header = self.fd.read ( self.headerSize )

        return header
