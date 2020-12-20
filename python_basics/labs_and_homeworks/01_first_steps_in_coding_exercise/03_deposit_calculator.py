deposit = float(input())

deposit_period = int(input())

yearly_interest_percent = float(input())

total_sum = deposit + deposit_period * ((deposit * yearly_interest_percent /100) /12)

print(total_sum)