# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_coordinates.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18object_coordinates.proto\x12\x07RpcDemo\"\xcb\x01\n\x0cPointStamped\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.RpcDemo.PointStamped.Header\x12\x30\n\x05point\x18\x02 \x01(\x0b\x32!.RpcDemo.PointStamped.Coordinates\x1a#\n\x0b\x43oordinates\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x1a\x36\n\x06Header\x12\x0b\n\x03seq\x18\x01 \x01(\r\x12\r\n\x05stamp\x18\x02 \x01(\x04\x12\x10\n\x08\x66rame_id\x18\x03 \x01(\t\"\x07\n\x05\x45mpty2O\n\x12\x63oordinatesService\x12\x39\n\x0egetCoordinates\x12\x0e.RpcDemo.Empty\x1a\x15.RpcDemo.PointStamped\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'object_coordinates_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _POINTSTAMPED._serialized_start=38
  _POINTSTAMPED._serialized_end=241
  _POINTSTAMPED_COORDINATES._serialized_start=150
  _POINTSTAMPED_COORDINATES._serialized_end=185
  _POINTSTAMPED_HEADER._serialized_start=187
  _POINTSTAMPED_HEADER._serialized_end=241
  _EMPTY._serialized_start=243
  _EMPTY._serialized_end=250
  _COORDINATESSERVICE._serialized_start=252
  _COORDINATESSERVICE._serialized_end=331
# @@protoc_insertion_point(module_scope)
