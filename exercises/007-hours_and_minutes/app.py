def hours_minutes(seconds):
  
  return seconds // 3600, (seconds % 3600)/60

# Invoke the function and pass any integer as its argument
print(hours_minutes(60))
