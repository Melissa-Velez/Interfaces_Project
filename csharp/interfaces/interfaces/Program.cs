using System;
using Grpc.Core;
using RpcDemo;

namespace interfaces
{
    class Program
    {
        static void Main(string[] args)
        {
            Channel channel = new Channel("127.0.0.1:50051",ChannelCredentials.Insecure);
            var client = new coordinatesService.coordinatesServiceClient(channel);
            while (true) {
                var reply = client.getCoordinates(new RpcDemo.Empty { });
                Console.WriteLine(reply);
            }
        }
    }
}
