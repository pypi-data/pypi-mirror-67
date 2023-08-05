# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/inventory/v1/cloud_service_type.proto

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
  name='spaceone/api/inventory/v1/cloud_service_type.proto',
  package='spaceone.api.inventory.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n2spaceone/api/inventory/v1/cloud_service_type.proto\x12\x19spaceone.api.inventory.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\"\xda\x01\n\x18\x43reateServiceTypeRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08provider\x18\x02 \x01(\t\x12\r\n\x05group\x18\x03 \x01(\t\x12)\n\x08metadata\x18\x0b \x01(\x0b\x32\x17.google.protobuf.Struct\x12*\n\x06labels\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12%\n\x04tags\x18\r \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x15 \x01(\t\"\xcf\x01\n\x1dUpdateCloudServiceTypeRequest\x12\x1d\n\x15\x63loud_service_type_id\x18\x01 \x01(\t\x12)\n\x08metadata\x18\x0b \x01(\x0b\x32\x17.google.protobuf.Struct\x12*\n\x06labels\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.ListValue\x12%\n\x04tags\x18\r \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x15 \x01(\t\"`\n\x1ePinCloudServiceTypeDataRequest\x12\x1d\n\x15\x63loud_service_type_id\x18\x01 \x01(\t\x12\x0c\n\x04keys\x18\x02 \x03(\t\x12\x11\n\tdomain_id\x18\x03 \x01(\t\"K\n\x17\x43loudServiceTypeRequest\x12\x1d\n\x15\x63loud_service_type_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"\\\n\x1aGetCloudServiceTypeRequest\x12\x1d\n\x15\x63loud_service_type_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x0c\n\x04only\x18\x03 \x03(\t\"\xc9\x01\n\x15\x43loudServiceTypeQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x1d\n\x15\x63loud_service_type_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x10\n\x08provider\x18\x04 \x01(\t\x12\r\n\x05group\x18\x05 \x01(\t\x12#\n\x1binclude_cloud_service_count\x18\x06 \x01(\x08\x12\x11\n\tdomain_id\x18\x0b \x01(\t\"\x88\x03\n\x14\x43loudServiceTypeInfo\x12\x1d\n\x15\x63loud_service_type_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08provider\x18\x03 \x01(\t\x12\r\n\x05group\x18\x04 \x01(\t\x12)\n\x08metadata\x18\x0b \x01(\x0b\x32\x17.google.protobuf.Struct\x12%\n\x04tags\x18\x0c \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06labels\x18\r \x03(\t\x12\x30\n\x0f\x63ollection_info\x18\x0e \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x1b\n\x13\x63loud_service_count\x18\x0f \x01(\x05\x12\x11\n\tdomain_id\x18\x15 \x01(\t\x12.\n\ncreated_at\x18\x1f \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18  \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"n\n\x15\x43loudServiceTypesInfo\x12@\n\x07results\x18\x01 \x03(\x0b\x32/.spaceone.api.inventory.v1.CloudServiceTypeInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\"d\n\x19\x43loudServiceTypeStatQuery\x12\x34\n\x05query\x18\x01 \x01(\x0b\x32%.spaceone.api.core.v1.StatisticsQuery\x12\x11\n\tdomain_id\x18\x02 \x01(\t2\xce\t\n\x10\x43loudServiceType\x12\x99\x01\n\x06\x63reate\x12\x33.spaceone.api.inventory.v1.CreateServiceTypeRequest\x1a/.spaceone.api.inventory.v1.CloudServiceTypeInfo\")\x82\xd3\xe4\x93\x02#\"!/inventory/v1/cloud-service-types\x12\xb5\x01\n\x06update\x12\x38.spaceone.api.inventory.v1.UpdateCloudServiceTypeRequest\x1a/.spaceone.api.inventory.v1.CloudServiceTypeInfo\"@\x82\xd3\xe4\x93\x02:\x1a\x38/inventory/v1/cloud-service-type/{cloud_service_type_id}\x12\xc1\x01\n\x08pin_data\x12\x39.spaceone.api.inventory.v1.PinCloudServiceTypeDataRequest\x1a/.spaceone.api.inventory.v1.CloudServiceTypeInfo\"I\x82\xd3\xe4\x93\x02\x43\x1a\x41/inventory/v1/cloud-service-type/{cloud_service_type_id}/pin-data\x12\x96\x01\n\x06\x64\x65lete\x12\x32.spaceone.api.inventory.v1.CloudServiceTypeRequest\x1a\x16.google.protobuf.Empty\"@\x82\xd3\xe4\x93\x02:*8/inventory/v1/cloud-service-type/{cloud_service_type_id}\x12\xaf\x01\n\x03get\x12\x35.spaceone.api.inventory.v1.GetCloudServiceTypeRequest\x1a/.spaceone.api.inventory.v1.CloudServiceTypeInfo\"@\x82\xd3\xe4\x93\x02:\x12\x38/inventory/v1/cloud-service-type/{cloud_service_type_id}\x12\xc1\x01\n\x04list\x12\x30.spaceone.api.inventory.v1.CloudServiceTypeQuery\x1a\x30.spaceone.api.inventory.v1.CloudServiceTypesInfo\"U\x82\xd3\xe4\x93\x02O\x12!/inventory/v1/cloud-service-typesZ*\"(/inventory/v1/cloud-service-types/search\x12\x92\x01\n\x04stat\x12\x34.spaceone.api.inventory.v1.CloudServiceTypeStatQuery\x1a$.spaceone.api.core.v1.StatisticsInfo\".\x82\xd3\xe4\x93\x02(\"&/inventory/v1/cloud-service-types/statb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,spaceone_dot_api_dot_core_dot_v1_dot_query__pb2.DESCRIPTOR,])




_CREATESERVICETYPEREQUEST = _descriptor.Descriptor(
  name='CreateServiceTypeRequest',
  full_name='spaceone.api.inventory.v1.CreateServiceTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='spaceone.api.inventory.v1.CreateServiceTypeRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='provider', full_name='spaceone.api.inventory.v1.CreateServiceTypeRequest.provider', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group', full_name='spaceone.api.inventory.v1.CreateServiceTypeRequest.group', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='spaceone.api.inventory.v1.CreateServiceTypeRequest.metadata', index=3,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='spaceone.api.inventory.v1.CreateServiceTypeRequest.labels', index=4,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='spaceone.api.inventory.v1.CreateServiceTypeRequest.tags', index=5,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.inventory.v1.CreateServiceTypeRequest.domain_id', index=6,
      number=21, type=9, cpp_type=9, label=1,
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
  serialized_start=238,
  serialized_end=456,
)


_UPDATECLOUDSERVICETYPEREQUEST = _descriptor.Descriptor(
  name='UpdateCloudServiceTypeRequest',
  full_name='spaceone.api.inventory.v1.UpdateCloudServiceTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cloud_service_type_id', full_name='spaceone.api.inventory.v1.UpdateCloudServiceTypeRequest.cloud_service_type_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='spaceone.api.inventory.v1.UpdateCloudServiceTypeRequest.metadata', index=1,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='spaceone.api.inventory.v1.UpdateCloudServiceTypeRequest.labels', index=2,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='spaceone.api.inventory.v1.UpdateCloudServiceTypeRequest.tags', index=3,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.inventory.v1.UpdateCloudServiceTypeRequest.domain_id', index=4,
      number=21, type=9, cpp_type=9, label=1,
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
  serialized_start=459,
  serialized_end=666,
)


_PINCLOUDSERVICETYPEDATAREQUEST = _descriptor.Descriptor(
  name='PinCloudServiceTypeDataRequest',
  full_name='spaceone.api.inventory.v1.PinCloudServiceTypeDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cloud_service_type_id', full_name='spaceone.api.inventory.v1.PinCloudServiceTypeDataRequest.cloud_service_type_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keys', full_name='spaceone.api.inventory.v1.PinCloudServiceTypeDataRequest.keys', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.inventory.v1.PinCloudServiceTypeDataRequest.domain_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=668,
  serialized_end=764,
)


_CLOUDSERVICETYPEREQUEST = _descriptor.Descriptor(
  name='CloudServiceTypeRequest',
  full_name='spaceone.api.inventory.v1.CloudServiceTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cloud_service_type_id', full_name='spaceone.api.inventory.v1.CloudServiceTypeRequest.cloud_service_type_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.inventory.v1.CloudServiceTypeRequest.domain_id', index=1,
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
  serialized_start=766,
  serialized_end=841,
)


_GETCLOUDSERVICETYPEREQUEST = _descriptor.Descriptor(
  name='GetCloudServiceTypeRequest',
  full_name='spaceone.api.inventory.v1.GetCloudServiceTypeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cloud_service_type_id', full_name='spaceone.api.inventory.v1.GetCloudServiceTypeRequest.cloud_service_type_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.inventory.v1.GetCloudServiceTypeRequest.domain_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='only', full_name='spaceone.api.inventory.v1.GetCloudServiceTypeRequest.only', index=2,
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
  serialized_start=843,
  serialized_end=935,
)


_CLOUDSERVICETYPEQUERY = _descriptor.Descriptor(
  name='CloudServiceTypeQuery',
  full_name='spaceone.api.inventory.v1.CloudServiceTypeQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='spaceone.api.inventory.v1.CloudServiceTypeQuery.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cloud_service_type_id', full_name='spaceone.api.inventory.v1.CloudServiceTypeQuery.cloud_service_type_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='spaceone.api.inventory.v1.CloudServiceTypeQuery.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='provider', full_name='spaceone.api.inventory.v1.CloudServiceTypeQuery.provider', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group', full_name='spaceone.api.inventory.v1.CloudServiceTypeQuery.group', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='include_cloud_service_count', full_name='spaceone.api.inventory.v1.CloudServiceTypeQuery.include_cloud_service_count', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.inventory.v1.CloudServiceTypeQuery.domain_id', index=6,
      number=11, type=9, cpp_type=9, label=1,
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
  serialized_start=938,
  serialized_end=1139,
)


_CLOUDSERVICETYPEINFO = _descriptor.Descriptor(
  name='CloudServiceTypeInfo',
  full_name='spaceone.api.inventory.v1.CloudServiceTypeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cloud_service_type_id', full_name='spaceone.api.inventory.v1.CloudServiceTypeInfo.cloud_service_type_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='spaceone.api.inventory.v1.CloudServiceTypeInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='provider', full_name='spaceone.api.inventory.v1.CloudServiceTypeInfo.provider', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group', full_name='spaceone.api.inventory.v1.CloudServiceTypeInfo.group', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='spaceone.api.inventory.v1.CloudServiceTypeInfo.metadata', index=4,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='spaceone.api.inventory.v1.CloudServiceTypeInfo.tags', index=5,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='spaceone.api.inventory.v1.CloudServiceTypeInfo.labels', index=6,
      number=13, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collection_info', full_name='spaceone.api.inventory.v1.CloudServiceTypeInfo.collection_info', index=7,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cloud_service_count', full_name='spaceone.api.inventory.v1.CloudServiceTypeInfo.cloud_service_count', index=8,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.inventory.v1.CloudServiceTypeInfo.domain_id', index=9,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='spaceone.api.inventory.v1.CloudServiceTypeInfo.created_at', index=10,
      number=31, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='spaceone.api.inventory.v1.CloudServiceTypeInfo.updated_at', index=11,
      number=32, type=11, cpp_type=10, label=1,
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
  serialized_start=1142,
  serialized_end=1534,
)


_CLOUDSERVICETYPESINFO = _descriptor.Descriptor(
  name='CloudServiceTypesInfo',
  full_name='spaceone.api.inventory.v1.CloudServiceTypesInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='spaceone.api.inventory.v1.CloudServiceTypesInfo.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_count', full_name='spaceone.api.inventory.v1.CloudServiceTypesInfo.total_count', index=1,
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
  serialized_start=1536,
  serialized_end=1646,
)


_CLOUDSERVICETYPESTATQUERY = _descriptor.Descriptor(
  name='CloudServiceTypeStatQuery',
  full_name='spaceone.api.inventory.v1.CloudServiceTypeStatQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='spaceone.api.inventory.v1.CloudServiceTypeStatQuery.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.inventory.v1.CloudServiceTypeStatQuery.domain_id', index=1,
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
  serialized_start=1648,
  serialized_end=1748,
)

_CREATESERVICETYPEREQUEST.fields_by_name['metadata'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_CREATESERVICETYPEREQUEST.fields_by_name['labels'].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_CREATESERVICETYPEREQUEST.fields_by_name['tags'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_UPDATECLOUDSERVICETYPEREQUEST.fields_by_name['metadata'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_UPDATECLOUDSERVICETYPEREQUEST.fields_by_name['labels'].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_UPDATECLOUDSERVICETYPEREQUEST.fields_by_name['tags'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_CLOUDSERVICETYPEQUERY.fields_by_name['query'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_query__pb2._QUERY
_CLOUDSERVICETYPEINFO.fields_by_name['metadata'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_CLOUDSERVICETYPEINFO.fields_by_name['tags'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_CLOUDSERVICETYPEINFO.fields_by_name['collection_info'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_CLOUDSERVICETYPEINFO.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CLOUDSERVICETYPEINFO.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CLOUDSERVICETYPESINFO.fields_by_name['results'].message_type = _CLOUDSERVICETYPEINFO
_CLOUDSERVICETYPESTATQUERY.fields_by_name['query'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_query__pb2._STATISTICSQUERY
DESCRIPTOR.message_types_by_name['CreateServiceTypeRequest'] = _CREATESERVICETYPEREQUEST
DESCRIPTOR.message_types_by_name['UpdateCloudServiceTypeRequest'] = _UPDATECLOUDSERVICETYPEREQUEST
DESCRIPTOR.message_types_by_name['PinCloudServiceTypeDataRequest'] = _PINCLOUDSERVICETYPEDATAREQUEST
DESCRIPTOR.message_types_by_name['CloudServiceTypeRequest'] = _CLOUDSERVICETYPEREQUEST
DESCRIPTOR.message_types_by_name['GetCloudServiceTypeRequest'] = _GETCLOUDSERVICETYPEREQUEST
DESCRIPTOR.message_types_by_name['CloudServiceTypeQuery'] = _CLOUDSERVICETYPEQUERY
DESCRIPTOR.message_types_by_name['CloudServiceTypeInfo'] = _CLOUDSERVICETYPEINFO
DESCRIPTOR.message_types_by_name['CloudServiceTypesInfo'] = _CLOUDSERVICETYPESINFO
DESCRIPTOR.message_types_by_name['CloudServiceTypeStatQuery'] = _CLOUDSERVICETYPESTATQUERY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateServiceTypeRequest = _reflection.GeneratedProtocolMessageType('CreateServiceTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESERVICETYPEREQUEST,
  '__module__' : 'spaceone.api.inventory.v1.cloud_service_type_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.CreateServiceTypeRequest)
  })
_sym_db.RegisterMessage(CreateServiceTypeRequest)

UpdateCloudServiceTypeRequest = _reflection.GeneratedProtocolMessageType('UpdateCloudServiceTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATECLOUDSERVICETYPEREQUEST,
  '__module__' : 'spaceone.api.inventory.v1.cloud_service_type_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.UpdateCloudServiceTypeRequest)
  })
_sym_db.RegisterMessage(UpdateCloudServiceTypeRequest)

PinCloudServiceTypeDataRequest = _reflection.GeneratedProtocolMessageType('PinCloudServiceTypeDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _PINCLOUDSERVICETYPEDATAREQUEST,
  '__module__' : 'spaceone.api.inventory.v1.cloud_service_type_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.PinCloudServiceTypeDataRequest)
  })
_sym_db.RegisterMessage(PinCloudServiceTypeDataRequest)

CloudServiceTypeRequest = _reflection.GeneratedProtocolMessageType('CloudServiceTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDSERVICETYPEREQUEST,
  '__module__' : 'spaceone.api.inventory.v1.cloud_service_type_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.CloudServiceTypeRequest)
  })
_sym_db.RegisterMessage(CloudServiceTypeRequest)

GetCloudServiceTypeRequest = _reflection.GeneratedProtocolMessageType('GetCloudServiceTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCLOUDSERVICETYPEREQUEST,
  '__module__' : 'spaceone.api.inventory.v1.cloud_service_type_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.GetCloudServiceTypeRequest)
  })
_sym_db.RegisterMessage(GetCloudServiceTypeRequest)

CloudServiceTypeQuery = _reflection.GeneratedProtocolMessageType('CloudServiceTypeQuery', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDSERVICETYPEQUERY,
  '__module__' : 'spaceone.api.inventory.v1.cloud_service_type_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.CloudServiceTypeQuery)
  })
_sym_db.RegisterMessage(CloudServiceTypeQuery)

CloudServiceTypeInfo = _reflection.GeneratedProtocolMessageType('CloudServiceTypeInfo', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDSERVICETYPEINFO,
  '__module__' : 'spaceone.api.inventory.v1.cloud_service_type_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.CloudServiceTypeInfo)
  })
_sym_db.RegisterMessage(CloudServiceTypeInfo)

CloudServiceTypesInfo = _reflection.GeneratedProtocolMessageType('CloudServiceTypesInfo', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDSERVICETYPESINFO,
  '__module__' : 'spaceone.api.inventory.v1.cloud_service_type_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.CloudServiceTypesInfo)
  })
_sym_db.RegisterMessage(CloudServiceTypesInfo)

CloudServiceTypeStatQuery = _reflection.GeneratedProtocolMessageType('CloudServiceTypeStatQuery', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDSERVICETYPESTATQUERY,
  '__module__' : 'spaceone.api.inventory.v1.cloud_service_type_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.inventory.v1.CloudServiceTypeStatQuery)
  })
_sym_db.RegisterMessage(CloudServiceTypeStatQuery)



_CLOUDSERVICETYPE = _descriptor.ServiceDescriptor(
  name='CloudServiceType',
  full_name='spaceone.api.inventory.v1.CloudServiceType',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1751,
  serialized_end=2981,
  methods=[
  _descriptor.MethodDescriptor(
    name='create',
    full_name='spaceone.api.inventory.v1.CloudServiceType.create',
    index=0,
    containing_service=None,
    input_type=_CREATESERVICETYPEREQUEST,
    output_type=_CLOUDSERVICETYPEINFO,
    serialized_options=b'\202\323\344\223\002#\"!/inventory/v1/cloud-service-types',
  ),
  _descriptor.MethodDescriptor(
    name='update',
    full_name='spaceone.api.inventory.v1.CloudServiceType.update',
    index=1,
    containing_service=None,
    input_type=_UPDATECLOUDSERVICETYPEREQUEST,
    output_type=_CLOUDSERVICETYPEINFO,
    serialized_options=b'\202\323\344\223\002:\0328/inventory/v1/cloud-service-type/{cloud_service_type_id}',
  ),
  _descriptor.MethodDescriptor(
    name='pin_data',
    full_name='spaceone.api.inventory.v1.CloudServiceType.pin_data',
    index=2,
    containing_service=None,
    input_type=_PINCLOUDSERVICETYPEDATAREQUEST,
    output_type=_CLOUDSERVICETYPEINFO,
    serialized_options=b'\202\323\344\223\002C\032A/inventory/v1/cloud-service-type/{cloud_service_type_id}/pin-data',
  ),
  _descriptor.MethodDescriptor(
    name='delete',
    full_name='spaceone.api.inventory.v1.CloudServiceType.delete',
    index=3,
    containing_service=None,
    input_type=_CLOUDSERVICETYPEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002:*8/inventory/v1/cloud-service-type/{cloud_service_type_id}',
  ),
  _descriptor.MethodDescriptor(
    name='get',
    full_name='spaceone.api.inventory.v1.CloudServiceType.get',
    index=4,
    containing_service=None,
    input_type=_GETCLOUDSERVICETYPEREQUEST,
    output_type=_CLOUDSERVICETYPEINFO,
    serialized_options=b'\202\323\344\223\002:\0228/inventory/v1/cloud-service-type/{cloud_service_type_id}',
  ),
  _descriptor.MethodDescriptor(
    name='list',
    full_name='spaceone.api.inventory.v1.CloudServiceType.list',
    index=5,
    containing_service=None,
    input_type=_CLOUDSERVICETYPEQUERY,
    output_type=_CLOUDSERVICETYPESINFO,
    serialized_options=b'\202\323\344\223\002O\022!/inventory/v1/cloud-service-typesZ*\"(/inventory/v1/cloud-service-types/search',
  ),
  _descriptor.MethodDescriptor(
    name='stat',
    full_name='spaceone.api.inventory.v1.CloudServiceType.stat',
    index=6,
    containing_service=None,
    input_type=_CLOUDSERVICETYPESTATQUERY,
    output_type=spaceone_dot_api_dot_core_dot_v1_dot_query__pb2._STATISTICSINFO,
    serialized_options=b'\202\323\344\223\002(\"&/inventory/v1/cloud-service-types/stat',
  ),
])
_sym_db.RegisterServiceDescriptor(_CLOUDSERVICETYPE)

DESCRIPTOR.services_by_name['CloudServiceType'] = _CLOUDSERVICETYPE

# @@protoc_insertion_point(module_scope)
