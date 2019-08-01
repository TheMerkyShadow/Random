using System;
using System.Linq;
using System.Collections.Generic;
using System.Timers;
using Sandbox.Common.ObjectBuilders;
using Sandbox.Definitions;
using Sandbox.Game;
using Sandbox.Game.WorldEnvironment;
using Sandbox.Game.SessionComponents;
using Sandbox.Game.Gui;
using Sandbox.ModAPI;

using VRage.ObjectBuilders;
using VRage.Collections;
using VRage.Game;
using VRage.Game.Components;
using VRage.Game.ModAPI;
using VRage.ModAPI;
using VRageMath;

public class Merky : MySessionComponentBase
{

    public Merky()
    {
        var timer = new System.Timers.Timer();
        timer.Elapsed += new ElapsedEventHandler(this.Think);
        timer.Interval = 1000; // 1 second
        timer.Enabled = true;

    }

    public void Think(object sender, ElapsedEventArgs args)
    {

        var SpawnPlanet = MyAPIGateway.Session.GetWorld().Planets[0];
        var pos = SpawnPlanet.PositionAndOrientation.Value.Position;
        
        var players = new List<IMyPlayer>();
        MyAPIGateway.Players.GetPlayers(players);

        foreach (var ply in players)
        {

            var identify = ply.Identity;
            var character = ply.Character;

            if (!character.IsDead)
            {

                var max = (SpawnPlanet.Radius + SpawnPlanet.AtmosphereRadius);
                var dist = Vector3D.Distance(pos, ply.GetPosition());

                if (dist >= max) { character.Kill(); }

            }

        }

    }

}



