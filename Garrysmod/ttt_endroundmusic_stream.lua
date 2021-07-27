local sounds = {
	innocent = {
		"innocent1.mp3",
		"innocent2.mp3",
		"innocent3.mp3",
		"innocent4.mp3",
		"innocent5.mp3"
	},
	traitor = {
		"traitor1.mp3",
		"traitor2.mp3",
		"traitor3.mp3",
		"traitor4.mp3",
		"traitor5.mp3"
	},
	timeout = {
		"time.mp3"
	}
}


if SERVER then
	util.AddNetworkString("EndMusic")
	url = ( "http://" .. string.Split(game.GetIPAddress(),":")[1] .. ":80" .. "/audio/" )
	hook.Add("TTTEndRound", "endroundurl", function(result)
		if result == WIN_TRAITOR then
			file, _ = table.Random(sounds.traitor)
		elseif result == WIN_INNOCENT then
			file, _ = table.Random(sounds.innocent)
		else
			file, _ = table.Random(sounds.timeout)	
		end	
		net.Start("EndMusic")
			net.WriteString( url .. file)
        	net.Broadcast()
	end)
else

	CreateClientConVar( "music_vol", "1", true, false )
	
	hook.Add("TTTSettingsTabs", "setting", function(dtabs)
	
		dsettings = dtabs:GetItems()[2].Panel
		
		dform = vgui.Create("DForm")
		dform:SetName("EndRound Music")
			
		dform:NumSlider("Volume", "music_vol", 0, 1, 2 )
		
		dsettings:AddItem(dform)
		
	end)
   
	net.Receive( "EndMusic", function() 
		url = net.ReadString()
		music_vol = GetConVar("music_vol"):GetFloat()
		if music_vol then
			sound.PlayURL(url, "", function(station)
				if ( IsValid( station ) ) then
					station:Play()
					station:SetVolume(music_vol)
				end
			end)
		end
	end)
	
end
