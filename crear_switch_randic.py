f=open("switches.txt","r")
for switch in f:
#    print "add     user            %s     spinyol" % (switch.rstrip().lower(),)
#    print "add     userpassword    %s     Cambiame_123" % (switch.rstrip().lower(),)
#    print "add     password        %s     Cambiame_123" % (switch.rstrip().lower(),)
#    print switch.rstrip().lower()
    print "%s:h3c:up" % (switch.rstrip().upper(),)
