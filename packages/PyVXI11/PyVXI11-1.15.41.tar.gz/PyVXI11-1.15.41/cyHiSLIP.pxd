#!cython
# -*- coding:utf-8 -*-

cdef int HiSLIPPort=4880        # not in /etc/services used for both sync/async
cdef int SCPIRawSocketPort=5025 # both udp/tcp
cdef int SCPITelnetPort=5024    # both udp/tcp

cdef enum HiSLIPMessageType:
     """
     Table 3. HiSLIP messages
     Table 4. Message Type Value Definitions
     """
     # sync
     Initialize=0          
     InitializeResPonce=1  
     FatalError=2          
     Error=3               
     # async
     AsynLock=4
     AsynLockResponse=5,
     # sync
     Data=6
     DataEnd=7
     DeviceClearComplete=8
     # async
     DeviceCLearAcknowledge=9
     AsyncRemoteLocalContro=10 
     AsyncRemoteLocalResponcse=11
     #s sync
     Trigger=12
     Interrupted=13
     # async
     AsyncInterrupted=14 
     AsyncMaximumMessageSize=15 
     AsyncMaximumMessageSizeResponse=16
     AsyncInitilalize=17
     AsyncIntializeResponse=18
     AsyncDeviceClear=19
     AsyncServiceRequest=20
     AsynStatusQuery=21
     AsyncStatusResponse=22
     AsyncDeviceClearAcknowledge=23
     AsynLockInfo=24 
     AsynLockInfoResponse=25
     # N/A
     # reserved for future use: 26-127
     # Ether
     # VendorSpecific 128-255 inclusive

cdef enum FatalErrorCodes: # Defined Fatal Error codes. Table-7
        UndefinedError=0
        PoorlyFormedMessage=1
        UnEstablishedConnection=2
        InvalidInitializationSequence=3
        ServerRefued=4
        # 5-127 : reserved
        FirstDeviceDefinedError=128
        # 128-255 : Device Defined Error

cdef enum ErrorCode:  # defined Error codes(non-fatal). Table-9
        UndefinedError=0
        UnrecognizedMessageType=1
        UnrecognizedControlCode=2
        UnrecognizedVendorDefinedMessage=3
        MessageTooLarge=4
        # 5-127 : Reserved
        FirstDviceDefinedError=128
        #128-255:Device Defined Error

cdef enum  LockControlCode: # Table 14 Lock request/release operation descriptions
        release=0
        request=1

cdef enum LockResponseControlCode:
        fail=0   # /Lock was requested but not granted (timeout expired)
        success=1   # Release of exclusive lock was granted./The lock was requested and granted
        successSharedLock=2 # Release of shared lock was granted
        error=3 #Invalid attempt to release a lock that was not acquired./Invalid (redundant) request that is, requesting a lock already granted

cdef RemoteLocalControlCode: # Table 18 Remote Local Control Transactions
    # Control Code (request), Corresponding VISA mode ,RemoteEnable/Local Lockout/Remote  
    disableRemote=0 # VI_GPIB_REN_DEASSERT             F/F/F
    enableRemote=1  # VI_GPIB_REN_ASSERT               T/nc/nc
    disableAndGTL=2 # VI_GPIB_REN_DEASSERT_GTL         F/F/F
    enableAndGotoRemote=3 # VI_GPIB_REN_ASSERT_ADDRESS T/nc/T
    enableAndLockoutLocal=4 # VI_GPIB_REN_ASSERT_LLO   T/T/nc
    enableAndGTRLLO=5 # VI_GPIB_REN_ASSERT_ADDRESS_LLO T/T/T
    justGTL=6         # VI_GPIB_REN_ADDRESS_GTL        nc/nc/F


