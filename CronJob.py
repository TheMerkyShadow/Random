import os
import sys

from crontab import CronTab

class CronJob:
    """
 
    id      - A unique string identifier.
    cmd     - The console command.
    time    - A string slice or special variable.
    
    state   - The state of the cron job.
      * None   = Remove if it exists.
      * True   = Enable.
      * False  = Disable.

    user    - Specify user to run on (default: root)

    """
    def __init__(self, id, cmd, time, state=True, user="root" ):
        self.Cron = CronTab(user)
        self.Validate(id,cmd)
        self.SetTime(time)
        self.SetEnabled(state)        
        self.Save(state)
        
    def Validate(self,id,cmd):
        self.Job = next( self.Cron.find_comment(id), None)
        if self.Job is None:
            self.Job = self.Cron.new(comment=id,command=cmd)
            self.Job.every_reboot()
        self.SetCommand(cmd)

    def SetCommand(self,cmd):
        self.Job.set_command(cmd)

    def SetTime(self,time):
        self.Job.slices.setall(time)   

    def SetEnabled(self,state):
        self.Job.enable(state)
        
    def Save(self,state):
        if state is None:
            self.Cron.remove(self.Job)    
        self.Cron.write() 
        return
     
# Example Of Usage          
CronJob( "Test", "touch test", "@reboot", state = True )
