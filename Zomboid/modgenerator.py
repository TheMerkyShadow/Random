Mods = []
WorkshopItems = []

def Add(name,id):
    Mods.append(name)
    WorkshopItems.append(id)

if __name__ == "__main__":

    Add("Skateboard","2728300240")
    Add("SurvivorRadioV3.4","2224576262")
    
    print( 'Mods=' +";".join(Mods) )
    print( 'WorkshopItems=' +";".join(WorkshopItems) ) 
