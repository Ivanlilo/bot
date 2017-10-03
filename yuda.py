        self.sender = cl.getContactOrRoomOrGroupById(message._from)

        self.receiver = cl.getContactOrRoomOrGroupById(message.to)