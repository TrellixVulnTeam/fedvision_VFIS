# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fedvision/framework/protobuf/coordinator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fedvision.framework.protobuf import job_pb2 as fedvision_dot_framework_dot_protobuf_dot_job__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fedvision/framework/protobuf/coordinator.proto',
  package='fedvision.framework.coordinator',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n.fedvision/framework/protobuf/coordinator.proto\x12\x1f\x66\x65\x64vision.framework.coordinator\x1a&fedvision/framework/protobuf/job.proto\"\xfa\x01\n\tSubscribe\x1a>\n\x03REQ\x12\x10\n\x08party_id\x18\x01 \x01(\t\x12\x11\n\tjob_types\x18\x02 \x03(\t\x12\x12\n\ncredential\x18\x03 \x01(\t\x1ao\n\x03REP\x12\x41\n\x06status\x18\x01 \x01(\x0e\x32\x31.fedvision.framework.coordinator.Subscribe.Status\x12\x13\n\x0bproposal_id\x18\x02 \x01(\t\x12\x10\n\x08job_type\x18\x03 \x01(\t\"<\n\x06Status\x12\x14\n\x10\x44UPLICATE_ENROLL\x10\x00\x12\x0f\n\x0bNOT_SERVING\x10\x01\x12\x0b\n\x07SUCCESS\x10\x02\"\x8a\x02\n\tFetchTask\x1a,\n\x03REQ\x12\x10\n\x08party_id\x18\x01 \x01(\t\x12\x13\n\x0bproposal_id\x18\x02 \x01(\t\x1aq\n\x03REP\x12\x41\n\x06status\x18\x01 \x01(\x0e\x32\x31.fedvision.framework.coordinator.FetchTask.Status\x12\'\n\x04task\x18\x02 \x01(\x0b\x32\x19.fedvision.framework.Task\"\\\n\x06Status\x12\r\n\tNOT_FOUND\x10\x00\x12\r\n\tNOT_ALLOW\x10\x01\x12\x0b\n\x07TIMEOUT\x10\x02\x12\x0c\n\x08\x43\x41NCELED\x10\x03\x12\x0e\n\nRANDOM_OUT\x10\x04\x12\t\n\x05READY\x10\x05\"\xe2\x02\n\x08Proposal\x1a\xa5\x01\n\x03REQ\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x10\n\x08job_type\x18\x02 \x01(\t\x12(\n\x05tasks\x18\x04 \x03(\x0b\x32\x19.fedvision.framework.Task\x12\x1a\n\x12proposal_wait_time\x18\x05 \x01(\r\x12\x1a\n\x12minimum_acceptance\x18\x06 \x01(\r\x12\x1a\n\x12maximum_acceptance\x18\x07 \x01(\r\x1aG\n\x03REP\x12@\n\x06status\x18\x01 \x01(\x0e\x32\x30.fedvision.framework.coordinator.Proposal.Status\"e\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x19\n\x15NOT_ENOUGH_RESPONDERS\x10\x02\x12\x1a\n\x16NOT_ENOUGH_SUBSCRIBERS\x10\x03\x12\n\n\x06REJECT\x10\x04\"\x8c\x01\n\x05Leave\x1a\x17\n\x03REQ\x12\x10\n\x08party_id\x18\x01 \x01(\t\x1a\x44\n\x03REP\x12=\n\x06status\x18\x01 \x01(\x0e\x32-.fedvision.framework.coordinator.Leave.Status\"$\n\x06Status\x12\r\n\tNOT_FOUND\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x32\xbc\x03\n\x0b\x43oordinator\x12o\n\tSubscribe\x12..fedvision.framework.coordinator.Subscribe.REQ\x1a..fedvision.framework.coordinator.Subscribe.REP\"\x00\x30\x01\x12j\n\x08Proposal\x12-.fedvision.framework.coordinator.Proposal.REQ\x1a-.fedvision.framework.coordinator.Proposal.REP\"\x00\x12m\n\tFetchTask\x12..fedvision.framework.coordinator.FetchTask.REQ\x1a..fedvision.framework.coordinator.FetchTask.REP\"\x00\x12\x61\n\x05Leave\x12*.fedvision.framework.coordinator.Leave.REQ\x1a*.fedvision.framework.coordinator.Leave.REP\"\x00\x62\x06proto3'
  ,
  dependencies=[fedvision_dot_framework_dot_protobuf_dot_job__pb2.DESCRIPTOR,])



_SUBSCRIBE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='fedvision.framework.coordinator.Subscribe.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE_ENROLL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_SERVING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=314,
  serialized_end=374,
)
_sym_db.RegisterEnumDescriptor(_SUBSCRIBE_STATUS)

_FETCHTASK_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='fedvision.framework.coordinator.FetchTask.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_ALLOW', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TIMEOUT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANCELED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RANDOM_OUT', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='READY', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=551,
  serialized_end=643,
)
_sym_db.RegisterEnumDescriptor(_FETCHTASK_STATUS)

_PROPOSAL_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='fedvision.framework.coordinator.Proposal.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_ENOUGH_RESPONDERS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_ENOUGH_SUBSCRIBERS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REJECT', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=899,
  serialized_end=1000,
)
_sym_db.RegisterEnumDescriptor(_PROPOSAL_STATUS)

_LEAVE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='fedvision.framework.coordinator.Leave.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1107,
  serialized_end=1143,
)
_sym_db.RegisterEnumDescriptor(_LEAVE_STATUS)


_SUBSCRIBE_REQ = _descriptor.Descriptor(
  name='REQ',
  full_name='fedvision.framework.coordinator.Subscribe.REQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='party_id', full_name='fedvision.framework.coordinator.Subscribe.REQ.party_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_types', full_name='fedvision.framework.coordinator.Subscribe.REQ.job_types', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='credential', full_name='fedvision.framework.coordinator.Subscribe.REQ.credential', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=137,
  serialized_end=199,
)

_SUBSCRIBE_REP = _descriptor.Descriptor(
  name='REP',
  full_name='fedvision.framework.coordinator.Subscribe.REP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='fedvision.framework.coordinator.Subscribe.REP.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='fedvision.framework.coordinator.Subscribe.REP.proposal_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_type', full_name='fedvision.framework.coordinator.Subscribe.REP.job_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=201,
  serialized_end=312,
)

_SUBSCRIBE = _descriptor.Descriptor(
  name='Subscribe',
  full_name='fedvision.framework.coordinator.Subscribe',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_SUBSCRIBE_REQ, _SUBSCRIBE_REP, ],
  enum_types=[
    _SUBSCRIBE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=374,
)


_FETCHTASK_REQ = _descriptor.Descriptor(
  name='REQ',
  full_name='fedvision.framework.coordinator.FetchTask.REQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='party_id', full_name='fedvision.framework.coordinator.FetchTask.REQ.party_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proposal_id', full_name='fedvision.framework.coordinator.FetchTask.REQ.proposal_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=390,
  serialized_end=434,
)

_FETCHTASK_REP = _descriptor.Descriptor(
  name='REP',
  full_name='fedvision.framework.coordinator.FetchTask.REP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='fedvision.framework.coordinator.FetchTask.REP.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task', full_name='fedvision.framework.coordinator.FetchTask.REP.task', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=436,
  serialized_end=549,
)

_FETCHTASK = _descriptor.Descriptor(
  name='FetchTask',
  full_name='fedvision.framework.coordinator.FetchTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_FETCHTASK_REQ, _FETCHTASK_REP, ],
  enum_types=[
    _FETCHTASK_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=377,
  serialized_end=643,
)


_PROPOSAL_REQ = _descriptor.Descriptor(
  name='REQ',
  full_name='fedvision.framework.coordinator.Proposal.REQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='fedvision.framework.coordinator.Proposal.REQ.job_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_type', full_name='fedvision.framework.coordinator.Proposal.REQ.job_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tasks', full_name='fedvision.framework.coordinator.Proposal.REQ.tasks', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proposal_wait_time', full_name='fedvision.framework.coordinator.Proposal.REQ.proposal_wait_time', index=3,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='minimum_acceptance', full_name='fedvision.framework.coordinator.Proposal.REQ.minimum_acceptance', index=4,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='maximum_acceptance', full_name='fedvision.framework.coordinator.Proposal.REQ.maximum_acceptance', index=5,
      number=7, type=13, cpp_type=3, label=1,
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
  serialized_start=659,
  serialized_end=824,
)

_PROPOSAL_REP = _descriptor.Descriptor(
  name='REP',
  full_name='fedvision.framework.coordinator.Proposal.REP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='fedvision.framework.coordinator.Proposal.REP.status', index=0,
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
  serialized_start=826,
  serialized_end=897,
)

_PROPOSAL = _descriptor.Descriptor(
  name='Proposal',
  full_name='fedvision.framework.coordinator.Proposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_PROPOSAL_REQ, _PROPOSAL_REP, ],
  enum_types=[
    _PROPOSAL_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=646,
  serialized_end=1000,
)


_LEAVE_REQ = _descriptor.Descriptor(
  name='REQ',
  full_name='fedvision.framework.coordinator.Leave.REQ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='party_id', full_name='fedvision.framework.coordinator.Leave.REQ.party_id', index=0,
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
  serialized_start=137,
  serialized_end=160,
)

_LEAVE_REP = _descriptor.Descriptor(
  name='REP',
  full_name='fedvision.framework.coordinator.Leave.REP',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='fedvision.framework.coordinator.Leave.REP.status', index=0,
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
  serialized_start=1037,
  serialized_end=1105,
)

_LEAVE = _descriptor.Descriptor(
  name='Leave',
  full_name='fedvision.framework.coordinator.Leave',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_LEAVE_REQ, _LEAVE_REP, ],
  enum_types=[
    _LEAVE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1003,
  serialized_end=1143,
)

_SUBSCRIBE_REQ.containing_type = _SUBSCRIBE
_SUBSCRIBE_REP.fields_by_name['status'].enum_type = _SUBSCRIBE_STATUS
_SUBSCRIBE_REP.containing_type = _SUBSCRIBE
_SUBSCRIBE_STATUS.containing_type = _SUBSCRIBE
_FETCHTASK_REQ.containing_type = _FETCHTASK
_FETCHTASK_REP.fields_by_name['status'].enum_type = _FETCHTASK_STATUS
_FETCHTASK_REP.fields_by_name['task'].message_type = fedvision_dot_framework_dot_protobuf_dot_job__pb2._TASK
_FETCHTASK_REP.containing_type = _FETCHTASK
_FETCHTASK_STATUS.containing_type = _FETCHTASK
_PROPOSAL_REQ.fields_by_name['tasks'].message_type = fedvision_dot_framework_dot_protobuf_dot_job__pb2._TASK
_PROPOSAL_REQ.containing_type = _PROPOSAL
_PROPOSAL_REP.fields_by_name['status'].enum_type = _PROPOSAL_STATUS
_PROPOSAL_REP.containing_type = _PROPOSAL
_PROPOSAL_STATUS.containing_type = _PROPOSAL
_LEAVE_REQ.containing_type = _LEAVE
_LEAVE_REP.fields_by_name['status'].enum_type = _LEAVE_STATUS
_LEAVE_REP.containing_type = _LEAVE
_LEAVE_STATUS.containing_type = _LEAVE
DESCRIPTOR.message_types_by_name['Subscribe'] = _SUBSCRIBE
DESCRIPTOR.message_types_by_name['FetchTask'] = _FETCHTASK
DESCRIPTOR.message_types_by_name['Proposal'] = _PROPOSAL
DESCRIPTOR.message_types_by_name['Leave'] = _LEAVE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Subscribe = _reflection.GeneratedProtocolMessageType('Subscribe', (_message.Message,), {

  'REQ' : _reflection.GeneratedProtocolMessageType('REQ', (_message.Message,), {
    'DESCRIPTOR' : _SUBSCRIBE_REQ,
    '__module__' : 'fedvision.framework.protobuf.coordinator_pb2'
    # @@protoc_insertion_point(class_scope:fedvision.framework.coordinator.Subscribe.REQ)
    })
  ,

  'REP' : _reflection.GeneratedProtocolMessageType('REP', (_message.Message,), {
    'DESCRIPTOR' : _SUBSCRIBE_REP,
    '__module__' : 'fedvision.framework.protobuf.coordinator_pb2'
    # @@protoc_insertion_point(class_scope:fedvision.framework.coordinator.Subscribe.REP)
    })
  ,
  'DESCRIPTOR' : _SUBSCRIBE,
  '__module__' : 'fedvision.framework.protobuf.coordinator_pb2'
  # @@protoc_insertion_point(class_scope:fedvision.framework.coordinator.Subscribe)
  })
_sym_db.RegisterMessage(Subscribe)
_sym_db.RegisterMessage(Subscribe.REQ)
_sym_db.RegisterMessage(Subscribe.REP)

FetchTask = _reflection.GeneratedProtocolMessageType('FetchTask', (_message.Message,), {

  'REQ' : _reflection.GeneratedProtocolMessageType('REQ', (_message.Message,), {
    'DESCRIPTOR' : _FETCHTASK_REQ,
    '__module__' : 'fedvision.framework.protobuf.coordinator_pb2'
    # @@protoc_insertion_point(class_scope:fedvision.framework.coordinator.FetchTask.REQ)
    })
  ,

  'REP' : _reflection.GeneratedProtocolMessageType('REP', (_message.Message,), {
    'DESCRIPTOR' : _FETCHTASK_REP,
    '__module__' : 'fedvision.framework.protobuf.coordinator_pb2'
    # @@protoc_insertion_point(class_scope:fedvision.framework.coordinator.FetchTask.REP)
    })
  ,
  'DESCRIPTOR' : _FETCHTASK,
  '__module__' : 'fedvision.framework.protobuf.coordinator_pb2'
  # @@protoc_insertion_point(class_scope:fedvision.framework.coordinator.FetchTask)
  })
_sym_db.RegisterMessage(FetchTask)
_sym_db.RegisterMessage(FetchTask.REQ)
_sym_db.RegisterMessage(FetchTask.REP)

Proposal = _reflection.GeneratedProtocolMessageType('Proposal', (_message.Message,), {

  'REQ' : _reflection.GeneratedProtocolMessageType('REQ', (_message.Message,), {
    'DESCRIPTOR' : _PROPOSAL_REQ,
    '__module__' : 'fedvision.framework.protobuf.coordinator_pb2'
    # @@protoc_insertion_point(class_scope:fedvision.framework.coordinator.Proposal.REQ)
    })
  ,

  'REP' : _reflection.GeneratedProtocolMessageType('REP', (_message.Message,), {
    'DESCRIPTOR' : _PROPOSAL_REP,
    '__module__' : 'fedvision.framework.protobuf.coordinator_pb2'
    # @@protoc_insertion_point(class_scope:fedvision.framework.coordinator.Proposal.REP)
    })
  ,
  'DESCRIPTOR' : _PROPOSAL,
  '__module__' : 'fedvision.framework.protobuf.coordinator_pb2'
  # @@protoc_insertion_point(class_scope:fedvision.framework.coordinator.Proposal)
  })
_sym_db.RegisterMessage(Proposal)
_sym_db.RegisterMessage(Proposal.REQ)
_sym_db.RegisterMessage(Proposal.REP)

Leave = _reflection.GeneratedProtocolMessageType('Leave', (_message.Message,), {

  'REQ' : _reflection.GeneratedProtocolMessageType('REQ', (_message.Message,), {
    'DESCRIPTOR' : _LEAVE_REQ,
    '__module__' : 'fedvision.framework.protobuf.coordinator_pb2'
    # @@protoc_insertion_point(class_scope:fedvision.framework.coordinator.Leave.REQ)
    })
  ,

  'REP' : _reflection.GeneratedProtocolMessageType('REP', (_message.Message,), {
    'DESCRIPTOR' : _LEAVE_REP,
    '__module__' : 'fedvision.framework.protobuf.coordinator_pb2'
    # @@protoc_insertion_point(class_scope:fedvision.framework.coordinator.Leave.REP)
    })
  ,
  'DESCRIPTOR' : _LEAVE,
  '__module__' : 'fedvision.framework.protobuf.coordinator_pb2'
  # @@protoc_insertion_point(class_scope:fedvision.framework.coordinator.Leave)
  })
_sym_db.RegisterMessage(Leave)
_sym_db.RegisterMessage(Leave.REQ)
_sym_db.RegisterMessage(Leave.REP)



_COORDINATOR = _descriptor.ServiceDescriptor(
  name='Coordinator',
  full_name='fedvision.framework.coordinator.Coordinator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1146,
  serialized_end=1590,
  methods=[
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='fedvision.framework.coordinator.Coordinator.Subscribe',
    index=0,
    containing_service=None,
    input_type=_SUBSCRIBE_REQ,
    output_type=_SUBSCRIBE_REP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Proposal',
    full_name='fedvision.framework.coordinator.Coordinator.Proposal',
    index=1,
    containing_service=None,
    input_type=_PROPOSAL_REQ,
    output_type=_PROPOSAL_REP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FetchTask',
    full_name='fedvision.framework.coordinator.Coordinator.FetchTask',
    index=2,
    containing_service=None,
    input_type=_FETCHTASK_REQ,
    output_type=_FETCHTASK_REP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Leave',
    full_name='fedvision.framework.coordinator.Coordinator.Leave',
    index=3,
    containing_service=None,
    input_type=_LEAVE_REQ,
    output_type=_LEAVE_REP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_COORDINATOR)

DESCRIPTOR.services_by_name['Coordinator'] = _COORDINATOR

# @@protoc_insertion_point(module_scope)