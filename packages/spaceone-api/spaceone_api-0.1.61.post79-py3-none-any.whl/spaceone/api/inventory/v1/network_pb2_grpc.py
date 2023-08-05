# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from spaceone.api.core.v1 import query_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_query__pb2
from spaceone.api.inventory.v1 import network_pb2 as spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2


class NetworkStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.inventory.v1.Network/create',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.CreateNetworkRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworkInfo.FromString,
                )
        self.update = channel.unary_unary(
                '/spaceone.api.inventory.v1.Network/update',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.UpdateNetworkRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworkInfo.FromString,
                )
        self.pin_data = channel.unary_unary(
                '/spaceone.api.inventory.v1.Network/pin_data',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.PinNetworkDataRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworkInfo.FromString,
                )
        self.delete = channel.unary_unary(
                '/spaceone.api.inventory.v1.Network/delete',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworkRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.get = channel.unary_unary(
                '/spaceone.api.inventory.v1.Network/get',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.GetNetworkRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworkInfo.FromString,
                )
        self.list = channel.unary_unary(
                '/spaceone.api.inventory.v1.Network/list',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworkQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworksInfo.FromString,
                )
        self.stat = channel.unary_unary(
                '/spaceone.api.inventory.v1.Network/stat',
                request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworkStatQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_core_dot_v1_dot_query__pb2.StatisticsInfo.FromString,
                )


class NetworkServicer(object):
    """Missing associated documentation comment in .proto file"""

    def create(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def pin_data(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NetworkServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.CreateNetworkRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworkInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.UpdateNetworkRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworkInfo.SerializeToString,
            ),
            'pin_data': grpc.unary_unary_rpc_method_handler(
                    servicer.pin_data,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.PinNetworkDataRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworkInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworkRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.GetNetworkRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworkInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworkQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworksInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworkStatQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_core_dot_v1_dot_query__pb2.StatisticsInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.inventory.v1.Network', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Network(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.Network/create',
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.CreateNetworkRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworkInfo.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.Network/update',
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.UpdateNetworkRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworkInfo.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def pin_data(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.Network/pin_data',
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.PinNetworkDataRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworkInfo.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.Network/delete',
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworkRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.Network/get',
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.GetNetworkRequest.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworkInfo.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def list(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.Network/list',
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworkQuery.SerializeToString,
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworksInfo.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/spaceone.api.inventory.v1.Network/stat',
            spaceone_dot_api_dot_inventory_dot_v1_dot_network__pb2.NetworkStatQuery.SerializeToString,
            spaceone_dot_api_dot_core_dot_v1_dot_query__pb2.StatisticsInfo.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
