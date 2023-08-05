# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/inventory/v1/network_type.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spaceone.api.core.v1 import query_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_query__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='spaceone/api/inventory/v1/network_type.proto',
  package='spaceone.api.inventory.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n,spaceone/api/inventory/v1/network_type.proto\x12\x19spaceone.api.inventory.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\"b\n\x18\x43reateNetworkTypeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12%\n\x04tags\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\"{\n\x18UpdateNetworkTypeRequest\x12\x17\n\x0fnetwork_type_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tdomain_id\x18\x03 \x01(\t\x12%\n\x04tags\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\"@\n\x12NetworkTypeRequest\x12\x17\n\x0fnetwork_type_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"Q\n\x15GetNetworkTypeRequest\x12\x17\n\x0fnetwork_type_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x0c\n\x04only\x18\x03 \x03(\t\"x\n\x10NetworkTypeQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x17\n\x0fnetwork_type_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x11\n\tdomain_id\x18\x04 \x01(\t\"\xa2\x01\n\x0fNetworkTypeInfo\x12\x17\n\x0fnetwork_type_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04tags\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x04 \x01(\t\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"d\n\x10NetworkTypesInfo\x12;\n\x07results\x18\x01 \x03(\x0b\x32*.spaceone.api.inventory.v1.NetworkTypeInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"_\n\x14NetworkTypeStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t2\x9c\x07\n\x0bNetworkType\x12\x8e\x01\n\x06\x63reate\x12\x33.spaceone.api.inventory.v1.CreateNetworkTypeRequest\x1a*.spaceone.api.inventory.v1.NetworkTypeInfo\"#\x82\xd3\xe4\x93\x02\x1d\"\x1b/inventory/v1/network-types\x12\x9f\x01\n\x06update\x12\x33.spaceone.api.inventory.v1.UpdateNetworkTypeRequest\x1a*.spaceone.api.inventory.v1.NetworkTypeInfo\"4\x82\xd3\xe4\x93\x02.\x1a,/inventory/v1/network-type/{network_type_id}\x12\x85\x01\n\x06\x64\x65lete\x12-.spaceone.api.inventory.v1.NetworkTypeRequest\x1a\x16.google.protobuf.Empty\"4\x82\xd3\xe4\x93\x02.*,/inventory/v1/network-type/{network_type_id}\x12\x99\x01\n\x03get\x12\x30.spaceone.api.inventory.v1.GetNetworkTypeRequest\x1a*.spaceone.api.inventory.v1.NetworkTypeInfo\"4\x82\xd3\xe4\x93\x02.\x12,/inventory/v1/network-type/{network_type_id}\x12\xab\x01\n\x04list\x12+.spaceone.api.inventory.v1.NetworkTypeQuery\x1a+.spaceone.api.inventory.v1.NetworkTypesInfo\"I\x82\xd3\xe4\x93\x02\x43\x12\x1b/inventory/v1/network-typesZ$\"\"/inventory/v1/network-types/search\x12\x87\x01\n\x04stat\x12/.spaceone.api.inventory.v1.NetworkTypeStatQuery\x1a$.spaceone.api.core.v1.StatisticsInfo\"(\x82\xd3\xe4\x93\x02\"\" /inventory/v1/network-types/statb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,spaceone_dot_api_dot_core_dot_v1_dot_query__pb2.DESCRIPTOR,])




_CREATENETWORKTYPEREQUEST = _descriptor.Descriptor(
  name='CreateNetworkTypeRequest',
  full_name='spaceone.api.inventory.v1.CreateNetworkTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='spaceone.api.inventory.v1.CreateNetworkTypeRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.inventory.v1.CreateNetworkTypeRequest.domain_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='spaceone.api.inventory.v1.CreateNetworkTypeRequest.tags', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=231,
  serialized_end=329,
)


_UPDATENETWORKTYPEREQUEST = _descriptor.Descriptor(
  name='UpdateNetworkTypeRequest',
  full_name='spaceone.api.inventory.v1.UpdateNetworkTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='network_type_id', full_name='spaceone.api.inventory.v1.UpdateNetworkTypeRequest.network_type_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='spaceone.api.inventory.v1.UpdateNetworkTypeRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.inventory.v1.UpdateNetworkTypeRequest.domain_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='spaceone.api.inventory.v1.UpdateNetworkTypeRequest.tags', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=331,
  serialized_end=454,
)


_NETWORKTYPEREQUEST = _descriptor.Descriptor(
  name='NetworkTypeRequest',
  full_name='spaceone.api.inventory.v1.NetworkTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='network_type_id', full_name='spaceone.api.inventory.v1.NetworkTypeRequest.network_type_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.inventory.v1.NetworkTypeRequest.domain_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=456,
  serialized_end=520,
)


_GETNETWORKTYPEREQUEST = _descriptor.Descriptor(
  name='GetNetworkTypeRequest',
  full_name='spaceone.api.inventory.v1.GetNetworkTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='network_type_id', full_name='spaceone.api.inventory.v1.GetNetworkTypeRequest.network_type_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.inventory.v1.GetNetworkTypeRequest.domain_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='only', full_name='spaceone.api.inventory.v1.GetNetworkTypeRequest.only', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=522,
  serialized_end=603,
)


_NETWORKTYPEQUERY = _descriptor.Descriptor(
  name='NetworkTypeQuery',
  full_name='spaceone.api.inventory.v1.NetworkTypeQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='spaceone.api.inventory.v1.NetworkTypeQuery.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network_type_id', full_name='spaceone.api.inventory.v1.NetworkTypeQuery.network_type_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='spaceone.api.inventory.v1.NetworkTypeQuery.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.inventory.v1.NetworkTypeQuery.domain_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=605,
  serialized_end=725,
)


_NETWORKTYPEINFO = _descriptor.Descriptor(
  name='NetworkTypeInfo',
  full_name='spaceone.api.inventory.v1.NetworkTypeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='network_type_id', full_name='spaceone.api.inventory.v1.NetworkTypeInfo.network_type_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='spaceone.api.inventory.v1.NetworkTypeInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='spaceone.api.inventory.v1.NetworkTypeInfo.tags', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.inventory.v1.NetworkTypeInfo.domain_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='spaceone.api.inventory.v1.NetworkTypeInfo.created_at', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=728,
  serialized_end=890,
)


_NETWORKTYPESINFO = _descriptor.Descriptor(
  name='NetworkTypesInfo',
  full_name='spaceone.api.inventory.v1.NetworkTypesInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='spaceone.api.inventory.v1.NetworkTypesInfo.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_count', full_name='spaceone.api.inventory.v1.NetworkTypesInfo.total_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=892,
  serialized_end=992,
)


_NETWORKTYPESTATQUERY = _descriptor.Descriptor(
  name='NetworkTypeStatQuery',
  full_name='spaceone.api.inventory.v1.NetworkTypeStatQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='spaceone.api.inventory.v1.NetworkTypeStatQuery.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.inventory.v1.NetworkTypeStatQuery.domain_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=994,
  serialized_end=1089,
)

_CREATENETWORKTYPEREQUEST.fields_by_name['tags'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_UPDATENETWORKTYPEREQUEST.fields_by_name['tags'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_NETWORKTYPEQUERY.fields_by_name['query'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_query__pb2._QUERY
_NETWORKTYPEINFO.fields_by_name['tags'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_NETWORKTYPEINFO.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_NETWORKTYPESINFO.fields_by_name['results'].message_type = _NETWORKTYPEINFO
_NETWORKTYPESTATQUERY.fields_by_name['query'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_query__pb2._STATISTICSQUERY
DESCRIPTOR.message_types_by_name['CreateNetworkTypeRequest'] = _CREATENETWORKTYPEREQUEST
DESCRIPTOR.message_types_by_name['UpdateNetworkTypeRequest'] = _UPDATENETWORKTYPEREQUEST
DESCRIPTOR.message_types_by_name['NetworkTypeRequest'] = _NETWORKTYPEREQUEST
DESCRIPTOR.message_types_by_name['GetNetworkTypeRequest'] = _GETNETWORKTYPEREQUEST
DESCRIPTOR.message_types_by_name['NetworkTypeQuery'] = _NETWORKTYPEQUERY
DESCRIPTOR.message_types_by_name['NetworkTypeInfo'] = _NETWORKTYPEINFO
DESCRIPTOR.message_types_by_name['NetworkTypesInfo'] = _NETWORKTYPESINFO
DESCRIPTOR.message_types_by_name['NetworkTypeStatQuery'] = _NETWORKTYPESTATQUERY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateNetworkTypeRequest = _reflection.GeneratedProtocolMessageType('CreateNetworkTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATENETWORKTYPEREQUEST,
  '__module__' : 'spaceone.api.inventory.v1.network_type_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.CreateNetworkTypeRequest)
  })
_sym_db.RegisterMessage(CreateNetworkTypeRequest)

UpdateNetworkTypeRequest = _reflection.GeneratedProtocolMessageType('UpdateNetworkTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATENETWORKTYPEREQUEST,
  '__module__' : 'spaceone.api.inventory.v1.network_type_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.UpdateNetworkTypeRequest)
  })
_sym_db.RegisterMessage(UpdateNetworkTypeRequest)

NetworkTypeRequest = _reflection.GeneratedProtocolMessageType('NetworkTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKTYPEREQUEST,
  '__module__' : 'spaceone.api.inventory.v1.network_type_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.NetworkTypeRequest)
  })
_sym_db.RegisterMessage(NetworkTypeRequest)

GetNetworkTypeRequest = _reflection.GeneratedProtocolMessageType('GetNetworkTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETNETWORKTYPEREQUEST,
  '__module__' : 'spaceone.api.inventory.v1.network_type_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.GetNetworkTypeRequest)
  })
_sym_db.RegisterMessage(GetNetworkTypeRequest)

NetworkTypeQuery = _reflection.GeneratedProtocolMessageType('NetworkTypeQuery', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKTYPEQUERY,
  '__module__' : 'spaceone.api.inventory.v1.network_type_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.NetworkTypeQuery)
  })
_sym_db.RegisterMessage(NetworkTypeQuery)

NetworkTypeInfo = _reflection.GeneratedProtocolMessageType('NetworkTypeInfo', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKTYPEINFO,
  '__module__' : 'spaceone.api.inventory.v1.network_type_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.NetworkTypeInfo)
  })
_sym_db.RegisterMessage(NetworkTypeInfo)

NetworkTypesInfo = _reflection.GeneratedProtocolMessageType('NetworkTypesInfo', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKTYPESINFO,
  '__module__' : 'spaceone.api.inventory.v1.network_type_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.NetworkTypesInfo)
  })
_sym_db.RegisterMessage(NetworkTypesInfo)

NetworkTypeStatQuery = _reflection.GeneratedProtocolMessageType('NetworkTypeStatQuery', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKTYPESTATQUERY,
  '__module__' : 'spaceone.api.inventory.v1.network_type_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.NetworkTypeStatQuery)
  })
_sym_db.RegisterMessage(NetworkTypeStatQuery)



_NETWORKTYPE = _descriptor.ServiceDescriptor(
  name='NetworkType',
  full_name='spaceone.api.inventory.v1.NetworkType',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1092,
  serialized_end=2016,
  methods=[
  _descriptor.MethodDescriptor(
    name='create',
    full_name='spaceone.api.inventory.v1.NetworkType.create',
    index=0,
    containing_service=None,
    input_type=_CREATENETWORKTYPEREQUEST,
    output_type=_NETWORKTYPEINFO,
    serialized_options=b'\202\323\344\223\002\035\"\033/inventory/v1/network-types',
  ),
  _descriptor.MethodDescriptor(
    name='update',
    full_name='spaceone.api.inventory.v1.NetworkType.update',
    index=1,
    containing_service=None,
    input_type=_UPDATENETWORKTYPEREQUEST,
    output_type=_NETWORKTYPEINFO,
    serialized_options=b'\202\323\344\223\002.\032,/inventory/v1/network-type/{network_type_id}',
  ),
  _descriptor.MethodDescriptor(
    name='delete',
    full_name='spaceone.api.inventory.v1.NetworkType.delete',
    index=2,
    containing_service=None,
    input_type=_NETWORKTYPEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002.*,/inventory/v1/network-type/{network_type_id}',
  ),
  _descriptor.MethodDescriptor(
    name='get',
    full_name='spaceone.api.inventory.v1.NetworkType.get',
    index=3,
    containing_service=None,
    input_type=_GETNETWORKTYPEREQUEST,
    output_type=_NETWORKTYPEINFO,
    serialized_options=b'\202\323\344\223\002.\022,/inventory/v1/network-type/{network_type_id}',
  ),
  _descriptor.MethodDescriptor(
    name='list',
    full_name='spaceone.api.inventory.v1.NetworkType.list',
    index=4,
    containing_service=None,
    input_type=_NETWORKTYPEQUERY,
    output_type=_NETWORKTYPESINFO,
    serialized_options=b'\202\323\344\223\002C\022\033/inventory/v1/network-typesZ$\"\"/inventory/v1/network-types/search',
  ),
  _descriptor.MethodDescriptor(
    name='stat',
    full_name='spaceone.api.inventory.v1.NetworkType.stat',
    index=5,
    containing_service=None,
    input_type=_NETWORKTYPESTATQUERY,
    output_type=spaceone_dot_api_dot_core_dot_v1_dot_query__pb2._STATISTICSINFO,
    serialized_options=b'\202\323\344\223\002\"\" /inventory/v1/network-types/stat',
  ),
])
_sym_db.RegisterServiceDescriptor(_NETWORKTYPE)

DESCRIPTOR.services_by_name['NetworkType'] = _NETWORKTYPE

# @@protoc_insertion_point(module_scope)
