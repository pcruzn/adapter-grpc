# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import patient_adapter_unary_pb2 as patient__adapter__unary__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in patient_adapter_unary_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class PatientAdapterServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_patient = channel.unary_unary(
                '/PatientAdapterService/get_patient',
                request_serializer=patient__adapter__unary__pb2.PatientID.SerializeToString,
                response_deserializer=patient__adapter__unary__pb2.AdaptedPatient.FromString,
                _registered_method=True)


class PatientAdapterServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_patient(self, request, context):
        """unary service
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PatientAdapterServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_patient': grpc.unary_unary_rpc_method_handler(
                    servicer.get_patient,
                    request_deserializer=patient__adapter__unary__pb2.PatientID.FromString,
                    response_serializer=patient__adapter__unary__pb2.AdaptedPatient.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PatientAdapterService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('PatientAdapterService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PatientAdapterService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_patient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/PatientAdapterService/get_patient',
            patient__adapter__unary__pb2.PatientID.SerializeToString,
            patient__adapter__unary__pb2.AdaptedPatient.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
