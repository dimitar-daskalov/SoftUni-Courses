numbers_received = [int(el) for el in input().split(", ")]
task_index = int(input())
task_value = numbers_received[task_index]
needed_task = (task_index, task_value)

total_clock_cycles = 0
tasks_dict = {}
for current_job_i in range(len(numbers_received)):
    tasks_dict[current_job_i] = numbers_received[current_job_i]

sorted_tasks = sorted(tasks_dict.items(), key=lambda x: x[1])

for (task) in sorted_tasks:
    if task == needed_task:
        total_clock_cycles += task[1]
        break
    total_clock_cycles += task[1]

print(total_clock_cycles)