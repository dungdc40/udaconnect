# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: location.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0elocation.proto\"l\n\x0fLocationMessage\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\tperson_id\x18\x02 \x01(\x05\x12\x11\n\tlongitude\x18\x03 \x01(\t\x12\x10\n\x08latitude\x18\x04 \x01(\t\x12\x15\n\rcreation_time\x18\x05 \x01(\t\"\x07\n\x05\x45mpty\":\n\x13LocationMessageList\x12#\n\tlocations\x18\x01 \x03(\x0b\x32\x10.LocationMessage2j\n\x0fLocationService\x12,\n\x06\x43reate\x12\x10.LocationMessage\x1a\x10.LocationMessage\x12)\n\x03Get\x12\x10.LocationMessage\x1a\x10.LocationMessageb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'location_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LOCATIONMESSAGE._serialized_start=18
  _LOCATIONMESSAGE._serialized_end=126
  _EMPTY._serialized_start=128
  _EMPTY._serialized_end=135
  _LOCATIONMESSAGELIST._serialized_start=137
  _LOCATIONMESSAGELIST._serialized_end=195
  _LOCATIONSERVICE._serialized_start=197
  _LOCATIONSERVICE._serialized_end=303
# @@protoc_insertion_point(module_scope)