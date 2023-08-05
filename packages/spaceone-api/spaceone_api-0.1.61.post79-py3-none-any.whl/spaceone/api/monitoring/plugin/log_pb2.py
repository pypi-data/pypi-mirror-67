# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/monitoring/plugin/log.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spaceone.api.core.v1 import plugin_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_plugin__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='spaceone/api/monitoring/plugin/log.proto',
  package='spaceone.api.monitoring.plugin',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n(spaceone/api/monitoring/plugin/log.proto\x12\x1espaceone.api.monitoring.plugin\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\x1a!spaceone/api/core/v1/plugin.proto\"!\n\x04Sort\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\x08\"\xb6\x02\n\nLogRequest\x12(\n\x07options\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12,\n\x0bsecret_data\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\'\n\x06\x66ilter\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x10\n\x08resource\x18\x04 \x01(\t\x12)\n\x05start\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x03\x65nd\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x04sort\x18\x07 \x01(\x0b\x32$.spaceone.api.monitoring.plugin.Sort\x12\r\n\x05limit\x18\x08 \x01(\x05\"4\n\x08LogsInfo\x12(\n\x04logs\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.ListValue\"\x9a\x01\n\x12PluginLogsResponse\x12\x15\n\rresource_type\x18\x01 \x01(\t\x12\x33\n\x07\x61\x63tions\x18\x02 \x03(\x0b\x32\".spaceone.api.core.v1.PluginAction\x12\x38\n\x06result\x18\x03 \x01(\x0b\x32(.spaceone.api.monitoring.plugin.LogsInfo2q\n\x03Log\x12j\n\x04list\x12*.spaceone.api.monitoring.plugin.LogRequest\x1a\x32.spaceone.api.monitoring.plugin.PluginLogsResponse\"\x00\x30\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,spaceone_dot_api_dot_core_dot_v1_dot_plugin__pb2.DESCRIPTOR,])




_SORT = _descriptor.Descriptor(
  name='Sort',
  full_name='spaceone.api.monitoring.plugin.Sort',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='spaceone.api.monitoring.plugin.Sort.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='desc', full_name='spaceone.api.monitoring.plugin.Sort.desc', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=204,
  serialized_end=237,
)


_LOGREQUEST = _descriptor.Descriptor(
  name='LogRequest',
  full_name='spaceone.api.monitoring.plugin.LogRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='options', full_name='spaceone.api.monitoring.plugin.LogRequest.options', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secret_data', full_name='spaceone.api.monitoring.plugin.LogRequest.secret_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='spaceone.api.monitoring.plugin.LogRequest.filter', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource', full_name='spaceone.api.monitoring.plugin.LogRequest.resource', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='spaceone.api.monitoring.plugin.LogRequest.start', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='spaceone.api.monitoring.plugin.LogRequest.end', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort', full_name='spaceone.api.monitoring.plugin.LogRequest.sort', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='spaceone.api.monitoring.plugin.LogRequest.limit', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=240,
  serialized_end=550,
)


_LOGSINFO = _descriptor.Descriptor(
  name='LogsInfo',
  full_name='spaceone.api.monitoring.plugin.LogsInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='logs', full_name='spaceone.api.monitoring.plugin.LogsInfo.logs', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=552,
  serialized_end=604,
)


_PLUGINLOGSRESPONSE = _descriptor.Descriptor(
  name='PluginLogsResponse',
  full_name='spaceone.api.monitoring.plugin.PluginLogsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_type', full_name='spaceone.api.monitoring.plugin.PluginLogsResponse.resource_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actions', full_name='spaceone.api.monitoring.plugin.PluginLogsResponse.actions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result', full_name='spaceone.api.monitoring.plugin.PluginLogsResponse.result', index=2,
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
  serialized_start=607,
  serialized_end=761,
)

_LOGREQUEST.fields_by_name['options'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_LOGREQUEST.fields_by_name['secret_data'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_LOGREQUEST.fields_by_name['filter'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_LOGREQUEST.fields_by_name['start'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LOGREQUEST.fields_by_name['end'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LOGREQUEST.fields_by_name['sort'].message_type = _SORT
_LOGSINFO.fields_by_name['logs'].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_PLUGINLOGSRESPONSE.fields_by_name['actions'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_plugin__pb2._PLUGINACTION
_PLUGINLOGSRESPONSE.fields_by_name['result'].message_type = _LOGSINFO
DESCRIPTOR.message_types_by_name['Sort'] = _SORT
DESCRIPTOR.message_types_by_name['LogRequest'] = _LOGREQUEST
DESCRIPTOR.message_types_by_name['LogsInfo'] = _LOGSINFO
DESCRIPTOR.message_types_by_name['PluginLogsResponse'] = _PLUGINLOGSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Sort = _reflection.GeneratedProtocolMessageType('Sort', (_message.Message,), {
  'DESCRIPTOR' : _SORT,
  '__module__' : 'spaceone.api.monitoring.plugin.log_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.monitoring.plugin.Sort)
  })
_sym_db.RegisterMessage(Sort)

LogRequest = _reflection.GeneratedProtocolMessageType('LogRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGREQUEST,
  '__module__' : 'spaceone.api.monitoring.plugin.log_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.monitoring.plugin.LogRequest)
  })
_sym_db.RegisterMessage(LogRequest)

LogsInfo = _reflection.GeneratedProtocolMessageType('LogsInfo', (_message.Message,), {
  'DESCRIPTOR' : _LOGSINFO,
  '__module__' : 'spaceone.api.monitoring.plugin.log_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.monitoring.plugin.LogsInfo)
  })
_sym_db.RegisterMessage(LogsInfo)

PluginLogsResponse = _reflection.GeneratedProtocolMessageType('PluginLogsResponse', (_message.Message,), {
  'DESCRIPTOR' : _PLUGINLOGSRESPONSE,
  '__module__' : 'spaceone.api.monitoring.plugin.log_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.monitoring.plugin.PluginLogsResponse)
  })
_sym_db.RegisterMessage(PluginLogsResponse)



_LOG = _descriptor.ServiceDescriptor(
  name='Log',
  full_name='spaceone.api.monitoring.plugin.Log',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=763,
  serialized_end=876,
  methods=[
  _descriptor.MethodDescriptor(
    name='list',
    full_name='spaceone.api.monitoring.plugin.Log.list',
    index=0,
    containing_service=None,
    input_type=_LOGREQUEST,
    output_type=_PLUGINLOGSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOG)

DESCRIPTOR.services_by_name['Log'] = _LOG

# @@protoc_insertion_point(module_scope)
