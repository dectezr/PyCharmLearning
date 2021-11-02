def final_deposit_amount(*interest, amount=1000):
    for rate in interest:
        amount *= 1 + rate / 100
    return round(amount, 2)

# 递归解
#     if not interest:
#         return round(amount, 2)
#     return final_deposit_amount(*interest[1:], amount=amount * (1 + interest[0] / 100))
