import pyupbit

access = "1hgJN4cKypbOBCkCYRBMza5bUMwgtbxekdS0K0Mv"          # 본인 값으로 변경
secret = "kOjVBExkf55hfL7uUZUcwj4OH3cgNx2k0zYEBkGA"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회