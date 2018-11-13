# coding: utf-8

if __name__=='__main__':
    print("You can use this commands: 'wholive','start','startdefault','save','restore','shutdown','listactive','listdefined','listall','suspend','suspendF','resume','resumeF','destroy','reboot','quit','help'")
    flag=True
    while flag:
        command = input('>>')
        if  command == "startdefault":
            print('Starting 2F+1 VMs now!')
            #startdefault()
        if command == "start":
            print('Starting F+1 VMs now!')
            #start()
        elif command == "save":
            print('Saveing now!')
            #save()
        elif command == "restore":
            print('Restoring now!')
            #restore()
        elif command == "shutdown":
            print('Shutdowning all VMs now!')
            #shutdown()
        elif command =="listactive":
            print('Listing active domains now!')
            #listactive()
        elif command == "listdefined":
            print('Listing definded domains now!')
            #listdefined()
        elif command == "listall":
            print('Listing all domains now!')
            #listall()
        elif command == "suspend":
            print('Suspending now!')
            #suspend()
        elif command == "suspendF":
            print('Suspending to F+1 now!')
            #suspendF()
        elif command == "resume":
            print('Resuming now!')
            #resume()
        elif command == "resumeF":
            print('Resuming to F+1 now!')
            #resumeF()
        elif command == "destroy":
            print('Destroying now!')
            #destroy()
        elif command == "reboot":
            print('Rebooting now!')
            #reboot()
        elif command == "quit":
            flag=False
            #sys.exit(0)
        elif command == "wholive":
            #MulticasDom0 = groupCommunicationDom0.MulticasDom0()
            #MulticasDom0.run()
            pass
        elif command == "help":
            print("All commands: 'wholive','start','startdefault','save','restore','shutdown','listactive','listdefined','listall','suspend','suspendF','resume','resumeF','destroy','reboot','quit','help'")