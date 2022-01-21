# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fedvision/paddle_fl/protobuf/scheduler.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fedvision/paddle_fl/protobuf/scheduler.proto',
  package='fedvision.paddle_fl',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,fedvision/paddle_fl/protobuf/scheduler.proto\x12\x13\x66\x65\x64vision.paddle_fl\"t\n\x04Init\x1a\x13\n\x03REQ\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a\x37\n\x03REP\x12\x30\n\x06status\x18\x01 \x01(\x0e\x32 .fedvision.paddle_fl.Init.Status\"\x1e\n\x06Status\x12\n\n\x06REJECT\x10\x00\x12\x08\n\x04INIT\x10\x01\"\xa2\x01\n\nWorkerJoin\x1a!\n\x03REQ\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04step\x18\x02 \x01(\r\x1a=\n\x03REP\x12\x36\n\x06status\x18\x01 \x01(\x0e\x32&.fedvision.paddle_fl.WorkerJoin.Status\"2\n\x06Status\x12\n\n\x06REJECT\x10\x00\x12\x10\n\x0cNOT_SELECTED\x10\x01\x12\n\n\x06\x41\x43\x43\x45PT\x10\x02\"\x84\x01\n\x0cWorkerFinish\x1a\x13\n\x03REQ\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a?\n\x03REP\x12\x38\n\x06status\x18\x01 \x01(\x0e\x32(.fedvision.paddle_fl.WorkerFinish.Status\"\x1e\n\x06Status\x12\n\n\x06REJECT\x10\x00\x12\x08\n\x04\x44ONE\x10\x01\x32\x8d\x02\n\tScheduler\x12\x46\n\x04Init\x12\x1d.fedvision.paddle_fl.Init.REQ\x1a\x1d.fedvision.paddle_fl.Init.REP\"\x00\x12X\n\nWorkerJoin\x12#.fedvision.paddle_fl.WorkerJoin.REQ\x1a#.fedvision.paddle_fl.WorkerJoin.REP\"\x00\x12^\n\x0cWorkerFinish\x12%.fedvision.paddle_fl.WorkerFinish.REQ\x1a%.fedvision.paddle_fl.WorkerFinish.REP\"\x00\x62\x06proto3'
)



_INIT_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='fedvision.paddle_fl.Init.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REJECT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INIT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=155,
  serialized_end=185,
)
_sym_db.RegisterEnumDescriptor(_INIT_STATUS)

_WORKERJOIN_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='fedvision.paddle_fl.WorkerJoin.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REJECT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_SELECTED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACCEPT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=300,
  serialized_end=350,
)
_sym_db.RegisterEnumDescriptor(_WORKERJOIN_STATUS)

_WORKERFINISH_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='fedvision.paddle_fl.WorkerFinish.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REJECT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DONE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=455,
  serialized_end=485,
)
_sym_db.RegisterEnumDescriptor(_WORKERFINISH_STATUS)


_INIT_REQ = _descriptor.Descriptor(
  name='REQ',
  full_name='fedvision.paddle_fl.Init.REQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='fedvision.paddle_fl.Init.REQ.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=77,
  serialized_end=96,
)

_INIT_REP = _descriptor.Descriptor(
  name='REP',
  full_name='fedvision.paddle_fl.Init.REP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='fedvision.paddle_fl.Init.REP.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=98,
  serialized_end=153,
)

_INIT = _descriptor.Descriptor(
  name='Init',
  full_name='fedvision.paddle_fl.Init',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_INIT_REQ, _INIT_REP, ],
  enum_types=[
    _INIT_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=185,
)


_WORKERJOIN_REQ = _descriptor.Descriptor(
  name='REQ',
  full_name='fedvision.paddle_fl.WorkerJoin.REQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='fedvision.paddle_fl.WorkerJoin.REQ.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='step', full_name='fedvision.paddle_fl.WorkerJoin.REQ.step', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=202,
  serialized_end=235,
)

_WORKERJOIN_REP = _descriptor.Descriptor(
  name='REP',
  full_name='fedvision.paddle_fl.WorkerJoin.REP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='fedvision.paddle_fl.WorkerJoin.REP.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=237,
  serialized_end=298,
)

_WORKERJOIN = _descriptor.Descriptor(
  name='WorkerJoin',
  full_name='fedvision.paddle_fl.WorkerJoin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_WORKERJOIN_REQ, _WORKERJOIN_REP, ],
  enum_types=[
    _WORKERJOIN_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=350,
)


_WORKERFINISH_REQ = _descriptor.Descriptor(
  name='REQ',
  full_name='fedvision.paddle_fl.WorkerFinish.REQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='fedvision.paddle_fl.WorkerFinish.REQ.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=77,
  serialized_end=96,
)

_WORKERFINISH_REP = _descriptor.Descriptor(
  name='REP',
  full_name='fedvision.paddle_fl.WorkerFinish.REP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='fedvision.paddle_fl.WorkerFinish.REP.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=390,
  serialized_end=453,
)

_WORKERFINISH = _descriptor.Descriptor(
  name='WorkerFinish',
  full_name='fedvision.paddle_fl.WorkerFinish',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_WORKERFINISH_REQ, _WORKERFINISH_REP, ],
  enum_types=[
    _WORKERFINISH_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=353,
  serialized_end=485,
)

_INIT_REQ.containing_type = _INIT
_INIT_REP.fields_by_name['status'].enum_type = _INIT_STATUS
_INIT_REP.containing_type = _INIT
_INIT_STATUS.containing_type = _INIT
_WORKERJOIN_REQ.containing_type = _WORKERJOIN
_WORKERJOIN_REP.fields_by_name['status'].enum_type = _WORKERJOIN_STATUS
_WORKERJOIN_REP.containing_type = _WORKERJOIN
_WORKERJOIN_STATUS.containing_type = _WORKERJOIN
_WORKERFINISH_REQ.containing_type = _WORKERFINISH
_WORKERFINISH_REP.fields_by_name['status'].enum_type = _WORKERFINISH_STATUS
_WORKERFINISH_REP.containing_type = _WORKERFINISH
_WORKERFINISH_STATUS.containing_type = _WORKERFINISH
DESCRIPTOR.message_types_by_name['Init'] = _INIT
DESCRIPTOR.message_types_by_name['WorkerJoin'] = _WORKERJOIN
DESCRIPTOR.message_types_by_name['WorkerFinish'] = _WORKERFINISH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Init = _reflection.GeneratedProtocolMessageType('Init', (_message.Message,), {

  'REQ' : _reflection.GeneratedProtocolMessageType('REQ', (_message.Message,), {
    'DESCRIPTOR' : _INIT_REQ,
    '__module__' : 'fedvision.paddle_fl.protobuf.scheduler_pb2'
    # @@protoc_insertion_point(class_scope:fedvision.paddle_fl.Init.REQ)
    })
  ,

  'REP' : _reflection.GeneratedProtocolMessageType('REP', (_message.Message,), {
    'DESCRIPTOR' : _INIT_REP,
    '__module__' : 'fedvision.paddle_fl.protobuf.scheduler_pb2'
    # @@protoc_insertion_point(class_scope:fedvision.paddle_fl.Init.REP)
    })
  ,
  'DESCRIPTOR' : _INIT,
  '__module__' : 'fedvision.paddle_fl.protobuf.scheduler_pb2'
  # @@protoc_insertion_point(class_scope:fedvision.paddle_fl.Init)
  })
_sym_db.RegisterMessage(Init)
_sym_db.RegisterMessage(Init.REQ)
_sym_db.RegisterMessage(Init.REP)

WorkerJoin = _reflection.GeneratedProtocolMessageType('WorkerJoin', (_message.Message,), {

  'REQ' : _reflection.GeneratedProtocolMessageType('REQ', (_message.Message,), {
    'DESCRIPTOR' : _WORKERJOIN_REQ,
    '__module__' : 'fedvision.paddle_fl.protobuf.scheduler_pb2'
    # @@protoc_insertion_point(class_scope:fedvision.paddle_fl.WorkerJoin.REQ)
    })
  ,

  'REP' : _reflection.GeneratedProtocolMessageType('REP', (_message.Message,), {
    'DESCRIPTOR' : _WORKERJOIN_REP,
    '__module__' : 'fedvision.paddle_fl.protobuf.scheduler_pb2'
    # @@protoc_insertion_point(class_scope:fedvision.paddle_fl.WorkerJoin.REP)
    })
  ,
  'DESCRIPTOR' : _WORKERJOIN,
  '__module__' : 'fedvision.paddle_fl.protobuf.scheduler_pb2'
  # @@protoc_insertion_point(class_scope:fedvision.paddle_fl.WorkerJoin)
  })
_sym_db.RegisterMessage(WorkerJoin)
_sym_db.RegisterMessage(WorkerJoin.REQ)
_sym_db.RegisterMessage(WorkerJoin.REP)

WorkerFinish = _reflection.GeneratedProtocolMessageType('WorkerFinish', (_message.Message,), {

  'REQ' : _reflection.GeneratedProtocolMessageType('REQ', (_message.Message,), {
    'DESCRIPTOR' : _WORKERFINISH_REQ,
    '__module__' : 'fedvision.paddle_fl.protobuf.scheduler_pb2'
    # @@protoc_insertion_point(class_scope:fedvision.paddle_fl.WorkerFinish.REQ)
    })
  ,

  'REP' : _reflection.GeneratedProtocolMessageType('REP', (_message.Message,), {
    'DESCRIPTOR' : _WORKERFINISH_REP,
    '__module__' : 'fedvision.paddle_fl.protobuf.scheduler_pb2'
    # @@protoc_insertion_point(class_scope:fedvision.paddle_fl.WorkerFinish.REP)
    })
  ,
  'DESCRIPTOR' : _WORKERFINISH,
  '__module__' : 'fedvision.paddle_fl.protobuf.scheduler_pb2'
  # @@protoc_insertion_point(class_scope:fedvision.paddle_fl.WorkerFinish)
  })
_sym_db.RegisterMessage(WorkerFinish)
_sym_db.RegisterMessage(WorkerFinish.REQ)
_sym_db.RegisterMessage(WorkerFinish.REP)



_SCHEDULER = _descriptor.ServiceDescriptor(
  name='Scheduler',
  full_name='fedvision.paddle_fl.Scheduler',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=488,
  serialized_end=757,
  methods=[
  _descriptor.MethodDescriptor(
    name='Init',
    full_name='fedvision.paddle_fl.Scheduler.Init',
    index=0,
    containing_service=None,
    input_type=_INIT_REQ,
    output_type=_INIT_REP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='WorkerJoin',
    full_name='fedvision.paddle_fl.Scheduler.WorkerJoin',
    index=1,
    containing_service=None,
    input_type=_WORKERJOIN_REQ,
    output_type=_WORKERJOIN_REP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='WorkerFinish',
    full_name='fedvision.paddle_fl.Scheduler.WorkerFinish',
    index=2,
    containing_service=None,
    input_type=_WORKERFINISH_REQ,
    output_type=_WORKERFINISH_REP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SCHEDULER)

DESCRIPTOR.services_by_name['Scheduler'] = _SCHEDULER

# @@protoc_insertion_point(module_scope)
