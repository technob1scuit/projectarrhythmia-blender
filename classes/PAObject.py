from __future__ import annotations
from ..util import genPAid
import re

# base class for actual in-game objects
class PAObject():

    # stores data that can then be manipulated into the forms required for different saving formats
    _id: str = None # object unique id

    _prefabID: str = None # id of the prefab the object came from if it did
    _prefabImmediateID: str = None # id shared by objects of an instance of an expanded prefab

    _parentType: dict[str, bool] = { # what to inherit from the parent
        "pos": True,
        "sca": False,
        "rot": True 
    }
    _parentOffset: dict[str, int] = { # parent offset - pos, sc
        "pos": 0,
        "sca": 0,
        "rot": 0
    }

    _parentID: str = None


    # --------------------------------------------------------
    # stuff for ls format files
    # --------------------------------------------------------
    @property
    def ls_id(self):
        return self.id
    
    # --------------------------------------------------------
    @property
    def ls_pid(self):
        return self.prefabID
    
    # --------------------------------------------------------
    @property
    def ls_piid(self):
        return self.prefabImmediateID
    
    # --------------------------------------------------------
    @property
    def ls_pt(self):
        return f"{'1' if self.inheritPosition else '0'}{'1' if self.inheritScale else '0'}{'1' if self.inheritRotation else '0'}"


    # --------------------------------------------------------
    # stuff for vg format files
    # --------------------------------------------------------
    @property
    def vg_id(self):
        return self.id

    
    # --------------------------------------------------------
    #   id
    # --------------------------------------------------------
    @property
    def id(self) -> str:
        return str(self._id)

    @id.setter
    def id(self, a: str):
        pattern = re.compile("^[A-Za-z0-9~!@#$%^&*_+{}|:<>?,./;'\[\]▓▒░▐▆▉☰☱☲☳☴☵☶☷►▼◄▬▩▨▧▦▥▤▣▢□■¤ÿòèµ¶™ßÃ®¾ð¥œ⁕(◠‿◠✿)]{16}$", "g")
        if pattern.match(a) == False or isinstance(a, str) == False:
            raise ValueError("Invalid value passed in for the ID of a PAObject.")
        else: self._id = a
    
    # --------------------------------------------------------
    #   prefab id
    # --------------------------------------------------------
    @property
    def prefabID(self) -> str:
        return str(self._prefabID)
    
    @prefabID.setter
    def prefabID(self, a: str):
        pattern = re.compile("^[A-Za-z0-9~!@#$%^&*_+{}|:<>?,./;'\[\]▓▒░▐▆▉☰☱☲☳☴☵☶☷►▼◄▬▩▨▧▦▥▤▣▢□■¤ÿòèµ¶™ßÃ®¾ð¥œ⁕(◠‿◠✿)]{16}$", "g")
        if pattern.match(a) == False or isinstance(a, str) == False:
            raise ValueError("Invalid value passed in for the prefab ID of a PAObject.")
        else: self._prefabID = a
    
    # --------------------------------------------------------
    #   prefab immediate id
    # --------------------------------------------------------
    @property
    def prefabImmediateID(self) -> str:
        return str(self._prefabImmediateID)
    
    @prefabImmediateID.setter
    def prefamImmediateID(self, a: str):
        pattern = re.compile("^[A-Za-z0-9~!@#$%^&*_+{}|:<>?,./;'\[\]▓▒░▐▆▉☰☱☲☳☴☵☶☷►▼◄▬▩▨▧▦▥▤▣▢□■¤ÿòèµ¶™ßÃ®¾ð¥œ⁕(◠‿◠✿)]{16}$", "g")
        if pattern.match(a) == False or isinstance(a, str) == False:
            raise ValueError("Invalid value passed in for the prefab immediate ID of a PAObject.")
        else: self._prefabImmediateID = a

    # --------------------------------------------------------
    #   parent type
    # --------------------------------------------------------
    @property
    def inheritPosition(self):
        return self._parentType["pos"]
    
    @inheritPosition.setter
    def inheritPosition(self, a: bool):
        if isinstance(a, bool) == False:
            raise ValueError("Invalid value passed in for transform inheritance setting.")
        else: self._parentType["pos"] = a
    
    @property
    def inheritScale(self):
        return self._parentType["sca"]
    
    @inheritScale.setter
    def inheritScale(self, a: bool):
        if isinstance(a, bool) == False:
            raise ValueError("Invalid value passed in for transform inheritance setting.")
        else: self._parentType["sca"] = a
    
    @property
    def inheritRotation(self):
        return self._parentType["rot"]
    
    @inheritRotation.setter
    def inheritRotation(self, a: bool):
        if isinstance(a, bool) == False:
            raise ValueError("Invalid value passed in for transform inheritance setting.")
        else: self._parentType["rot"] = a

    # --------------------------------------------------------
    #   parent offset
    # --------------------------------------------------------

    def __init__(self) -> None:
        self._id = genPAid()