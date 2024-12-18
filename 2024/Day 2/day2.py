##AOF 2024 Day 2

## Plan

def PartOne():
   safe_reports = 0
   i = 0
   safe_count = 0
   with open('./data.txt', 'r') as f:
      for line in f:
         report = line.strip().split(' ')
         current_report = []
         for level in report:
            current_report.append(int(level))
         
         increase_one = 1
         increase_two = 2
         increase_three = 3

         while i < len(current_report):
            
            
        
    
   return safe_reports
        
print('Part one ', PartOne())
