sounds = {
	innocent = {
		"example1.mp3"
	},
	traitor = {
		"example2.mp3"
	},
	timeout = {
		"example3.mp3"
	}
}

if SERVER then
	url = ( "http://127.0.0.1/audio/" )
	util.AddNetworkString("EndMusic")
	hook.Add("TTTEndRound", "endroundurl", function(result)
		local file = ""
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

	CreateClientConVar( "music", "1", true, false )
	CreateClientConVar( "music_vol", "0.75", true, false )
	
	hook.Add("TTTSettingsTabs", "setting", function(dtabs)
		custom = vgui.Create( "DPanel" )	
		list = vgui.Create( "DPanelList", custom )	
		list:SetSpacing( 5 )		
		list:Dock( FILL )
		list:DockMargin( 5, 5, 5, 0 )
		
		local volume = vgui.Create( "DNumSlider", list )
			volume:SetText( "Volume" )
			volume:SetDark(true)
			volume:SetMin( 0 )
			volume:SetMax( 1 )
			volume:SetDecimals( 2 )
			volume:SetConVar( "music_vol" ) 
				
		local check = vgui.Create( "DCheckBoxLabel", list )
			check:SetText( "Allow EndRound Music" )
			check:SetDark(true)
			check:SetConVar( "music" )
			
		list:AddItem( volume )
		list:AddItem( check )		
		
		dtabs:AddSheet( "Custom", custom, "icon16/tick.png" )
	end)
   
	net.Receive( "EndMusic", function() 
		music = GetConVar("music"):GetInt() 
		music_vol = GetConVar("music_vol"):GetFloat()
		if music then
			sound.PlayURL(net.ReadString(), "", function(station)
				if ( IsValid( station ) ) then
					station:Play()
					station:SetVolume(music_vol)
				end
			end)
		end
	end)
	
end
