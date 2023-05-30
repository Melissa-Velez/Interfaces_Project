using System;
using System.Threading.Tasks; // no agregado
using Grpc.Core;
using RpcCoordinates;

class rpc_Coordinates{
    static async Task Main(string[] args)
    {
        var channel = new Channel("127.0.0.1:50051", ChannelCredentials.Insecure);
        var client = new coordinatesService(channel); // .????

        var response = await client.ObtenerCoordenadasAsync(new TuSolicitudDeCoordenadas()); // Reemplaza "ObtenerCoordenadasAsync" y "TuSolicitudDeCoordenadas" con los nombres de los métodos y mensajes definidos en tu servicio RPC.
        Console.WriteLine($"Coordenadas: X = {response.X}, Y = {response.Y}"); // Reemplaza "X" y "Y" con los nombres de los campos de la respuesta de tu servicio RPC.
        await channel.ShutdownAsync();
    }
}

// V2 -----------------------
using Google.Protobuf.WellKnownTypes;

namespace RpcDemo
{
    public partial class PointStamped
    {
        public PointStamped()
        {
        }

        public PointStamped(float x, float y)
        {
            Header = new Header();


// \V2 ------------------------



// 
//////////// ---------------------------
using RpcDemo;

namespace RpcDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            Channel channel = new Channel("127.0.0.1:50051", ChannelCredentials.Insecure);

            var client = new CoordsComm.CoordsCommClient(channel);
            while (true){
                var reply = client.GetCoords(new RpcDemo.Empty {});
                Console.WriteLine(reply);
            }
        }
    }
}