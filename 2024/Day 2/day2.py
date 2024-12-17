##AOF 2024 Day 2

## Plan

def PartOne():
   safe_reports = 0
   with open('./data.txt', 'r') as f:
      for line in f:
         report = line.strip().split(' ')
         current_report = []
         for level in report:
            current_report.append(int(level))
         
         increase_one = 1
         increase_two = 2
         increase_three = 3

         for idx in range(len(current_report) - 1 ):
            if (current_report[idx + 1] != current_report[idx] + increase_one) or (current_report[idx + 1] != current_report[idx] + increase_two) or (current_report[idx + 1] != current_report[idx] + increase_three):
               safe_reports += 1

    
   return safe_reports
        
print('Part one ', PartOne())
