# このソフトウェアについて

Pythonでreadonlyにする方法。

## 参考

* https://sites.google.com/site/michinobumaeda/programming/pythonconst

丸パクリした。感謝。

## 前回まで

* https://github.com/ytyaru/Python.MusicTheory.Chord.Triad.201709071957
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709131752
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709131811
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709132015
* https://github.com/ytyaru/Python.MusicTheory.Pitch.201709132126

# 実行

```sh
$ python 0.py
```

# ポイント

const.py
```python
class _const:
    class ConstError(TypeError): pass
    def __setattr__(self,name,value):
        if name in self.__dict__.keys():
            raise self.ConstError('readonly。再代入禁止。')
        self.__dict__[name]=value
import sys
sys.modules[__name__]=_const()
```

objectの`__setattr__`を継承する。属性が既存なら例外発生させる。

0.py
```python
import const
const.test = "Test1"
const.test = "Test2"
```

本来`import const`で参照できるのは`const.py`モジュールであるが、`sys.modules[__name__]=_const()`により`const`モジュールでなく`_const`クラスが参照されるようになる。これにより、`const.test`はモジュール変数でなく、クラス変数として扱われる。クラス変数に代入されると`__setattr__`が実行される。

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [pyenv](https://github.com/pylangstudy/201705/blob/master/27/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83%E3%82%92%E7%94%A8%E6%84%8F%E3%81%99%E3%82%8B.md) 1.0.10
    * Python 3.6.1

# ライセンス

* https://sites.google.com/site/michinobumaeda/programming/pythonconst

Library|License|Copyright
-------|-------|---------
http://code.activestate.com/recipes/65207/|[PSF](https://ja.osdn.net/projects/opensource/wiki/licenses%2FPython_Software_Foundation_License)|Copyright (c) 2001 Python Software Foundation; All Rights Reserved
