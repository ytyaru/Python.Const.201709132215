class _const:
    class ConstError(TypeError): pass
    def __setattr__(self,name,value):
#        print(dir(self.__dict__))
#        if self.__dict__.has_key(name):
        if name in self.__dict__.keys():
#            raise(self.ConstError, "Can't rebind const(%s)"%name)
            raise self.ConstError('readonly。再代入禁止。')
        self.__dict__[name]=value
import sys
sys.modules[__name__]=_const()
