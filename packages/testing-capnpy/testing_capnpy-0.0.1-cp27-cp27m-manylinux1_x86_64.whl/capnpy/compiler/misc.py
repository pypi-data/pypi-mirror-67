from capnpy.schema import Value, Type
from capnpy.annotate import TextType

@Type.__extend__
class Type:

    def compile_name(self, m, prefix=''):
        if self.is_builtin():
            return '_Types.%s' % self.which()
        elif self.is_struct() or self.is_enum():
            node = self.get_node(m)
            return node.compile_name(m, prefix)
        else:
            raise NotImplementedError

    def runtime_name(self, m):
        if self.is_builtin():
            return '_Types.%s' % self.which()
        elif self.is_struct() or self.is_enum():
            node = self.get_node(m)
            return node.runtime_name(m)
        else:
            raise NotImplementedError

    def _get_prebuilt_compile_name(self, options):
        if self.is_text():
            # '_text_bytes' or '_text_unicode'
            return '_text_%s' % str(options.text_type)
        else:
            # e.g. '_int16'
            return '_%s' % self.which()

    def list_item_type(self, m, options):
        """
        This is the compile-time equivalent of capnpy.list.ItemType.from_type
        """
        if m.pyx:
            # on Cython, try to use the prebuilt ItemType when possible
            if self.is_builtin():
                prebuilt_compile_name = self._get_prebuilt_compile_name(options)
                use_prebuilt_item_type = True
            elif self.is_struct() or self.is_enum():
                node = self.get_node(m)
                prebuilt_compile_name = self.compile_name(m, prefix='_')
                use_prebuilt_item_type = not node.is_imported(m)
            else:
                use_prebuilt_item_type = False
        else:
            if self.is_struct() or self.is_enum():
                use_prebuilt_item_type = True
                prebuilt_compile_name = self.compile_name(m, prefix='_')
            else:
                use_prebuilt_item_type = False

        if use_prebuilt_item_type:
            # e.g. _int16_list_item_type
            return '%s_list_item_type' % prebuilt_compile_name
        elif self.is_list():
            inner_item_type = self.list.elementType.list_item_type(m, options)
            return '_ListItemType(%s)' % inner_item_type
        elif self.is_primitive():
            return '_PrimitiveItemType(_Types.%s)' % self.which()
        elif self.is_bool():
            return '_BoolItemType()'
        elif self.is_text() and options.text_type == TextType.bytes:
            return '_TextItemType(_Types.text)'
        elif self.is_text() and options.text_type == TextType.unicode:
            return '_TextUnicodeItemType(_Types.text)'
        elif self.is_data():
            return '_TextItemType(_Types.data)'
        elif self.is_void():
            return '_VoidItemType()'
        elif self.is_struct():
            return '_StructItemType(%s)' % self.compile_name(m)
        elif self.is_enum():
            return '_EnumItemType(%s)' % self.compile_name(m)
        else:
            raise NotImplementedError


@Value.__extend__
class Value:

    def as_pyobj(self):
        val_type = str(self.which())
        return getattr(self, val_type)

