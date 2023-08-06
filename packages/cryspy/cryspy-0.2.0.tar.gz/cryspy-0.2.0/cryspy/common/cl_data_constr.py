import warnings
from cryspy.common.cl_item_constr import ItemConstr
from cryspy.common.cl_loop_constr import LoopConstr
from typing import List, Tuple
from pycifstar import Data


class DataConstr(object):
    def __init__(self, data_name="",
                 mandatory_classes = None,
                 optional_classes = None,
                 internal_classes = None):
        super(DataConstr, self).__init__()
        setattr(self, "__data_name", data_name)
        if mandatory_classes is None: mandatory_classes = []
        if optional_classes is None: optional_classes = []
        if internal_classes is None: internal_classes = []
        setattr(self, "__mandatory_classes", mandatory_classes)
        setattr(self, "__optional_classes", optional_classes)
        setattr(self, "__internal_classes", internal_classes)

        setattr(self, "__mandatory_objs", [])
        setattr(self, "__optional_objs", [])
        setattr(self, "__internal_objs", [])

    def __repr__(self) -> str:
        ls_out = [f"{type(self).__name__:}: ", f"{str(self):}"]
        return "\n".join(ls_out)

    def __str__(self) -> str:
        ls_out = []
        ls_out.append("Mandatory classes:")
        ls_out.extend([str(_) for _ in self.mandatory_classes])
        ls_out.append("\nOptional classes:")
        ls_out.extend([str(_) for _ in self.optional_classes])
        ls_out.append("\nMandatory objects:")
        ls_out.extend([str(_)+"\n" for _ in self.mandatory_objs])
        ls_out.append("\nOptional objects:")
        ls_out.extend([str(_)+"\n" for _ in self.optional_objs])
        ls_out.append("\nInternal objects:")
        ls_out.extend([str(_)+"\n" for _ in self.internal_objs])
        return "\n".join(ls_out)

    def to_cif(self, separator="_", flag=False, flag_minimal=True) -> str: 
        """
Print information about object in string in STAR format

Args:
    prefix: prefix in front of label of attribute
    separator: separator between prefix and attribute ("_" or ".")
    flag: for undefined attribute "." will be printed
    flag_minimal if it's True the minimal set of object will be printed

Returns:
    A string in STAR/CIF format
        """
        ls_out = []
        ls_out.append(f"data_{self.data_name:}\n")
        l_obj = self.mandatory_objs + self.optional_objs
        l_s_item_const = [_obj.to_cif(separator=separator, flag=flag, flag_minimal=flag_minimal)+"\n"
                             for _obj in l_obj if isinstance(_obj, ItemConstr)]
        l_s_loop_const = [_obj.to_cif(separator=separator, flag=flag, flag_minimal=flag_minimal)+"\n"
                             for _obj in l_obj if isinstance(_obj, LoopConstr)]
        if l_s_loop_const != []:
            n_max_loop = max([len(_) for _ in l_s_loop_const])
            if n_max_loop < 1000:
                n_max_loop = 1000
        else:
            n_max_loop = 10000
        l_n_max_item = [len(_) for _ in l_s_item_const]

        ls_out.extend([_1 for _1, _2 in zip(l_s_item_const, l_n_max_item) if _2 <= n_max_loop])
        ls_out.extend([_ for _ in l_s_loop_const])
        ls_out.extend([_1 for _1, _2 in zip(l_s_item_const, l_n_max_item) if _2 > n_max_loop])
        return "\n".join(ls_out)

    @classmethod
    def from_cif(cls, string: str):
        cif_data = Data()
        flag = cif_data.take_from_string(string)

        cif_items = cif_data.items
        cif_loops = cif_data.loops

        mandatory_objs = []
        optional_objs = []

        flag = True
        for _cls in cls.MANDATORY_CLASSES:
            flag = False
            if issubclass(_cls, ItemConstr):
                prefix_cls = _cls.PREFIX
                if cif_items.is_prefix(prefix_cls):
                    cif_items_prefix = cif_items[prefix_cls]
                    cif_string = str(cif_items_prefix)
                    _obj_prefix = _cls.from_cif(cif_string)
                    mandatory_objs.append(_obj_prefix)
                    flag = True
            elif issubclass(_cls, LoopConstr):
                prefix_cls = _cls.ITEM_CLASS.PREFIX
                for cif_loop in cif_loops:
                    if cif_loop.is_prefix("_"+prefix_cls):
                        cif_string = str(cif_loop)
                        _obj_prefix = _cls.from_cif(cif_string)
                        mandatory_objs.extend(_obj_prefix)
                        flag = True
            if not(flag):
                #warnings.warn(f"unknown class type : '{_cls:}'", UserWarning, stacklevel=2)
                break
        
        if not(flag):
            return None

        for _cls in cls.OPTIONAL_CLASSES:
            if issubclass(_cls, ItemConstr):
                prefix_cls = _cls.PREFIX
                if cif_items.is_prefix(prefix_cls):
                    cif_items_prefix = cif_items[prefix_cls]
                    cif_string = str(cif_items_prefix)
                    _obj_prefix = _cls.from_cif(cif_string)
                    optional_objs.append(_obj_prefix)
            elif issubclass(_cls, LoopConstr):
                prefix_cls = _cls.ITEM_CLASS.PREFIX
                for cif_loop in cif_loops:
                    if cif_loop.is_prefix("_"+prefix_cls):
                        cif_string = str(cif_loop)
                        _obj_prefix = _cls.from_cif(cif_string)
                        optional_objs.extend(_obj_prefix)
            else:
                warnings.warn(f"unknown class type : '{_cls:}'", UserWarning, stacklevel=2)
        data_name = cif_data.name
        _obj = cls(data_name=data_name)
        _obj.mandatory_objs = mandatory_objs
        _obj.optional_objs = optional_objs
        
        return _obj


    @property
    def data_name(self) -> str:
        return getattr(self, "__data_name")
    @data_name.setter
    def data_name(self, x) -> str:
        if x is None:
            x_in = ""
        else:
            x_in = str(x)
        setattr(self, "__data_name", x_in)

    @property
    def mandatory_classes(self):
        return getattr(self, "__mandatory_classes")
    @property
    def optional_classes(self):
        return getattr(self, "__optional_classes")

    @property
    def mandatory_objs(self):
        return getattr(self, "__mandatory_objs")
    @mandatory_objs.setter
    def mandatory_objs(self, l_x: List) -> str:
        l_x_in = []
        for x in l_x:
            if any([isinstance(x, _cls) for _cls in self.mandatory_classes]):
                l_x_in.append(x)
        return setattr(self, "__mandatory_objs", l_x_in)

    @property
    def optional_objs(self) -> str:
        return getattr(self, "__optional_objs")
    @optional_objs.setter
    def optional_objs(self, l_x: List) -> str:
        l_x_in = []
        for x in l_x:
            if any([isinstance(x, _cls) for _cls in self.optional_classes]):
                l_x_in.append(x)
        return setattr(self, "__optional_objs", l_x_in)

    @property
    def internal_objs(self) -> str:
        return getattr(self, "__internal_objs")

    @property
    def remove_internal_objs(self):
        l_objs = self.internal_objs
        for _objs in l_objs:
            l_objs.remove(_objs)

    def is_class(self,  _cls) -> bool:
        flag = any([isinstance(_obj, _cls) for _obj in 
                  (self.mandatory_objs + self.optional_objs + self.internal_objs)])
        return flag

    def __getitem__(self, _cls):
        l_res = []
        if self.is_class(_cls):
            for _obj in (self.mandatory_objs + self.optional_objs + self.internal_objs):
                if isinstance(_obj, _cls):
                    l_res.append(_obj)
        return tuple(l_res)
    @property
    def is_defined(self):
        flag_1 = all([self.is_class(_cls) for _cls in getattr(self, "mandatory_classes")])
        flag_2 = all([_obj.is_defined for _obj in getattr(self, "mandatory_objs")])
        flag = flag_1 & flag_2
        return flag
    @property
    def form_object(self):
        return True


    @property
    def is_variable(self) -> bool:
        """
Output: True if there is any refined parameter
        """
        res = any([_obj.is_variable for _obj in self.mandatory_objs] +
                  [_obj.is_variable for _obj in self.optional_objs])
        return res
        
    def get_variables(self) -> List:
        """
Output: the list of the refined parameters
        """
        l_variable = []
        for _obj in self.mandatory_objs:
            l_variable.extend(_obj.get_variables())
        for _obj in self.optional_objs:
            l_variable.extend(_obj.get_variables())
        return l_variable
       

    def _show_message(self, s_out: str):
        warnings.warn("***  Error ***\n"+s_out, UserWarning, stacklevel=2)


    #def __getattr__(self, attr):
    #    if attr in self.__mandatory_attribute:
    #        res = [getattr(_item, attr) for _item in self.__item]
    #    elif attr in self.__optional_attribute:
    #        res = [getattr(_item, attr) for _item in self.__item]
    #    elif attr in self.__internal_attribute:
    #        res = [getattr(_item, attr) for _item in self.__item]
    #    else:
    #        res = None
    #        print(f"Attribute '{attr:}' is not defined")
    #    return res

