# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/clarifai/api/visualization.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from clarifai.rest.grpc.proto.clarifai.api import common_pb2 as proto_dot_clarifai_dot_api_dot_common__pb2
from clarifai.rest.grpc.proto.clarifai.api import data_pb2 as proto_dot_clarifai_dot_api_dot_data__pb2
from clarifai.rest.grpc.proto.clarifai.api import input_pb2 as proto_dot_clarifai_dot_api_dot_input__pb2
from clarifai.rest.grpc.proto.clarifai.api.status import status_pb2 as proto_dot_clarifai_dot_api_dot_status_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/clarifai/api/visualization.proto',
  package='clarifai.api',
  syntax='proto3',
  serialized_pb=_b('\n&proto/clarifai/api/visualization.proto\x12\x0c\x63larifai.api\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1fproto/clarifai/api/common.proto\x1a\x1dproto/clarifai/api/data.proto\x1a\x1eproto/clarifai/api/input.proto\x1a&proto/clarifai/api/status/status.proto\"\xe3\x01\n\x13VisualizationOutput\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.clarifai.api.status.Status\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0e\n\x06\x61pp_id\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12 \n\x04\x64\x61ta\x18\x05 \x01(\x0b\x32\x12.clarifai.api.Data\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12#\n\x06inputs\x18\x07 \x03(\x0b\x32\x13.clarifai.api.Input\"K\n\x18PostVisualizationRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\"d\n\x17GetVisualizationRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\x12\x18\n\x10visualization_id\x18\x02 \x01(\t\"M\n\x1aGetAppVisualizationRequest\x12/\n\x0buser_app_id\x18\x01 \x01(\x0b\x32\x1a.clarifai.api.UserAppIDSet\"\x8b\x01\n\x1bSingleVisualizationResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.clarifai.api.status.Status\x12?\n\x14visualization_output\x18\x02 \x01(\x0b\x32!.clarifai.api.VisualizationOutputBZ\n\x1b\x63larifai2.internal.grpc.apiZ\x03\x61pi\xa2\x02\x04\x43\x41IP\xaa\x02\x16\x43larifai.Internal.GRPC\xc2\x02\x01_\xca\x02\x11\x43larifai\\Internalb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,proto_dot_clarifai_dot_api_dot_common__pb2.DESCRIPTOR,proto_dot_clarifai_dot_api_dot_data__pb2.DESCRIPTOR,proto_dot_clarifai_dot_api_dot_input__pb2.DESCRIPTOR,proto_dot_clarifai_dot_api_dot_status_dot_status__pb2.DESCRIPTOR,])




_VISUALIZATIONOUTPUT = _descriptor.Descriptor(
  name='VisualizationOutput',
  full_name='clarifai.api.VisualizationOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='clarifai.api.VisualizationOutput.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='clarifai.api.VisualizationOutput.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_id', full_name='clarifai.api.VisualizationOutput.app_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='clarifai.api.VisualizationOutput.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='clarifai.api.VisualizationOutput.data', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='clarifai.api.VisualizationOutput.created_at', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='clarifai.api.VisualizationOutput.inputs', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=453,
)


_POSTVISUALIZATIONREQUEST = _descriptor.Descriptor(
  name='PostVisualizationRequest',
  full_name='clarifai.api.PostVisualizationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.PostVisualizationRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=455,
  serialized_end=530,
)


_GETVISUALIZATIONREQUEST = _descriptor.Descriptor(
  name='GetVisualizationRequest',
  full_name='clarifai.api.GetVisualizationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.GetVisualizationRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visualization_id', full_name='clarifai.api.GetVisualizationRequest.visualization_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=532,
  serialized_end=632,
)


_GETAPPVISUALIZATIONREQUEST = _descriptor.Descriptor(
  name='GetAppVisualizationRequest',
  full_name='clarifai.api.GetAppVisualizationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_app_id', full_name='clarifai.api.GetAppVisualizationRequest.user_app_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=634,
  serialized_end=711,
)


_SINGLEVISUALIZATIONRESPONSE = _descriptor.Descriptor(
  name='SingleVisualizationResponse',
  full_name='clarifai.api.SingleVisualizationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='clarifai.api.SingleVisualizationResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='visualization_output', full_name='clarifai.api.SingleVisualizationResponse.visualization_output', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=714,
  serialized_end=853,
)

_VISUALIZATIONOUTPUT.fields_by_name['status'].message_type = proto_dot_clarifai_dot_api_dot_status_dot_status__pb2._STATUS
_VISUALIZATIONOUTPUT.fields_by_name['data'].message_type = proto_dot_clarifai_dot_api_dot_data__pb2._DATA
_VISUALIZATIONOUTPUT.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_VISUALIZATIONOUTPUT.fields_by_name['inputs'].message_type = proto_dot_clarifai_dot_api_dot_input__pb2._INPUT
_POSTVISUALIZATIONREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_GETVISUALIZATIONREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_GETAPPVISUALIZATIONREQUEST.fields_by_name['user_app_id'].message_type = proto_dot_clarifai_dot_api_dot_common__pb2._USERAPPIDSET
_SINGLEVISUALIZATIONRESPONSE.fields_by_name['status'].message_type = proto_dot_clarifai_dot_api_dot_status_dot_status__pb2._STATUS
_SINGLEVISUALIZATIONRESPONSE.fields_by_name['visualization_output'].message_type = _VISUALIZATIONOUTPUT
DESCRIPTOR.message_types_by_name['VisualizationOutput'] = _VISUALIZATIONOUTPUT
DESCRIPTOR.message_types_by_name['PostVisualizationRequest'] = _POSTVISUALIZATIONREQUEST
DESCRIPTOR.message_types_by_name['GetVisualizationRequest'] = _GETVISUALIZATIONREQUEST
DESCRIPTOR.message_types_by_name['GetAppVisualizationRequest'] = _GETAPPVISUALIZATIONREQUEST
DESCRIPTOR.message_types_by_name['SingleVisualizationResponse'] = _SINGLEVISUALIZATIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VisualizationOutput = _reflection.GeneratedProtocolMessageType('VisualizationOutput', (_message.Message,), dict(
  DESCRIPTOR = _VISUALIZATIONOUTPUT,
  __module__ = 'proto.clarifai.api.visualization_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.VisualizationOutput)
  ))
_sym_db.RegisterMessage(VisualizationOutput)

PostVisualizationRequest = _reflection.GeneratedProtocolMessageType('PostVisualizationRequest', (_message.Message,), dict(
  DESCRIPTOR = _POSTVISUALIZATIONREQUEST,
  __module__ = 'proto.clarifai.api.visualization_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.PostVisualizationRequest)
  ))
_sym_db.RegisterMessage(PostVisualizationRequest)

GetVisualizationRequest = _reflection.GeneratedProtocolMessageType('GetVisualizationRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETVISUALIZATIONREQUEST,
  __module__ = 'proto.clarifai.api.visualization_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.GetVisualizationRequest)
  ))
_sym_db.RegisterMessage(GetVisualizationRequest)

GetAppVisualizationRequest = _reflection.GeneratedProtocolMessageType('GetAppVisualizationRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETAPPVISUALIZATIONREQUEST,
  __module__ = 'proto.clarifai.api.visualization_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.GetAppVisualizationRequest)
  ))
_sym_db.RegisterMessage(GetAppVisualizationRequest)

SingleVisualizationResponse = _reflection.GeneratedProtocolMessageType('SingleVisualizationResponse', (_message.Message,), dict(
  DESCRIPTOR = _SINGLEVISUALIZATIONRESPONSE,
  __module__ = 'proto.clarifai.api.visualization_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.SingleVisualizationResponse)
  ))
_sym_db.RegisterMessage(SingleVisualizationResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033clarifai2.internal.grpc.apiZ\003api\242\002\004CAIP\252\002\026Clarifai.Internal.GRPC\302\002\001_\312\002\021Clarifai\\Internal'))
# @@protoc_insertion_point(module_scope)