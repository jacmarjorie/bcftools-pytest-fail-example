```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
py.test
```

This will produce this error:

```
===================================================== test session starts ======================================================
platform darwin -- Python 2.7.10, pytest-2.9.1, py-1.4.31, pluggy-0.3.1
rootdir: /Users/smijac/ohsu/pysam-bcftools-pytest, inifile:
collected 1 items

test/test_bcftool.py FE

============================================================ ERRORS ============================================================
____________________________________________ ERROR at teardown of TestBCF.test_bcf _____________________________________________

self = <CallInfo when='teardown' exception: [Errno 9] Bad file descriptor>, func = <function <lambda> at 0x10ffe7d70>
when = 'teardown'

    def __init__(self, func, when):
        #: context of invocation: one of "setup", "call",
        #: "teardown", "memocollect"
        self.when = when
        self.start = time()
        try:
>           self.result = func()

../bcftoolstest/lib/python2.7/site-packages/_pytest/runner.py:150:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
../bcftoolstest/lib/python2.7/site-packages/_pytest/runner.py:138: in <lambda>
    return CallInfo(lambda: ihook(item=item, **kwds), when=when)
../bcftoolstest/lib/python2.7/site-packages/_pytest/vendored_packages/pluggy.py:724: in __call__
    return self._hookexec(self, self._nonwrappers + self._wrappers, kwargs)
../bcftoolstest/lib/python2.7/site-packages/_pytest/vendored_packages/pluggy.py:338: in _hookexec
    return self._inner_hookexec(hook, methods, kwargs)
../bcftoolstest/lib/python2.7/site-packages/_pytest/vendored_packages/pluggy.py:333: in <lambda>
    _MultiCall(methods, kwargs, hook.spec_opts).execute()
../bcftoolstest/lib/python2.7/site-packages/_pytest/vendored_packages/pluggy.py:595: in execute
    return _wrapped_call(hook_impl.function(*args), self.execute)
../bcftoolstest/lib/python2.7/site-packages/_pytest/vendored_packages/pluggy.py:244: in _wrapped_call
    next(wrap_controller)   # first yield
../bcftoolstest/lib/python2.7/site-packages/_pytest/capture.py:137: in pytest_runtest_teardown
    self.resumecapture()
../bcftoolstest/lib/python2.7/site-packages/_pytest/capture.py:84: in resumecapture
    self._capturing.resume_capturing()
../bcftoolstest/lib/python2.7/site-packages/_pytest/capture.py:281: in resume_capturing
    self.out.resume()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <FDCapture 1 oldfd=5>

    def resume(self):
        self.syscapture.resume()
>       os.dup2(self.tmpfile_fd, self.targetfd)
E       OSError: [Errno 9] Bad file descriptor

../bcftoolstest/lib/python2.7/site-packages/_pytest/capture.py:375: OSError
=========================================================== FAILURES ===========================================================
_______________________________________________________ TestBCF.test_bcf _______________________________________________________

self = <CallInfo when='call' exception: I/O operation on closed file>, func = <function <lambda> at 0x10ffe7398>, when = 'call'

    def __init__(self, func, when):
        #: context of invocation: one of "setup", "call",
        #: "teardown", "memocollect"
        self.when = when
        self.start = time()
        try:
>           self.result = func()

../bcftoolstest/lib/python2.7/site-packages/_pytest/runner.py:150:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
../bcftoolstest/lib/python2.7/site-packages/_pytest/runner.py:138: in <lambda>
    return CallInfo(lambda: ihook(item=item, **kwds), when=when)
../bcftoolstest/lib/python2.7/site-packages/_pytest/vendored_packages/pluggy.py:724: in __call__
    return self._hookexec(self, self._nonwrappers + self._wrappers, kwargs)
../bcftoolstest/lib/python2.7/site-packages/_pytest/vendored_packages/pluggy.py:338: in _hookexec
    return self._inner_hookexec(hook, methods, kwargs)
../bcftoolstest/lib/python2.7/site-packages/_pytest/vendored_packages/pluggy.py:333: in <lambda>
    _MultiCall(methods, kwargs, hook.spec_opts).execute()
../bcftoolstest/lib/python2.7/site-packages/_pytest/vendored_packages/pluggy.py:595: in execute
    return _wrapped_call(hook_impl.function(*args), self.execute)
../bcftoolstest/lib/python2.7/site-packages/_pytest/vendored_packages/pluggy.py:249: in _wrapped_call
    wrap_controller.send(call_outcome)
../bcftoolstest/lib/python2.7/site-packages/_pytest/capture.py:133: in pytest_runtest_call
    self.suspendcapture_item(item, "call")
../bcftoolstest/lib/python2.7/site-packages/_pytest/capture.py:150: in suspendcapture_item
    out, err = self.suspendcapture()
../bcftoolstest/lib/python2.7/site-packages/_pytest/capture.py:91: in suspendcapture
    outerr = cap.readouterr()
../bcftoolstest/lib/python2.7/site-packages/_pytest/capture.py:302: in readouterr
    return (self.out.snap() if self.out is not None else "",
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
```

self = <FDCapture 1 oldfd=5>

    def snap(self):
        f = self.tmpfile
>       f.seek(0)
E       ValueError: I/O operation on closed file

../bcftoolstest/lib/python2.7/site-packages/_pytest/capture.py:349: ValueError
============================================== 1 failed, 1 error in 0.24 seconds ===============================================
Traceback (most recent call last):
  File "/Users/smijac/ohsu/bcftoolstest/bin/py.test", line 11, in <module>
    sys.exit(main())
  File "/Users/smijac/ohsu/bcftoolstest/lib/python2.7/site-packages/_pytest/config.py", line 49, in main
    return config.hook.pytest_cmdline_main(config=config)
  File "/Users/smijac/ohsu/bcftoolstest/lib/python2.7/site-packages/_pytest/vendored_packages/pluggy.py", line 724, in __call__
    return self._hookexec(self, self._nonwrappers + self._wrappers, kwargs)
  File "/Users/smijac/ohsu/bcftoolstest/lib/python2.7/site-packages/_pytest/vendored_packages/pluggy.py", line 338, in _hookexec
    return self._inner_hookexec(hook, methods, kwargs)
  File "/Users/smijac/ohsu/bcftoolstest/lib/python2.7/site-packages/_pytest/vendored_packages/pluggy.py", line 333, in <lambda>
    _MultiCall(methods, kwargs, hook.spec_opts).execute()
  File "/Users/smijac/ohsu/bcftoolstest/lib/python2.7/site-packages/_pytest/vendored_packages/pluggy.py", line 596, in execute
    res = hook_impl.function(*args)
  File "/Users/smijac/ohsu/bcftoolstest/lib/python2.7/site-packages/_pytest/main.py", line 119, in pytest_cmdline_main
    return wrap_session(config, _main)
  File "/Users/smijac/ohsu/bcftoolstest/lib/python2.7/site-packages/_pytest/main.py", line 115, in wrap_session
    config._ensure_unconfigure()
  File "/Users/smijac/ohsu/bcftoolstest/lib/python2.7/site-packages/_pytest/config.py", line 848, in _ensure_unconfigure
    fin()
  File "/Users/smijac/ohsu/bcftoolstest/lib/python2.7/site-packages/_pytest/capture.py", line 80, in reset_capturings
    cap.pop_outerr_to_orig()
  File "/Users/smijac/ohsu/bcftoolstest/lib/python2.7/site-packages/_pytest/capture.py", line 263, in pop_outerr_to_orig
    out, err = self.readouterr()
  File "/Users/smijac/ohsu/bcftoolstest/lib/python2.7/site-packages/_pytest/capture.py", line 302, in readouterr
    return (self.out.snap() if self.out is not None else "",
  File "/Users/smijac/ohsu/bcftoolstest/lib/python2.7/site-packages/_pytest/capture.py", line 349, in snap
    f.seek(0)
ValueError: I/O operation on closed file
```
