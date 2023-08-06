#!cython
# -*- coding:utf-8 -*-
cimport cyHiSLIP

import struct 

ctypedef class MessageHeader:
    cdef short prologue #"HS"
    cdef unsigned char messageType 
    cdef unsinged char controlCode
    cdef unsinged int messageParameter
    cdef unsinged long payloadLength
    cdef char data[]
    cdef char *raw

    def __cinit__(self,messageType, controlCode, messageParameter, data=b""):
        sefl.prologue=b"HS"
        self.messageType=messageType
        self.controlCode=controlCode
        if type(messageParameter) is list: #
            self.messageParameter= messageParameter[0]& 0xff)
        elif type(messageParameter) is str:
            self.messageParameter=messageParameter & 0xffffffff
        else:
            self.messageParameter=messageParameter & 0xffffffff
        self.payloadLength=len(data)
        
    def unpack(self,data):
    """
    messageParameters: check the Table3 "HiSLIP message'  in the HiSLIP reference cocuments.
    """
        self.prologue=data[:2] # ASCII "HS"
        self.messageType=data[2] # Message Type 
        self.controlCode=data[3] # Control Code
        self.messageParameter=data[4:8] # Message Parameter. messageID for Data/DataEND/AsyncLock/AsyncRemoteLocalControl/Trigger/Interrupted/AsyncInterrupted/AsyncInterrupted messages
        ## Clients shall maintain a MessageID count that is initially set to 0xffff ff00. When clients send Data, DataEND or Trigger messages, they shall set the MessageID field of the message header to the current MessageID and increment the MessageID by two in an unsigned 32-bit sense (permitting wrap-around). (3.2.2. Overlap Mode requirement)
        self.payloadLength=long(data[8:16]) # PayloadLength (8byte int:
        self.data=data[16:] # len(self.data) should be self.payloadLength

    def pack(self):
        ""
        initial messageID is  0xffff ff00
        ""
        self.raw=struct.pack(
            "2cccil",
            self.prologue,
            self.messageType,
            self.controlCode,
            self.messageParameter,
            self.payloadLength)
        self.raw +=self.data # extend binary payload

    @classmethod
    def build_packet(cls, mtype, cc, mparm, payload):
        self.raw=struct.pack(
            "2cccil",
            "HS",
            mtype,
            cc,
            mparm,
            len(payload))
        self.raw +=pyload
        retrun self.raw

    @classmethod
    def unpack_packet(raw):
        obj=cls().unpack(raw)
        return obj
    
import socket
class HiSLIPDataTransferMessage:
    def __init__(self):
        super(HiSLIPDataTransferMessage, self).__init__()
        
cdef HiSLIPDevice:
    """
     Table 8 Synchronous Error Notification Transaction
     Table 10 Data Transfer Messages from Client to Server
     Table 11 Data Transfer Messages from Server to Client
     Table 12 Lock Transaction – Requesting a Lock
     Table 13 Lock Transaction – Releasing a Lock
     Table 15 Lock Behavior
     Table 16 Lock Info Transaction
     Table 17 RemoteLocal Control Transaction
     Table 18 Remote Local Control Transactions
     Table 19 Trigger Message
     Table 20 Vendor Defined Transaction
     Table 21 Maximum Message Size Transaction
     Table 22 Interrupted Transaction
     Table 23 Device Clear Complete Transaction
     Table 25 Service Request
     Table 26 Status Message
     3.2.2 Overlap Mode Client Requirements
     HiSLIP clients shall implement the following:
     1. In overlap mode, when sending AsyncStatusQuery the client shall place the MessageID of the most recent message that has been entirely delivered to the client in the message parameter.
     Clients shall maintain a MessageID count that is initially set to 0xffff ff00. When clients send Data, DataEND or Trigger messages, they shall set the MessageID field of the message header to the current MessageID and increment the MessageID by two in an unsigned 32-bit sense (permitting wrap-around).
     The MesssageID is reset after device clear, and when the connection is initialized. In overlap mode, the MessageID is only used for locking.

     3.1.2 Synchronized Mode Client Requirements
     HiSLIP clients shall implement the following:
     1. When receiving DataEND (that is an RMT) verify that the MessageID indicated in the DataEND message is
     the MessageID that the client sent to the server with the most recent Data, DataEND or Trigger message. If the MessageIDs do not match, the client shall clear any Data responses already buffered and discard the
     offending DataEND message.
     IVI-6.1: IVI High-Speed LAN Instrument Protocol 18 IVI Foundation
     2. When receiving Data messages if the MessageID is not 0xffff ffff, then verify that the MessageID indicated in the Data message is the MessageID that the client sent to the server with the most recent Data, DataEND or Trigger message.
     If the MessageIDs do not match, the client shall clear any Data responses already buffered and discard the offending Data message.
     3. When the client sends Data, DataEND or Trigger if there are any whole or partial server messages that have been validated per rules 1 and 2 and buffered they shall be cleared.
     4. When the client receives Interrupted or AsyncInterrupted it shall clear any whole or partial server messages that have been validated per rules 1 and 2.
     If the client initially detects AsyncInterrupted it shall also discard any further Data or DataEND messages from the server until Interrupted is encountered.
     If the client detects Interrupted before it detects AsyncInterrupted, the client shall not send any further messages until AsyncInterrupted is received.
     Clients shall maintain a MessageID count that is initially set to 0xffff ff00. When clients send Data, DataEND or Trigger messages, they shall set the message parameter field of the message header to the current MessageID and increment the MessageID by two in an unsigned 32-bit sense (permitting wrap-around).
     The MesssageID is reset to 0xffff ff00 after device clear, and when the connection is initialized. After interrupted error processing is complete, the client resumes normal operation.
     """
     
    def __init__(self,server, port=HiSLIPPort):# Table 5
        self.syncport=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.asyncport=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.syncport.connect((server, port))
        self.asyncport.connect((server, port))
        self.syncport.send(self.buidmessage(HiSLIPMessageType.Initialize, 0,))
        self.asyncport.send(self.buidmessage(HiSLIPMessageType.AsyncInitialize, 0,))
        
        self.messageID=0xffffff00
        
    def incrementMessageID(self):
        self.messageID +=2
        self.messageID &= 0xffffffff

    def resetMessageID(self):
        self.messageID=0xffffff00

    #
    def Open(self):
        pass

    def Write(self):
        pass
    
    def Read(self):
        pass
    
    def ReadSTB(self):
        pass
    
    def Clear(self):
        pass
    
    def Lock(self):
        pass
    
    def AsynLock(self):
        pass
    
    def Unlock(self):
        pass
    
     
