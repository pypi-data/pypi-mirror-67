from capnpy.struct_ import Struct
from capnpy.list import VoidItemType
from capnpy.schema import (Node, Node__Enum, Node__Const, Node__Annotation,
                           Enumerant)
from capnpy import annotate
from capnpy.compiler.util import as_identifier

# The implementation of each node is divided in three parts:
#     1. forward declaration
#     2. definition
#     3. reference as child
#
# They are slightly different in pyx or python mode. It is probably easier to
# explain by giving an example in each mode.
#
# PYTHON MODE
#
#     class Outer__Nested: pass  # forward declaration
#     class Outer: pass          # forward declaration
#
#     # definition of Outer__Nested
#     @Outer__Nested.__extend__
#     class Outer__Nested:
#         ...
#
#     # definition of Outer
#     @Outer.__extend__
#     class Outer:
#         ...
#         Nested = Outer__Nested # reference as child
#
# PYX MODE
#
#     cdef class Outer__Nested  # forward declaration
#     cdef class Outer          # forward declaration
#
#     # definition of Outer__Nested
#     cdef class Outer__Nested:
#         ...
#
#     # definition of Outer
#     cdef class Outer:
#         ...
#         Nested = Outer__Nested # reference as child


@Node.__extend__
class Node:

    def get_parent(self, m):
        if self.scopeId == 0:
            return None
        return m.allnodes[self.scopeId]

    def compute_options(self, m, parent_opt):
        m.compute_options_generic(self, parent_opt)
        opt = m.options(self)
        for child in m.children[self.id]:
            child.compute_options(m, opt)

    def is_nested(self, m):
        parent = self.get_parent(m)
        return parent.scopeId != 0

    def is_imported(self, m):
        node = self
        while node is not None:
            if node.is_file() and node != m.current_scope:
                return True
            node = node.get_parent(m)
        return False

    def shortname(self, m):
        name = self.displayName[self.displayNamePrefixLength:]
        if self.is_file():
            filename = as_identifier(self.displayName)
            return m.importnames[filename]
        return as_identifier(name)

    def _fullname(self, m, sep):
        parent = self.get_parent(m)
        if parent is None or parent == m.current_scope:
            return self.shortname(m)
        return '%s%s%s' % (parent._fullname(m, sep), sep, self.shortname(m))

    def compile_name(self, m, prefix=''):
        if self.is_imported(m):
            return self.runtime_name(m, sep='.' + prefix)
        return prefix + self._fullname(m, '_')

    def runtime_name(self, m, sep='.'):
        return self._fullname(m, sep)

    def emit_declaration(self, m):
        assert False, 'Unkown node type: %s' % self.which()

    def emit_definition(self, m):
        pass # do nothing by default

    def emit_reference_as_child(self, m):
        pass # do nothing by default


@Node__Annotation.__extend__
class Node__Annotation:

    def emit_declaration(self, m):
        ns = m.code.new_scope()
        ns.name = self.shortname(m)
        ns.id = self.id
        ns.targets_file = self.annotation.targetsFile
        ns.targets_const = self.annotation.targetsConst
        ns.targets_enum = self.annotation.targetsEnum
        ns.targets_enumerant = self.annotation.targetsEnumerant
        ns.targets_struct = self.annotation.targetsStruct
        ns.targets_field = self.annotation.targetsField
        ns.targets_union = self.annotation.targetsUnion
        ns.targets_group = self.annotation.targetsGroup
        ns.targets_interface = self.annotation.targetsInterface
        ns.targets_method = self.annotation.targetsMethod
        ns.targets_param = self.annotation.targetsParam
        ns.targets_annotation = self.annotation.targetsAnnotation
        ns.ww("""
            class {name}(object):
                __capnpy_id__ = {id:#x}
                targets_file = {targets_file}
                targets_const = {targets_const}
                targets_enum = {targets_enum}
                targets_enumerant = {targets_enumerant}
                targets_struct = {targets_struct}
                targets_field = {targets_field}
                targets_union = {targets_union}
                targets_group = {targets_group}
                targets_interface = {targets_interface}
                targets_method = {targets_method}
                targets_param = {targets_param}
                targets_annotation = {targets_annotation}
        """)


@Node__Const.__extend__
class Node__Const:

    def emit_declaration(self, m):
        pass

    def emit_reference_as_child(self, m):
        options = m.options(self)
        ns = m.code.new_scope()
        ns.varname = self.shortname(m)
        if self.const.type.is_struct():
            struct_type = m.allnodes[self.const.type.struct.typeId]
            clsname = struct_type.compile_name(m)
            val = self.const.value.struct.as_struct(Struct)
            if options.include_reflection_data:
                # the desired constant is already in the the _reflection_data
                # segment: reuse it to save RAM
                ns.constdecl = m.declare_const(clsname, val,
                                               segment='_reflection_data.request._seg')
            else:
                # we don't have reflection_data, so just create a new segment
                val = val.compact()
                ns.constdecl = m.declare_const(clsname, val)
        elif self.const.type.is_list():
            if not options.include_reflection_data:
                raise NotImplementedError("list constants if include_reflection_data == False")
            # we don't care about the precise item type here: we just need val
            # to inspect it's _offset, _size_tag and _item_count
            # attributes. So, we just use VoidItemType, which is unused since
            # we never access any item
            val = self.const.value.list.as_list(VoidItemType())
            item_type = self.const.type.list.elementType.list_item_type(m, options)
            ns.constdecl = self._declare_list_const(val, item_type)
        else:
            # for primitive types
            val = self.const.value.as_pyobj()
            ns.constdecl = repr(val)
        #
        ns.w('{varname} = {constdecl}')

    def _declare_list_const(self, val, item_type):
        segment = '_reflection_data.request._seg'
        s = '_List.from_buffer({seg}, {offset}, {size_tag}, {item_count}, {item_type})'
        return s.format(
            seg=segment,
            offset=val._offset,
            size_tag=val._size_tag,
            item_count=val._item_count,
            item_type=item_type)
