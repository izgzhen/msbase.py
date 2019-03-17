from msbase.subprocess_ import try_call_std
ret = try_call_std(["ping", "-c", "3", "google.com"])
print()
print(ret)
