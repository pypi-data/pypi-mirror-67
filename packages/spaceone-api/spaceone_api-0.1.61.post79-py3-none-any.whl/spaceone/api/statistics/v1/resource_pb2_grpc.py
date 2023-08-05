# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from spaceone.api.core.v1 import query_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_query__pb2
from spaceone.api.statistics.v1 import resource_pb2 as spaceone_dot_api_dot_statistics_dot_v1_dot_resource__pb2


class ResourceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.stat = channel.unary_unary(
                '/spaceone.api.statistics.v1.Resource/stat',
                request_serializer=spaceone_dot_api_dot_statistics_dot_v1_dot_resource__pb2.ResourceStatRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_core_dot_v1_dot_query__pb2.StatisticsInfo.FromString,
                )


class ResourceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ResourceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_statistics_dot_v1_dot_resource__pb2.ResourceStatRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_core_dot_v1_dot_query__pb2.StatisticsInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.statistics.v1.Resource', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Resource(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def stat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.statistics.v1.Resource/stat',
            spaceone_dot_api_dot_statistics_dot_v1_dot_resource__pb2.ResourceStatRequest.SerializeToString,
            spaceone_dot_api_dot_core_dot_v1_dot_query__pb2.StatisticsInfo.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
