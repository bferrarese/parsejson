import unohelper
from org.openoffice.addin.sample import Xjsonparse
from com.sun.star.sheet import XAddIn
from com.sun.star.lang import XLocalizable, XServiceName, Locale
import urllib.request
import json

class jsonparse( unohelper.Base, Xjsonparse,  XAddIn, XServiceName ):
    def __init__( self, ctx ):
        self.ctx = ctx
        self.locale = Locale("ja","JP", "" )

    def getServiceName( self ):
        return "JSONPARSE Function"

    def setLocale( self, locale ):
        self.locale = locale

    def getLocale( self ):
        return self.locale

    def getProgrammaticFuntionName( self, aDisplayName ):
        return aDisplayName

    def getDisplayFunctionName( self, aProgrammaticName ):
        return aProgrammaticName

    def getFunctionDescription( self , aProgrammaticName ):
        return "Parse JSON Function"

    def getArgumentDescription( self, aProgrammaticFunctionName, nArgument ):
        return "Get String"
    
    def getProgrammaticCategoryName( self, aProgrammaticFunctionName ):
        return "Add-In"

    def getDisplayArgumentName( self, aProgrammaticFunctionName, nArgument ):
        return "JSON"
    
    def getArgumentDescription( self, aProgrammaticFunctionName, nArgument ):
        return "Pattern. example (results1.0.address1)"
    
    def getProgrammaticCategoryName( self, aProgrammaticFunctionName ):
        return "Add-In"

    def getDisplayArgumentName( self, aProgrammaticFunctionName, nArgument ):
        return "Pattern"

    def jsonparse(self,data,tuple)->str:
        """
        Parse JSON Data
        :rtype:object
        :param:dict:data
        :return:data
        """
        for key in tuple:
            data=data[key]
        
        return data
