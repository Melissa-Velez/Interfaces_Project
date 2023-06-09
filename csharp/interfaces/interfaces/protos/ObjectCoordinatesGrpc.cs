// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: object_coordinates.proto
#region Designer generated code

using System;
using System.Threading;
using System.Threading.Tasks;
using grpc = global::Grpc.Core;

namespace RpcDemo {
  public static partial class coordinatesService
  {
    static readonly string __ServiceName = "RpcDemo.coordinatesService";

    static readonly grpc::Marshaller<global::RpcDemo.Empty> __Marshaller_Empty = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::RpcDemo.Empty.Parser.ParseFrom);
    static readonly grpc::Marshaller<global::RpcDemo.PointStamped> __Marshaller_PointStamped = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::RpcDemo.PointStamped.Parser.ParseFrom);

    static readonly grpc::Method<global::RpcDemo.Empty, global::RpcDemo.PointStamped> __Method_getCoordinates = new grpc::Method<global::RpcDemo.Empty, global::RpcDemo.PointStamped>(
        grpc::MethodType.Unary,
        __ServiceName,
        "getCoordinates",
        __Marshaller_Empty,
        __Marshaller_PointStamped);

    /// <summary>Service descriptor</summary>
    public static global::Google.Protobuf.Reflection.ServiceDescriptor Descriptor
    {
      get { return global::RpcDemo.ObjectCoordinatesReflection.Descriptor.Services[0]; }
    }

    /// <summary>Base class for server-side implementations of coordinatesService</summary>
    public abstract partial class coordinatesServiceBase
    {
      public virtual global::System.Threading.Tasks.Task<global::RpcDemo.PointStamped> getCoordinates(global::RpcDemo.Empty request, grpc::ServerCallContext context)
      {
        throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
      }

    }

    /// <summary>Client for coordinatesService</summary>
    public partial class coordinatesServiceClient : grpc::ClientBase<coordinatesServiceClient>
    {
      /// <summary>Creates a new client for coordinatesService</summary>
      /// <param name="channel">The channel to use to make remote calls.</param>
      public coordinatesServiceClient(grpc::Channel channel) : base(channel)
      {
      }
      /// <summary>Creates a new client for coordinatesService that uses a custom <c>CallInvoker</c>.</summary>
      /// <param name="callInvoker">The callInvoker to use to make remote calls.</param>
      public coordinatesServiceClient(grpc::CallInvoker callInvoker) : base(callInvoker)
      {
      }
      /// <summary>Protected parameterless constructor to allow creation of test doubles.</summary>
      protected coordinatesServiceClient() : base()
      {
      }
      /// <summary>Protected constructor to allow creation of configured clients.</summary>
      /// <param name="configuration">The client configuration.</param>
      protected coordinatesServiceClient(ClientBaseConfiguration configuration) : base(configuration)
      {
      }

      public virtual global::RpcDemo.PointStamped getCoordinates(global::RpcDemo.Empty request, grpc::Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return getCoordinates(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual global::RpcDemo.PointStamped getCoordinates(global::RpcDemo.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.BlockingUnaryCall(__Method_getCoordinates, null, options, request);
      }
      public virtual grpc::AsyncUnaryCall<global::RpcDemo.PointStamped> getCoordinatesAsync(global::RpcDemo.Empty request, grpc::Metadata headers = null, DateTime? deadline = null, CancellationToken cancellationToken = default(CancellationToken))
      {
        return getCoordinatesAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
      }
      public virtual grpc::AsyncUnaryCall<global::RpcDemo.PointStamped> getCoordinatesAsync(global::RpcDemo.Empty request, grpc::CallOptions options)
      {
        return CallInvoker.AsyncUnaryCall(__Method_getCoordinates, null, options, request);
      }
      /// <summary>Creates a new instance of client from given <c>ClientBaseConfiguration</c>.</summary>
      protected override coordinatesServiceClient NewInstance(ClientBaseConfiguration configuration)
      {
        return new coordinatesServiceClient(configuration);
      }
    }

    /// <summary>Creates service definition that can be registered with a server</summary>
    /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
    public static grpc::ServerServiceDefinition BindService(coordinatesServiceBase serviceImpl)
    {
      return grpc::ServerServiceDefinition.CreateBuilder()
          .AddMethod(__Method_getCoordinates, serviceImpl.getCoordinates).Build();
    }

  }
}
#endregion
