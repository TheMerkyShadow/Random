AddCSLuaFile()

ENT.Type = "anim"
ENT.Base = "base_gmodentity"

ENT.PrintName = "Merky_Nade"
ENT.Category = "Other"

ENT.Editable = true
ENT.Spawnable = true
ENT.AdminOnly = false

ENT.Delay = 5


function ENT:SpawnFunction( ply, tr, ClassName )
	if ( !tr.Hit ) then return end
	local size = math.random( 16, 48 )
	local ent = ents.Create( ClassName )
	ent:SetPos( tr.HitPos + tr.HitNormal * size )
	ent:Spawn()
	ent:Activate()
	return ent
end

function ENT:Initialize()

    self:SetModel( "models/Combine_Helicopter/helicopter_bomb01.mdl" )
    self:PhysicsInit(SOLID_VPHYSICS)
    self:SetMoveType( MOVETYPE_VPHYSICS )
    self:SetSolid(SOLID_VPHYSICS)

    local phys = self:GetPhysicsObject()
    if (phys:IsValid()) then
        phys:Wake()
    end   
	
    if !SERVER then return end
 
    self.Nade = ents.Create("env_explosion")
    self.Nade:SetPos( self:GetPos() )
    self.Nade:SetParent( self )
    self.Nade:SetKeyValue( "iMagnitude", "100" )
    self.Nade:Spawn()
	
    timer.Simple( self.Delay, function() self:Explode() end)
	
end

function ENT:Explode()
    if !SERVER then return end
    SafeRemoveEntityDelayed(self,0.1)
    self.Nade:Fire("Explode", 0, 0 ) 	
end

