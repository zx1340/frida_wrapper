traceconfig = {
'Method':[
	# 'android.content.Intent.setClassName',
	# 'android.content.Intent.putExtra'
	# 'android.os.B'
	# 'java.lang.StringBuilder.toString',
	# 'android.os.Parcel.nativeMarshall',
	# 'android.os.Parcel.marshall',
	# 'android.os.Parcel.nativeReadString',
	# 'android.os.Parcel.nativeWriteString',
	# 'android.os.Parcel.nativeWriteByteArray',
    # 'android.os.Parcel.nativeWriteInt',
    # 'android.os.Parcel.nativeWriteLong',
    # 'android.os.Parcel.nativeWriteFloat',
    # 'android.os.Parcel.nativeWriteDouble',
    # 'android.os.Parcel.nativeWriteString',
    # 'android.os.Parcel.nativeWriteStrongBinder',
	# 'android.os.Parcel.readInt'
	# 'android.os.Parcel.writeStringArray',
	# 'android.os.Parcel.writeInt',
	# 'com.google.android.gms.fido.fido2.api.common.PublicKeyCredentialDescriptor.writeToParcel',
	# 'slv.a',
],
'Class':[
	# 'ybx',
	# 'cmx'
	# 'com.google.android.gms.fido.fido2.ui.Fido2FullScreenActivity',
	# 'com.google.android.gms.fido.fido2.ui.AuthenticateChimeraActivity',
	# 'com.google.android.gms.fido.fido2.api.common.PublicKeyCredentialCreationOptions',
	# 'com.google.android.gms.fido.fido2.api.common.PublicKeyCredentialUserEntity',
	# 'xqw',	# call from fullscreen 
# 	'cdsl',
'java.security.KeyStore'
#'android.os.Parcel'
# 'skx',
# 'xzm',
# 'smb',
# 'xoh',
# 'xrc',
# 'xrr',
# 'xxp',
# 'xzy',
# 'yet',
# 'yfy',
# 'yfz',
# 'ygd',
	],
'BacktraceBlock':[
	'Dropbox'
	],
'BacktradeWhiteList':[
	'PublicKeyCredentialCreationOptions'
	]
}

# phook com.google.android.gms.fido.fido2.api.common

"""
12-20 14:43:22.186  1357  3893 I ActivityTaskManager: START u0 {cmp=com.google.android.gms/.fido.fido2.ui.Fido2FullScreenActivity (has extras)} from uid 10051
12-20 14:43:22.187   836   836 D android.hardware.power@1.3-service.pixel-libperfmgr: LAUNCH: 1
12-20 14:43:22.198 25335 25335 W ActivityThread: handleWindowVisibility: no activity for token android.os.BinderProxy@5199f3a
12-20 14:43:22.212 25335 25335 I Fido    : [AuthenticateChimeraActivity] FIDO2 operation is called from com.example.android.fido2
12-20 14:43:22.214 25335 25335 I Fido    : [StringStoreKeyHandleCache] initU2fDeviceCache
12-20 14:43:22.222 25335 25335 I Fido    : [FidoApiImpl] updateTransaction is called for resume
12-20 14:43:22.268  1357  1417 I ActivityTaskManager: Displayed com.google.android.gms/.fido.fido2.ui.Fido2FullScreenActivity: +71ms
12-20 14:43:22.275   836   836 D android.hardware.power@1.3-service.pixel-libperfmgr: LAUNCH: 0
12-20 14:43:22.421  1357  1369 I system_server: Background concurrent copying GC freed 392038(20MB) AllocSpace objects, 20(860KB) LOS objects, 42% free, 32MB/56MB, paused 120us total 222.527ms
12-20 14:43:22.428   898   898 I keystore: del USRPKEY_1.IDL+AFBLTIvGmAoL02n8pe9yiJ+Hi8n+bjuPS8/Gp3E=.webauthn-codelab.glitch.me 10051
12-20 14:43:22.428   898   898 I keystore: del USRSKEY_1.IDL+AFBLTIvGmAoL02n8pe9yiJ+Hi8n+bjuPS8/Gp3E=.webauthn-codelab.glitch.me 10051
12-20 14:43:22.429   898   898 I keystore: del USRCERT_1.IDL+AFBLTIvGmAoL02n8pe9yiJ+Hi8n+bjuPS8/Gp3E=.webauthn-codelab.glitch.me 10051
12-20 14:43:22.430   898   898 I keystore: del CACERT_1.IDL+AFBLTIvGmAoL02n8pe9yiJ+Hi8n+bjuPS8/Gp3E=.webauthn-codelab.glitch.me 10051
12-20 14:43:22.450   898 25664 D DropBoxManager: About to call service->add()
12-20 14:43:22.451  1357  1855 I DropBoxManagerService: add tag=keymaster isTagEnabled=true flags=0x0
12-20 14:43:22.453   898 25664 D DropBoxManager: service->add returned No error
12-20 14:43:22.499  1357  1855 I ActivityTaskManager: START u0 {act=android.app.action.CONFIRM_DEVICE_CREDENTIAL pkg=com.android.settings cmp=com.android.settings/.password.ConfirmDeviceCredentialActivity (has extras)} from uid 10051
12-20 14:43:22.508   836   836 D android.hardware.power@1.3-service.pixel-libperfmgr: LAUNCH: 1
12-20 14:43:22.516 25335 25335 I Fido    : [FidoApiImpl] updateTransaction is called for pause
12-20 14:43:22.517 13218 13218 W ActivityThread: handleWindowVisibility: no activity for token android.os.BinderProxy@f7a739d
12-20 14:43:22.535  1357  1357 D BiometricService: Creating auth session. Modality: 1, cookie: 212854890
12-20 14:43:22.536  1357  1357 V FingerprintService: startAuthentication(com.android.settings)
12-20 14:43:22.536  1357  1357 V FingerprintService: Returning cookie: 212854890
12-20 14:43:22.536  1357  1357 D BiometricService: Matched cookie: 212854890, 0 remaining
12-20 14:43:22.536  1357  1357 V FingerprintService: starting client AuthenticationClientImpl(com.android.settings) cookie: 212854890/212854890
12-20 14:43:22.536   933  1126 I fpc_tac : fpc_irq_wait {{20,10,0},{17,1,1}}
12-20 14:43:22.536   933  1126 E fpc_tac : fpc_irq_wait error FPC_ERROR_CANCELLED
12-20 14:43:22.553  1357  1357 W FingerprintService: client com.android.settings is authenticating...
12-20 14:43:22.554  1831  1831 D BiometricDialogImpl: showBiometricDialog, type: 1, requireConfirmation: false
12-20 14:43:22.563  1831  1831 D BiometricDialogImpl: handleShowDialog,  savedState: null mCurrentDialog: com.android.systemui.biometrics.FingerprintDialogView{3c0060b V.E...... ......I. 0,0-1080,2040} newDialog: com.android.systemui.biometrics.FingerprintDialogView{9040804 V.E...... ......I. 0,0-0,0} type: 1
12-20 14:43:22.579  1357  1417 I ActivityTaskManager: Displayed com.android.settings/.password.ConfirmDeviceCredentialActivity: +75ms
12-20 14:43:22.593   836   836 D android.hardware.power@1.3-service.pixel-libperfmgr: LAUNCH: 0
12-20 14:43:23.348   837  1160 D VSC     : @ 176455.299: [Significant Motion] Stop motion_detect
12-20 14:43:23.348   837  1160 D VSC     : @ 176455.300: [Significant Motion] Request accel, interval 20000000 ns, latency 3200000000 ns
12-20 14:43:23.548 25335 25382 E bqyh    : RuntimeException while executing runnable bqyv{yar@36b1cf9} with executor MoreExecutors.directExecutor()
12-20 14:43:23.548 25335 25382 E bqyh    : java.lang.IllegalStateException
12-20 14:43:23.548 25335 25382 E bqyh    : 	at bmyz.b(:com.google.android.gms@19629037@19.6.29 (120400-278422107):3)
12-20 14:43:23.548 25335 25382 E bqyh    : 	at yhc.a(:com.google.android.gms@19629037@19.6.29 (120400-278422107):12)
12-20 14:43:23.548 25335 25382 E bqyh    : 	at yau.h(:com.google.android.gms@19629037@19.6.29 (120400-278422107):6)
12-20 14:43:23.548 25335 25382 E bqyh    : 	at yar.a(:com.google.android.gms@19629037@19.6.29 (120400-278422107):2)
12-20 14:43:23.548 25335 25382 E bqyh    : 	at bqyv.run(:com.google.android.gms@19629037@19.6.29 (120400-278422107):4)
12-20 14:43:23.548 25335 25382 E bqyh    : 	at bqye.execute(Unknown Source:0)
12-20 14:43:23.548 25335 25382 E bqyh    : 	at bqyh.b(:com.google.android.gms@19629037@19.6.29 (120400-278422107):1)
12-20 14:43:23.548 25335 25382 E bqyh    : 	at bqyh.a(:com.google.android.gms@19629037@19.6.29 (120400-278422107):4)
12-20 14:43:23.548 25335 25382 E bqyh    : 	at swu.done(Unknown Source:5)
12-20 14:43:23.548 25335 25382 E bqyh    : 	at java.util.concurrent.FutureTask.finishCompletion(FutureTask.java:383)
12-20 14:43:23.548 25335 25382 E bqyh    : 	at java.util.concurrent.FutureTask.set(FutureTask.java:234)
12-20 14:43:23.548 25335 25382 E bqyh    : 	at java.util.concurrent.FutureTask.run(FutureTask.java:274)
12-20 14:43:23.548 25335 25382 E bqyh    : 	at swp.b(:com.google.android.gms@19629037@19.6.29 (120400-278422107):15)
12-20 14:43:23.548 25335 25382 E bqyh    : 	at swp.run(:com.google.android.gms@19629037@19.6.29 (120400-278422107):10)
12-20 14:43:23.548 25335 25382 E bqyh    : 	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1167)
12-20 14:43:23.548 25335 25382 E bqyh    : 	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:641)
12-20 14:43:23.548 25335 25382 E bqyh    : 	at tcn.run(Unknown Source:7)
12-20 14:43:23.548 25335 25382 E bqyh    : 	at java.lang.Thread.run(Thread.java:919)
12-20 14:43:23.778  1831  1851 D Elmyra/Logger: Receiving pull request from statsd.
12-20 14:43:23.785   821   821 V ContextHubHal: sendMessageToHub
12-20 14:43:23.787   837  1160 D CHRE    : @ 176455.739: Parsed nanoapp message from host: app ID 0x476f6f676c00100e, endpoint 0x1, msgType 203, payload size 2
12-20 14:43:23.791  1831  1851 D Elmyra/Logger: Snapshot took 13 milliseconds.
12-20 14:43:24.455  1357  1418 W BroadcastQueue: Background execution not allowed: receiving Intent { act=android.intent.action.DROPBOX_ENTRY_ADDED flg=0x10 (has extras) } to com.google.android.gms/.stats.service.DropBoxEntryAddedReceiver
12-20 14:43:24.456  1357  1418 W BroadcastQueue: Background execution not allowed: receiving Intent { act=android.intent.action.DROPBOX_ENTRY_ADDED flg=0x10 (has extras) } to com.google.android.gms/.chimera.GmsIntentOperationService$PersistentTrustedReceiver
12-20 14:43:24.769   821   821 V ContextHubHal: sendMessageToHub
12-20 14:43:24.771   837  1160 D CHRE    : @ 176456.723: Parsed nanoapp message from host: app ID 0x476f6f676c00100e, endpoint 0x1, msgType 203, payload size 13
12-20 14:43:24.772   933  1125 D fpc_hidl: onAcquired(code=5, vendor=0)
12-20 14:43:24.776  1357  1357 V FingerprintService: Acquired: 5 0
12-20 14:43:24.780  1831  1831 D BiometricDialogImpl: onBiometricHelp: Finger moved too fast. Please try again.
12-20 14:43:24.782  1831  1831 D BiometricDialogImpl: handleBiometricHelp: Finger moved too fast. Please try again.
12-20 14:43:25.106   933  1125 D fpc_hidl: onAcquired(code=0, vendor=0)
12-20 14:43:25.107  1357  1357 V FingerprintService: Acquired: 0 0
12-20 14:43:25.111   933  1125 D fpc_hidl: onAuthenticated(fid=-2121288470, gid=0)
12-20 14:43:25.112  1357  1357 V BiometricStats: Authentication latency: 5
12-20 14:43:25.112  1357  1357 V FingerprintService: onAuthenticated(true), ID:-2121288470, Owner: com.android.settings, isBP: true, listener: com.android.server.biometrics.fingerprint.FingerprintService$BiometricPromptServiceListenerImpl@5db88ed, requireConfirmation: false, user: 0
12-20 14:43:25.118  1357  1357 V FingerprintService: Done with client: com.android.settings
12-20 14:43:25.119   898   898 D keystore: AddAuthenticationToken: timestamp = 176456857, time_received = 63525
12-20 14:43:25.129  1831  1831 D BiometricDialogImpl: onBiometricAuthenticated: true reason: null
12-20 14:43:25.132 13218 13218 D ConfirmDeviceCredentialActivity: Authenticating: false
12-20 14:43:25.133  1357  3893 W ActivityTaskManager: Duplicate finish request for ActivityRecord{4a32236 u0 com.android.settings/.password.ConfirmDeviceCredentialActivity t782 f}
12-20 14:43:25.144  1831  1831 D BiometricDialogImpl: handleBiometricAuthenticated: true
12-20 14:43:25.162  1831  1831 D BiometricDialogImpl: handleHideDialog, userCanceled: false
12-20 14:43:25.162  1831  1831 I Elmyra/ElmyraService: Unblocked; current action: SetupWizardAction
12-20 14:43:25.163  1831  1831 I Elmyra/ElmyraService: Unblocked; current action: SetupWizardAction
12-20 14:43:25.205 25335 25335 I Fido    : [FidoApiImpl] updateTransaction is called for resume
12-20 14:43:25.207 25335 25379 I Fido    : [RequestController] Timeout Runnable is removed, and timer is stopped.
12-20 14:43:25.209 25335 25335 D AndroidRuntime: Shutting down VM
12-20 14:43:25.210 25335 25335 E AndroidRuntime: FATAL EXCEPTION: main
12-20 14:43:25.210 25335 25335 E AndroidRuntime: Process: com.google.android.gms.ui, PID: 25335
12-20 14:43:25.210 25335 25335 E AndroidRuntime: java.lang.RuntimeException: Unable to resume activity {com.google.android.gms/com.google.android.gms.fido.fido2.ui.Fido2FullScreenActivity}: java.lang.NullPointerException: Attempt to invoke interface method 'java.lang.Object java.util.Map.put(java.lang.Object, java.lang.Object)' on a null object reference
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	at android.app.ActivityThread.performResumeActivity(ActivityThread.java:4205)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	at android.app.ActivityThread.handleResumeActivity(ActivityThread.java:4237)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	at android.app.servertransaction.ResumeActivityItem.execute(ResumeActivityItem.java:52)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	at android.app.servertransaction.TransactionExecutor.executeLifecycleState(TransactionExecutor.java:176)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	at android.app.servertransaction.TransactionExecutor.execute(TransactionExecutor.java:97)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:2016)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	at android.os.Handler.dispatchMessage(Handler.java:107)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	at android.os.Looper.loop(Looper.java:214)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	at android.app.ActivityThread.main(ActivityThread.java:7356)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	at java.lang.reflect.Method.invoke(Native Method)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:492)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:930)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: Caused by: java.lang.NullPointerException: Attempt to invoke interface method 'java.lang.Object java.util.Map.put(java.lang.Object, java.lang.Object)' on a null object reference
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	at xrc.a(:com.google.android.gms@19629037@19.6.29 (120400-278422107):25)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	at yau.b(:com.google.android.gms@19629037@19.6.29 (120400-278422107):13)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	at xqw.a(:com.google.android.gms@19629037@19.6.29 (120400-278422107):39)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	at com.google.android.gms.fido.fido2.ui.AuthenticateChimeraActivity.a(:com.google.android.gms@19629037@19.6.29 (120400-278422107):27)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	at com.google.android.gms.fido.fido2.ui.AuthenticateChimeraActivity.onResume(Unknown Source:5)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	at com.google.android.chimera.Activity.publicOnResume(Unknown Source:0)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	at qrr.onResume(:com.google.android.gms@19629037@19.6.29 (120400-278422107):2)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	at android.app.Instrumentation.callActivityOnResume(Instrumentation.java:1453)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	at android.app.Activity.performResume(Activity.java:7939)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	at android.app.ActivityThread.performResumeActivity(ActivityThread.java:4195)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: 	... 11 more
12-20 14:43:25.217 25335 25379 I Fido    : [RequestController] Timeout Runnable is removed, and timer is stopped.
12-20 14:43:25.223 25335 25335 I GCore-Chimera-Crash: ChgKB2Fkc19mZHIQpuqBChiBAiDguICvjgYKZAoJY29udGFpbm
12-20 14:43:25.223 25335 25335 I GCore-Chimera-Crash: VyEKDndxhAIJC38o9JKgZicmVsbGEqD2JyZWxsYV9keW5hbWl0
12-20 14:43:25.223 25335 25335 I GCore-Chimera-Crash: ZSoJZmFzdF9wYWlyKg52aXNpb24uYmFyY29kZSoLdmlzaW9uLm
12-20 14:43:25.223 25335 25335 I GCore-Chimera-Crash: ZhY2UqCnZpc2lvbi5vY3IKGgoIcGF5bWVudHMQ6fHpXRiBAiCQ
12-20 14:43:25.223 25335 25335 I GCore-Chimera-Crash: xcy74d4sIAA=
12-20 14:43:25.223 25335 25335 I GCore-Chimera-Crash: GCore-Chimera-Crash
12-20 14:43:25.232 25335 25335 I DeviceDrDatabaseHelper: Cleaning stale data from database!
12-20 14:43:25.241 25335 25335 W DeviceDoctorHandler: Crash Hash: 5f7b77a80285dcd5b44d7125ba7d20cf4837b6c9
12-20 14:43:25.261 25335 25335 W DeviceDoctorHandler: Shushing due to low average crash frequency.
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: FATAL EXCEPTION: main
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: Process: com.google.android.gms.ui, PID: 25335
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: java.lang.RuntimeException: Unable to resume activity {com.google.android.gms/com.google.android.gms.fido.fido2.ui.Fido2FullScreenActivity}: java.lang.NullPointerException: Attempt to invoke interface method 'java.lang.Object java.util.Map.put(java.lang.Object, java.lang.Object)' on a null object reference
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	at android.app.ActivityThread.performResumeActivity(ActivityThread.java:4205)
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	at android.app.ActivityThread.handleResumeActivity(ActivityThread.java:4237)
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	at android.app.servertransaction.ResumeActivityItem.execute(ResumeActivityItem.java:52)
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	at android.app.servertransaction.TransactionExecutor.executeLifecycleState(TransactionExecutor.java:176)
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	at android.app.servertransaction.TransactionExecutor.execute(TransactionExecutor.java:97)
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:2016)
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	at android.os.Handler.dispatchMessage(Handler.java:107)
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	at android.os.Looper.loop(Looper.java:214)
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	at android.app.ActivityThread.main(ActivityThread.java:7356)
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	at java.lang.reflect.Method.invoke(Native Method)
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:492)
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:930)
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: Caused by: java.lang.NullPointerException: Attempt to invoke interface method 'java.lang.Object java.util.Map.put(java.lang.Object, java.lang.Object)' on a null object reference
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	at xrc.a(:com.google.android.gms@19629037@19.6.29 (120400-278422107):25)
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	at yau.b(:com.google.android.gms@19629037@19.6.29 (120400-278422107):13)
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	at xqw.a(:com.google.android.gms@19629037@19.6.29 (120400-278422107):39)
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	at com.google.android.gms.fido.fido2.ui.AuthenticateChimeraActivity.a(:com.google.android.gms@19629037@19.6.29 (120400-278422107):27)
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	at com.google.android.gms.fido.fido2.ui.AuthenticateChimeraActivity.onResume(Unknown Source:5)
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	at com.google.android.chimera.Activity.publicOnResume(Unknown Source:0)
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	at qrr.onResume(:com.google.android.gms@19629037@19.6.29 (120400-278422107):2)
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	at android.app.Instrumentation.callActivityOnResume(Instrumentation.java:1453)
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	at android.app.Activity.performResume(Activity.java:7939)
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	at android.app.ActivityThread.performResumeActivity(ActivityThread.java:4195)
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler: 	... 11 more
12-20 14:43:25.261 25335 25335 E DeviceDoctorHandler:
12-20 14:43:25.265  1357  2004 I DropBoxManagerService: add tag=system_app_crash isTagEnabled=true flags=0x2
12-20 14:43:25.267 25335 25335 I Process : Sending signal. PID: 25335 SIG: 9
12-20 14:43:25.268  1357  1418 W BroadcastQueue: Background execution not allowed: receiving Intent { act=android.intent.action.DROPBOX_ENTRY_ADDED flg=0x10 (has extras) } to com.google.android.gms/.stats.service.DropBoxEntryAddedReceiver
12-20 14:43:25.268  1357  1418 W BroadcastQueue: Background execution not allowed: receiving Intent { act=android.intent.action.DROPBOX_ENTRY_ADDED flg=0x10 (has extras) } to com.google.android.gms/.chimera.GmsIntentOperationService$PersistentTrustedReceiver
12-20 14:43:25.282  1357  1691 W InputDispatcher: channel '5f81a12 com.google.android.gms/com.google.android.gms.fido.fido2.ui.Fido2FullScreenActivity (server)' ~ Consumer closed input channel or an error occurred.  events=0x9
12-20 14:43:25.282  1357  1691 E InputDispatcher: channel '5f81a12 com.google.android.gms/com.google.android.gms.fido.fido2.ui.Fido2FullScreenActivity (server)' ~ Channel is unrecoverably broken and will be disposed!
12-20 14:43:25.285  1357  2076 I ActivityManager: Process com.google.android.gms.ui (pid 25335) has died: fore TOP
12-20 14:43:25.285  1357  1421 I libprocessgroup: Successfully killed process cgroup uid 10051 pid 25335 in 0ms
12-20 14:43:25.285  1357  2199 I WindowManager: WIN DEATH: Window{5f81a12 u0 com.google.android.gms/com.google.android.gms.fido.fido2.ui.Fido2FullScreenActivity}
12-20 14:43:25.285  1357  2199 W InputDispatcher: Attempted to unregister already unregistered input channel '5f81a12 com.google.android.gms/com.google.android.gms.fido.fido2.ui.Fido2FullScreenActivity (server)'
12-20 14:43:25.286   805   805 I Zygote  : Process 25335 exited due to signal 9 (Killed)
12-20 14:43:25.313  1357  1406 W ActivityManager: setHasOverlayUi called on unknown pid: 25335
12-20 14:43:25.550  1831  1831 E FingerprintDialogView: Animation not found, 1 -> 0
12-20 14:43:25.584  2601  2626 I QcrilOemhookMsgTunnel: [0]processOemHookIndication length=21
12-20 14:43:25.584  2601  2601 D QcrilMsgTunnelIfaceManager: handleMessage what = 0
12-20 14:43:25.628  2601  2626 I QcrilOemhookMsgTunnel: [0]processOemHookIndication length=22
12-20 14:43:25.635  1357  3572 I LocationAccessPolicy: Allowing com.quvideo.xiaoying fine because it doesn't target API 29 yet. Please fix this app. Called from TelephonyRegistry push
12-20 14:43:25.636  2092  2173 I QCNEJ/CndHalConnector: -> SND notifyWwanSubtypeChanged(13)
12-20 14:43:25.638  2092  2173 I QCNEJ/CndHalConnector: -> SND notifyMobileDataEnabledChanged(true)
12-20 14:43:25.643  2143  2143 D ServiceStateProvider: subId=1
12-20 14:43:25.644  6393  6393 I CarrierServices: [2] cnv.onReceive: Received SERVICE_STATE intent, clearing cached cell info
12-20 14:43:25.646 10451 10451 D CellBroadcastReceiver: onReceive Intent { act=android.intent.action.SERVICE_STATE flg=0x1000010 cmp=com.android.cellbroadcastreceiver/.CellBroadcastReceiver (has extras) }
12-20 14:43:25.671  2601  2626 I QcrilOemhookMsgTunnel: [0]processOemHookIndication length=21
12-20 14:43:25.671  2601  2601 D QcrilMsgTunnelIfaceManager: handleMessage what = 0
12-20 14:43:25.690  1357  3572 I LocationAccessPolicy: Allowing com.quvideo.xiaoying fine because it doesn't target API 29 yet. Please fix this app. Called from TelephonyRegistry push
12-20 14:43:25.697  2143  2143 D ServiceStateProvider: subId=1
12-20 14:43:25.698  2092  2173 I QCNEJ/CndHalConnector: -> SND notifyWwanSubtypeChanged(13)
12-20 14:43:25.698  6393  6393 I CarrierServices: [2] cnv.onReceive: Received SERVICE_STATE intent, clearing cached cell info
12-20 14:43:25.700  2092  2173 I QCNEJ/CndHalConnector: -> SND notifyMobileDataEnabledChanged(true)
12-20 14:43:25.702 10451 10451 D CellBroadcastReceiver: onReceive Intent { act=android.intent.action.SERVICE_STATE flg=0x1000010 cmp=com.android.cellbroadcastreceiver/.CellBroadcastReceiver (has extras) }
12-20 14:43:25.713  1357  1406 W ActivityTaskManager: Activity top resumed state loss timeout for ActivityRecord{aa18dba u0 com.google.android.gms/.fido.fido2.ui.Fido2FullScreenActivity t-1 f}
12-20 14:43:25.746  1357  1973 I LocationAccessPolicy: Allowing com.quvideo.xiaoying fine because it doesn't target API 29 yet. Please fix this app. Called from TelephonyRegistry push
12-20 14:43:25.754  2143  2143 D ServiceStateProvider: subId=1
12-20 14:43:25.755  2092  2173 I QCNEJ/CndHalConnector: -> SND notifyWwanSubtypeChanged(13)
12-20 14:43:25.756  6393  6393 I CarrierServices: [2] cnv.onReceive: Received SERVICE_STATE intent, clearing cached cell info
12-20 14:43:25.760  2092  2173 I QCNEJ/CndHalConnector: -> SND notifyMobileDataEnabledChanged(true)
12-20 14:43:25.761 10451 10451 D CellBroadcastReceiver: onReceive Intent { act=android.intent.action.SERVICE_STATE flg=0x1000010 cmp=com.android.cellbroadcastreceiver/.CellBroadcastReceiver (has extras) }
12-20 14:43:26.145  1357  1357 V SettingsProvider: Notifying for 0: content://settings/system/screen_brightness
12-20 14:43:27.179  1636  1813 I WorkerManager: dispose()
12-20 14:43:27.180  1636  1813 W ThreadPoolDumper: Queue length for executor EventBus is now 11. Perhaps some tasks are too long, or the pool is too small.
12-20 14:43:28.433  2601  2626 I QcrilOemhookMsgTunnel: [0]processOemHookIndication length=21
12-20 14:43:28.434  2601  2601 D QcrilMsgTunnelIfaceManager: handleMessage what = 0
12-20 14:43:28.499  1357  1973 I LocationAccessPolicy: Allowing com.quvideo.xiaoying fine because it doesn't target API 29 yet. Please fix this app. Called from TelephonyRegistry push
12-20 14:43:28.509  2143  2143 D ServiceStateProvider: subId=1
12-20 14:43:28.512  6393  6393 I CarrierServices: [2] cnv.onReceive: Received SERVICE_STATE intent, clearing cached cell info
12-20 14:43:28.515 10451 10451 D CellBroadcastReceiver: onReceive Intent { act=android.intent.action.SERVICE_STATE flg=0x1000010 cmp=com.android.cellbroadcastreceiver/.CellBroadcastReceiver (has extras) }
12-20 14:43:28.518  2092  2173 I QCNEJ/CndHalConnector: -> SND notifyWwanSubtypeChanged(13)
12-20 14:43:28.521  2092  2173 I QCNEJ/CndHalConnector: -> SND notifyMobileDataEnabledChanged(true)
12-20 14:43:30.794  2601  2626 I QcrilOemhookMsgTunnel: [0]processOemHookIndication length=22
12-20 14:43:30.811  2601  2626 I QcrilOemhookMsgTunnel: [0]processOemHookIndication length=22
12-20 14:43:30.818  2143  2212 I QImsService: ImsSenderRxr : [UNSL]< UNSOL_VOPS_CHANGED true[SUB0]
12-20 14:43:30.820  2143  2143 I QImsService: ImsServiceSubHandler : Message received: what = 25
12-20 14:43:30.822  2601  2626 I QcrilOemhookMsgTunnel: [0]processOemHookIndication length=22
12-20 14:43:30.896  1357  3572 I LocationAccessPolicy: Allowing com.quvideo.xiaoying fine because it doesn't target API 29 yet. Please fix this app. Called from TelephonyRegistry push
als12-20 14:43:30.902  2092  2173 I QCNEJ/CndHalConnector: -> SND notifyWwanSubtypeChanged(13)
12-20 14:43:30.902  2143  2143 D ServiceStateProvider: subId=1
12-20 14:43:30.904  6393  6393 I CarrierServices: [2] cnv.onReceive: Received SERVICE_STATE intent, clearing cached cell info
12-20 14:43:30.904  2092  2173 I QCNEJ/CndHalConnector: -> SND notifyMobileDataEnabledChanged(true)
12-20 14:43:30.906 10451 10451 D CellBroadcastReceiver: onReceive Intent { act=android.intent.action.SERVICE_STATE flg=0x1000010 cmp=com.android.cellbroadcastreceiver/.CellBroadcastReceiver (has extras) }
hd12-20 14:43:31.044  2601  2626 I QcrilOemhookMsgTunnel: [0]processOemHookIndication length=21
12-20 14:43:31.044  2601  2601 D QcrilMsgTunnelIfaceManager: handleMessage what = 0
12-20 14:43:31.054  1357  3572 I LocationAccessPolicy: Allowing com.quvideo.xiaoying fine because it doesn't target API 29 yet. Please fix this app. Called from TelephonyRegistry push
12-20 14:43:31.061  2092  2173 I QCNEJ/CndHalConnector: -> SND notifyWwanSubtypeChanged(13)
12-20 14:43:31.064  2092  2173 I QCNEJ/CndHalConnector: -> SND notifyMobileDataEnabledChanged(true)
l12-20 14:43:31.068  6393  6393 I CarrierServices: [2] cnv.onReceive: Received SERVICE_STATE intent, clearing cached cell info
12-20 14:43:31.070 10451 10451 D CellBroadcastReceiver: onReceive Intent { act=android.intent.action.SERVICE_STATE flg=0x1000010 cmp=com.android.cellbroadcastreceiver/.CellBroadcastReceiver (has extras) }
ka12-20 14:43:31.109  1357  3909 I LocationAccessPolicy: Allowing com.quvideo.xiaoying fine because it doesn't target API 29 yet. Please fix this app. Called from TelephonyRegistry push
s12-20 14:43:31.115  2092  2173 I QCNEJ/CndHalConnector: -> SND notifyWwanSubtypeChanged(13)
12-20 14:43:31.118  2092  2173 I QCNEJ/CndHalConnector: -> SND notifyMobileDataEnabledChanged(true)
12-20 14:43:31.120  2143  2143 D ServiceStateProvider: subId=1
12-20 14:43:31.122  6393  6393 I CarrierServices: [2] cnv.onReceive: Received SERVICE_STATE intent, clearing cached cell info
12-20 14:43:31.124 10451 10451 D CellBroadcastReceiver: onReceive Intent { act=android.intent.action.SERVICE_STATE flg=0x1000010 cmp=com.android.cellbroadcastreceiver/.CellBroadcastReceiver (has extras) }
12-20 14:43:31.176   837  1160 D CHRE    : @ 176463.128: [ImuCal] Dynamic sensor configuration: high-performance.
jdkl;asj;djasldjasjdasljdlkasjdaskdk12-20 14:43:32.859  2601  2626 I QcrilOemhookMsgTunnel: [0]processOemHookIndication length=21
12-20 14:43:32.860  2601  2601 D QcrilMsgTunnelIfaceManager: handleMessage what = 0
12-20 14:43:32.944  1357  3572 I LocationAccessPolicy: Allowing com.quvideo.xiaoying fine because it doesn't target API 29 yet. Please fix this app. Called from TelephonyRegistry push
12-20 14:43:32.950  2092  2173 I QCNEJ/CndHalConnector: -> SND notifyWwanSubtypeChanged(13)
12-20 14:43:32.953  2092  2173 I QCNEJ/CndHalConnector: -> SND notifyMobileDataEnabledChanged(true)
12-20 14:43:32.956  2143  2143 D ServiceStateProvider: subId=1
12-20 14:43:32.958  6393  6393 I CarrierServices: [2] cnv.onReceive: Received SERVICE_STATE intent, clearing cached cell info
12-20 14:43:32.962 10451 10451 D CellBroadcastReceiver: onReceive Intent { act=android.intent.action.SERVICE_STATE flg=0x1000010 cmp=com.android.cellbroadcastreceiver/.CellBroadcastReceiver (has extras) }
 π frida_wrapper master ✗ ❯ 12-20 14:43:25.210 25335 25335 E AndroidRuntime:    at android.app.ActivityThread.performResumeActivity(ActivityThread.java:4205)
12-20 14:43:25.210 25335 25335 E AndroidRuntime:        at android.app.ActivityThread.handleResumeActivity(ActivityThread.java:4237)
12-20 14:43:25.210 25335 25335 E AndroidRuntime:        at android.app.servertransaction.ResumeActivityItem.execute(ResumeActivityItem.java:52)
12-20 14:43:25.210 25335 25335 E AndroidRuntime:        at android.app.servertransaction.TransactionExecutor.executeLifecycleState(TransactionExecutor.java:176)
12-20 14:43:25.210 25335 25335 E AndroidRuntime:        at android.app.servertransaction.TransactionExecutor.execute(TransactionExecutor.java:97)
12-20 14:43:25.210 25335 25335 E AndroidRuntime:        at android.app.ActivityThread$H.handleMessage(ActivityThread.java:2016)
12-20 14:43:25.210 25335 25335 E AndroidRuntime:        at android.os.Handler.dispatchMessage(Handler.java:107)
12-20 14:43:25.210 25335 25335 E AndroidRuntime:        at android.os.Looper.loop(Looper.java:214)
12-20 14:43:25.210 25335 25335 E AndroidRuntime:        at android.app.ActivityThread.main(ActivityThread.java:7356)
12-20 14:43:25.210 25335 25335 E AndroidRuntime:        at java.lang.reflect.Method.invoke(Native Method)
12-20 14:43:25.210 25335 25335 E AndroidRuntime:        at com.android.internal.os.RuntimeInit$MethodAndArgsCaller.run(RuntimeInit.java:492)
12-20 14:43:25.210 25335 25335 E AndroidRuntime:        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:930)
12-20 14:43:25.210 25335 25335 E AndroidRuntime: Caused by: java.lang.NullPointerException: Attempt to invoke interface method 'java.lang.Object java.util.Map.put(java.lang.Object, java.lang.Object)' on a null object reference
12-20 14:43:25.210 25335 25335 E AndroidRuntime:        at xrc.a(:com.google.android.gms@19629037@19.6.29 (120400-278422107):25)
12-20 14:43:25.210 25335 25335 E AndroidRuntime:        at yau.b(:com.google.android.gms@19629037@19.6.29 (120400-278422107):13)
12-20 14:43:25.210 25335 25335 E AndroidRuntime:        at xqw.a(:com.google.android.gms@19629037@19.6.29 (120400-278422107):39)
12-20 14:43:25.210 25335 25335 E AndroidRuntime:        at com.google.android.gms.fido.fido2.ui.AuthenticateChimeraActivity.a(:com.google.android.gms@19629037@19.6.29 (120400-278422107):27)
12-20 14:43:25.210 25335 25335 E AndroidRuntime:        at com.google.android.gms.fido.fido2.ui.AuthenticateChimeraActivity.onResume(Unknown Source:5)
12-20 14:43:25.210 25335 25335 E AndroidRuntime:        at com.google.android.chimera.Activity.publicOnResume(Unknown Source:0)
12-20 14:43:25.210 25335 25335 E AndroidRuntime:        at qrr.onResume(:com.google.android.gms@19629037@19.6.29 (120400-278422107):2)
12-20 14:43:25.210 25335 25335 E AndroidRuntime:        at android.app.Instrumentation.callActivityOnResume(Instrumentation.java:1453)
12-20 14:43:25.210 25335 25335 E AndroidRuntime:        at android.app.Activity.performResume(Activity.java:7939)
12-20 14:43:25.210 25335 25335 E AndroidRuntime:        at android.app.ActivityThread.performResumeActivity(ActivityThread.java:4195)
12-20 14:43:25.210 25335 25335 E AndroidRuntime:        ... 11 more
12-20 14:43:25.217 25335 25379 I Fido    : [RequestController] Timeout Runnable is removed, and timer is stopped.
12-20 14:43:25.223 25335 25335 I GCore-Chimera-Crash: ChgKB2Fkc19mZHIQpuqBChiBAiDguICvjgYKZAoJY29udGFpbm
12-20 14:43:25.223 25335 25335 I GCore-Chimera-Crash: VyEKDndxhAIJC38o9JKgZicmVsbGEqD2JyZWxsYV9keW5hbWl0
zsh: number expected
zsh: number expected
zsh: missing end of string
zsh: number expected
zsh: number expected
zsh: number expected
zsh: unknown file attribute: H
zsh: number expected
zsh: number expected
zsh: number expected
zsh: unknown username 'timeI'
zsh: unknown file attribute: Z
zsh: command not found: 12-20
zsh: no matches found: xrc.a(:com.google.android.gms@19629037@19.6.29 (120400-278422107):25)
zsh: no matches found: yau.b(:com.google.android.gms@19629037@19.6.29 (120400-278422107):13)
zsh: no matches found: xqw.a(:com.google.android.gms@19629037@19.6.29 (120400-278422107):39)
zsh: no matches found: com.google.android.gms.fido.fido2.ui.AuthenticateChimeraActivity.a(:com.google.android.gms@19629037@19.6.29 (120400-278422107):27)
zsh: unknown file attribute: k
zsh: unknown file attribute: k
zsh: no matches found: qrr.onResume(:com.google.android.gms@19629037@19.6.29 (120400-278422107):2)
zsh: missing delimiter for 'u' glob qualifier
zsh: number expected
zsh: number expected
zsh: command not found: 12-20
zsh: no matches found: [RequestController]
zsh: command not found: 12-20
zsh: command not found: 12-20
 π frida_wrapper master ✗ ❯
 π frida_wrapper master ✗ ❯
 π frida_wrapper master ✗ ❯
 π frida_wrapper master ✗ ❯
 """